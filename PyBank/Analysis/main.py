import os
import csv


csvpath = os.path.join("..", "Resources", "budget_data.csv")


total = 0 
revenues = []
Net_revenue = []
dates = []
change_revenue = []
months = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    for row in csvreader:
        dates.append(row[0])
        revenues.append(int(row[1]))

months = len(dates)
total = sum(revenues)
                
for i in range(len(revenues)-1):
    change = float(revenues[i+1]) - float(revenues[i])
    change_revenue.append(change)
    Net_revenue = sum(change_revenue)

average_change = round((Net_revenue / (months-1)),2)

min_revenues = revenues[revenues.index(min(revenues))] - revenues[revenues.index(min(revenues))-1]
min_month = dates[revenues.index(min(revenues))]

max_revenues = revenues[revenues.index(max(revenues))] - revenues[revenues.index(max(revenues))-1]
max_month = dates[revenues.index(max(revenues))]


print("Financial Analysis")
print("-------------------------------")
print("Total Months: " + str(months))
print("Total: $ " + str(total))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(max_month) + " ($" +str(max_revenues)+")")
print("Greatest Decrease in Profits: " + str(min_month) + " ($" +str(min_revenues)+")")

output_path = os.path.join('..', 'Analysis', 'Analysis_PyBank.txt')
with open(output_path, 'w') as csvfile:

    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------------"])
    csvwriter.writerow(["Total Months: " + str(months)])
    csvwriter.writerow(["Total: $ "+ str(total)])
    csvwriter.writerow(["Average Change: $" + str(average_change)])
    csvwriter.writerow(["Greatest Increase in Profits: " + str(max_month) + " ($" +str(max_revenues)+")"])
    csvwriter.writerow(["[Greatest Decrease in Profits: " + str(min_month) + " ($" +str(min_revenues)+")"])

