from azure.mgmt.resource import ResourceManagementClient
from azure.identity import AzureCliCredential
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.sql import SqlManagementClient
from azure.common.client_factory import get_client_from_cli_profile
import os

credential = AzureCliCredential()

subscription_id = "880b615d-e130-4835-bb12-c6b33dcaec5b"

resource_client = ResourceManagementClient(credential, subscription_id)
RESOURCE_GROUP_NAME = "Python-RG"
LOCATION = "centralindia"
client = ResourceManagementClient(credential, subscription_id)
delete_async_operation = client.resource_groups.delete('Python-RG')
delete_async_operation.wait()

# rg_result = resource_client.resource_groups.(
#     "Python-RG",
#     {
#         "location": "centralindia"
#     }
# )

# print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")


# rg_result = resource_client.resource_groups.create_or_update(
#     "Python-RG",
#     {
#         "location": "centralindia",
#         "tags": { "environment":"test", "department":"tech" }
#     }
# )

# print(f"Updated resource group {rg_result.name} with tags")

# VNET_NAME = "vnet-01"
# SUBNET_NAME = "python--subnet"
# IP_NAME = "python-ip"
# IP_NAME1 = "python-ip1"
# IP_NAME2 = "python-ip2"
# IP_NAME3 = "python-ip3"
# IP_CONFIG_NAME = "python-ip-config"
# IP_CONFIG_NAME1 = "python-ip-config1"
# IP_CONFIG_NAME2 = "python-ip-config2"
# IP_CONFIG_NAME3 = "python-ip-config3"
# NIC_NAME = "python-nic"
# NIC_NAME1 = "python-nic1"
# NIC_NAME2 = "python-nic2"
# NIC_NAME3 = "python-nic3"
# LB_NAME = 'loadbalancer'
# frontend_ip = "fip"
# network_client = NetworkManagementClient(credential, subscription_id)

# poller = network_client.virtual_networks.begin_create_or_update(RESOURCE_GROUP_NAME,
#     VNET_NAME,
#     {
#         "location": LOCATION,
#         "address_space": {
#             "address_prefixes": ["10.0.0.0/16"]
#         }
#     }
# )

# vnet_result = poller.result()

# print(f"Provisioned virtual network {vnet_result.name} with address prefixes {vnet_result.address_space.address_prefixes}")


# poller = network_client.subnets.begin_create_or_update(RESOURCE_GROUP_NAME, 
#     VNET_NAME, SUBNET_NAME,
#     { "address_prefix": "10.0.0.0/24" }
# )
# subnet_result = poller.result()

# print(f"Provisioned virtual subnet {subnet_result.name} with address prefix {subnet_result.address_prefix}")


# poller = network_client.public_ip_addresses.begin_create_or_update(RESOURCE_GROUP_NAME,
#     IP_NAME,
#     {
#         "location": LOCATION,
#         "sku": { "name": "Standard" },
#         "public_ip_allocation_method": "Static",
#         "public_ip_address_version" : "IPV4"
#     }
# )

# ip_address_result = poller.result()
# poller1 = network_client.public_ip_addresses.begin_create_or_update(RESOURCE_GROUP_NAME,
#     IP_NAME1,
#     {
#         "location": LOCATION,
#         "sku": { "name": "Standard" },
#         "public_ip_allocation_method": "Static",
#         "public_ip_address_version" : "IPV4"
#     }
# )

# ip_address_result1 = poller1.result()
# poller2 = network_client.public_ip_addresses.begin_create_or_update(RESOURCE_GROUP_NAME,
#     IP_NAME2,
#     {
#         "location": LOCATION,
#         "sku": { "name": "Standard" },
#         "public_ip_allocation_method": "Static",
#         "public_ip_address_version" : "IPV4"
#     }
# )

# ip_address_result2 = poller2.result()
# poller3 = network_client.public_ip_addresses.begin_create_or_update(RESOURCE_GROUP_NAME,
#     IP_NAME3,
#     {
#         "location": LOCATION,
#         "sku": { "name": "Standard" },
#         "public_ip_allocation_method": "Static",
#         "public_ip_address_version" : "IPV4"
#     }
# )

# ip_address_result3 = poller3.result()

# print(f"Provisioned public IP address {ip_address_result.name} with address {ip_address_result.ip_address}")

# poller = network_client.network_interfaces.begin_create_or_update(RESOURCE_GROUP_NAME,
#     NIC_NAME, 
#     {
#         "location": LOCATION,
#         "ip_configurations": [ {
#             "name": IP_CONFIG_NAME,
#             "subnet": { "id": subnet_result.id },
#             "public_ip_address": {"id": ip_address_result.id }
#         }]
#     }
# )

