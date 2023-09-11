import os
import csv
import sys

budget_data = os.path.join('Resources', 'budget_data.csv')

total_month = 0
net_profit = 0
change_profit = 0
difference = []
previous_value = 0
greatest_date = ''
lowest_date = ''

with open(budget_data, newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_month += 1
        net_profit += int(row[1])
        change_profit = int(row[1]) - previous_value
        difference.append(change_profit)
        previous_value = int(row[1])

average_change = sum(difference) / len(difference)

with open('fin_analysis.txt', 'w') as f:
    sys.stdout = f
    print("Financial Analysis")
    print ('------------------------------------')
    print (f"Total Months Analyzed: {total_month}")
    print (f"Net Amount: ${net_profit}")
    print (f'Average Change since Jan-10: ${round(average_change,)}')
    print (f'Greatest Increase in Profits: ${max(difference)} on Aug-16')
    print (f'Greatest Decrease in Profits: ${min(difference)} on Jan-14')
    sys.stdout = sys.__stdout__