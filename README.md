# Python Challenge
> I was tasked with two Python challenges called PyBank and PyPoll for the Module 3 Challenge of my Data Analytics and Visualization Boot Camp. 


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
- The PyBank challenge was to create a Python script that analyzes the dataset of a financial company.  The dataset reflected the profit and losses of the company over a period. The script must calculate the total number of months included in the dataset, net total amount of "Profits/Losses", the changes in "Profits/Losses" and the both the greatest increase and decrease for the entire period.  The results must print out to the terminal and export a text file with the results.
- The PyPoll Challenge was to create a Python script that analyzes the outcome of an election dataset.  The dataset reflected the voter’s ID, the candidate voted for and the counties.  From the dataset, the script must calculate the total amount of votes, a list of candidates who received votes, the percentage and number of votes for each candidate and the winner of the election.  The results must print out to the terminal and export a text file with the results.


## Technologies Used
- Visual Studio
- Python
- Excel


## Setup
You can find the complete datasets for both in the resource folders and the analysis text files in the analysis folders.


## Usage
To analyze the datasets for PyBank and PyPoll, please see scripts below.

`PyBank
#Importing modules
import os
import csv
import numpy as np

#Filepath for csv
budget_csv = os.path.join("C:/Users/diane/Desktop/Homework/Module3_Python/python-challenge/Pybank", "resources", "budget_data.csv")

#Assigning empty lists for appending
dates = []
p1 = []
p2 = []
change = []

#Opening csv file to read
with open(budget_csv, "r", encoding="utf8") as csvfile:

    #Assigning reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skipping header row on csv
    csvheader = next(csvreader)

    #Creating a lists for dates and profit/loss
    #Creating a duplicate list of profit/loss for change in profit calculation
    for line in csvreader:
        dates.append(line[0])
        p1.append(line[1])
        p2.append(line[1])

    #Zipped the two lists and converted to a dictionary
    newlist = dict(zip(dates, p1))

    #Converting the values in pl from strings to integers and summing up for total
    i_p1 = [int(x) for x in p1]
    i_p2 = [int(x) for x in p1]
    total = (sum(i_p1)) 

    #Popping index 0 on duplicate list to use to subtract for changes
    i_p2.pop(0)
    
    #Zipping the two lists of profits/losses to create a new lists with the calculated changes in profit
    for x, y in zip(i_p1, i_p2):
        c = x - y
        change.append(c)
    
    #Calculating the average of change in profits
    average = round(sum(change) / len(i_p2),2)
        
    #Finding the max and min from the change list  
    increase = (max(change))
    decrease = (min(change))

    #Adding index 0 back into the list for $0 change at the beginning of the year
    change.insert(0,0)  
     
    #Zipping the lists and converting to dictionary
    d = dict(zip(dates, change)) 
    
    #Using the values of increase and decrease to find the dictionary keys for increase/decrease dates
    date = [k for k, v in d.items() if v == increase]
    date2 = [k for k, v in d.items() if v == decrease]

    #Printing Finanacial Analysis Results
    print("------------------------------------------------------------")
    print("Financial Analysis")
    print("------------------------------------------------------------")
    print(f"Total Months:  {len(dates)}")
    print(f"Total:  ${total}")
    print(f"Average Change:  ${average}")
    print(f"Greatest Increase in Profits:  {date} ${increase}")
    print(f"Greatest Decrease in Profits:  {date2} ${decrease}")
    print("------------------------------------------------------------")

#Creating a variable called analysis as a list of the lines to write to txt file
analysis = ["-------------------------------------------------------",
            "",
            "Financial Analysis",
            "",
            "-------------------------------------------------------",
            "",
            "Total Months: 86",
            "",
            "Average Change:  $8311.11",
            "",
            "Greatest Increase in Profits:  Feb-14  $1825558",
            "",
            "Greatest Decrease in Profits:  Aug-16  $-1862002",
            "",
            "-------------------------------------------------------"]
#Naming the txt file
filename = "financialanalysis.txt"

#Writing to txt file using for loop to write each line item in the variable called analysis
with open(filename, "w") as f:
    for items in analysis:
        f.write(items + "\n") 
        
PyPoll
#Importing modules
import os
import csv

#Filepath for csv
election_csv = os.path.join("C:/Users/diane/Desktop/Homework\Module3_Python/python-challenge/PyPoll","Resources", "election_data.csv")

#Creating empty lists
voter = []
county = []
candidate = []
candidates = []

#Opening csv file to read
with open(election_csv, "r", encoding="utf8") as csvfile:

    #Creating reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skipping header row on csv
    csvheader = next(csvreader)

    #Creating new lists 
    for line in csvreader:
        voter.append(line[0])
        county.append(line[1])
        candidate.append(line[2])
    
    #Creating a set from candidate list to get the unique candidates
    candidates = list(set(candidate))
    
    #Counting the total votes for each candidate
    cancount1 = candidate.count(candidates[0])
    cancount2 = candidate.count(candidates[1])
    cancount3 = candidate.count(candidates[2])

    #Calculating the percentage of votes for each candidate
    canpercent1 = round(((cancount1 / len(voter)) * 100),3)
    canpercent2 = round(((cancount2 / len(voter)) * 100),3)
    canpercent3 = round(((cancount3 / len(voter)) * 100),3)

    #Checking which candidate has the greatest number of votes with conditional statements
    winner = ""
    if cancount1 > (cancount2 and cancount3):
        winner = candidates[0]
    elif cancount2 > (cancount1 and cancount3):
        winner = candidates[1]
    elif cancount3 > (cancount1 and cancount2):
        winner = candidates[2]
 
    #Printing results
    print("-----------------------------------------------------------")
    print("Election Results")
    print("-----------------------------------------------------------")
    print("Total Votes:  "+ str(len(voter)))
    print("-----------------------------------------------------------")
    print(f"{candidates[0]}: {canpercent1}%  ({cancount1})")
    print(f"{candidates[1]}: {canpercent2}%  ({cancount2})") 
    print(f"{candidates[2]}: {canpercent3}%  ({cancount3})")
    print("-----------------------------------------------------------")
    print(f"Winner:  {winner}")
    print("-----------------------------------------------------------")

#Creating a variable called results as a list of the lines to write to txt file
results = ["-------------------------------------------------------",
            "",
            "Election Results",
            "",
            "-------------------------------------------------------",
            "",
            "Total Votes: 369711",
            "",
            "-------------------------------------------------------",
            "",
            "Charles Casper Stockham: 23.049%  (85213)",
            "",
            "Raymon Anthony Doane: 3.139%  (11606)",
            "",
            "Diana DeGette: 73.812%  (272892)",
            "",
            "-------------------------------------------------------",
            "",
            "Winner:  Diana DeGette",
            "",
            "-------------------------------------------------------"]

#Naming the txt file
filename = "results.txt"

#Writing to txt file using for loop to write each line item in the variable called results 
with open(filename, "w") as f:
    for items in results:
        f.write(items + "\n")
`


## Project Status
Project is in progress.


## Acknowledgements
- Many thanks to my learning instructors, TAs, classmates and learning assistants.


## Contact
Created by Diane Guzman
