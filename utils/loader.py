from yaml import safe_load

def load(file: str = "config/config.yml"):
    with open(file) as f:
        return safe_load(f)
