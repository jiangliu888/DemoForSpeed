#  coding=utf-8
# if the python sdk is not install using 'sudo pip install aliyun-python-sdk-ecs'
# if the python sdk is install using 'sudo pip install --upgrade aliyun-python-sdk-ecs'
# make sure the sdk version is 4.4.3, you can use command 'pip show aliyun-python-sdk-ecs' to check
import json
import logging
import time
import oss2
from aliyunsdkcore import client
from aliyunsdkecs.request.v20140526.CreateInstanceRequest import CreateInstanceRequest
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526.StartInstanceRequest import StartInstanceRequest
from aliyunsdkecs.request.v20140526.ImportImageRequest import ImportImageRequest
from aliyunsdkecs.request.v20140526.CreateVpcRequest import CreateVpcRequest
from aliyunsdkecs.request.v20140526.CreateVSwitchRequest import CreateVSwitchRequest
from aliyunsdkecs.request.v20140526.CreateSecurityGroupRequest import CreateSecurityGroupRequest
from aliyunsdkecs.request.v20140526.AuthorizeSecurityGroupRequest import AuthorizeSecurityGroupRequest
from aliyunsdkecs.request.v20140526.CreateNetworkInterfaceRequest import CreateNetworkInterfaceRequest
from aliyunsdkecs.request.v20140526.AttachNetworkInterfaceRequest import AttachNetworkInterfaceRequest
from aliyunsdkecs.request.v20140526.DeleteInstanceRequest import DeleteInstanceRequest
from aliyunsdkecs.request.v20140526.DeleteImageRequest import DeleteImageRequest
from aliyunsdkecs.request.v20140526.DeleteNetworkInterfaceRequest import DeleteNetworkInterfaceRequest
from aliyunsdkecs.request.v20140526.DeleteVSwitchRequest import DeleteVSwitchRequest
from aliyunsdkecs.request.v20140526.DeleteSecurityGroupRequest import DeleteSecurityGroupRequest
from aliyunsdkecs.request.v20140526.DeleteVpcRequest import DeleteVpcRequest
from aliyunsdkecs.request.v20140526.AllocateEipAddressRequest import AllocateEipAddressRequest
from aliyunsdkecs.request.v20140526.AssociateEipAddressRequest import AssociateEipAddressRequest
from aliyunsdkecs.request.v20140526.ReleaseEipAddressRequest import ReleaseEipAddressRequest
from aliyunsdkecs.request.v20140526.DescribeImagesRequest import DescribeImagesRequest
from aliyunsdkecs.request.v20140526.StopInstanceRequest import StopInstanceRequest
from aliyunsdkecs.request.v20140526.DescribeVSwitchesRequest import DescribeVSwitchesRequest
from aliyunsdkecs.request.v20140526.DescribeVpcsRequest import DescribeVpcsRequest
from aliyunsdkecs.request.v20140526.DescribeSecurityGroupsRequest import DescribeSecurityGroupsRequest
from aliyunsdkecs.request.v20140526.DescribeNetworkInterfacesRequest import DescribeNetworkInterfacesRequest
from aliyunsdkecs.request.v20140526.DescribeEipAddressesRequest import DescribeEipAddressesRequest


