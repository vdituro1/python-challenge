import os
import csv

def writeout(output_text):

    # Display output to the terminal and store it in an output file
    print(output_text)
    output_report.write(output_text + "\n")


budget_data_csv_path = "budget_data.csv"

# Write the Output Report
output_report = open("FinancialAnalysis.txt", 'w')

with open(budget_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Initialize Variables
    total_months = 0
    net_total = 0
    max_increase = 0
    max_increase_date = ""
    max_decrease = 0
    max_decrease_date = ""
    previous_profit_loss = 0
    profit_loss_changes = []
    profit_loss_change = 0

    # Skip the header row
    next(csv_reader)

    # Read through each row of data after the header
    for row in csv_reader:

        total_months += 1

        profit_loss_date = row[0]
        profit_loss = int(row[1])

        net_total += profit_loss
  
        if total_months > 1:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)

        if profit_loss_change > max_increase:
            max_increase_date = profit_loss_date
            max_increase = profit_loss_change

        if profit_loss_change < max_decrease:
            max_decrease_date = profit_loss_date
            max_decrease = profit_loss_change

        previous_profit_loss = profit_loss

sum_profit_loss_change = 0
profit_loss_change_count = 0

for profit_loss_change in profit_loss_changes:
    sum_profit_loss_change += profit_loss_change
    profit_loss_change_count += 1

# Print Results
writeout("Financial Analysis")
writeout("----------------------------")
writeout(f"Total Months: {total_months}")
writeout(f"Total: ${net_total}")
writeout(f"Average Change: ${round(sum_profit_loss_change/profit_loss_change_count,2)}")
writeout(f"Greatest Increase In Profits: {max_increase_date} (${max_increase})")
writeout(f"Greatest Decrease In Profits: {max_decrease_date} (${max_decrease})")
