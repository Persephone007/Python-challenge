import os
import csv
pybank_csv = os.path.join("budget_data.csv")

#bucket to store Polly Parrot , err, list 
months = []
profit_loss = []


#The numbers are deceased, bereft of life, it rests in peace AKA starting at 0 
average_profit_loss = 0
greatest_increase_profits = 0
greatest_decrease_profits = 0

with open(pybank_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    for row in csvreader:
        
         months.append(row[0])
         profit_loss.append(int(row[1]))

total_months = len(months)

total_profit_loss = sum(profit_loss)

#    loop through data to get month by month change 
# (Flying through it, unlike Polly, May she rest in Peace)
monthly_profit_loss = [profit_loss[i + 1] - profit_loss[i] 
for i in range(len(profit_loss) -1)]

# sum of month to month change / total months = average change 
count = total_months -1
average_profit_loss = round(sum(monthly_profit_loss)/count ,2)


# find greatest increase and decrease in profits by month 
largest_profit = max(monthly_profit_loss)
largest_loss = min(monthly_profit_loss)

largest_profit_month = months[monthly_profit_loss.index(largest_profit) +1]
largest_loss_month = months[monthly_profit_loss.index(largest_loss) +1]


print ( "Financial Analysis")
print ("----------------------------")
print ("Total Months: " + str(total_months))

print ("Total: " + " $" + str(total_profit_loss))
print ("Average Change: " + " $" + str(average_profit_loss))

print ("Greatest Increase in Profits: " + str(largest_profit_month) + "  $" + str(largest_profit))
print ("Greatest Decrease in Profits: " + str(largest_loss_month) + "  $" + str(largest_loss))

# export a text file with results

output_file = os.path.join("budget_data_final.csv")

#  Open the output file
with open(output_file , "w") as file:
     

    
     file.writelines("Financial Analysis" + "\n")
     file.writelines("----------------------------" + "\n")
     file.writelines("Total Months: " + str(total_months) + "\n")

     file.writelines("Total: " + " $" + str(total_profit_loss) + "\n")
     file.writelines("Average Change: " + " $" + str(average_profit_loss) + "\n")

     file.writelines("Greatest Increase in Profits: " + str(largest_profit_month) + "  $" + str(largest_profit) + "\n")
     file.writelines("Greatest Decrease in Profits: " + str(largest_loss_month) + "  $" + str(largest_loss) + "\n")

