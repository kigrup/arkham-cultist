import logging
import sys

from logging.handlers import RotatingFileHandler

def init_logger():
    log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # INFO+ → file
    file_handler = RotatingFileHandler(
        "data/bot.log",
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(log_format))

    # WARNING+ → docker logs
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(logging.Formatter(log_format))

    root_logger.handlers.clear()
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    logging.info("Logger initialized")