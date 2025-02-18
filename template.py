import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] : %(messagess)s:')
project_name = "text_Summarizer"



list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/units/comman.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/comfiguration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "confg/config.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirments.txt",
    "setup.py",
    "research/tarials.ipynb"
    
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir,filename = os.path.split(file_path)


    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"created directory:{filedir} for the {filename}")

if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
    with open(file_path,"w") as f:
        pass
        logging.info(f"created file:{file_path}")
else:
    logging.info(f"file:{file_path} already exists")
    