# -*-coding:utf-8 -*-
from openstack import connection
from openstack import utils
from obs import ObsClient
from obs import StorageClass
from obs import HeadPermission
from obs import CreateBucketHeader
from obs import LogConf
import time


class hwCloudInterface(object):
    times = 60
    interval = 2
    header = CreateBucketHeader()
    # 设置桶访问权限为公共读，默认是私有读写
    header.aclControl = HeadPermission.PUBLIC_READ
    # 设置桶的存储类型为标准存储
    header.storageClass = StorageClass.STANDARD

    def __init__(self, projectId, cloud, region, access_key_id, secret_access_key, bucketServer):
        self.conn = connection.Connection(
            project_id=projectId,
            cloud=cloud,
            region=region,
            ak=access_key_id,
            sk=secret_access_key)
        self.obsClient = ObsClient(
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            server=bucketServer
        )

    # Create Bucket
    def create_Bucket(self, bucketName, location):
        resp = self.obsClient.createBucket(bucketName, header=self.header, location=location)
        if resp.status < 300:
            print('requestId:', resp.requestId)
            print('Create bucket:{} successfully!\n'.format(bucketName))
        else:
            print('errorCode:', resp.errorCode)
            print('errorMessage:', resp.errorMessage)

    # upload local file to Bucket
    def uploadImage(self, bucketName, objName, imagePath):
        resp = self.obsClient.putFile(bucketName, objName, file_path=imagePath)
        if resp.status < 300:
            print('requestId:', resp.requestId)
            print('upload {} to {} successfully!\n'.format(imagePath, bucketName))
        else:
            print('errorCode:', resp.errorCode)
            print('errorMessage:', resp.errorMessage)

    # Create image by file which in obs.
    # Image_url format: bucketName:objectFileName.
    def create_cloudimage_by_file(self, bucketName, objName, imageName):
        cloudimage = self.conn.ims.create_cloudimage(
            image_url="{}:{}".format(bucketName, objName),
            name=imageName,
            min_disk=40,
            os_version='Other Linux(64 bit)',
            description='for ci'
        )
        print('create image {} by {} successfully!\njob id is {}\n'.format(imageName, imageName, cloudimage.job_id))
        print(cloudimage)
        return cloudimage.job_id

    # wait image to be available
    def wait_image_tobe_available(self, job_id, times, interval):
        for index in range(times):
            time.sleep(interval)
            job = self.conn.ims.get_job(job_id)
            print("image job is still running")
            if job.status == "SUCCESS":
                print("Get job success after %s tries" % index)
                break
            elif job.status == "FAIL":
                print("Get job failed after %s tries" % index)
                break

    # get imageId by job_id
    def get_imageId_by_job(self, job_id):
        job = self.conn.ims.get_job(job_id)
        print('image id is {}\n'.format(job.entities['image_id']))
        return job.entities['image_id']

    # create security_group
    def create_sgroup(self, sgroupName):
        data = {
            "name": sgroupName
        }
        sg = self.conn.vpcv1.create_security_group(**data)
        print('sgroup id is {}\n'.format(sg.id))
        print sg
        return sg.id

    # create sg_rule
    def create_security_group_rule(self, sgroupId):
        data = {
            "security_group_id": sgroupId,
            "direction": "ingress"
        }
        print(self.conn.vpcv1.create_security_group_rule(**data))

    # create VPC
    def create_vpc(self, vpcName, vpcCIDR):
        data = {
            "name": vpcName,
            "cidr": vpcCIDR
        }
        vpc = self.conn.vpcv1.create_vpc(**data)
        print('vpc id is {}\n'.format(vpc.id))
        print vpc
        return vpc.id

    def get_resourceInfo_by_resourceName(self, resourceType, resourceName, info):
        query = {
            "limit": 2
        }
        match = {
            "vpc": self.conn.vpcv1.vpcs,
            "subnet": self.conn.vpcv1.subnets,
            "sgroup": self.conn.vpcv1.security_groups
        }
        objs = match[resourceType](**query)
        objList = list(objs)
        print("-------check-result-is----{},----result len is {}".format(objList, len(objList)))
        if len(objList):
            for obj in objList:
                if obj.name == resourceName:
                    return obj.id if info == "id" else obj.status
            return "0"
        else:
            return "0"

    # create wan/lan subnet in vpc
    def create_subnet(self, NetName, CIDR, gw, vpcid):
        data = {
            "name": NetName,
            "cidr": CIDR,
            "gateway_ip": gw,
            "vpc_id": vpcid
        }
        subnet = self.conn.vpcv1.create_subnet(**data)
        print('subnet is {}'.format(subnet))
        self.wait_subnet_tobe_active(NetName, self.times, self.interval)
        return subnet.neutron_network_id

    # wait subnet to be active
    def wait_subnet_tobe_active(self, netName, times, interval):
        for index in range(times):
            time.sleep(interval)
            status = self.get_resourceInfo_by_resourceName("subnet", netName, "status")
            print("net status is {}".format(status))
            if status == "ACTIVE":
                print("{} after {} tries".format(netName, index))
                break

    # create ECS server
    def create_server(self, imageId, sgroupId, vpcId, netList, availability_zone, serverName, flavorType):

        def get_net_iface_list(net_id):
            netBody = {
                "uuid": net_id
            }
            return netBody
        network_interfacesList = map(lambda x: get_net_iface_list(x), netList)
        user_date_org = "#!/bin/bash \r\n echo 'root:Passw0rd' | chpasswd ;"
        user_data = utils.b64encode(user_date_org)
        data = {
            "availability_zone": availability_zone,
            "name": serverName,
            "imageRef": imageId,
            "flavorRef": flavorType,
            "security_groups": [
                {
                    "name": sgroupId
                }
            ],
            "networks": network_interfacesList,
            "data_volumes": [
                {
                    "size": 40,
                    "volumetype": "SSD"
                }
            ],
            "extendparam": {
                "chargingMode": "postPaid"
            },
            "user_data": user_data,
            "vpcid": vpcId
        }

        print(data)
        ff = self.conn.compute.create_server(**data)
        server_create = self.conn.compute.wait_for_server(ff, status="ACTIVE", wait=300)
        print("server id is:{}".format(ff.id))
        print(ff)
        return ff.id

    # get list of interface
    def get_wan_interfaces_id(self, server_id, wan_subnetId):
        wan_Id = ""
        server_ifas = self.conn.compute.server_interfaces(server_id)
        for ifa in server_ifas:
            print(ifa)
            if ifa.net_id == wan_subnetId:
                wan_Id = ifa.port_id
                break
        print("wan nic id is {}".format(wan_Id))
        print(server_ifas)
        return wan_Id

    # create floating ip
    def associate_ip_to_wan(self, port_id, floating_network_id):
        data = {
            "floating_network_id": floating_network_id,
            "port_id": port_id
        }
        ipinfo = self.conn.network.create_ip(**data)
        print("public ip is: {}\n".format(ipinfo.floating_ip_address))
        print(ipinfo)
        return ipinfo.id, ipinfo.floating_ip_address

    def delete_ip(self, ipId):
        print(self.conn.network.delete_ip(ipId))

    def delete_security_group(self, sgId):
        print(self.conn.network.delete_security_group(sgId))

    def delete_subnet(self, netId, vpcId):
        print(self.conn.vpcv1.delete_subnet(netId, vpcId))

    def delete_vpc(self, vpcId):
        print(self.conn.vpcv1.delete_vpc(vpcId))

    def delete_image(self, imageId):
        print(self.conn.image.delete_image(imageId))

    # delete server
    def delete_server(self, server_id):
        print(self.conn.compute.delete_server(server_id))
