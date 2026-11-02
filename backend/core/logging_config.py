
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from colorlog import ColoredFormatter


BASE_DIR = Path(__file__).resolve().parents[2]

LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "delivery_risk.log"

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
BACKUP_COUNT = 30


def setup_logging():
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    file_formatter = logging.Formatter(
        fmt="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_formatter = ColoredFormatter(
        fmt="%(log_color)s%(asctime)s - %(levelname)s - %(name)s - %(message)s%(reset)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        }
    )

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=MAX_FILE_SIZE,
        backupCount=BACKUP_COUNT,
        encoding="utf-8"
    )
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)

    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            file_handler,
            console_handler
        ],
        force=True
    )

    logging.getLogger("backend").setLevel(logging.DEBUG)
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("uvicorn.access").setLevel(logging.INFO)
