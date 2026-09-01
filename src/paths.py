# This file defines all important filepaths
from pathlib import Path

# Main project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Data storage
PATH_DATA = PROJECT_ROOT / 'data'
PATH_DATA_RAW = PATH_DATA / 'raw'
PATH_DATA_CLEAN = PATH_DATA / 'clean'

# Figure/output storage
PATH_FIGURES = PROJECT_ROOT / 'figures'
PATH_FIGURES_ARCHIVE = PATH_FIGURES / 'archive'

def make_project_folders():
    '''
    Create the folders used by this project if they do not already exist.
    '''
    PATH_DATA.mkdir(parents=True, exist_ok=True)
    PATH_DATA_RAW.mkdir(parents=True, exist_ok=True)
    PATH_DATA_CLEAN.mkdir(parents=True, exist_ok=True)
    PATH_FIGURES.mkdir(parents=True, exist_ok=True)
    PATH_FIGURES_ARCHIVE.mkdir(parents=True, exist_ok=True)
    return None