#Importing modules
import os
import csv

#Filepath for csv
budget_csv = os.path.join("C:/Users/diane/Desktop/Homework/Module3_Python/python-challenge/Pybank", "resources", "budget_data.csv")
#Assigning empty lists
dates = []
pl = []

#Opening csv file to read
with open(budget_csv, "r", encoding="utf8") as csvfile:

    #Assigning reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skipping header row on csv
    csvheader = next(csvreader)

    #Looping through reader object and appending each line to dates list and pl list
    for line in csvreader:
        dates.append(line[0])
        pl.append(line[1])

    #Zipped the two lists and converted to a dictionary
    newlist = dict(zip(dates, pl))

    #Converting the values in pl from strings to integers and summing up for total
    f_pl = [int(x) for x in pl]
    total = (sum(f_pl))

    #Looping through f_pl to find the max and min 
    for items in f_pl:
        increase = (max(f_pl))
        decrease = (min(f_pl))

    #Converting from integers to stings    
    increase = str(increase)
    decrease = str(decrease)

    #Using the string values of increase and decrease to find the dict keys for date
    date = str([k for k, v in newlist.items() if v == increase])
    date2 = str([k for k, v in newlist.items() if v == decrease])

    #???Calc is wrong??? Average of the changes from month to month???
    average = round(((f_pl[-1] - f_pl[0]) / len(pl)), 2)

    #??? How to print the dates without the brackets and quotes???
    #Printing analysis results
    print("------------------------------------------------------------")
    print("Financial Analysis")
    print("------------------------------------------------------------")
    print(f"Total Months:  {len(dates)}")
    print(f"Total:  ${total}")
    print(f"Average Change:  ${average}")
    print(f"Greatest Increase in Profits:  {date} ${increase}")
    print(f"Greatest Decrease in Profits:  {date2} ${decrease}")
    print("------------------------------------------------------------")

#???How to write the analysis to file??? 
analysis = ["-------------------------------------------------------",
            "",
            "Financial Analysis",
            "",
            "-------------------------------------------------------",
            "",
            "Total Months: 86",
            "",
            "Average Change:  $-8214.47",
            "",
            "Greatest Increase in Profits:  Mar-13  $1141840",
            "",
            "Greatest Decrease in Profits:  Dec-10  $-1194133",
            "",
            "-------------------------------------------------------"]

filename = "financialanalysis.txt"

with open(filename, "w") as f:
    for items in analysis:
        f.write(items + "\n")
