from string import Template

class YamlGenerator:
    def __init__(self):
        pass

    def deployment(self, inputs={}):

        with open("scriptGenerators/deployment_template.yaml", "r") as file:
            deployment_template = Template(file.read())
            deployment_yaml = deployment_template.substitute(inputs)

        with open("deployment.yaml", "w") as output_file:
            output_file.write(deployment_yaml)


yaml_generator = YamlGenerator()
yaml_generator.deployment({'app_name':'my-app','replicas': 3,'container_name': 'my-app-container','image_name': 'my-app-image','image_tag': 'latest','container_port': 80,'env_var_name': 'MY_ENV_VAR','env_var_value': 'my_value'})
