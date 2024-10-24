from parserOcs.parser import ParserOcs
from parserKube.parser import ParserKube


class Migration:

    def __init__(self):
        pass

    def _parse_ocs(self, base_folder_path):
        parser_ocs = ParserOcs(base_folder_path)
        parser_ocs.parse_tf_files_in_folder()
        return parser_ocs.parsed_vars

    def _parse_kube(self, base_folder_path):
        parser_kube = ParserKube(base_folder_path)
        parser_kube.parse_k8s_files_in_folder()
        return parser_kube.parsed_vars
        pass

    def parser(self, base_type, base_folder_path):
        if base_type == "ocs":
            return self._parse_ocs(base_folder_path)

        if base_type == "kube":
            return self._parse_kube(base_folder_path)

        else:
            return {"error": "invalid base type"}


migration_engine = Migration()

# ocs
print("#####OCS#####")
base_folder_path = "terraform/infra"
parsed_response = migration_engine.parser("ocs", base_folder_path)
for key, value in parsed_response.items():
    print(f"{key}: {value}")

# priv k8s
print("#####Private K8s#####")
base_folder_path = "k8s"
parsed_response = migration_engine.parser("kube", base_folder_path)
for key, value in parsed_response.items():
    print(f"{key}: {value}")