# nic_result = poller.result()
# poller1 = network_client.network_interfaces.begin_create_or_update(RESOURCE_GROUP_NAME,
#     NIC_NAME1, 
#     {
#         "location": LOCATION,
#         "ip_configurations": [ {
#             "name": IP_CONFIG_NAME1,
#             "subnet": { "id": subnet_result.id },
#             "public_ip_address": {"id": ip_address_result1.id }
#         }]
#     }
# )

# nic_result1 = poller1.result()
# poller2 = network_client.network_interfaces.begin_create_or_update(RESOURCE_GROUP_NAME,
#     NIC_NAME2, 
#     {
#         "location": LOCATION,
#         "ip_configurations": [ {
#             "name": IP_CONFIG_NAME2,
#             "subnet": { "id": subnet_result.id },
#             "public_ip_address": {"id": ip_address_result2.id }
#         }]
#     }
# )

# nic_result2 = poller2.result()
# poller3 = network_client.network_interfaces.begin_create_or_update(RESOURCE_GROUP_NAME,
#     NIC_NAME3, 
#     {
#         "location": LOCATION,
#         "ip_configurations": [ {
#             "name": IP_CONFIG_NAME3,
#             "subnet": { "id": subnet_result.id },
#             "public_ip_address": {"id": ip_address_result3.id }
#         }]
#     }
# )

# nic_result3 = poller3.result()

# print(f"Provisioned network interface client {nic_result.name}")


# compute_client = ComputeManagementClient(credential, subscription_id)

# VM_NAME1 = "webVM1"
# USERNAME = "rukrukkhan"
# PASSWORD = "Pa$$w0rd24"

# VM_NAME2 = "webVM2"
# VM_NAME3 = "webVM3"
# VM_NAME4 = "webVM4"


# print(f"Provisioning virtual machine {VM_NAME1}; this operation might take a few minutes.")


# poller = compute_client.virtual_machines.begin_create_or_update(RESOURCE_GROUP_NAME, VM_NAME1,
#     {
#         "location": LOCATION,
#         "storage_profile": {
#             "image_reference": {
#                 'publisher': 'MicrosoftWindowsServer',
#                 'offer': 'WindowsServer',
#                 'sku': '2012-R2-Datacenter',
#                 'version': 'latest'
#             }
#         },
#         "hardware_profile": {
#             "vm_size": "Standard_DS1_v2"
#         },
#         "os_profile": {
#             "computer_name": VM_NAME1,
#             "admin_username": USERNAME,
#             "admin_password": PASSWORD
#         },
#         "network_profile": {
#             "network_interfaces": [{
#                 "id": nic_result.id,
#             }]
#         }
#     }
# )
# print(f"Provisioning virtual machine {VM_NAME2}; this operation might take a few minutes.")

# poller = compute_client.virtual_machines.begin_create_or_update(RESOURCE_GROUP_NAME, VM_NAME2,
#     {
#         "location": LOCATION,
#         "storage_profile": {
#             "image_reference": {
#                 'publisher': 'MicrosoftWindowsServer',
#                 'offer': 'WindowsServer',
#                 'sku': '2012-R2-Datacenter',
#                 'version': 'latest'
#             }
#         },
#         "hardware_profile": {
#             "vm_size": "Standard_DS1_v2"
#         },
#         "os_profile": {
#             "computer_name": VM_NAME2,
#             "admin_username": USERNAME,
#             "admin_password": PASSWORD
#         },
#         "network_profile": {
#             "network_interfaces": [{
#                 "id": nic_result1.id,
#             }]
#         }
#     }
# )
# print(f"Provisioning virtual machine {VM_NAME3}; this operation might take a few minutes.")

# poller = compute_client.virtual_machines.begin_create_or_update(RESOURCE_GROUP_NAME, VM_NAME3,
#     {
#         "location": LOCATION,
#         "storage_profile": {
#             "image_reference": {
#                 'publisher': 'MicrosoftWindowsServer',
#                 'offer': 'WindowsServer',
#                 'sku': '2012-R2-Datacenter',
#                 'version': 'latest'
#             }
#         },
#         "hardware_profile": {
#             "vm_size": "Standard_DS1_v2"
#         },
#         "os_profile": {
#             "computer_name": VM_NAME3,
#             "admin_username": USERNAME,
#             "admin_password": PASSWORD
#         },
#         "network_profile": {
#             "network_interfaces": [{
#                 "id": nic_result2.id,
#             }]
#         }
#     }
# )
# print(f"Provisioning virtual machine {VM_NAME4}; this operation might take a few minutes.")
# poller = compute_client.virtual_machines.begin_create_or_update(RESOURCE_GROUP_NAME, VM_NAME4,
#     {
#         "location": LOCATION,
#         "storage_profile": {
#             "image_reference": {
#                 'publisher': 'MicrosoftWindowsServer',
#                 'offer': 'WindowsServer',
#                 'sku': '2012-R2-Datacenter',
#                 'version': 'latest'
#             }
#         },
#         "hardware_profile": {
#             "vm_size": "Standard_DS1_v2"
#         },
#         "os_profile": {
#             "computer_name": VM_NAME4,
#             "admin_username": USERNAME,
#             "admin_password": PASSWORD
#         },
#         "network_profile": {
#             "network_interfaces": [{
#                 "id": nic_result3.id,
#             }]
#         }
#     }
# )
# vm_result = poller.result()

