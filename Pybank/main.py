#Importing modules
import os
import csv

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