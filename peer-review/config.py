import os
import logging
import time
from tqdm import tqdm
from datetime import datetime

FORMATTED_DATE_TIME = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

""" Directories """
PROJECT_DIR = os.getcwd()

LOG_DIR = os.path.join(PROJECT_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, f"{FORMATTED_DATE_TIME}.log")


""" Other Configurations """
logging.basicConfig(
    filename=LOG_FILE, 
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)
tqdm.pandas(desc="Unknown Process.")

# Output CSV
OUTPUT_CSV = "output.csv"
FINAL_CSV = "final.csv"

# Input
INPUT_DIR = "input"
