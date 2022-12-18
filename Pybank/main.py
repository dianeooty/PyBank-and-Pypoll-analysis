#Importing modules
import os
import csv

#Filepath for csv
budget_csv = os.path.join("C:/Users/diane/Desktop/Homework/Module3_Python/python-challenge/Pybank", "resources", "budget_data.csv")

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
----------------------------
Total Months: {total_month}
Total: ${total_p:,}
Average Change: ${total_change / month_change:,.2f}
Greatest Increase in Profits: {increase_month} (${increase:,})
Greatest Decrease in Profits: {decrease_month} (${decrease:,})
"""

#Printing the output to terminal for variable called result
print(result)

#Naming the txt file
filename = "financialanalysis.txt"

#Writing to txt file of the analysis data contained in the result variable
with open(filename, "w") as f:
        f.write(result)