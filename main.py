from src.paths import make_project_folders
import src.get_data as get_data
import src.clean_data as clean_data
import src.make_figures as make_figures

def main() -> None:
    make_project_folders()

    print('Running pipeline: Getting data...')
    get_data.main()
    print('Running pipeline: Cleaning data...')
    clean_data.main()
    print('Running pipeline: Making figures...')
    make_figures.main()
    return None

if __name__ == '__main__':
    main()