import os
import csv

budget_data_csv_path = "budget_data.csv"

with open(budget_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Initialize Variables
    total_months = 0
    net_total = 0
    max_increase = 0
    max_increase_date = ""
    max_decrease = 0
    max_decrease_date = ""

    next(csv_reader)

    # Read through each row of data after the header
    for row in csv_reader:

        total_months += 1

        profit_loss_date = row[0]
        profit_loss = int(row[1])

        net_total += profit_loss

        if profit_loss > max_increase:
            max_increase_date = profit_loss_date
            max_increase = profit_loss

        if profit_loss < max_decrease:
            max_decrease_date = profit_loss_date
            max_decrease = profit_loss

# Print Results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(net_total/total_months,2)}")
print(f"Greatest Increase In Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease In Profits: {max_decrease_date} (${max_decrease})")


with open("FinancialAnalysis.txt", 'w') as output_report:
    output_report.write("Financial Analysis\n")
    output_report.write("----------------------------\n")
    output_report.write(f"Total Months: {total_months}\n")
    output_report.write(f"Total: ${net_total}\n")
    output_report.write(f"Average Change: ${round(net_total/total_months,2)}\n")
    output_report.write(f"Greatest Increase In Profits: {max_increase_date} (${max_increase})\n")
    output_report.write(f"Greatest Decrease In Profits: {max_decrease_date} (${max_decrease})\n")
