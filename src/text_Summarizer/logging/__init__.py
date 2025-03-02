import os 
import sys 
import logging

# Create a custom logger
logging_str = "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s] [%(funcName)s] %(message)s"
log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'text_summarizer.log')
os.makedirs(log_dir,exist_ok=True)



logging.basicConfig(
    level=logging.DEBUG,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger= logging.getLogger('text_summarizer')
