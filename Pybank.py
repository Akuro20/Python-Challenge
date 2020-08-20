
import os
import csv

pybank_csv = os.path.join("C:/Users/akuro/Gitlab/jhu-apl-data-pt-07-2020-u-c/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")


totalmonths = []

totallossprofit = []

averagechange = []

# greatestprofitincreas = []

# largestloss = []

with open (pybank_csv, "r") as csvfile:
    csvreader= csv.reader(csvfile, delimiter =",")
    
    next(csvreader)
    for row in csvreader:
                         
        totalmonths.append(row[0])
        
        totallossprofit.append(row[1])
        
    total1 = len(totalmonths)
    print('Total months: ' + str(total1))
 #Revenue 
    lossprofit = map(int,totallossprofit)  # I could not figure out a way to 
    actuallossprofit = (sum(lossprofit))   # to serparate string form intergers
    print(actuallossprofit)                # so i used a code from github. I understand how it works
                                            # i understand how it works but it is not my original work

 # Here I determine the average change by finding the difference between months
 #loading this differences into a list, then finding the average of this list.
    # By summing the differences and diving by the number of differences. 
    i = 0
    for i in range(len(totallossprofit) - 1):
        difference = int(totallossprofit[i+1]) - int(totallossprofit[i])
 # append profit_loss
        averagechange.append(difference)
    sumtotal = sum(averagechange)
    
    # average is a total sum divided by the number of values.
    average_change = sumtotal / len(averagechange)
    print(average_change)
   
   # once i have my list of the monthly changes that occur. I simply have to 
    # use the max and min functions in python to determine the greatest monthly profit
    # and the greates monthly loss respectively. The exact month that it occures is determine by 
    # using the index fuction to find the index from the average change list and calling the same index
    # in the totalmonths list.
    # the 
#Greatest Increase
    profit_increase = max(averagechange)
    print(profit_increase)
    k = averagechange.index(profit_increase)
    month_increase = totalmonths[k+1]
    
#Greatest Decrease
    profit_decrease = min(averagechange)
    print(profit_decrease)
    j = averagechange.index(profit_decrease)
    month_decrease = totalmonths[j+1]


#Print Statements

print(f'Financial Analysis'+'\n')


print(f'----------------------------'+'\n')


print("Total number of months: " + str(len(totalmonths)))

print("Total Revenue in period: $ " + str(actuallossprofit))
      
print("Average monthly change in Revenue : $" + str(average_change))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")




#Notes Notes Notes Notes
# import os
# import csv

# pybank_csv = os.path.join("C:/Users/akuro/Gitlab/jhu-apl-data-pt-07-2020-u-c/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")


# totalmonths = []

# totallossprofit = []

# averagechange = []

# greatestprofitincreas = []

# largestloss = []






# with open (pybank_csv, "r") as csvfile:
#     csvreader= csv.reader(csvfile, delimiter =",")
    
      
#     next(csvreader)
#     for row in csvreader:
       
#         print(row[0], row[1])
        
                 
#         total = float(totallossprofit)
       
#         totalmonths.append(row[0])
        
#         totallossprofit.append(row[1])
        
       
        
#         print(totalmonths)
#         print(total)
        
        
#         print(totalmonths)
#         total1 = len(totalmonths)
#         print(total1)
        
#         total2 =sum(totallossprofit)
#         print(total2)
# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * The average of the changes in "Profit/Losses" over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period
