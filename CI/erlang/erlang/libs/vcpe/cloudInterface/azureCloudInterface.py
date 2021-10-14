"""Create and manage virtual machines.

This script expects that the following environment vars are set:

AZURE_TENANT_ID: your Azure Active Directory tenant id or domain
AZURE_CLIENT_ID: your Azure Active Directory Application Client ID
AZURE_CLIENT_SECRET: your Azure Active Directory Application Secret
AZURE_SUBSCRIPTION_ID: your Azure Subscription Id
"""
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from msrestazure.azure_cloud import AZURE_CHINA_CLOUD
import os


class azureCloudInterface(object):
    def __init__(self, client_id, secret, location, tenant_id, subscription_id, resourceGrpName):
        self.location = location
        self.resourceGrpName = resourceGrpName
        subscription_id = subscription_id
        credentials = ServicePrincipalCredentials(
            client_id=client_id,
            secret=secret,
            tenant=tenant_id,
            china=True
        )
        self.resource_client = ResourceManagementClient(credentials, subscription_id, base_url=AZURE_CHINA_CLOUD.endpoints.resource_manager)
        self.compute_client = ComputeManagementClient(credentials, subscription_id, base_url=AZURE_CHINA_CLOUD.endpoints.resource_manager)
        self.network_client = NetworkManagementClient(credentials, subscription_id, base_url=AZURE_CHINA_CLOUD.endpoints.resource_manager)

    def create_vnet(self, vNetName, vNetCIDR):
        # Create VNet
        print('\nCreate Vnet')
        async_vnet_creation = self.network_client.virtual_networks.create_or_update(
            self.resourceGrpName,
            vNetName,
            {
                'location': self.location,
                'address_space': {
                    'address_prefixes': [vNetCIDR]
                }
            }
        )
        async_vnet_creation.wait()
        return async_vnet_creation.result()

    def create_sgroup_with_rule(self, sgroupName):
        body = {
            "properties": {
                "securityRules": [{
                    "name": "rule1",
                    "properties": {
                        "protocol": "*",
                        "sourceAddressPrefix": "*",
                        "destinationAddressPrefix": "*",
                        "access": "Allow",
                        "destinationPortRange": "*",
                        "sourcePortRange": "*",
                        "priority": 130,
                        "direction": "Inbound"
                    }
                }]
            },
            "location": self.location
        }
        aysn_create_sgroup = self.network_client.network_security_groups.create_or_update(self.resourceGrpName, sgroupName, body)
        aysn_create_sgroup.wait()
        return aysn_create_sgroup.result()

    def create_subnet(self, vNetName, subnetName, subnetCIDR, sgroup_id):
        # Create Subnet
        print('\nCreate Subnet')
        body = {
            "properties": {
                "addressPrefix": subnetCIDR,
                "NetworkSecurityGroup": {
                    'id': sgroup_id
                }
            }
        }
        async_subnet_creation = self.network_client.subnets.create_or_update(self.resourceGrpName, vNetName, subnetName, body)
        return async_subnet_creation.result()

    def create_nic(self, wan_nic_name, sgroup_id, subnet_id, pubIp_id=None):
        # Create NIC
        print('\nCreate NIC')
        ipJson = {
            'name': "wan_ip_name",
            'subnet': {
                'id': subnet_id
            },
            "NetworkSecurityGroup": {
                'id': sgroup_id
            }
        }
        if pubIp_id:
            pubIpDic = {
                "id": pubIp_id
            }
            ipJson['publicIPAddress'] = pubIpDic
        body = {
            'location': self.location,
            'ip_configurations': [ipJson]
        }
        async_nic_creation = self.network_client.network_interfaces.create_or_update(self.resourceGrpName, wan_nic_name, body)
        return async_nic_creation.result()

    def create_resourceGroup(self):
        print('\nCreate Resource Group')
        self.resource_client.resource_groups.create_or_update(
            self.resourceGrpName, {'location': self.location})

