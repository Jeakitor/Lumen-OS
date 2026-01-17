import logging
from pathlib import Path

LOG_FILE = "/var/log/lumen-installer.log"

def setup_logger():
    Path("/var/log").mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

def log(message):
    logging.info(message)
