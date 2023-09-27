import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}"
log_file = os.path.join(os.getcwd(), 'logs', LOG_FILE)

LOG_FILE_PATH = os.path.join(log_file, LOG_FILE)

if not os.path.exists(log_file):
    os.makedirs(log_file, exist_ok=True)
    
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)