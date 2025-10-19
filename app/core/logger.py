# app/core/logger.py
# ✅ Ensure logs directory exists
import os
import logging
from logging.handlers import RotatingFileHandler
import sys
# Create custom logger
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
# ✅ Ensure logs directory exists
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)
# Configure file handler
file_handler = RotatingFileHandler(
    os.path.join(LOG_DIR, "app.log"),
    maxBytes=5_000_000,
    backupCount=5,
    encoding="utf-8"
)

# Configure logger
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
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
