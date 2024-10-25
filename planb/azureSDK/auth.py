from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient


credential = DefaultAzureCredential()
subscription_id = "b69cd756-6fae-4e22-af13-639b77732f1d"

resource_client = ResourceManagementClient(credential, subscription_id)
compute_client = ComputeManagementClient(credential, subscription_id)

tenant_id = "782ee8a9-08a6-4c1b-86f5-b083d7f1122f"
client_id = "f0bb51a4-067f-443f-b377-1a1d8631050b"
client_secret = "X0.8Q~ofyGd9-g3ylCU66G14XPayfvBS26SPRcBY"
subscription_id = "b69cd756-6fae-4e22-af13-639b77732f1d"

# Create a credential object
credential = ClientSecretCredential(
    tenant_id=tenant_id, client_id=client_id, client_secret=client_secret
)

# Use the credential to get a token and authenticate with Azure SDK
resource_client = ResourceManagementClient(credential, subscription_id)

resource_groups = resource_client.resource_groups.list()
for rg in resource_groups:
    print(rg.name)

token = credential.get_token("https://management.azure.com/.default")

# Print the token
print(f"Access Token: {token.token}")


resource_group_name = "finalrescue"
location = "eastus"

resource_group_params = {"location": location}
resource_client.resource_groups.create_or_update(
    resource_group_name, resource_group_params
)
