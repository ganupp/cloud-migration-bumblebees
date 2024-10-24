import hcl2
import os
import yaml
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient


def parse_tf_files_in_folder(folder_path):
    parsed_vars = {}

    for filename in os.listdir(folder_path):
        if filename.endswith(".tf"):
            tf_file_path = os.path.join(folder_path, filename)
            with open(tf_file_path, "r") as tf_file:
                tf_config = hcl2.load(tf_file)
                variables = tf_config.get("variable", [])
                for var in variables:
                    if isinstance(var, dict):
                        for key, value in var.items():
                            parsed_vars[key] = value.get("default", None)

    return parsed_vars


def parse_k8s_files_in_folder(folder_path):
    parsed_k8s_info = {}

    for filename in os.listdir(folder_path):
        if filename.endswith((".yaml", ".yml")):
            k8s_file_path = os.path.join(folder_path, filename)

            with open(k8s_file_path, "r") as k8s_file:
                try:
                    k8s_config = yaml.safe_load(k8s_file)
                    kind = k8s_config.get("kind")
                    metadata = k8s_config.get("metadata", {})
                    name = metadata.get("name")
                    namespace = metadata.get("namespace")
                    labels = metadata.get("labels", {})

                    if kind == "Deployment":
                        parsed_k8s_info[name] = {
                            "kind": kind,
                            "namespace": namespace,
                            "labels": labels,
                            "annotations": metadata.get("annotations", {}),
                            "containers": {},
                        }

                        for container in k8s_config["spec"]["template"]["spec"].get(
                            "containers", []
                        ):
                            container_name = container["name"]
                            parsed_k8s_info[name]["containers"][container_name] = {
                                "image": container["image"],
                                "env_vars": {
                                    env_var["name"]: env_var.get("value")
                                    for env_var in container.get("env", [])
                                },
                            }

                    elif kind == "Service":
                        parsed_k8s_info[name] = {
                            "kind": kind,
                            "namespace": namespace,
                            "labels": labels,
                            "ports": k8s_config.get("spec", {}).get("ports", []),
                        }

                except yaml.YAMLError as e:
                    print(f"Error parsing YAML file {filename}: {e}")
                except KeyError as e:
                    print(f"Missing expected key in file {filename}: {e}")

    return parsed_k8s_info


# # Step 2: Create Azure Resource via Azure APIs
# def create_azure_resource(parsed_vars):
#     # Authenticate with Azure
#     credential = DefaultAzureCredential()
#     subscription_id = "<Your Azure Subscription ID>"

#     # Initialize Resource Management Client
#     resource_client = ResourceManagementClient(credential, subscription_id)

#     # Extract values from parsed Terraform variables
#     resource_group_name = parsed_vars.get("app_name", "my-resource-group")
#     region = parsed_vars.get("region", "eastus")

#     # Create Resource Group
#     resource_group_params = {"location": region}

#     print(f"Creating resource group '{resource_group_name}' in region '{region}'")

#     resource_group_result = resource_client.resource_groups.create_or_update(
#         resource_group_name, resource_group_params
#     )

#     print(f"Resource group created: {resource_group_result.id}")

#     # Additional resources can be created here using other parsed variables


def main():
    tf_folder_path = "terraform/infra"
    k8s_folder_path = "k8s"

    parsed_tf_vars = parse_tf_files_in_folder(tf_folder_path)

    parsed_k8s_vars = parse_k8s_files_in_folder(k8s_folder_path)

    print("Parsed Terraform Variables:")
    tf_dic = {}
    for key, value in parsed_tf_vars.items():
        tf_dic[key] = value
    print(tf_dic)

    print("\nParsed Kubernetes Environment Variables:")
    k8s_dic = {}
    for key, value in parsed_k8s_vars.items():
        k8s_dic[key] = value
    print(k8s_dic)

    # Step 2: Create Azure resources using the parsed variables
    # create_azure_resource(parsed_vars)


if __name__ == "__main__":
    main()
