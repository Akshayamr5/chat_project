import json
import os


def load_config():
    config_path = os.path.join("app", "config", "client_config.json")

    with open(config_path, "r") as f:
        return json.load(f)