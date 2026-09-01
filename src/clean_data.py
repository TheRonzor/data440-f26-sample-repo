# This file should contain code that reads in raw data,
# performs cleaning/preprocessing, and saves the cleaned data.
#
# It should not contain code related to gathering raw data
# or producing figures/output.

import numpy as np
from src.paths import PATH_DATA_RAW, PATH_DATA_CLEAN, make_project_folders

def load_data() -> np.ndarray:
    filepath = PATH_DATA_RAW / 'my_raw_data.npy'
    return np.load(filepath)

def mark_outliers(data: np.ndarray) -> None:
    '''
    Replace outliers with np.nan.

    An outlier is defined as a value that is more than a certain number
    of standard deviations away from the average value in its column.

    Operate on the array in place.
    '''

    # Loop through each column in the array.
    for col_index in range(data.shape[1]):

        # Select the current column.
        column = data[:, col_index]

        # Compute the average and standard deviation of the column.
        # The nan versions ignore missing values.
        column_average = np.nanmean(column)
        column_standard_deviation = np.nanstd(column)

        # If the standard deviation is 0, all non-missing values are the same.
        # In that case, we skip this column.
        if column_standard_deviation == 0:
            continue

        # Compute how far each value is from the column average.
        distance_from_average = np.abs(column - column_average)

        # Decide which values are unusually far away.
        outliers = distance_from_average > 5 * column_standard_deviation

        # Replace outliers with missing values.
        column[outliers] = np.nan

def impute_missing_values(data: np.ndarray) -> None:
    '''
    Fill in missing values with the average across their column.
    Operate on the array in place.
    '''

    # Loop through each column in the array.
    for col_index in range(data.shape[1]):

        # Select the current column.
        column = data[:, col_index]

        # Find which values in the column are missing.
        missing_values = np.isnan(column)

        # Select the values that are not missing.
        non_missing_values = column[~missing_values]

        # If the whole column is missing, skip it.
        if len(non_missing_values) == 0:
            continue

        # Compute the average of the non-missing values.
        column_average = np.mean(non_missing_values)

        # Replace the missing values with the column average.
        column[missing_values] = column_average
    return None

def save_clean_data(data: np.ndarray) -> None:
    filepath = PATH_DATA_CLEAN / 'my_clean_data.npy'
    np.save(filepath, data)
    return None

def main():
    make_project_folders()
    
    data = load_data()
    mark_outliers(data)
    impute_missing_values(data)
    save_clean_data(data)
    return None

if __name__ == '__main__':
    print('Cleaning data...')
    main()