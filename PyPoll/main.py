#Importing modules
import os
import csv

#Filepath for csv
election_csv = os.path.join("C:/Users/diane/Desktop/Homework\Module3_Python/python-challenge/PyPoll","Resources", "election_data.csv")

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
            
        
    
