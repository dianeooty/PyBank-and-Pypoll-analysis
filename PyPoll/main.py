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
    if cancount1 > cancount2 and cancount1 > cancount3:
        winner = candidates[0]
    elif cancount2 > cancount1 and cancount2 > cancount3:
        winner = candidates[1]
    elif cancount3 > cancount1 and cancount3 > cancount2:
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
