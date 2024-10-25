from parsers.parserOcs.parser import ParserOcs
from parsers.parserKube.parser import ParserKube
from azureManager.azure_manager import Manager
from scriptGenerators.yaml import YamlGenerator


class Migration:

    def __init__(self):
        self.parse_vars = {}

    def _parse_ocs(self, base_folder_path):
        parser_ocs = ParserOcs(base_folder_path)
        parser_ocs.parse_tf_files_in_folder()
        return parser_ocs.parsed_vars

    def _parse_kube(self, base_folder_path):
        parser_kube = ParserKube(base_folder_path)
        parser_kube.parse_k8s_files_in_folder()
        return parser_kube.parsed_vars

    def parser(self, base_type, base_folder_path):
        if base_type == "ocs":
            self.parse_vars = self._parse_ocs(base_folder_path)
            return self.parse_vars

        if base_type == "kube":
            self.parse_vars = self._parse_kube(base_folder_path)
            return self.parse_vars

        else:
            return {"error": "invalid base type"}

    def set_up_aks(self, base_type):
        self.azure_instance = Manager()
        self.azure_instance.token_gen()

        if base_type == "ocs":
            self.azure_instance.create_aks(
                cluster_name=self.parse_vars["app_name"],
                location="australiacentral",
                dns_prefix="myakscluster",
                node_pool_name="nodepool2",
                node_count="1",
                vm_size="Standard_DS2_v2",
                os_type="Linux",
            )

        if base_type == "kube":
            pass
    
    def generate_yaml(self, base_type):
        self.yaml_generator = YamlGenerator()

        if base_type == "ocs":
            self.yaml_generator.deployment({'app_name':self.parse_vars["app_name"],'replicas': 1,'container_name': f'{self.parse_vars["app_name"]}container','image_name': 'my-app-image','image_tag': 'latest','container_port': 80,'env_var_name': 'MY_ENV_VAR','env_var_value': 'my_value'})

        if base_type == "kube":
            pass

migration_engine = Migration()

# ocs
base_folder_path = "base-appl/terraform/infra"
parsed_response = migration_engine.parser("ocs", base_folder_path)
# for key, value in parsed_response.items():
#     print(f"{key}: {value}")

migration_engine.set_up_aks("ocs")
migration_engine.generate_yaml("ocs")

# priv k8s
base_folder_path = "base-appl/k8s"
parsed_response = migration_engine.parser("kube", base_folder_path)
# for key, value in parsed_response.items():
#     print(f"{key}: {value}")


print("Success")
