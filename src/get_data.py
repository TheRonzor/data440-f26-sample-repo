# Code that generates or obtains raw data should live in one place
#
# This file should not contain any code that is not directly related
#  to the initial acquisition or generation of raw data.
#
# Examples of code that should go in a file like this include:
#  - web scraping
#  - API calls
#  - Random data generation
#
# Any code that performs additional cleaning or preprocessing does not belong here!

import numpy as np
from src.paths import PATH_DATA_RAW, make_project_folders

def make_random_data(n_features: int = 10, n_observations: int = 100) -> np.ndarray:
    np.random.seed(42)
    return np.random.normal(size=(n_observations, n_features))

def add_missing_values(data: np.ndarray) -> None:
    data[0, 0] = np.nan
    data[-1, -1] = np.nan
    return None

def add_outliers(data: np.ndarray) -> None:
    data[1, 1] = 10000
    data[2, 3] = 99999
    return None

def save_raw_data(data:np.ndarray) -> np.ndarray:
    '''
    Saves the raw data as a .npy file
    '''
    filepath = PATH_DATA_RAW / 'my_raw_data.npy'
    np.save(filepath, data)
    return None

def main() -> None:
    make_project_folders()
    
    data = make_random_data()
    add_missing_values(data)
    add_outliers(data)
    save_raw_data(data)
    return None

if __name__ == '__main__':
    
    print('Generating data...')
    main()