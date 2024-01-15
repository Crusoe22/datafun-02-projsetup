''' This module provides functions for creating a series of project folders. '''
import Nolan_utils
import pathlib
import time


def create_folders_for_range(start_year, end_year):
    """
    Creates folders from a given range
    :param start: First year to be creates, e.g. 2000
    :param end: Last year to be created, e.g 2024
    """
    for year in range(start_year, end_year + 1):
        pathlib.Path(str(year)).mkdir(exist_ok=True)

def create_folders_from_list(folder_names, to_lowercase=False, remove_spaces=False):
    """
    Creates folders from list of names.
    :param folder_names: folders to be created
    :param to_lowercase: option to convert tring to lowercase 
    :param remove_spaces: option to remove spaces from string
    """
    for folder in folder_names:
        folder_check = folder
        if to_lowercase and remove_spaces:
            folder_check = folder.replace(' ', '') # Removes spaces from string
            folder_check = folder.lower() # Converts string to lowercase
        pathlib.Path(folder_check).mkdir(exist_ok=True) 

def create_prefixed_folders(folder_list, prefix):
    """
    Creates prefixed folders from a list of names in the current working directory.
    :param folder_list: List of names, e.g., ['Geometry', 'Consumer Math']
    :param prefix: Prefix to be added to each folder name, e.g., "data-"
    """
    # Using list comprehension to create prefixed folders
    folders = [pathlib.Path(f"{prefix}{name}") for name in folder_list]

    # Creating the folders in the current working directory
    for folder in folders:
        pathlib.Path(folder).mkdir(exist_ok=True)

def create_folders_periodically(delay_seconds):
    """
    Creates folders periodically with a specified delay.
    :param prefix: Prefix to be added to each folder name, e.g., "folder-"
    :param num_folders: Number of folders to create
    :param delay_seconds: Delay between each folder creation (default is 5 seconds)
    """
    num_folders = 5 # Number of folders to be created
    next_file = 1 # Int to start while loop

    while next_file <= num_folders:
        pathlib.Path("folder-" + str(next_file)).mkdir(exist_ok=True)
        next_file += 1
        time.sleep(delay_seconds)

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {Nolan_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'sdata-' 
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

if __name__ == '__main__':
    main()
