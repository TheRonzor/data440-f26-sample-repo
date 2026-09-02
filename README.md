# Sample Repository

The purpose of this repository is to demonstrate good organizational structure that can apply to many different types of projects. This is not a catch-all template that you should apply directly to your projects - it serves as a simple example of how you should try to organize your work.

This "workflow" consists of three main steps:

1. Data generation. Many workflows begin with raw data, and raw data often has issues. In this workflow, a random array of numbers is generated and then some missing values and outliers are inserted. The raw data is stored in [`data/raw/`](data/raw/).

2. Preprocessing. The natural next step is to clean/preprocess the data. In this workflow, some very basic rules are applied to fix the outliers and missing data. The cleaned up data is stored in [`data/clean/`](data/clean/). Saving both the raw and clean versions of the data allow us to more easily investigate issues if/when something goes wrong.

3. Visualization. Many workflows end with some set of summaries/tables/visualizations. In this workflow, the data in [`data/clean/`](data/clean/) is used to create a histogram. The most recent version of the histogram is stored in [`figures/`](figures/). Older versions of the histogram will be moved to [`figures/archive/`](figures/archive/) when a new histogram is created. All figures are saved with a timestamp in their filename, making it easy to compare before/after versions if/when we need to make a revision (for example, if an error was found in the data or preprocessing steps).

## Code Organization

All of the source code is stored in [`src/`](src/). Source code should be separated by responsibility. This helps make the code more maintainable, reduces the risk of side effects when making edits, and also makes the code more readily testable. In this workflow:

- [`src/get_data.py`](src/get_data.py): This file contains all of the code related to the data generation process, and nothing else.
- [`src/clean_data.py`](src/clean_data.py): This file contains all of the code related to the data preprpocessing, and nothing else.
- [`src/make_figures.py`](src/make_figures.py): This file contains all of the code related to making figures, and nothing else.

Other files included are:

- [`src/paths.py`](src/paths.py): This file contains a list of the file/folder paths used by the workflow. Some people might incorporate this into something like a `config.py` file
- [`src/helpers.py`](src/helpers.py): This file contains helper/utility functions that are intended to be shared across modules.
