from collections import UserDict
from pathlib import Path

import yaml


class ConfigurationManager(UserDict):
    def __init__(self, config_path: Path = Path(__file__).parent.resolve()) -> None:
        super().__init__()
        config_file = config_path / f"application.yml"

        with open(config_file) as f:
            self.update(yaml.safe_load(f))


config_map = ConfigurationManager()
