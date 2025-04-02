import os 
import yaml
from text_Summarizer.logging import logger
from ensure import ensure_annotation
from box import ConfigBox
from pathlib import Path
from typing import Any, List, Dict

@ensure_annotation
def read_yaml(path_to_yaml:Path) ->ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Returns:
        ConfigBox: Contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error reading YAML file {path_to_yaml}: {e}")
        raise e
    


@ensure_annotation
def create_directories(path_to_dirs:List,verbose:bool=True):
    """
    Creates directories if they do not exist.
    
    Args:
        path_to_dirs (List): List of directory paths to create.
        verbose (bool): If True, prints the status of directory creation.
    """
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")
        else:
            logger.debug(f"Directory already exists: {path}")



@ensure_annotation
def get_size(path:Path)->str:
    """
    Returns the size of a file or directory.
    
    Args:
        path (Path): Path to the file or directory.
        
    Returns:
        str: Size of the file or directory in bytes.
    """
    size_in_Kb = round(os.path.getsize(path)/1024)
    return f"{size_in_Kb} KB"