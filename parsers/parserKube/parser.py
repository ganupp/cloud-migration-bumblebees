import hcl2
import os
import yaml


class ParserKube:
    def __init__(self, folder_path):
        self.parsed_vars = {}
        self.folder_path = folder_path

    def parse_k8s_files_in_folder(self):

        for filename in os.listdir(self.folder_path):
            if filename.endswith((".yaml", ".yml")):
                k8s_file_path = os.path.join(self.folder_path, filename)

                with open(k8s_file_path, "r") as k8s_file:
                    try:
                        k8s_config = yaml.safe_load(k8s_file)
                        kind = k8s_config.get("kind")
                        metadata = k8s_config.get("metadata", {})
                        name = metadata.get("name")
                        namespace = metadata.get("namespace")
                        labels = metadata.get("labels", {})

                        if kind == "Deployment":
                            self.parsed_vars[name] = {
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
                                self.parsed_vars[name]["containers"][container_name] = {
                                    "image": container["image"],
                                    "env_vars": {
                                        env_var["name"]: env_var.get("value")
                                        for env_var in container.get("env", [])
                                    },
                                }

                        elif kind == "Service":
                            self.parsed_vars[name] = {
                                "kind": kind,
                                "namespace": namespace,
                                "labels": labels,
                                "ports": k8s_config.get("spec", {}).get("ports", []),
                            }

                    except yaml.YAMLError as e:
                        print(f"Error parsing YAML file {filename}: {e}")
                    except KeyError as e:
                        print(f"Missing expected key in file {filename}: {e}")
