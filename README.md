# PyBank-and-Pypoll-analysis
> Using python scripts, analyze the PyBank and PyPoll datasets.  


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
- The PyBank project was to create a Python script that analyzes the dataset of a financial company.  The dataset reflected the profit and losses of the company over a period. The script must calculate the total number of months included in the dataset, net total amount of "Profits/Losses", the changes in "Profits/Losses" and the both the greatest increase and decrease for the entire period.  The results must print out to the terminal and export a text file with the results.
- The PyPoll project was to create a Python script that analyzes the outcome of an election dataset.  The dataset reflected the voter’s ID, the candidate voted for and the counties.  From the dataset, the script must calculate the total amount of votes, a list of candidates who received votes, the percentage and number of votes for each candidate and the winner of the election.  The results must print out to the terminal and export a text file with the results.


## Technologies Used
- Visual Studio
- Python
- Excel


## Screenshots
![1](https://user-images.githubusercontent.com/117790100/236303955-eb49a8c8-addc-489c-8f67-61ab89abb7bf.png)
![2](https://user-images.githubusercontent.com/117790100/236303957-bcbdf8d4-471b-42a8-9f18-3cbf4d91a80c.png)


## Setup
You can find the complete datasets for both in the resource folders and the analysis text files in the analysis folders.


## Usage
To analyze the datasets for PyBank and PyPoll, please see scripts below.

```
PyBank

#Importing modules
import os
import csv

#Filepath for csv
budget_csv = os.path.join("resources", "budget_data.csv")

#Assigning empty lists and variables
total_month = 0
total_p = 0
previous_p = 0
current_p = 0
change = 0
month_change = 0
increase = 0
decrease = 0
increase_month = ""
decrease_month = ""
total_change = 0

#Opening csv file to read
with open(budget_csv, "r", encoding="utf8") as csvfile:

    #Assigning reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skipping header row on csv
    csvheader = next(csvreader)
    
    #Using for loop to obtain needed data for analyis
    for line in csvreader:
        #Counting total months
        total_month += 1
        #Converting the string values of line[1] to integer values for calculation
        total_p += int(line[1])
        current_p = int(line[1])     
        
        #Conditional statement to find the total change in profits not including the first month since there isn't a previous value
        #The change value is the difference of the current minus the previous
        #Counting the number of months for changes using a counter that started at 0 and add 1 for each row  
        #Total change started at 0 and updated with change value for each row
        #Reassigning previous to current values for each row it loops through
        if previous_p != 0:
            change = current_p - previous_p
            month_change += 1  
            total_change += change                    
        previous_p = current_p  
        
        #Conditional statement to check change value for greatest increase and finding the corresponding month of the increase
        #Reassigning increase value if change is greater than increase
        #Grabbing the increase month which is the value of line[0] 
        if change > increase:
            increase = change
            increase_month = line[0]

        #Conditional statement to check change value for greatest decrease and finding the corresponding month of the decrease
        #Reassigning decrease value if change is lower than decrease
        #Grabbing the decrease month which is the value of line[0]     
        if change < decrease:
            decrease = change
            decrease_month = line[0]
    
#Assigning the printout to a variable called result that contains all the analysis data for output   
result = f"""

Financial Analysis

---------------------------------------------------

Total Months: {total_month}

Total: ${total_p:,}

Average Change: ${total_change / month_change:,.2f}

Greatest Increase in Profits: {increase_month} (${increase:,})

Greatest Decrease in Profits: {decrease_month} (${decrease:,})

---------------------------------------------------

"""

#Printing the output to terminal for variable called result
print(result)

#Naming the txt file
filename = "financialanalysis.txt"

#Writing to txt file of the analysis data contained in the result variable
with open(filename, "w") as f:
        f.write(result)
 
 
PyPoll

#Importing modules
import os
import csv

#Filepath for csv
election_csv = os.path.join("resources", "election_data.csv")

#Creating empty lists, dictionary and variables
candidate_list = []
candidates = {}
total_votes = 0
winning_count = 0
winning_percentage = 0


#Opening csv file to read
with open(election_csv, "r", encoding="utf8") as csvfile:

    #Creating reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skipping header row on csv
    csvheader = next(csvreader)

    #Using for loop to count total number of votes through each row and adding 1
    #Assigning variable called candidate name for values in line[2]
    for line in csvreader:
        total_votes += 1
        candidate_name = line[2]

        #Conditional statement to check the values in candidate name is not in the candidate list
        #Appending the values found to candidate list which will contain the unique candidates found in each row from candidate name
        #Starting the dictionary with vote count value of 0 for each unique candidate's name key 
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidates[candidate_name] = 0
            
        #Adding 1 to their vote count as dictionary value with each row and key as candidate's name
        candidates[candidate_name] += 1
                      
#Naming the txt file
filename = "results.txt" 

#Writing to the text file
with open(filename, "w") as f:
    
#Using a variable called election results and displaying the count from the total votes variable
    election_results = f"""
    Election Results

    -------------------------------------------------

    Total Votes: {total_votes:,}

    -------------------------------------------------
    """
    #Printing election results to the terminal
    print(election_results)
    #Writing the election results to the text file  
    f.write(election_results)

    #Using for loop to search through the dictionary to get the number of votes for each candidate
    #Calculating each candidates vote percentage using their vote counts and dividing by total votes and multiplying by 100
    #Assigning a variable called candidate results to print out each candidate's total votes and vote percentage from calculation
    for candidate_name in candidates:
        votes = candidates[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = f"""
    {candidate_name}: {vote_percentage:.3f}% ({votes:,})
    """   
        #Printing the candidate results to the terminal
        print(candidate_results)
        
        #Writing the results for each candidate to text file                   
        f.write(candidate_results)
          
        #Conditional statement to check which candidate has the greatest vote counts and vote percentage
        #Assiging the greatest vote counts and vote percentage to variables called winning count and winning percentage
        #Grabbing the name of the winning candidate and assigning value to variable called winning candidate
        if (votes > winning_count) and ( vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    #Printing the winning candidate to the terminal
    winner = f"""
    --------------------------------------------------

    Winner: {winning_candidate}

    --------------------------------------------------\n
    """
    print(winner)

    #Writing the winning candidate's name to the text file
    f.write(winner)  
```


## Project Status
Project is complete and no longer being worked on.


## Acknowledgements
- Many thanks to the instructional team and special thanks to Kelsey Brantner, Alex Hart, and David Chao.


## Contact
Created by Diane Guzman
