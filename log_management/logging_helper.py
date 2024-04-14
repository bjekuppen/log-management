import logging.config
from datetime import datetime
from typing import Dict, Any
import os


def setup_logging(config: Dict[str, Any]):
    # Replace the placeholders in the filename for each file handler
    for handler_name, handler_config in config["handlers"].items():
        if handler_config.get("class") == "logging.FileHandler":
            timestamp_placeholder(handler_config)
    logging.config.dictConfig(config)


def timestamp_placeholder(handler_config):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    handler_config["filename"] = os.path.join(
        handler_config["filename"] % {"timestamp": timestamp}
    )
