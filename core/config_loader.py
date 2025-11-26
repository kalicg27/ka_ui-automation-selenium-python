import yaml
from pathlib import Path

class Config:
    def __init__(self, path: str = "config/config.yaml"):
        config_path = Path(path)
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        self.base_url: str = data.get("base_url")
        self.browser: str = data.get("browser", "chrome")
        self.implicit_wait: int = data.get("implicit_wait", 5)
        self.page_load_timeout: int = data.get("page_load_timeout", 20)
        self.headless: bool = data.get("headless", False)
