# app/core/logger.py
import logging
from logging.handlers import RotatingFileHandler
import sys
# Create custom logger
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] [%(name)s] — %(message)s", "%Y-%m-%d %H:%M:%S"
)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# File handler (rotating to prevent huge log files)
file_handler = RotatingFileHandler("logs/app.log", maxBytes=5_000_000, backupCount=5)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)
