from azure.mgmt.resource import ResourceManagementClient
from azure.identity import AzureCliCredential
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.sql import SqlManagementClient
from azure.common.client_factory import get_client_from_cli_profile
from azure.core.exceptions import (
    ServiceRequestError,
    ResourceNotFoundError,
    AzureError
)

import os

credential = AzureCliCredential()

subscription_id = "2f773cc5-3171-4039-a610-89797bb7df23"

resource_client = ResourceManagementClient(credential, subscription_id)
RESOURCE_GROUP_NAME = "007"
LOCATION = "eastus2"

rg_result = resource_client.resource_groups.create_or_update(
    "007",
    {
        "location": "eastus2"
    }
)

print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")


rg_result = resource_client.resource_groups.create_or_update(
    "007",
    {
        "location": "eastus2",
        "tags": { "environment":"test", "department":"tech" }
    }
)

print(f"Updated resource group {rg_result.name} with tags")



network_client = NetworkManagementClient(credential, subscription_id)
SQL_SERVER = 'sqlserver-07'
SQL_DB1 = 'APP DB-01'
SQL_DB2 = 'APP DB-02'
SQL_DB3 = 'APP DB-03'
SQL_DB4 = 'APP DB-04'
USERNAME = 'rukrukkhan'
PASSWORD = 'Paav0515#'

db_server_name = 'database55'
sql_client = get_client_from_cli_profile(SqlManagementClient)


server = sql_client.servers.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    SQL_SERVER,
    {
        'location': LOCATION,
        'version': '12.0',
        'administrator_login': USERNAME,
        'administrator_login_password': PASSWORD
    }
)
server_result = server.result()

RULE_NAME = "allow_ip"
ip_address = "PUBLIC_IP_ADDRESS"

firstPoolName = "App pool-01"
secondPoolName = "App pool 02"


# elastic1= sql_client.elastic_pools.begin_create_or_update(
#     RESOURCE_GROUP_NAME,
#     SQL_SERVER,
#    secondPoolName,
#    {
#        'location': LOCATION,   
#      "DTU_Storage" : {
#       'Edition' : 'Standard',
#       'dtu' :  '200',
#       'db_dtu_min'  : '0',
#       'db_dtu_max'   :'2',
#       'pool_size': '2000'
#      }

#    }
# )
# elastic_result = elastic1.result()

elastic= sql_client.elastic_pools.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    SQL_SERVER,
   firstPoolName,
   {
       'location': LOCATION, 
    #    'Database' :  'SQL_DB',
     "dtu_storage" :  {
      'Edition' : 'Standard',
      'Dtu' :  '200',
      'db_dtu_min': '0',
      'db_dtu_max' :'4',
      'pool_size': '200'
     }

   }
)
elastic_result = elastic.result()

database = sql_client.databases.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    SQL_SERVER,
    SQL_DB1,
    {
        'location': LOCATION,
        'collation': 'SQL_Latin1_General_CP1_CI_AS',
        'create_mode': 'default',
        'requested_service_objective_name': 'Basic',
        "elastic_pool_id": elastic_result.id

    }
)
database_result = database.result()

database1 = sql_client.databases.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    SQL_SERVER,
    SQL_DB2,
    {
        'location': LOCATION,
        'collation': 'SQL_Latin1_General_CP1_CI_AS',
        'create_mode': 'default',
        'requested_service_objective_name': 'Basic',
        # "elastic_pool_id": elastic_result.id

    }
)
database_result1 = database1.result()
database2 = sql_client.databases.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    SQL_SERVER,
    SQL_DB3,
    {
        'location': LOCATION,
        'collation': 'SQL_Latin1_General_CP1_CI_AS',
        'create_mode': 'default',
        'requested_service_objective_name': 'Basic',
        # "elastic_pool_id": elastic_result.id

    }
)
database_result2 = database2.result()
database3 = sql_client.databases.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    firstPoolName,
    SQL_DB4,
    {
        'location': LOCATION,
        'collation': 'SQL_Latin1_General_CP1_CI_AS',
        'create_mode': 'default',
        'requested_service_objective_name': 'Basic',
        # "elastic_pool_id": elastic_result.id
    }
)
database_result3 = database3.result()

