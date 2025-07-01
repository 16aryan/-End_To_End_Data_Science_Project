# src/logger.py

import logging
import os
from datetime import datetime

# Define log file name with timestamp
log_file = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
logs_path = os.path.join("logs")
os.makedirs(logs_path, exist_ok=True)  # Create logs/ if it doesn't exist

log_file_path = os.path.join(logs_path, log_file)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

"""
import logging
import os
from datetime import datetime

log_file = f"logs/{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=log_file,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
"""