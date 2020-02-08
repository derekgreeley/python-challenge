#Create py script for analyzing finance records using budget_data.csv
#dataset is used made of two columns: Date and Profit/Losses
    #Create script that analyzes records to calculate the following
    #Total number of months included in data set
    #Net total amount of "Profit/Losses" over entire period
    #Avg changes in "Profit/Losses"
    #Greatest increase in profits(Date and amt) over entire period
    #Greates decrease in losses(Date and amt) over entire period
#Should look like 
    #Financial Analysis
    #----------------------------
    #Total Months: 86
    #Total: $38382578
    #Average  Change: $-2315.12
    #Greatest Increase in Profits: Feb-2012 ($1926159)
    #Greatest Decrease in Profits: Sep-2013 ($-2196167)
#Final Script should both print analysis to the termal and export a text file

#start with imports
#Activity 3.2.7 and 3.2.8 
import os
import csv

#Set path for CSV file in PyBankcsv
#Activity 3.2.7
#csvpath = os.path.join('accounting.csv')
##this is where the problem really is
##tried changing the file location, the extended file path, nothing is working
#pyBankcsv = os.path.join('C:\Users\derek\Desktop\daAnalyticsBootCamp\Homework\Homework3Python\python-challenge\PyBank\budget_data.csv')
#pyBankcsv = os.path.join('C:', 'Users', 'derek', 'Desktop', 'daAnalyticsBootCamp', 'Homework', 'Homework3Python', 'python-challenge', 'PyBank', 'budget_data.csv')
#pyBankcsv = os.path.join('..', 'PyBank', 'budget_data.csv')
pyBankcsv = 'budget_data.csv'

#Create lists for the data
#Activity 3.2.8

profit = []
monthlychanges = []
date = []


#Set up the variables needed
#Activity 3.3.8
count = 0
totalprofit = 0
totalchangeprofits = 0
initialprofit = 0

#Open the CSV with set path
##this is where the problem says it is
with open(pyBankcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #for loop
    #Activity 3.1.11, Activity 3.3.1
    #remember that colon!
    for row in csvreader:
        #count the number months in the dataset
        count = count + 1
    
    #Activity 3.3.8
    #Will need date to collect greatest increase and decrease
        date.append(row[0])

    #add on profit info and calculate total profit
        profit.append(row[1])
        totalprofit = totalprofit + int(row[1])
        
    #Average change in profits from month to month, then the average change in profits
        finalprofit = int(row[1])
        monthlychangesprofits = finalprofit - initialprofit

    #store monthly changes using a list
        monthlychanges.append(monthlychangesprofits)

        totalchangeprofits = totalchangeprofits +monthlychangesprofits
        initialprofit = finalprofit

    #calculate average change in profits
        averagechangeprofits = (totalchangeprofits/count)

    #find max and min with their dates
        greatestIncrease = max(monthlychanges)
        greatestDecrease = min(monthlychanges)

        dateIncrease = date[monthlychanges.index(greatestIncrease)]
        dateDecrease = date[monthlychanges.index(greatestDecrease)]
    #print it all out
    #Activity 3.3.3
    print("-----------------------------------------------")
    print("Financial Analysis")
    print("-----------------------------------------------")
    print(f"Total Months: {count}")
    print(f"Total Profits: ${totalprofit}")
    print(f"Average Change: ${int(averagechangeprofits)}")
    print(f"Greatest Increase in Profits: {dateIncrease} ${greatestIncrease}")
    print(f"Greatest Decrease in Profits: {dateDecrease} ${greatestDecrease}")
    print("-----------------------------------------------")

#Activity 3.2.5
with open ('financial_analysis.txt', 'w') as text:
    text.write("-----------------------------------------------")
    text.write("    Financial Analysis" + "\n")
    text.write("-----------------------------------------------")
    text.write("    Total Months: " + str(count)+ "\n")
    text.write("    Total Profits: " +str(totalprofit)+ "\n")
    text.write("    Average Change: " + '$' +str(int(averagechangeprofits) + "\n"))
    text.write("    Greatest Increase in Profits: " + str(dateDecrease)+ " ($" + str (greatestIncrease) + ") \n")
    text.write("    Greatest Decrease in Profits: " + str(dateDecrease)+ " ($" + str (greatestDecrease) + ") \n")
    text.write("-----------------------------------------------\n")
