from importlib import import_module
yaml = import_module("yaml")
safe_dump, YAMLError, safe_load = yaml.safe_dump, yaml.YAMLError, yaml.safe_load
from os import path

def get_yaml_safely(file_path) -> dict:
    if not path.exists(file_path):
        return None

    try:
        with open(file_path, "r") as file:
            data = safe_load(file)
            return data
    except YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None