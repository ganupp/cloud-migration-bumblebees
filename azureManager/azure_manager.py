import requests
import json
from . import constants


class Manager:
    def __init__(self):
        self.client_id = constants.CLIENT_ID
        self.client_secret = constants.CLIENT_SECRET
        self.subscription_id = constants.SUBSCRIPTION_ID
        self.resource_group_name = constants.RESOURCE_GROUP_NAME
        self.tenant_id = constants.TENANT_ID

    def token_gen(self):
        url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/token"

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "resource": "https://management.azure.com/",
        }

        response = requests.request(
            "POST", url, headers=headers, data=payload, verify=False
        )
        self.bearer_token = json.loads(response.text)["access_token"]

    def get_aks(self, cluster_name):
        url = f"https://management.azure.com/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{cluster_name}?api-version=2024-08-01"
        headers = {"Authorization": f"Bearer {self.bearer_token}"}
        response = requests.get(url, headers=headers)
        return response.json()

    def create_aks(
        self,
        cluster_name,
        location,
        dns_prefix,
        node_pool_name,
        node_count,
        vm_size,
        os_type,
    ):
        url = f"https://management.azure.com/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{cluster_name}?api-version=2023-09-01"
        headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json",
        }
        payload = {
            "location": location,
            "properties": {
                "dnsPrefix": dns_prefix,
                "agentPoolProfiles": [
                    {
                        "name": node_pool_name,
                        "count": int(node_count),
                        "vmSize": vm_size,
                        "osType": os_type,
                        "mode": "System",
                    }
                ],
                "servicePrincipalProfile": {
                    "clientId": self.client_id,
                    "secret": self.client_secret,
                },
            },
        }

        response = requests.request(
            "PUT", url, headers=headers, data=json.dumps(payload), verify=False
        )
        return response.json()


# print(requests_instance.create_aks(name="it-works", location="australiacentral", dnsPrefix="myakscluster", pool_name="nodepool2", count="1", vmSize="Standard_DS2_v2", osType="Linux"))
