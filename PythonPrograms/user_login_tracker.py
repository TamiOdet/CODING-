#read list of new hires
#generate random passwords for each user
#create user acc for all new hires to the company
#write new generated passwords into file
import csv #to read write csv files
import secrets  # generate random passwords for each acc
import subprocess # useed to create and add each user acc 
from pathlib import Path #to locate data files

cwd = Path.cwd() / "admin/Desktop/python"
#reading and parsing input in file
with open(cwd / "data/users_in.csv", "r") as file_input, open(cwd / "data/users_out.csv", "w") as file_output:
#each row in file read into dictionary 
reader = csv.DictReader(file_input)
writer = csv.DictWriter(file_output,fieldnames=reader.fieldnames)
writer.writeheader()
#run through each record from input file
for user in reader:
