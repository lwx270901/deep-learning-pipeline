import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src{project_name}/__init__.py",
    f"src{project_name}/components/__init__.py",
    f"src{project_name}/utils/__init__.py",
    f"src{project_name}/config/__init__.py",
    f"src{project_name}/config/configuration.py",
    f"src{project_name}/pipeline/__init__.py",
    f"src{project_name}/enity/__init__.py",
    f"src{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc/yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath) # Convert to Path object
    filedir, filename = os.path.split(filepath) # Split the path into directory and filename
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # Check if file does not exist or is empty
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")