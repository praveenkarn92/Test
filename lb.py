
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import AzureCliCredential
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
import os

credential = AzureCliCredential()

subscription_id = "2f773cc5-3171-4039-a610-89797bb7df23"

resource_client = ResourceManagementClient(credential, subscription_id)
RESOURCE_GROUP_NAME = "002"
LOCATION = "westus2"

rg_result = resource_client.resource_groups.create_or_update(
    "002",
    {
        "location": "westus2"
    }
)

print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")


rg_result = resource_client.resource_groups.create_or_update(
    "002",
    {
        "location": "westus2",
        "tags": { "environment":"test", "department":"tech" }
    }
)

print(f"Updated resource group {rg_result.name} with tags")

VNET_NAME = "python-vnet"
SUBNET_NAME = "python--subnet"
IP_NAME = "python-ip"
FIP_NAME = "python-fip"
IP_CONFIG_NAME = "ip-config"
frontend_ip = "fip"
ADDRESS_POOL_NAME = "addr-pool"
PROBE_NAME = 'azure-sample-probe'
LB_RULE_NAME = 'azure-sample-lb-rule'

NETRULE_NAME_1 = 'azure-sample-netrule1'
NETRULE_NAME_2 = 'azure-sample-netrule2'

FRONTEND_PORT_1 = 21
FRONTEND_PORT_2 = 23
BACKEND_PORT = 22

NIC_NAME = "python-nic"
LB_NAME ="load_balancer"
VM_NAME = "webVM"
USERNAME = "rukrukkhan"
PASSWORD = "Pa$$w0rd24"

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




# poller = network_client.public_ip_addresses.begin_create_or_update(RESOURCE_GROUP_NAME,
#     FIP_NAME,
#     {
#         "location": LOCATION,
#         "sku": { "name": "Basic" },
#         "public_ip_allocation_method": "Static",
#         "public_ip_address_version" : "IPV4"
#     }
# )

ip_address_result = poller.result()
poller1 = network_client.public_ip_addresses.begin_create_or_update(RESOURCE_GROUP_NAME,
    IP_NAME,
    {
        "location": LOCATION,
        "sku": { "name": "Standard" },
        "public_ip_allocation_method": "Static",
        "public_ip_address_version" : "IPV4"
    }
)

ip_address_result1 = poller1.result()
# print(f"Provisioned public IP address {ip_address_result.name} with address {ip_address_result.ip_address}")

poller = network_client.network_interfaces.begin_create_or_update(RESOURCE_GROUP_NAME,
    NIC_NAME, 
    {
        "location": LOCATION,
        "ip_configurations": [ {
            "name": IP_CONFIG_NAME,
            "subnet": { "id": subnet_result.id },
            "public_ip_address": {"id": ip_address_result1.id }
        }]
    }
)

nic_result = poller.result()

print(f"Provisioned network interface client {nic_result.name}")
print(f"Provisioning virtual machine {VM_NAME}; this operation might take a few minutes.")

# Provision the VM specifying only minimal arguments, which defaults to an Ubuntu 18.04 VM
# on a Standard DS1 v2 plan with a public IP address and a default virtual network/subnet.
compute_client = ComputeManagementClient(credential, subscription_id)

poller = compute_client.virtual_machines.begin_create_or_update(RESOURCE_GROUP_NAME, VM_NAME,
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
            "computer_name": VM_NAME,
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
        "sku": { "name": "standard" },
        "tag": {"type":"internal"},
        # "public_ip_allocation_method":"static",
        # "public_ip_address_version" : "IPV4",
         
           "frontend_ip_configurations": [ {
            "name": frontend_ip,
            "subnet": {"id": subnet_result.id }
        }],
       "backend_address_pools" : [{
        'name': ADDRESS_POOL_NAME
                }],
        "probes" : [{
        'name': PROBE_NAME,
        'protocol': 'Http',
        'port': 80,
        'interval_in_seconds': 15,
        'number_of_probes': 4,
        'request_path': 'healthprobe.aspx'
    }],

    "load_balancing_rules" : [{
        'name': LB_RULE_NAME,
        'protocol': 'tcp',
        'frontend_port': 80,
        'backend_port': 80,
        'idle_timeout_in_minutes': 4,
        'enable_floating_ip': False,
        'load_distribution': 'Default',
        "frontend_ip_configurations": [ {
            "name": frontend_ip,
            "subnet": {"id": subnet_result.id }
        }]
        # },
        # 'backend_address_pool': {
        #     'id': construct_bap_id(subscription_id)
        # },
        # 'probe': {
        #     'id': construct_probe_id(subscription_id)
        # }
    }],

    "inbound_nat_rules": [{
        'name': NETRULE_NAME_1,
        'protocol': 'tcp',
        'frontend_port': FRONTEND_PORT_1,
        'backend_port': BACKEND_PORT,
        'enable_floating_ip': False,
        'idle_timeout_in_minutes': 4,
        'frontend_ip_configuration': {
            'id': construct_fip_id(subscription_id)
        }
    }],

    "inbound_nat_rules.append"({
        'name': NETRULE_NAME_2,
        'protocol': 'tcp',
        'frontend_port': FRONTEND_PORT_2,
        'backend_port': BACKEND_PORT,
        'enable_floating_ip': False,
        'idle_timeout_in_minutes': 4,
        "frontend_ip_configurations": [{
            "name": frontend_ip,
            "subnet": {"id": subnet_result.id }
        }]
        
    })
    }
)
lb_result = poller.result()

