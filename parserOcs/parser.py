import hcl2
import os


class ParserOcs:
    def __init__(self, folder_path):
        self.parsed_vars = {}
        self.folder_path = folder_path

    def parse_tf_files_in_folder(self):

        for filename in os.listdir(self.folder_path):
            if filename.endswith(".tf"):
                tf_file_path = os.path.join(self.folder_path, filename)
                with open(tf_file_path, "r") as tf_file:
                    tf_config = hcl2.load(tf_file)
                    variables = tf_config.get("variable", [])
                    for var in variables:
                        if isinstance(var, dict):
                            for key, value in var.items():
                                self.parsed_vars[key] = value.get("default", None)

        return self.parsed_vars


# def main():
#     # Path to the folder containing Terraform files
#     tf_folder_path = "terraform/infra"

#     # Step 1: Parse all the Terraform files in the folder to get the variables
#     self.parsed_vars = parse_tf_files_in_folder(tf_folder_path)

#     # Print all parsed variables
#     print("Parsed Terraform Variables:")
#     for key, value in self.parsed_vars.items():
#         print(f"{key}: {value}")

#     # Step 2: Create Azure resources using the parsed variables
#     # create_azure_resource(self.parsed_vars)

# if __name__ == "__main__":
#     main()