# imageId, sgroupId, vpcId, wan_subnetId, lan_subnetId, availability_zone, serverName, flavorType
# imageDisk_id = "/subscriptions/11fbc75d-96a0-40d5-803e-4aaef769f9a6/resourceGroups/netskyperRes/providers/Microsoft.Compute/disks/netskyperDisk"
# size = Standard_B1s
    def create_vm_by_disk(self, imageDisk_id, netList, serverName, size):
        # nic = create_nic(network_client)

        def get_net_iface_list(net_id, primary):
            netBody = {
                'id': net_id,
                "properties": {
                    "primary": primary
                }
            }
            return netBody
        primaryList = [True if netList.index(x) == 0 else False for x in netList]
        network_interfacesList = map(lambda x, y: get_net_iface_list(x, y), netList, primaryList)

        print('\nCreating vCPE Machine')
        body = {
            'location': self.location,
            'hardware_profile': {
                'vm_size': size
            },
            'storage_profile': {
                "osDisk": {
                    "osType": "Linux",
                    "caching": "ReadWrite",
                    "managedDisk": {
                        "id": imageDisk_id,
                        "storageAccountType": "StandardSSD_LRS"
                        },
                    "name": "netskyperDisk",
                    "createOption": "Attach"
                }
            },
            'network_profile': {
                'network_interfaces': network_interfacesList
            },
        }
        async_vm_creation = self.compute_client.virtual_machines.create_or_update(self.resourceGrpName, serverName, body)
        async_vm_creation.wait()
        return async_vm_creation.result()

    def create_linux_server(self, vm_name, vm_user, vm_pwd, nic_id, size):
        vm_parameter = {
            'location': self.location,
            'os_profile': {
                'computer_name': vm_name,
                'admin_username': vm_user,
                'admin_password': vm_pwd
            },
            'hardware_profile': {
                'vm_size': size
            },
            'storage_profile': {
                'image_reference': {
                    'publisher': 'Canonical',
                    'offer': 'UbuntuServer',
                    'sku': '16.04.0-LTS',
                    'version': 'latest'
                },
            },
            'network_profile': {
                'network_interfaces': [{
                    'id': nic_id,
                }]
            },
        }
        async_vm_creation = self.compute_client.virtual_machines.create_or_update(self.resourceGrpName, vm_name, vm_parameter)
        async_vm_creation.wait()
        return async_vm_creation.result()

    def create_publicIp(self, ipName):
        body = {
            "properties": {
                "publicIPAllocationMethod": "Static",
                "idleTimeoutInMinutes": 10,
                "publicIPAddressVersion": "IPv4"
            },
            "sku": {
                "name": "Standard"
            },
            "location": self.location
        }
        async_ip_creation = self.network_client.public_ip_addresses.create_or_update(self.resourceGrpName, ipName, body)
        async_ip_creation.wait()
        return async_ip_creation.result()

    def delete_allResource(self):
        print('\nDelete Resource Group')
        delete_async_operation = self.resource_client.resource_groups.delete(
            self.resourceGrpName)
        delete_async_operation.wait()
        print("\nDeleted: {}".format(self.resourceGrpName))

    def create_disk_by_vhdFile(self, imageFilePath, azcopyToolPath, imageDiskName):
        cmd = 'ls -l {} | awk '.format(imageFilePath) + r"'{print $5}'"
        print(cmd)
        # get imageFile bytesize
        result = os.popen(cmd).read().splitlines()[0]
        body = {
            "location": "chinanorth2",
            "properties": {
                "creationData": {
                    "createOption": "Upload",
                    "uploadSizeBytes": result
                },
                "osType": "linux"
            },
            "sku": {
                "name": "StandardSSD_LRS"
            }
        }
        disk_create = self.compute_client.disks.create_or_update(self.resourceGrpName, imageDiskName, body)
        print('create disk successful')
        disk_sas = self.compute_client.disks.grant_access(self.resourceGrpName, imageDiskName, "Write", 86400)
        print('get access successful')
        print(disk_create.result())
        print(disk_sas.result())
        # start to copy localfile to azure disk
        cmd = '{} copy {} \'{}\''.format(azcopyToolPath, imageFilePath, disk_sas.result().access_sas)
        print(cmd)
        os.system(cmd)
        self.compute_client.disks.revoke_access(self.resourceGrpName, imageDiskName)
        disk = self.compute_client.disks.get(self.resourceGrpName, imageDiskName)
        print(disk)
