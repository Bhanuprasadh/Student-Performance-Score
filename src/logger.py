import logging
import os
from datetime import datetime

# 1. Define the filename with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the directory path (without the filename)
LOGS_DIR = os.path.join(os.getcwd(), "logs")

# 3. Create the directory (only the directory)
# This will create the 'logs' folder if it doesn't exist
os.makedirs(LOGS_DIR, exist_ok=True)

# 4. Define the full log file path
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# 5. Configure the logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
