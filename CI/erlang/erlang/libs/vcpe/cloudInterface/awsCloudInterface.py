import boto3


class awsCloudInterface(object):
    def __init__(self):
        self.client = boto3.client('ec2')
        self.ec2 = boto3.resource('ec2')
        self.ebsClient = boto3.client('ebs')

    def create_vpc(self, vpcName, vpcCIDR):
        tagBody = [{
            'ResourceType': 'vpc',
            'Tags': [{
                'Key': 'Name',
                'Value': vpcName
            }]
        }]
        response = self.client.create_vpc(
            CidrBlock=vpcCIDR,
            TagSpecifications=tagBody
        )
        print('create vpc {} successful -----\n{}'.format(vpcName, response))
        return response['Vpc']['VpcId']

    def get_vpcObj(self, vpc_id):
        return self.ec2.Vpc(vpc_id)

    def create_internet_gateway(self):
        response = self.client.create_internet_gateway()
        print('create internet_gateway result-----\n{}'.format(response))
        return response['InternetGateway']['InternetGatewayId']

    def attach_internet_gateway_to_vpc(self, vpcObj, internetGatewayId):
        # vpc = ec2.Vpc(vpc_id)
        rt = vpcObj.attach_internet_gateway(InternetGatewayId=internetGatewayId)
        print('attach igw successful-----\n{}'.format(rt))

    def add_default_out_route(self, vpcObj, internetGatewayId):
        routeTable = list(vpcObj.route_tables.all())[0]
        route = routeTable.create_route(
            DestinationCidrBlock='0.0.0.0/0',
            GatewayId=internetGatewayId
        )
        print('add out route successful-----\n{}'.format(route))
        return route

    def create_security_group(self, sgrpName, vpcObj):
        sgroup = vpcObj.create_security_group(Description=sgrpName, GroupName=sgrpName)
        sgroup.authorize_ingress(
            IpPermissions=[{
                'IpProtocol': '-1',
                'IpRanges': [{
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'all is ok',
                }]
            }]
        )
        print('create {} and add all in rule successful-----\n{}'.format(sgrpName, sgroup))
        return sgroup.id

    def create_subnet(self, vpcObj, subName, subCIDR):
        tagBody = [{
            'ResourceType': 'subnet',
            'Tags': [{
                'Key': 'Name',
                'Value': subName
            }]
        }]
        subnet = vpcObj.create_subnet(
            AvailabilityZone='cn-north-1a',
            CidrBlock=subCIDR,
            TagSpecifications=tagBody
        )
        print('create {} subnet successful-----\n{}'.format(subName, subnet))
        return subnet.id

    def create_linux_server(self, image_id, serverType, sgroup_id, subnet_id, serverName):
        response = self.client.run_instances(
            BlockDeviceMappings=[{
                'DeviceName': '/dev/sdh',
                'Ebs': {
                    'VolumeSize': 2,
                    },
                }],
            ImageId=image_id,
            InstanceType=serverType,
            KeyName='aiwan_aws',
            MaxCount=1,
            MinCount=1,
            SecurityGroupIds=[sgroup_id],
            SubnetId=subnet_id,
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{
                    'Key': 'Name',
                    'Value': serverName,
                }],
            }],
        )
        print('create linux server success, wait server to be running-----\n{}'.format(response))
        instance = self.ec2.Instance(response['Instances'][0]['InstanceId'])
        instance.wait_until_running()
        print('server now is running')
        vList = list(instance.volumes.all())
        ebs = filter(lambda x: x.size == 2, vList)
        return response['Instances'][0], ebs[0].id

    def create_pubIp(self):
        response = self.client.allocate_address(
            Domain='vpc',
        )
        print('create public ip result-----\n{}'.format(response))
        return response['PublicIp'], response['AllocationId']

    def attach_pubIp_to_server(self, allocation_id, nic_id):
        response = self.client.associate_address(
            AllocationId=allocation_id,
            NetworkInterfaceId=nic_id,
        )
        print('attach pubIp to nic {} successful-----\n{}'.format(nic_id, response))

    def detach_ebs(self, v_id):
        response = self.client.detach_volume(VolumeId=v_id)
        print('detach ebs volume success-----\n{}'.format(response))

    def create_snapshot(self, v_id):
        response = self.client.create_snapshot(
            Description='This is netskyper snapshot.',
            VolumeId=v_id,
        )
        print('create snapshot success and wait snapshot to be completed-----\n{}'.format(response))
        snapshot = self.ec2.Snapshot(response['SnapshotId'])
        snapshot.wait_until_completed()
        print('snapshot now is completed')
        return response['SnapshotId']

    def create_image(self, snapshot_id, imageName):
        response = self.client.register_image(
            Architecture='x86_64',
            BlockDeviceMappings=[{
                'DeviceName': '/dev/sda1',
                'Ebs': {
                    'DeleteOnTermination': True,
                    'SnapshotId': snapshot_id,
                    'VolumeSize': 2,
                    'VolumeType': 'gp2'
                }
            }],
            Description=imageName,
            KernelId='aki-9e8f1da7',
            Name=imageName,
            RootDeviceName='/dev/sda1',
            VirtualizationType='paravirtual'
        )
        print('create image from snapshot success-----\n{}'.format(response))
        return response['ImageId']

    def create_server(self, image_id, serverType, sgroup_id, subnet_id, serverName, linux=True):
        if linux:
            response = self.client.run_instances(
                BlockDeviceMappings=[{
                    'DeviceName': '/dev/sdh',
                    'Ebs': {
                        'VolumeSize': 2,
                        },
                    }],
                ImageId=image_id,
                InstanceType=serverType,
                KeyName='aiwan_aws',
                MaxCount=1,
                MinCount=1,
                Placement={
                    'AvailabilityZone': 'cn-north-1a'
                },
                SecurityGroupIds=[sgroup_id],
                SubnetId=subnet_id,
                TagSpecifications=[{
                    'ResourceType': 'instance',
                    'Tags': [{
                        'Key': 'Name',
                        'Value': serverName,
                    }],
                }],
            )
            print('create linux server success, wait server to be running-----\n{}'.format(response))
        else:
            response = self.client.run_instances(
                ImageId=image_id,
                InstanceType=serverType,
                KeyName='aiwan_aws',
                MaxCount=1,
                MinCount=1,
                Placement={
                    'AvailabilityZone': 'cn-north-1a'
                },
                SecurityGroupIds=[sgroup_id],
                SubnetId=subnet_id,
                TagSpecifications=[{
                    'ResourceType': 'instance',
                    'Tags': [{
                        'Key': 'Name',
                        'Value': serverName,
                    }],
                }],
            )
            print('create server {} success, wait server to be running-----\n{}'.format(serverName, response))
        instance = self.ec2.Instance(response['Instances'][0]['InstanceId'])
        instance.wait_until_running()
        print('server now is running')
        return response['Instances'][0]

    def get_ebs_id(self, instance_id):
        instance = self.ec2.Instance(instance_id)
        vList = list(instance.volumes.all())
        ebs = filter(lambda x: x.size == 2, vList)
        return ebs[0].id

    def create_lan_nic_and_attach_to_server(self, subnet_id, sgroup_id, server_id):
        instance = self.ec2.Instance(server_id)
        instance.stop()
        instance.wait_until_stopped()
        subnet = self.ec2.Subnet(subnet_id)
        nic = subnet.create_network_interface(
            Description='netskyper-lan-networkinterface',
            Groups=[sgroup_id],
        )
        nic.attach(DeviceIndex=1, InstanceId=server_id)
        print('attach lan to server success')
        instance.start()
        instance.wait_until_running()
        return nic.id

    def terminated_server(self, instance_id):
        instance = self.ec2.Instance(instance_id)
        instance.terminate()
        instance.wait_until_terminated()

    def delete_nic(self, nic_id):
        nic = self.ec2.NetworkInterface(nic_id)
        nic.delete()

    def delete_vpc(self, vpc_id):
        vpc = self.ec2.Vpc(vpc_id)
        vpc.delete()

    def delete_sgroup(self, sgroup_id):
        security_group = self.ec2.SecurityGroup(sgroup_id)
        security_group.delete()

    def delete_igw(self, igw_id):
        internet_gateway = self.ec2.InternetGateway(igw_id)
        internet_gateway.delete()

    def delete_route(self, rt_id):
        route = self.ec2.Route(rt_id, '0.0.0.0/0')
        route.delete()

    def delete_subnet(self, subnet_id):
        subnet = self.ec2.Subnet(subnet_id)
        subnet.delete()

    def detach_igw(self, vpc_id, igw_id):
        vpc = self.ec2.Vpc(vpc_id)
        response = vpc.detach_internet_gateway(
            InternetGatewayId=igw_id,
        )
        print(response)

    def delete_ebs(self, ebs_id):
        volume = self.ec2.Volume(ebs_id)
        volume.delete()

    def delete_snapshot(self, snapshot_id):
        snapshot = self.ec2.Snapshot(snapshot_id)
        snapshot.delete()

    def delete_ami(self, ami_id):
        image = self.ec2.Image(ami_id)
        image.deregister()

    def delete_pub(self, pub_id):
        response = self.client.release_address(AllocationId=pub_id)
        print(response)