class aliCloudInterface(object):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')

    def __init__(self, ak, sk, location):
        self.clt = client.AcsClient(ak, sk, location)
        self.url = 'http://oss-{}.aliyuncs.com'.format(location)
        self.auth = oss2.Auth(ak, sk)

    # send open api request
    def _send_request(self, request):
        request.set_accept_format('json')
        try:
            response_str = self.clt.do_action(request)
            logging.info(response_str)
            response_detail = json.loads(response_str)
            return response_detail
        except Exception as e:
            logging.error(e)
            print("status:------", e.get_http_status())
            print("error_code------", e.get_error_code())
            print("error_msg -------", e.get_error_msg())
            return e.get_http_status()

    # Create Bucket
    def create_Bucket_and_upload_imageFile(self, bucketName, location, objName, localFilePath):
        bucket = oss2.Bucket(self.auth, self.url, bucketName)
        bucket.create_bucket()
        bucket.put_object_from_file(objName, localFilePath)

    def delete_Bucket_and_file(self, bucketName):
        bucket = oss2.Bucket(self.auth, self.url, bucketName)
        # 列举存储空间下所有文件并删除。
        for obj in oss2.ObjectIterator(bucket):
            print(obj.key)
            bucket.delete_object(obj.key)
        try:
            # 删除存储空间。
            bucket.delete_bucket()
        except oss2.exceptions.BucketNotEmpty:
            print('bucket is not empty.')
        except oss2.exceptions.NoSuchBucket:
            print('bucket does not exist')

    # create image
    def create_image_by_file(self, bucketName, objName, imageName):
        request = ImportImageRequest()
        request.set_Platform('Others Linux')
        request.set_ImageName(imageName)
        request.set_Architecture('x86_64')
        deviceMap = {
            'OSSBucket': bucketName,
            'Format': 'qcow2',
            'OSSObject': objName,
            'DiskImageSize': '5'
        }
        request.set_DiskDeviceMappings([deviceMap])
        response = self._send_request(request)
        image_id = response.get('ImageId')
        logging.info("image %s import task submit successfully.", image_id)
        self.wait_image_tobe_available(image_id)
        return image_id

    # wait image to be available
    def wait_image_tobe_available(self, image_id):
        index = 0
        detail = self.get_image_detail_by_id(image_id)
        while detail is None and index < 100:
            detail = self.get_image_detail_by_id(image_id)
            time.sleep(10)
            index = index + 1
        logging.info("image %s is available now.", image_id)
        return image_id

    # output the image owned in current region.
    def get_image_detail_by_id(self, image_id, status='Available'):
        logging.info("Check image %s status is %s", image_id, status)
        request = DescribeImagesRequest()
        request.set_ImageId(image_id)
        response = self._send_request(request)
        image_detail = None
        if response is not None:
            image_list = response.get('Images').get('Image')
            for item in image_list:
                if item.get('Status') == status:
                    image_detail = item
                    break
            return image_detail

    # create sgroup
    def create_sgroup(self, sgName, vpcId):
        request = CreateSecurityGroupRequest()
        request.set_SecurityGroupName(sgName)
        request.set_VpcId(vpcId)
        response = self._send_request(request)
        sgroup_Id = response.get("SecurityGroupId")
        logging.info("sgroup %s create task submit successfully.", sgroup_Id)
        return sgroup_Id

    # create sgroup_rule
    def create_rule(self, sgId):
        request = AuthorizeSecurityGroupRequest()
        request.set_accept_format('json')
        request.set_SecurityGroupId(sgId)
        request.set_IpProtocol("all")
        request.set_PortRange("-1/-1")
        request.set_SourceCidrIp("0.0.0.0/0")
        response = self._send_request(request)
        print(response)

    # create vpc
    def create_vpc(self, vpcName, vpcCIDR):
        request = CreateVpcRequest()
        request.set_CidrBlock(vpcCIDR)
        request.set_VpcName(vpcName)
        response = self._send_request(request)
        vpc_Id = response.get('VpcId')
        logging.info("vpc %s create task submit successfully.", vpc_Id)
        return vpc_Id

    # create sgroup
    def create_vswitch(self, switchName, cidr, vpcId, zoneId):
        request = CreateVSwitchRequest()
        request.set_VpcId(vpcId)
        request.set_VSwitchName(switchName)
        request.set_CidrBlock(cidr)
        request.set_ZoneId(zoneId)
        response = self._send_request(request)
        vswitch_id = response.get('VSwitchId')
        logging.info("vswitch %s create task submit successfully.", vswitch_id)
        return vswitch_id

    # create one after pay ecs instance.
    def create_after_pay_instance(self, image_id, security_group_id, vsw_vswitch_id, zone_Id, serverName, instance_type):
        request = CreateInstanceRequest()
        request.set_ImageId(image_id)
        request.set_SecurityGroupId(security_group_id)
        request.set_InstanceType(instance_type)
        request.set_InstanceName(serverName)
        request.set_ZoneId(zone_Id)
        request.set_IoOptimized('optimized')
        request.set_VSwitchId(vsw_vswitch_id)
        request.set_SystemDiskCategory('cloud_ssd')
        request.set_InternetMaxBandwidthOut(10)
        request.set_Password("Passw0rd")
        response = self._send_request(request)
        instance_id = response.get('InstanceId')
        logging.info("instance %s created task submit successfully.", instance_id)
        return instance_id

    # create network interface
    def create_networkInterface(self, vswitch_id, security_group_id):
        request = CreateNetworkInterfaceRequest()
        request.set_VSwitchId(vswitch_id)
        request.set_SecurityGroupId(security_group_id)
        response = self._send_request(request)
        network_Id = response.get("NetworkInterfaceId")
        logging.info("network interface %s create task submit successfully.", network_Id)
        return network_Id

    # attach network to instance
    def attach_network_to_instance(self, networkId, instanceId):
        request = AttachNetworkInterfaceRequest()
        request.set_NetworkInterfaceId(networkId)
        request.set_InstanceId(instanceId)
        print(self._send_request(request))

    # allocate floating ip
    def allocate_floating_ip(self):
        request = AllocateEipAddressRequest()
        request.set_InternetChargeType("PayByTraffic")
        response = self._send_request(request)
        return response.get("EipAddress"), response.get("AllocationId")

    # associate floating ip to instance
    def associate_eip(self, eipId, instanceId):
        request = AssociateEipAddressRequest()
        request.set_AllocationId(eipId)
        request.set_InstanceId(instanceId)
        self._send_request(request)

    def start_instance(self, instance_id):
        request = StartInstanceRequest()
        request.set_InstanceId(instance_id)
        self._send_request(request)

    def check_instance_status(self, instance_id, status="Running"):
        detail = self.get_instance_detail_by_id(instance_id, status)
        index = 0
        while detail is None and index < 60:
            detail = self.get_instance_detail_by_id(instance_id, status)
            time.sleep(10)
            index = index + 1
        logging.info("instance %s is %s now.", instance_id, status)
        return instance_id

    # output the instance owned in current region.
    def get_instance_detail_by_id(self, instance_id, status='Running'):
        logging.info("Check instance %s status is %s", instance_id, status)
        request = DescribeInstancesRequest()
        request.set_InstanceIds(json.dumps([instance_id]))
        response = self._send_request(request)
        instance_detail = None
        if response is not None:
            instance_list = response.get('Instances').get('Instance')
            for item in instance_list:
                if item.get('Status') == status:
                    instance_detail = item
                    break
            return instance_detail

    def check_resource_status(self, resourcetype, resourceid, status):
        detail = self.get_resource_detail_by_id(resourcetype, resourceid, status)
        index = 0
        while detail is None and index < 60:
            detail = self.get_resource_detail_by_id(resourcetype, resourceid, status)
            time.sleep(10)
            index = index + 1
        logging.info("resource %s is %s now.", resourceid, status)
        return resourceid

    def get_resource_id_by_name(self, resourcetype, resourceName):
        logging.info("get %s.. %s id", resourcetype, resourceName)
        request = DescribeVSwitchesRequest()
        responseKey = '{}s'.format(resourcetype) if resourcetype == "Vpc" else '{}es'.format(resourcetype)
        itemNameKey = '{}Name'.format(resourcetype)
        itemIdKey = '{}Id'.format(resourcetype)
        if resourcetype == "VSwitch":
            request = DescribeVSwitchesRequest()
        elif resourcetype == "Vpc":
            request = DescribeVpcsRequest()
        response = self._send_request(request)
        if response is not None:
            resource_list = response.get(responseKey).get(resourcetype)
            for item in resource_list:
                if item.get(itemNameKey) == resourceName:
                    return item.get(itemIdKey)
            else:
                return "0"

    def get_sg_id_by_name_and_vpcId(self, sgName, vpc_Id):
        request = DescribeSecurityGroupsRequest()
        response = self._send_request(request)
        request.set_VpcId(vpc_Id)
        if response is not None:
            resource_list = response.get("SecurityGroups").get("SecurityGroup")
            for item in resource_list:
                if item.get("SecurityGroupName") == sgName:
                    return item.get("SecurityGroupId")
            else:
                return "0"

    # output the resource owned in current region.
    def get_resource_detail_by_id(self, resourcetype, resourceid, status='Available'):
        array = ["VSwitch", "EipAddress"]
        logging.info("Check %s.. %s status is %s", resourcetype, resourceid, status)
        request = DescribeVSwitchesRequest()
        responseKey = '{}es'.format(resourcetype) if resourcetype in array else '{}s'.format(resourcetype)
        if resourcetype == "VSwitch":
            request = DescribeVSwitchesRequest()
            request.set_VSwitchId(resourceid)
        elif resourcetype == "Vpc":
            request = DescribeVpcsRequest()
            request.set_VpcId(resourceid)
        elif resourcetype == "NetworkInterfaceSet":
            request = DescribeNetworkInterfacesRequest()
            request.set_NetworkInterfaceIds([resourceid])
        elif resourcetype == "EipAddress":
            request = DescribeEipAddressesRequest()
            request.set_AllocationId(resourceid)
        response = self._send_request(request)
        resource_detail = None
        if response is not None:
            resource_list = response.get(responseKey).get(resourcetype)
            for item in resource_list:
                if item.get('Status') == status:
                    resource_detail = item
                    break
            return resource_detail

    def stop_server(self, instance_id):
        request = StopInstanceRequest()
        request.set_InstanceId(instance_id)
        response = self._send_request(request)
        print(response)
        self.check_instance_status(instance_id, "Stopped")

    def delete_server(self, instance_id):
        self.stop_server(instance_id)
        request = DeleteInstanceRequest()
        request.set_InstanceId(instance_id)
        response = self._send_request(request)
        print(response)

    def delete_ip(self, eip_Id):
        request = ReleaseEipAddressRequest()
        request.set_AllocationId(eip_Id)
        response = self._send_request(request)
        print(response)

    def delete_image(self, image_id):
        request = DeleteImageRequest()
        request.set_ImageId(image_id)
        response = self._send_request(request)
        print(response)

    def delete_vpc(self, vpc_Id):
        request = DeleteVpcRequest()
        request.set_VpcId(vpc_Id)
        response = self._send_request(request)
        print(response)

    def delete_vswitch(self, vswitch_Id):
        request = DeleteVSwitchRequest()
        request.set_VSwitchId(vswitch_Id)
        response = self._send_request(request)
        print(response)

    def delete_networkInterface(self, networkInterface_Id):
        request = DeleteNetworkInterfaceRequest()
        request.set_NetworkInterfaceId(networkInterface_Id)
        response = self._send_request(request)
        print(response)

    def delete_security_group(self, sg_Id):
        request = DeleteSecurityGroupRequest()
        request.set_SecurityGroupId(sg_Id)
        response = self._send_request(request)
        print(response)
