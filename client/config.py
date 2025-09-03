import json
from pathlib import Path



cfg_path = str(Path(__file__).parent.resolve()) + "\\client.cfg"


print()

class ConfigManager():
    def __init__(self) -> None:
        self.reload_config()

    def reload_config(self):
        with open(cfg_path) as cfg:
            content = cfg.read()
        config = json.loads(content)
        self.host = config["host"]
        self.port = config["port"]

