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
RESOURCE_GROUP_NAME = "19"
LOCATION = "eastus2"

rg_result = resource_client.resource_groups.create_or_update(
    "19",
    {
        "location": "eastus2"
    }
)

print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")


rg_result = resource_client.resource_groups.create_or_update(
    "19",
    {
        "location": "eastus2",
        "tags": { "environment":"test", "department":"tech" }
    }
)

print(f"Updated resource group {rg_result.name} with tags")

VNET_NAME = "python-vnet"
SUBNET_NAME = "python--subnet"
SUBNET_NAME1 = "python--subnet1"
SUBNET_NAME2 = "python--subnet2"
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
FIP_NAME = 'frontendipname'

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

poller = network_client.subnets.begin_create_or_update(RESOURCE_GROUP_NAME, 
    VNET_NAME, SUBNET_NAME1,
    { "address_prefix": "10.0.1.0/24" }
)
subnet_result1 = poller.result()

poller = network_client.subnets.begin_create_or_update(RESOURCE_GROUP_NAME, 
    VNET_NAME, SUBNET_NAME2,
    { "address_prefix": "10.0.2.0/24" }
)
subnet_result2 = poller.result()

print(f"Provisioned virtual subnet {subnet_result.name} with address prefix {subnet_result.address_prefix}")


poller = network_client.public_ip_addresses.begin_create_or_update(RESOURCE_GROUP_NAME,
    IP_NAME,
    {
        "location": LOCATION,
        "sku": { "name": "Standard" },
        "public_ip_allocation_method": "Static",
        "public_ip_address_version" : "IPV4"
    }
)

ip_address_result = poller.result()
poller1 = network_client.public_ip_addresses.begin_create_or_update(RESOURCE_GROUP_NAME,
    IP_NAME1,
    {
        "location": LOCATION,
        "sku": { "name": "Standard" },
        "public_ip_allocation_method": "Static",
        "public_ip_address_version" : "IPV4"
    }
)

ip_address_result1 = poller1.result()
poller2 = network_client.public_ip_addresses.begin_create_or_update(RESOURCE_GROUP_NAME,
    IP_NAME2,
    {
        "location": LOCATION,
        "sku": { "name": "Standard" },
        "public_ip_allocation_method": "Static",
        "public_ip_address_version" : "IPV4"
    }
)

ip_address_result2 = poller2.result()
poller3 = network_client.public_ip_addresses.begin_create_or_update(RESOURCE_GROUP_NAME,
    IP_NAME3,
    {
        "location": LOCATION,
        "sku": { "name": "Standard" },
        "public_ip_allocation_method": "Static",
        "public_ip_address_version" : "IPV4"
    }
)

ip_address_result3 = poller3.result()
poller5 = network_client.public_ip_addresses.begin_create_or_update(RESOURCE_GROUP_NAME,
    FIP_NAME,
    {
        "location": LOCATION,
        "sku": { "name": "Basic" },
        "public_ip_allocation_method": "Dynamic",
        "public_ip_address_version" : "IPV4"
    }
)

ip_address_result5 = poller5.result()
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
poller1 = network_client.network_interfaces.begin_create_or_update(RESOURCE_GROUP_NAME,
    NIC_NAME1, 
    {
        "location": LOCATION,
        "ip_configurations": [ {
            "name": IP_CONFIG_NAME1,
            "subnet": { "id": subnet_result1.id },
            "public_ip_address": {"id": ip_address_result1.id }
        }]
    }
)

nic_result1 = poller1.result()
poller2 = network_client.network_interfaces.begin_create_or_update(RESOURCE_GROUP_NAME,
    NIC_NAME2, 
    {
        "location": LOCATION,
        "ip_configurations": [ {
            "name": IP_CONFIG_NAME2,
            "subnet": { "id": subnet_result2.id },
            "public_ip_address": {"id": ip_address_result2.id }
        }]
    }
)

nic_result2 = poller2.result()
poller3 = network_client.network_interfaces.begin_create_or_update(RESOURCE_GROUP_NAME,
    NIC_NAME3, 
    {
        "location": LOCATION,
        "ip_configurations": [ {
            "name": IP_CONFIG_NAME3,
            "subnet": { "id": subnet_result.id },
            "public_ip_address": {"id": ip_address_result3.id }
        }]
    }
)

nic_result3 = poller3.result()

print(f"Provisioned network interface client {nic_result.name}")


compute_client = ComputeManagementClient(credential, subscription_id)

VM_NAME1 = "webVM1"
USERNAME = "rukrukkhan"
PASSWORD = "Pa$$w0rd24"

VM_NAME2 = "webVM2"
VM_NAME3 = "webVM3"
VM_NAME4 = "webVM4"


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
print(f"Provisioning virtual machine {VM_NAME2}; this operation might take a few minutes.")

poller = compute_client.virtual_machines.begin_create_or_update(RESOURCE_GROUP_NAME, VM_NAME2,
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
            "computer_name": VM_NAME2,
            "admin_username": USERNAME,
            "admin_password": PASSWORD
        },
        "network_profile": {
            "network_interfaces": [{
                "id": nic_result1.id,
            }]
        }
    }
)
print(f"Provisioning virtual machine {VM_NAME3}; this operation might take a few minutes.")

poller = compute_client.virtual_machines.begin_create_or_update(RESOURCE_GROUP_NAME, VM_NAME3,
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
            "vm_size": "Standard_B2s"
        },
        "os_profile": {
            "computer_name": VM_NAME3,
            "admin_username": USERNAME,
            "admin_password": PASSWORD
        },
        "network_profile": {
            "network_interfaces": [{
                "id": nic_result2.id,
            }]
        }
    }
)
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

# lb_result = poller.result()

# print(f"Provisioned virtual machine {lb_result.name}")


SQL_SERVER = 'yourvirtualsqlserver'
SQL_DB = 'YOUR_SQLDB_NAME'
USERNAME = 'rukrukkhan'
PASSWORD = 'Paav0515#'

db_server_name = 'database55'
sql_client = get_client_from_cli_profile(SqlManagementClient)

# Create a SQL server
server = sql_client.servers.create_or_update(
    RESOURCE_GROUP_NAME,
    SQL_SERVER,
    {
        'location': LOCATION,
        'version': '12.0', # Required for create
        'administrator_login': USERNAME, # Required for create
        'administrator_login_password': PASSWORD # Required for create
    }
)
server_result = server.result()

RULE_NAME = "allow_ip"
ip_address = os.environ["PUBLIC_IP_ADDRESS"]

# For the above code, create an environment variable named PUBLIC_IP_ADDRESS that
# contains your workstation's public IP address as reported by a site like
# https://whatismyipaddress.com/.

# Provision the rule and wait for completion
poller = sql_client.firewall_rules.create_or_update(RESOURCE_GROUP_NAME,
    db_server_name, RULE_NAME,
    ip_address,  # Start ip range
    ip_address   # End ip range
)

firewall_rule = poller.result()

print(f"Provisioned firewall rule {firewall_rule.name}")
# Create a SQL database in the Basic tier
database = sql_client.databases.create_or_update(
    RESOURCE_GROUP_NAME,
    SQL_SERVER,
    SQL_DB,
    {
        'location': LOCATION,
        'collation': 'SQL_Latin1_General_CP1_CI_AS',
        'create_mode': 'default',
        'requested_service_objective_name': 'Basic'
    }
)
database_result = database.result()