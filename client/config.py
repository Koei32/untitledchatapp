import json
from pathlib import Path


cur_path = str(Path(__file__).parent.resolve())
cfg_path = cur_path + "\\client.cfg"


class ConfigManager:
    def __init__(self) -> None:
        self.reload_config()
        with open(self.style_path + "client.qss") as qss:
            self.style = qss.read()

    def reload_config(self):
        with open(cfg_path) as cfg:
            content = cfg.read()
        config = json.loads(content)
        self.host = config["host"]
        self.port = config["port"]

        self.img_path = cur_path + config["paths"]["images"]
        self.style_path = cur_path + config["paths"]["styles"]
