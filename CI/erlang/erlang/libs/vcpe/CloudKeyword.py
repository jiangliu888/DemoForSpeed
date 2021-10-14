# -*-coding:utf-8 -*-
from erlang.libs.vcpe.cloudInterface.hwCloudInterface import hwCloudInterface
from erlang.libs.vcpe.cloudInterface.aliCloudInterface import aliCloudInterface
from erlang.libs.vcpe.cloudInterface.azureCloudInterface import azureCloudInterface
from erlang.libs.vcpe.cloudInterface.awsCloudInterface import awsCloudInterface


class CloudKeyword(object):
    cloudObj_list = {}
    times = 60
    interval = 10

    def __init__(self):
        pass

    @staticmethod
    def connect_to_cloud(cloudType, ak, sk, region, **para):
        if cloudType == 'hw_cloud':
            hwCloudObj = hwCloudInterface(para['project_id'], para['cloud'], region, ak, sk, para['bucketServer'])
            CloudKeyword.cloudObj_list[cloudType] = hwCloudObj
            print(cloudType)
        elif cloudType == 'ali_cloud':
            aliCloudObj = aliCloudInterface(ak, sk, region)
            CloudKeyword.cloudObj_list[cloudType] = aliCloudObj
            print(cloudType)
        elif cloudType == 'azure_cloud':
            azureCloudObj = azureCloudInterface(ak, sk, region, para['tenant_id'], para['subscription_id'], para['resourceGrpName'])
            CloudKeyword.cloudObj_list[cloudType] = azureCloudObj
            print(cloudType)
        elif cloudType == 'aws_cloud':
            awsCloudObj = awsCloudInterface()
            CloudKeyword.cloudObj_list[cloudType] = awsCloudObj

    # Create Bucket and upload Image file
    @staticmethod
    def create_Bucket_and_upload_imageFile(cloudType, bucketName, location, objName, localFilePath):
        if cloudType == 'hw_cloud':
            CloudKeyword.cloudObj_list[cloudType].create_Bucket(bucketName, location)
            CloudKeyword.cloudObj_list[cloudType].uploadImage(bucketName, objName, localFilePath)
        elif cloudType == 'ali_cloud':
            CloudKeyword.cloudObj_list[cloudType].create_Bucket_and_upload_imageFile(bucketName, location, objName, localFilePath)

    # Create image by file which in obs.
    # Image_url format: bucketName:objectFileName.
    @staticmethod
    def create_image(cloudType, bucketName, objName, imageName):
        if cloudType == 'hw_cloud':
            job_id = CloudKeyword.cloudObj_list[cloudType].create_cloudimage_by_file(bucketName, objName, imageName)
            CloudKeyword.cloudObj_list[cloudType].wait_image_tobe_available(job_id, CloudKeyword.times, CloudKeyword.interval)
            return CloudKeyword.cloudObj_list[cloudType].get_imageId_by_job(job_id)
        elif cloudType == 'ali_cloud':
            return CloudKeyword.cloudObj_list[cloudType].create_image_by_file(bucketName, objName, imageName)

    @staticmethod
    def create_azure_image_disk(imageFilePath, azcopyToolPath, imageDiskName):
        CloudKeyword.cloudObj_list['azure_cloud'].create_disk_by_vhdFile(imageFilePath, azcopyToolPath, imageDiskName)

    # create security_group
    @staticmethod
    def create_sgroup_and_addrule(cloudType, sgroupName, vpcId):
        if cloudType == 'hw_cloud':
            sg_id = CloudKeyword.cloudObj_list[cloudType].get_resourceInfo_by_resourceName("sgroup", sgroupName, "id")
            if sg_id != "0":
                print("find exsit sgroup----{}".format(sg_id))
                return sg_id
            else:
                sgroupId = CloudKeyword.cloudObj_list[cloudType].create_sgroup(sgroupName)
                CloudKeyword.cloudObj_list[cloudType].create_security_group_rule(sgroupId)
                return sgroupId
        elif cloudType == 'ali_cloud':
            sg_id = CloudKeyword.cloudObj_list[cloudType].get_sg_id_by_name_and_vpcId(sgroupName, vpcId)
            sgroupId = sg_id if sg_id != "0" else CloudKeyword.cloudObj_list[cloudType].create_sgroup(sgroupName, vpcId)
            CloudKeyword.cloudObj_list[cloudType].create_rule(sgroupId)
            return sgroupId
        elif cloudType == 'azure_cloud':
            sgInfor = CloudKeyword.cloudObj_list[cloudType].create_sgroup_with_rule(sgroupName)
            return sgInfor.id
        elif cloudType == 'aws_cloud':
            vpcObj = CloudKeyword.cloudObj_list[cloudType].get_vpcObj(vpcId)
            sg_id = CloudKeyword.cloudObj_list[cloudType].create_security_group(sgroupName, vpcObj)
            return sg_id

    # create VPC
    @staticmethod
    def create_vpc(cloudType, vpcName, vpcCIDR):
        if cloudType == 'hw_cloud':
            vpc_Id = CloudKeyword.cloudObj_list[cloudType].get_resourceInfo_by_resourceName("vpc", vpcName, "id")
            print("find if there exsit vpc----{}".format(vpc_Id))
            return vpc_Id if vpc_Id != "0" else CloudKeyword.cloudObj_list[cloudType].create_vpc(vpcName, vpcCIDR)
        elif cloudType == 'ali_cloud':
            vpc_Id = CloudKeyword.cloudObj_list[cloudType].get_resource_id_by_name("Vpc", vpcName)
            return vpc_Id if vpc_Id != "0" else CloudKeyword.cloudObj_list[cloudType].create_vpc(vpcName, vpcCIDR)
        elif cloudType == 'azure_cloud':
            print(CloudKeyword.cloudObj_list[cloudType].create_vnet(vpcName, vpcCIDR))
            return "azure"
        elif cloudType == 'aws_cloud':
            vpc_Id = CloudKeyword.cloudObj_list[cloudType].create_vpc(vpcName, vpcCIDR)
            return vpc_Id

    @staticmethod
    def create_aws_network(vpc_id, wanNetName, wanCIDR, lanNetName, lanCIDR):
        vpcObj = CloudKeyword.cloudObj_list['aws_cloud'].get_vpcObj(vpc_id)
        internetGatewayId = CloudKeyword.cloudObj_list['aws_cloud'].create_internet_gateway()
        CloudKeyword.cloudObj_list['aws_cloud'].attach_internet_gateway_to_vpc(vpcObj, internetGatewayId)
        CloudKeyword.cloudObj_list['aws_cloud'].add_default_out_route(vpcObj, internetGatewayId)
        wan_sub_id = CloudKeyword.cloudObj_list['aws_cloud'].create_subnet(vpcObj, wanNetName, wanCIDR)
        lan_sub_id = CloudKeyword.cloudObj_list['aws_cloud'].create_subnet(vpcObj, lanNetName, lanCIDR)
        pubIp, pubId = CloudKeyword.cloudObj_list['aws_cloud'].create_pubIp()
        return internetGatewayId, wan_sub_id, lan_sub_id, pubIp, pubId

    @staticmethod
    def create_linux_server_to_mk_image(image_id, serverType, sgroup_id, subnet_id, serverName, pubId):
        linux_instance = CloudKeyword.cloudObj_list['aws_cloud'].create_server(image_id, serverType, sgroup_id, subnet_id, serverName, True)
        ebs_id = CloudKeyword.cloudObj_list['aws_cloud'].get_ebs_id(linux_instance['InstanceId'])
        CloudKeyword.cloudObj_list['aws_cloud'].attach_pubIp_to_server(pubId, linux_instance['NetworkInterfaces'][0]['NetworkInterfaceId'])
        return ebs_id, linux_instance['InstanceId']

    @staticmethod
    def detach_ebs_and_make_image(ebs_id, imageName):
        CloudKeyword.cloudObj_list['aws_cloud'].detach_ebs(ebs_id)
        snapshotId = CloudKeyword.cloudObj_list['aws_cloud'].create_snapshot(ebs_id)
        imageId = CloudKeyword.cloudObj_list['aws_cloud'].create_image(snapshotId, imageName)
        return snapshotId, imageId

    @staticmethod
    def create_aws_server(image_id, serverType, sgroup_id, wannet_id, lannet_id, serverName):
        instance = CloudKeyword.cloudObj_list['aws_cloud'].create_server(image_id, serverType, sgroup_id, wannet_id, serverName, False)
        pubIp, pubId = CloudKeyword.cloudObj_list['aws_cloud'].create_pubIp()
        CloudKeyword.cloudObj_list['aws_cloud'].attach_pubIp_to_server(pubId, instance['NetworkInterfaces'][0]['NetworkInterfaceId'])
        lan_nic_id = CloudKeyword.cloudObj_list['aws_cloud'].create_lan_nic_and_attach_to_server(lannet_id, sgroup_id, instance['InstanceId'])
        return pubIp, pubId, instance['InstanceId'], lan_nic_id

    @staticmethod
    def delete_aws_server(instance_id):
        CloudKeyword.cloudObj_list['aws_cloud'].terminated_server(instance_id)

    @staticmethod
    def delete_aws_image(image_id, snapshot_id, ebs_id):
        CloudKeyword.cloudObj_list['aws_cloud'].delete_ami(image_id)
        CloudKeyword.cloudObj_list['aws_cloud'].delete_snapshot(snapshot_id)
        CloudKeyword.cloudObj_list['aws_cloud'].delete_ebs(ebs_id)

    @staticmethod
    def delete_aws_igw_and_sg(vpc_id, sgroup_id, igw_id, lan_nic_id, wan_id, lan_id):
        CloudKeyword.cloudObj_list['aws_cloud'].detach_igw(vpc_id, igw_id)
        CloudKeyword.cloudObj_list['aws_cloud'].delete_igw(igw_id)
        CloudKeyword.cloudObj_list['aws_cloud'].delete_nic(lan_nic_id)
        CloudKeyword.cloudObj_list['aws_cloud'].delete_subnet(wan_id)
        CloudKeyword.cloudObj_list['aws_cloud'].delete_subnet(lan_id)
        CloudKeyword.cloudObj_list['aws_cloud'].delete_sgroup(sgroup_id)
        CloudKeyword.cloudObj_list['aws_cloud'].delete_vpc(vpc_id)

    @staticmethod
    def delete_pubIp(pub_id):
        CloudKeyword.cloudObj_list['aws_cloud'].delete_pub(pub_id)

    # create ECS server
    @staticmethod
    def create_server_with_2subnet(cloudType, imageId, sgroupId, vpcId, wanNetName, wanCIDR, wangw, lanNetName, lanCIDR, langw, availability_zone, serverName, flavorType):
        if cloudType == 'hw_cloud':
            wan_Id = CloudKeyword.cloudObj_list[cloudType].get_resourceInfo_by_resourceName("subnet", wanNetName, "id")
            lan_Id = CloudKeyword.cloudObj_list[cloudType].get_resourceInfo_by_resourceName("subnet", lanNetName, "id")
            print("find if there is exsit wan----{}---------{}".format(wan_Id, lan_Id))
            wan_subnetId = wan_Id if wan_Id != "0" else CloudKeyword.cloudObj_list[cloudType].create_subnet(wanNetName, wanCIDR, wangw, vpcId)
            lan_subnetId = lan_Id if lan_Id != "0" else CloudKeyword.cloudObj_list[cloudType].create_subnet(lanNetName, lanCIDR, langw, vpcId)
            return wan_subnetId, lan_subnetId, CloudKeyword.cloudObj_list[cloudType].create_server(imageId, sgroupId, vpcId, [wan_subnetId, lan_subnetId], availability_zone, serverName, flavorType)
        elif cloudType == 'ali_cloud':
            wan_Id = CloudKeyword.cloudObj_list[cloudType].get_resource_id_by_name("VSwitch", wanNetName)
            lan_Id = CloudKeyword.cloudObj_list[cloudType].get_resource_id_by_name("VSwitch", lanNetName)
            wan_vswitch = wan_Id if wan_Id != "0" else CloudKeyword.cloudObj_list[cloudType].create_vswitch(wanNetName, wanCIDR, vpcId, availability_zone)
            lan_vswitch = lan_Id if lan_Id != "0" else CloudKeyword.cloudObj_list[cloudType].create_vswitch(lanNetName, lanCIDR, vpcId, availability_zone)
            CloudKeyword.cloudObj_list[cloudType].check_resource_status("VSwitch", lan_vswitch, "Available")
            server_Id = CloudKeyword.cloudObj_list[cloudType].create_after_pay_instance(imageId, sgroupId, wan_vswitch, availability_zone, serverName, flavorType)
            CloudKeyword.cloudObj_list[cloudType].check_instance_status(server_Id, "Stopped")
            lan_net = CloudKeyword.cloudObj_list[cloudType].create_networkInterface(lan_vswitch, sgroupId)
            CloudKeyword.cloudObj_list[cloudType].check_resource_status("NetworkInterfaceSet", lan_net, "Available")
            CloudKeyword.cloudObj_list[cloudType].attach_network_to_instance(lan_net, server_Id)
            return wan_vswitch, lan_vswitch, server_Id

    @staticmethod
    def create_azure_server(imageDisk_id, vpcName, sg_id, wanSubNetName, wanCIDR, lanSubNetName, lanCIDR, pubIpName, wanNicName, lanNicName, serverName, size):
        print("---------start to create azure server---------")
        wanSubnetInfo = CloudKeyword.cloudObj_list['azure_cloud'].create_subnet(vpcName, wanSubNetName, wanCIDR, sg_id)
        lanSubnetInfo = CloudKeyword.cloudObj_list['azure_cloud'].create_subnet(vpcName, lanSubNetName, lanCIDR, sg_id)
        print('wan-subnetInfo----{}\nlan-subnetInfo----{}\n'.format(wanSubnetInfo, lanSubnetInfo))
        publicIpInfo = CloudKeyword.cloudObj_list['azure_cloud'].create_publicIp(pubIpName)
        print('publicIpInfo----{}\n'.format(publicIpInfo))
        wanNicInfo = CloudKeyword.cloudObj_list['azure_cloud'].create_nic(wanNicName, sg_id, wanSubnetInfo.id, publicIpInfo.id)
        lanNicInfo = CloudKeyword.cloudObj_list['azure_cloud'].create_nic(lanNicName, sg_id, lanSubnetInfo.id)
        print('wan-nicInfo----{}\nlan-nicInfo----{}\n'.format(wanNicInfo, lanNicInfo))
        serverInfo = CloudKeyword.cloudObj_list['azure_cloud'].create_vm_by_disk(imageDisk_id, [wanNicInfo.id, lanNicInfo.id], serverName, size)
        return serverInfo.id, "azure", publicIpInfo.ip_address, lanSubnetInfo.id

    @staticmethod
    def create_azure_host(vm_user, vm_pwd, hostLanName, sg_id, lan_id, serverName, size):
        publicIpInfo = CloudKeyword.cloudObj_list['azure_cloud'].create_publicIp("hostLanPub")
        lanNicInfo = CloudKeyword.cloudObj_list['azure_cloud'].create_nic(hostLanName, sg_id, lan_id, publicIpInfo.id)
        serverInfo = CloudKeyword.cloudObj_list['azure_cloud'].create_linux_server(serverName, vm_user, vm_pwd, lanNicInfo.id, size)
        return serverInfo.id, publicIpInfo.ip_address

    @staticmethod
    def create_hw_host(imageId, sgroupId, vpcId, lanId, availability_zone, serverName, flavorType, floating_network_id):
        server_id = CloudKeyword.cloudObj_list["hw_cloud"].create_server(imageId, sgroupId, vpcId, [lanId], availability_zone, serverName, flavorType)
        ip_id, ip_addr = CloudKeyword.associate_ip_to_wan('hw_cloud', server_id, lanId, floating_network_id)
        return server_id, ip_id, ip_addr

    @staticmethod
    def create_ali_host(imageId, sgroupId, lan_vswitch, availability_zone, serverName, flavorType):
        server_Id = CloudKeyword.cloudObj_list['ali_cloud'].create_after_pay_instance(imageId, sgroupId, lan_vswitch, availability_zone, serverName, flavorType)
        ip_id, ip_addr = CloudKeyword.associate_ip_to_wan('ali_cloud', server_Id, lan_vswitch)
        return server_Id, ip_id, ip_addr

    @staticmethod
    def delete_azure_resource():
        print("------release all the resource-----")
        CloudKeyword.cloudObj_list['azure_cloud'].delete_allResource()

    @staticmethod
    def create_azure_resourceGroup():
        print("------create resourceGroup-----")
        CloudKeyword.cloudObj_list['azure_cloud'].create_resourceGroup()

    # create floating ip
    @staticmethod
    def associate_ip_to_wan(cloudType, server_id, wan_subnetId=None, floating_network_id=None):
        if cloudType == 'hw_cloud':
            port_id = CloudKeyword.cloudObj_list[cloudType].get_wan_interfaces_id(server_id, wan_subnetId)
            return CloudKeyword.cloudObj_list[cloudType].associate_ip_to_wan(port_id, floating_network_id)
        elif cloudType == 'ali_cloud':
            ipaddr, ipId = CloudKeyword.cloudObj_list[cloudType].allocate_floating_ip()
            CloudKeyword.cloudObj_list[cloudType].associate_eip(ipId, server_id)
            return ipId, ipaddr

    @staticmethod
    def start_ali_server(cloudType, server_id):
        if cloudType == 'hw_cloud':
            pass
        elif cloudType == 'ali_cloud':
            CloudKeyword.cloudObj_list[cloudType].start_instance(server_id)
            CloudKeyword.cloudObj_list[cloudType].check_instance_status(server_id)

    @staticmethod
    def check_ali_resource_status(cloudType, resourcetype, resourceid, status):
        CloudKeyword.cloudObj_list[cloudType].check_resource_status(resourcetype, resourceid, status)

    @staticmethod
    def delete_ip(cloudType, ipId):
        if cloudType == 'ali_cloud':
            CloudKeyword.cloudObj_list[cloudType].check_resource_status("EipAddress", ipId, "Available")
        print(CloudKeyword.cloudObj_list[cloudType].delete_ip(ipId))

    @staticmethod
    def delete_security_group(cloudType, sgId):
        print(CloudKeyword.cloudObj_list[cloudType].delete_security_group(sgId))

    @staticmethod
    def delete_subnet(cloudType, netId, **para):
        if cloudType == 'hw_cloud':
            vpcId = para["vpcId"]
            print(CloudKeyword.cloudObj_list[cloudType].delete_subnet(netId, vpcId))
        elif cloudType == 'ali_cloud':
            print(CloudKeyword.cloudObj_list[cloudType].delete_vswitch(netId))

    @staticmethod
    def delete_vpc(cloudType, vpcId):
        print(CloudKeyword.cloudObj_list[cloudType].delete_vpc(vpcId))

    @staticmethod
    def delete_image(cloudType, imageId):
        print(CloudKeyword.cloudObj_list[cloudType].delete_image(imageId))

    @staticmethod
    def delete_ali_Bucket(bucketName):
        print(CloudKeyword.cloudObj_list['ali_cloud'].delete_Bucket_and_file(bucketName))

    # delete server
    @staticmethod
    def delete_server(cloudType, server_id):
        print(CloudKeyword.cloudObj_list[cloudType].delete_server(server_id))
