import yaml

def load_config(path="{{ config_file_path }}"):
    with open(path, "r") as f:
        return yaml.safe_load(f)