# print(f"Provisioned virtual machine {vm_result.name}")

# poller = network_client.load_balancers.begin_create_or_update(RESOURCE_GROUP_NAME, LB_NAME,
#     {
#         "location": LOCATION,
#         "sku": { "name": "Standard" },
#          "frontend_ip_configurations": [ {
#             "name": frontend_ip,
#             "subnet": {"id": subnet_result.id }
#         }]
            
#         }
# )
# lb_result = poller.result()

# SQL_SERVER = 'sqlserver-05'
# SQL_DB1 = 'APP DB-01'
# SQL_DB2 = 'APP DB-02'
# SQL_DB3 = 'APP DB-03'
# SQL_DB4 = 'APP DB-04'
# SQL_DB5 = 'APP DB-05'
# USERNAME = 'rukrukkhan'
# PASSWORD = 'Paav0515#'

# db_server_name = 'database'
# sql_client = get_client_from_cli_profile(SqlManagementClient)


# server = sql_client.servers.begin_create_or_update(
#     RESOURCE_GROUP_NAME,
#     SQL_SERVER,
#     {
#         'location': LOCATION,
#         'version': '12.0',
#         'administrator_login': USERNAME,
#         'administrator_login_password': PASSWORD
#     }
# )
# server_result = server.result()

# RULE_NAME = "allow_ip"
# ip_address = "PUBLIC_IP_ADDRESS"

# firstPoolName = "Elastic Pool"
# # secondPoolName = "App pool 02"

# elastic= sql_client.elastic_pools.begin_create_or_update(
#     RESOURCE_GROUP_NAME,
#     SQL_SERVER,
#    firstPoolName,
#    {
#        'location': LOCATION, 
#        'Database' :  'SQL_DB',
#      "dtu_storage" :  {
#       'Edition' : 'Standard',
#       'Dtu' :  '500',
#       'db_dtu_min': '0',
#       'db_dtu_max' :'4',
#       'pool_size': '2000'
#      }

#    }
# )
# elastic_result = elastic.result()

# database1 = sql_client.databases.begin_create_or_update(
#     RESOURCE_GROUP_NAME,
#     SQL_SERVER,
#     SQL_DB1,
#     {
#         'location': LOCATION,
#         'collation': 'SQL_Latin1_General_CP1_CI_AS',
#         'create_mode': 'default',
#         'requested_service_objective_name': 'Basic',
#         "elastic_pool_id": elastic_result.id

#     }
# )
# database_result1 = database1.result()

# database2 = sql_client.databases.begin_create_or_update(
#     RESOURCE_GROUP_NAME,
#     SQL_SERVER,
#     SQL_DB2,
#     {
#         'location': LOCATION,
#         'collation': 'SQL_Latin1_General_CP1_CI_AS',
#         'create_mode': 'default',
#         'requested_service_objective_name': 'Basic',
#         "elastic_pool_id": elastic_result.id

#     }
# )
# database_result2 = database2.result()
# database3 = sql_client.databases.begin_create_or_update(
#     RESOURCE_GROUP_NAME,
#     SQL_SERVER,
#     SQL_DB3,
#     {
#         'location': LOCATION,
#         'collation': 'SQL_Latin1_General_CP1_CI_AS',
#         'create_mode': 'default',
#         'requested_service_objective_name': 'Basic',
#         "elastic_pool_id": elastic_result.id

#     }
# )
# database_result3 = database3.result()
# database4 = sql_client.databases.begin_create_or_update(
#     RESOURCE_GROUP_NAME,
#     firstPoolName,
#     SQL_DB4,
#     {
#         'location': LOCATION,
#         'collation': 'SQL_Latin1_General_CP1_CI_AS',
#         'create_mode': 'default',
#         'requested_service_objective_name': 'Basic',
#         "elastic_pool_id": elastic_result.id
#     }
# )
# database_result4 = database4.result()
# database5 = sql_client.databases.begin_create_or_update(
#     RESOURCE_GROUP_NAME,
#     firstPoolName,
#     SQL_DB5,
#     {
#         'location': LOCATION,
#         'collation': 'SQL_Latin1_General_CP1_CI_AS',
#         'create_mode': 'default',
#         'requested_service_objective_name': 'Basic',
#         "elastic_pool_id": elastic_result.id
#     }
# )
# database_result5 = database5.result()
