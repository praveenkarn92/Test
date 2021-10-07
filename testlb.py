from azure.mgmt.resource import ResourceManagementClient
from azure.identity import AzureCliCredential
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.sql import SqlManagementClient
from azure.common.client_factory import get_client_from_cli_profile
import os

credential = AzureCliCredential()

subscription_id = "2f773cc5-3171-4039-a610-89797bb7df23"

resource_client = ResourceManagementClient(credential, subscription_id)
RESOURCE_GROUP_NAME = "Python-RG"
LOCATION = "eastus2"
# Optional lines to delete the resource group. begin_delete is asynchronous.
# poller = resource_client.resource_groups.begin_delete(rg_result.name)
# result = poller.result()

rg_result = resource_client.resource_groups.create_or_update(
    "Python-RG",
    {
        "location": "eastus2"
    }
)

print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")


rg_result = resource_client.resource_groups.create_or_update(
    "Python-RG",
    {
        "location": "eastus2",
        "tags": { "environment":"test", "department":"tech" }
    }
)

print(f"Updated resource group {rg_result.name} with tags")

VNET_NAME = "vnet-01"
SUBNET_NAME = "python--subnet"
IP_NAME = "python-ip"
IP_NAME1 = "python-ip1"
IP_NAME2 = "python-ip2"
IP_NAME3 = "python-ip3"
IP_CONFIG_NAME = "python-ip-config"
IP_CONFIG_NAME1 = "python-ip-config1"
IP_CONFIG_NAME2 = "python-ip-config2"
IP_CONFIG_NAME3 = "python-ip-config3"
NIC_NAME = "python-nic"
NIC_NAME1 = "python-nic1"
NIC_NAME2 = "python-nic2"
NIC_NAME3 = "python-nic3"
LB_NAME = 'loadbalancer'
frontend_ip = "fip"
network_client = NetworkManagementClient(credential, subscription_id)

poller = network_client.virtual_networks.begin_create_or_update(RESOURCE_GROUP_NAME,
    VNET_NAME,
    {
        "location": LOCATION,
        "address_space": {
            "address_prefixes": ["10.0.0.0/16"]
        }
    }
)

vnet_result = poller.result()

print(f"Provisioned virtual network {vnet_result.name} with address prefixes {vnet_result.address_space.address_prefixes}")


poller = network_client.subnets.begin_create_or_update(RESOURCE_GROUP_NAME, 
    VNET_NAME, SUBNET_NAME,
    { "address_prefix": "10.0.0.0/24" }
)
subnet_result = poller.result()

print(f"Provisioned virtual subnet {subnet_result.name} with address prefix {subnet_result.address_prefix}")


poller = network_client.public_ip_addresses.begin_create_or_update(RESOURCE_GROUP_NAME,
    IP_NAME,
    {
        "location": LOCATION,
        "sku": { "name": "basic" },
        "public_ip_allocation_method": "Dynamic",
        "public_ip_address_version" : "IPV4"
    }
)

ip_address_result = poller.result()



print(f"Provisioned public IP address {ip_address_result.name} with address {ip_address_result.ip_address}")

poller = network_client.network_interfaces.begin_create_or_update(RESOURCE_GROUP_NAME,
    NIC_NAME, 
    {
        "location": LOCATION,
        "ip_configurations": [ {
            "name": IP_CONFIG_NAME,
            "subnet": { "id": subnet_result.id },
            "public_ip_address": {"id": ip_address_result.id }
        }]
    }
)

nic_result = poller.result()


print(f"Provisioned network interface client {nic_result.name}")


compute_client = ComputeManagementClient(credential, subscription_id)

VM_NAME1 = "webVM1"
USERNAME = "rukrukkhan"
PASSWORD = "Pa$$w0rd24"



print(f"Provisioning virtual machine {VM_NAME1}; this operation might take a few minutes.")


poller = compute_client.virtual_machines.begin_create_or_update(RESOURCE_GROUP_NAME, VM_NAME1,
    {
        "location": LOCATION,
        "storage_profile": {
            "image_reference": {
                'publisher': 'MicrosoftWindowsServer',
                'offer': 'WindowsServer',
                'sku': '2012-R2-Datacenter',
                'version': 'latest'
            }
        },
        "hardware_profile": {
            "vm_size": "Standard_DS1_v2"
        },
        "os_profile": {
            "computer_name": VM_NAME1,
            "admin_username": USERNAME,
            "admin_password": PASSWORD
        },
        "network_profile": {
            "network_interfaces": [{
                "id": nic_result.id,
            }]
        }
    }
)

vm_result = poller.result()

print(f"Provisioned virtual machine {vm_result.name}")

poller = network_client.load_balancers.begin_create_or_update(RESOURCE_GROUP_NAME, LB_NAME,
    {
        "location": LOCATION,
        "sku": { "name": "basic" },
         "frontend_ip_configurations": [ {
            "name": frontend_ip,
            "subnet": {"id": subnet_result.id }
        }]
            
        }
)
lb_result = poller.result()









