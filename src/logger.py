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