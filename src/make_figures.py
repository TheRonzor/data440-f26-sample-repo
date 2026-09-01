# This code should make figures from pre-prepared data.
# None of this code should be doing any complex math/processing/etc.
# The job of this code is to make figures only.

import shutil

import matplotlib.pyplot as plt
import numpy as np

from src.helpers import make_timestamp
from src.paths import (
    PATH_DATA_CLEAN,
    PATH_FIGURES,
    PATH_FIGURES_ARCHIVE,
    make_project_folders,
)


FIGURE_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.pdf', '.svg']


def load_clean_data() -> np.ndarray:
    '''
    Load the cleaned data.
    '''

    filepath = PATH_DATA_CLEAN / 'my_clean_data.npy'

    return np.load(filepath)


def archive_existing_figures() -> None:
    '''
    Move existing figures into the figure archive folder.

    This keeps the main figures folder focused on the most recent output.
    '''

    # Loop through everything in the main figures folder.
    for filepath in PATH_FIGURES.iterdir():

        # Skip folders, including the archive folder itself.
        if not filepath.is_file():
            continue

        # Only archive figure files.
        if filepath.suffix.lower() not in FIGURE_EXTENSIONS:
            continue

        # Decide where the archived file should go.
        archive_filepath = PATH_FIGURES_ARCHIVE / filepath.name

        # If a file with this name already exists in the archive,
        # add a timestamp to avoid overwriting it.
        if archive_filepath.exists():
            timestamp = make_timestamp()
            archive_filename = f'{filepath.stem}_archived_{timestamp}{filepath.suffix}'
            archive_filepath = PATH_FIGURES_ARCHIVE / archive_filename

        # Move the old figure into the archive folder.
        shutil.move(filepath, archive_filepath)

    return None


def make_histogram(data: np.ndarray) -> None:
    '''
    Create and save a histogram of the cleaned data.
    '''

    # Create a timestamped filename.
    timestamp = make_timestamp()
    filepath = PATH_FIGURES / f'histogram_{timestamp}.png'

    # Flatten the data so we can make one histogram
    # using all values in the array.
    values = data.flatten()

    # Create the figure and axes.
    fig, ax = plt.subplots(figsize=(8, 5))

    # Make the histogram.
    ax.hist(values, bins=30, edgecolor='black', alpha=0.8)

    # Add helpful labels.
    ax.set_title('Distribution of Cleaned Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

    # Add a light grid behind the histogram.
    ax.grid(axis='y', alpha=0.3)

    # Make sure labels fit nicely.
    fig.tight_layout()

    # Save the figure.
    fig.savefig(filepath, dpi=300)

    # Close the figure after saving.
    plt.close(fig)

    return None

def main() -> None:
    make_project_folders()
    archive_existing_figures()
    
    data = load_clean_data()
    make_histogram(data)

    return None


if __name__ == '__main__':
    print('Making figures...')
    main()