import os
from datetime import datetime

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

def log_request(input_type, value, result):
    with open(os.path.join(log_dir, "requests.log"), "a") as f:
        f.write(f"{datetime.now()} - {input_type} - {value} - {result}\n")

def log_error(input_type, value, error_msg):
    with open(os.path.join(log_dir, "errors.log"), "a") as f:   
        f.write(f"{datetime.now()} - {input_type} - {value} - ERROR: {error_msg}\n")
