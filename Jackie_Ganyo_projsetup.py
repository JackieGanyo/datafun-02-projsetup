''' This module provides functions for creating a series of project folders. '''
#import dependencies after introduction

import os
import math
import statistics
import stellar_analytics_utils
import GanyoDataServices_utils
import pathlib

# Define reusable functions to create a series of project folders. Each function should have a clear purpose, input parameters, and return values if applicable.

# Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).

def create_folders_for_range(start, end):

# Function 2. For Item in List: Develop a function to create folders from a list of names.

def create_folders_from_list(folder_list):

# Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").

def create_prefixed_folders(folder_list, prefix):

# Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).

def create_folders_periodically(duration):

# Create a path object
project_path = pathlib.Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

# 5. Define Main function
def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {GanyoDataServices_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
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

# Conditional Script Execution (at the end of the file)
if __name__ == '__main__':
    main()
