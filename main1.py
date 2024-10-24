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


def main():
    tf_folder_path = "terraform/infra"
    parsed_vars = parse_tf_files_in_folder(tf_folder_path)
    print("Parsed Terraform Variables:")
    d ={}
    for key, value in parsed_vars.items():
        d[key] = value
    print(d)

if __name__ == "__main__":
    main()