# import glob
#
# myfiles = glob.glob('project2/*.txt')
#
# for filepath in myfiles:
#     with open(filepath) as file:
#         new_file = file.readlines()
#         for line in new_file:
#             print(line.upper())
#

# import csv
#
# with open('weather.csv', 'r') as file:
#     data = list(csv.reader(file))
#
# print(data)

# import shutil
#
# shutil.make_archive('output', 'zip', '../project1')

import webbrowser

user_term = input("Enter a search term: ")

webbrowser.open(f"https://www.google.com/search?q={user_term}")
