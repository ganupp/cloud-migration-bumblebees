import requests
from azure.identity import ClientSecretCredential

tenant_id = "782ee8a9-08a6-4c1b-86f5-b083d7f1122f"
client_id = "f0bb51a4-067f-443f-b377-1a1d8631050b"
client_secret = "X0.8Q~ofyGd9-g3ylCU66G14XPayfvBS26SPRcBY"
subscription_id = "b69cd756-6fae-4e22-af13-639b77732f1d"
resource_group_name = "lastrescue"
location = "eastus"
deployment_name = "my-deployment"

# Authenticate and get the token
credential = ClientSecretCredential(
    tenant_id=tenant_id, client_id=client_id, client_secret=client_secret
)
token = credential.get_token("https://management.azure.com/.default").token

# Create Resource Group
url = f"https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}?api-version=2021-04-01"
payload = {"location": location}
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
response = requests.put(url, json=payload, headers=headers)
if response.status_code == 201:
    print("Resource Group created successfully.")
else:
    print(f"Error creating Resource Group: {response.json()}")

# # Deploy ARM Template
# url = f"https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deployments/{deployment_name}?api-version=2021-04-01"
# payload = {
#     "properties": {
#         "mode": "Incremental",
#         "template": {
#             "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
#             "contentVersion": "1.0.0.0",
#             "resources": [
#                 {
#                     "type": "Microsoft.Compute/virtualMachines",
#                     "apiVersion": "2021-03-01",
#                     "name": "[parameters('vmName')]",
#                     "location": "[parameters('location')]",
#                     "properties": {
#                         "hardwareProfile": {
#                             "vmSize": "[parameters('vmSize')]"
#                         },
#                         "storageProfile": {
#                             "imageReference": {
#                                 "publisher": "Canonical",
#                                 "offer": "UbuntuServer",
#                                 "sku": "18.04-LTS",
#                                 "version": "latest"
#                             }
#                         },
#                         "osProfile": {
#                             "computerName": "[parameters('vmName')]",
#                             "adminUsername": "[parameters('adminUsername')]",
#                             "adminPassword": "[parameters('adminPassword')]"
#                         },
#                         "networkProfile": {
#                             "networkInterfaces": [
#                                 {
#                                     "id": "[resourceId('Microsoft.Network/networkInterfaces', parameters('nicName'))]"
#                                 }
#                             ]
#                         }
#                     }
#                 }
#             ]
#         },
#         "parameters": {
#             "vmName": {"value": "myVM"},
#             "location": {"value": "eastus"},
#             "vmSize": {"value": "Standard_DS1_v2"},
#             "adminUsername": {"value": "azureuser"},
#             "adminPassword": {"value": "password123!"},
#             "nicName": {"value": "myNIC"}
#         }
#     }
# }
# response = requests.put(url, json=payload, headers=headers)
# if response.status_code == 201 or response.status_code == 202:
#     print("Deployment initiated successfully.")
# else:
#     print(f"Error initiating deployment: {response.json()}")

# # Check Deployment Status
# url = f"https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deployments/{deployment_name}?api-version=2021-04-01"
# response = requests.get(url, headers=headers)
# if response.status_code == 200:
#     deployment_status = response.json().get("properties", {}).get("provisioningState")
#     print(f"Deployment Status: {deployment_status}")
# else:
#     print(f"Error checking deployment status: {response.json()}")
