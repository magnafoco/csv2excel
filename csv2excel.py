import pandas
import os
import time
import argparse
import sys

# Banner ASCII "CSV to EXCEL" from manytools.org
banner = '''
 ██████╗███████╗██╗   ██╗    ██████╗     ███████╗██╗  ██╗ ██████╗███████╗██╗     
██╔════╝██╔════╝██║   ██║    ╚════██╗    ██╔════╝╚██╗██╔╝██╔════╝██╔════╝██║     
██║     ███████╗██║   ██║     █████╔╝    █████╗   ╚███╔╝ ██║     █████╗  ██║     
██║     ╚════██║╚██╗ ██╔╝    ██╔═══╝     ██╔══╝   ██╔██╗ ██║     ██╔══╝  ██║     
╚██████╗███████║ ╚████╔╝     ███████╗    ███████╗██╔╝ ██╗╚██████╗███████╗███████╗
 ╚═════╝╚══════╝  ╚═══╝      ╚══════╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚══════╝
Author: magnafoco 🔥                                                                     
'''
print(banner)

# Create arguments
parser = argparse.ArgumentParser(description="This script is developed to receive a big CSV file as input and parsing it returning a XLSX smaller file with only the data that you want.", epilog="Author: magnafoco 🔥")
parser.add_argument("-i", "--input", type=argparse.FileType('r'), default=sys.stdin, required=True, help="Input file")
args = parser.parse_args()

# Using DataFrame from pandas declare a variable and assign it a value using "read_csv" function.
input_data = args.input
dataFrame = pandas.read_csv(input_data)

# Print DataFrame header columns. 
print('\n' "I have found these column headers: " '\n')

# Get a list of header columns
headers = list(dataFrame.columns)

# Print headers with indices.
for idx, header in enumerate(headers):
    print(idx, header)

# Take user input for selecting headers using comma-separated indices.
selected_indices = input("\nInsert header indices separated by commas: ")
selected_indices = [int(idx) for idx in selected_indices.split(',')]

# Create a list with the headers selected by the user. 
selected_headers = [headers[idx] for idx in selected_indices]

# Assign value including as index of array only the headers selected by the user.
dataFrame2 = dataFrame[selected_headers]

# Assign actual date in format YYYY-MM-DD.
date = time.strftime("%Y_%m_%d")

# Create filename with user input in the format "date_filename.xlsx".
file_name = date + "_" + input('\n' "Insert filename: ") + ".xlsx"

# Assign current working directory.
current_path = os.getcwd() + ("/")

# While the file name exists in the current folder, ask to insert a new file name.
while os.path.exists(current_path + file_name):
    file_name = current_path (str(input(file_name + " already exists, please enter a different filename: ") + '.xlsx'))

# Export to an Excel file.
dataFrame2.to_excel(file_name)
print("\nSaved as: " + current_path + file_name)