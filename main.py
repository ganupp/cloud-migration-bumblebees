import hcl2
import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

def parse_tf_files_in_folder(folder_path):
    parsed_vars = {}
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".tf"):
            tf_file_path = os.path.join(folder_path, filename)
            with open(tf_file_path, 'r') as tf_file:
                tf_config = hcl2.load(tf_file)
                variables = tf_config.get('variable', [])
                for var in variables:
                    if isinstance(var, dict): 
                        for key, value in var.items():
                            parsed_vars[key] = value.get('default', None)
    
    return parsed_vars

# Step 2: Create Azure Resource via Azure APIs
def create_azure_resource(parsed_vars):
    # Authenticate with Azure
    credential = DefaultAzureCredential()
    subscription_id = "<Your Azure Subscription ID>"

    # Initialize Resource Management Client
    resource_client = ResourceManagementClient(credential, subscription_id)

    # Extract values from parsed Terraform variables
    resource_group_name = parsed_vars.get("app_name", "my-resource-group")
    region = parsed_vars.get("region", "eastus")

    # Create Resource Group
    resource_group_params = {"location": region}
    
    print(f"Creating resource group '{resource_group_name}' in region '{region}'")
    
    resource_group_result = resource_client.resource_groups.create_or_update(
        resource_group_name, resource_group_params
    )
    
    print(f"Resource group created: {resource_group_result.id}")
    
    # Additional resources can be created here using other parsed variables

def main():
    # Path to the folder containing Terraform files
    tf_folder_path = "terraform/infra"
    
    # Step 1: Parse all the Terraform files in the folder to get the variables
    parsed_vars = parse_tf_files_in_folder(tf_folder_path)
    
    # Print all parsed variables
    print("Parsed Terraform Variables:")
    for key, value in parsed_vars.items():
        print(f"{key}: {value}")
    
    # Step 2: Create Azure resources using the parsed variables
    # create_azure_resource(parsed_vars)

if __name__ == "__main__":
    main()
