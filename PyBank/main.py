##############################################################################################
# Project: Python sccript for analyzing the financial records of W company. 
# input dataset file:PyBank_Resources_budget_data.csv. two columns: Date and Profit/Losses
# Date: Feb 18 2020
##############################################################################################


from pathlib import Path
import csv
import numpy as np

#build a file path string using pathlib
data_folder=Path("/Users/jadetao/Documents/python-challenge/PyBank/")
Pybank_csv_path = data_folder / "PyBank_Resources_budget_data.csv"

TotalMonth=0
Total=0
matrList = []

with open(Pybank_csv_path) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header=next(csvfile)
    
    #counting months and calculateing total, add records to list then convert it to dictionary
    for row in csvreader:
        Total +=int(row[1])
        TotalMonth +=1
        matrList.append(row)
        Dicta=dict(matrList)

#calculating average for profit change              
Avg=Total/TotalMonth

#sort dictionary by it values 
d=dict((k,int(v)) for k,v in Dicta.items())
sortedList=sorted(d.items(),key=lambda x:x[1])

#print results to screen
print("Financial Analysis")
print("---------------------------------------------")
print(f"Total Months:  {TotalMonth}")
print(f"Total:   ${Total}")
print(f"Average Change:  ${Avg:.2f}")
print(f"Greast Increase in Profits:  {sortedList[-1][0]}(${sortedList[-1][1]})")
print(f"Greast Decrease in Profits:  {sortedList[0][0]}(${sortedList[0][1]})")


# write output to a txt file Pybank_output.txt
with open("Pybank_output.txt",'w') as f:
    print("Financial Analysis",file=f)
    print("---------------------------------------------",file=f)
    print(f"Total Months:  {TotalMonth}",file=f)
    print(f"Total:   ${Total}",file=f)
    print(f"Average Change:  ${Avg:.2f}",file=f)
    print(f"Greast Increase in Profits:  {sortedList[-1][0]}(${sortedList[-1][1]})",file=f)
    print(f"Greast Decrease in Profits:  {sortedList[0][0]}(${sortedList[0][1]})",file=f)


