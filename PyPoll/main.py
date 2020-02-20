########################################################################################################
# Project: Python sccript for vote-counting process. 
# input dataset file:PyPoll_Resources_election_data.csv. three columns: Voter ID, County, and Candidate
# Date: Feb 18 2020
########################################################################################################


from pathlib import Path
import csv
import numpy as np

#build a file path string using pathlib
data_folder=Path("/Users/jadetao/Documents/python-challenge/PyPoll/")
PyPoll_csv_path = data_folder / "PyPoll_Resources_election_data.csv"


counter=0

#set a Numpy array data types for candi
dty = [('name', 'U8'), ('PCT', float), ('Votes', int)]
candi_arr=np.array([('Khan',0.0,0),('Correy',0.0,0),('Li',0.0,0),("O'Tooley",0.0,0)],dtype=dty)

with open(PyPoll_csv_path) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header=next(csvfile)

    for row in csvreader:
        counter +=1
        if row[2]=="Khan":
            candi_arr[0][2] +=1
        elif row[2]=="Correy":
            candi_arr[1][2]  +=1
        elif row[2]=="Li":
            candi_arr[2][2] +=1
        elif row[2]=="O'Tooley":
            candi_arr[3][2]  +=1



#print results to screen
print("Election Results")
print("---------------------------------------------")
print(f"Total Votes:  {counter}")
print("---------------------------------------------")
#calulate percentage vote for each candi
for i in range(4):
    candi_arr[i][1]=candi_arr[i][2]/counter*100
    print(f"{candi_arr[i][0]} :  {candi_arr[i][1]:.3f}% ({candi_arr[i][2]})")

#sort Numpy arry by votes
sorted_NP=np.sort(candi_arr,order=["Votes"])
print("---------------------------------------------")
print(f"Winner     {sorted_NP[3][0]}")
print("---------------------------------------------")
# write output to a txt file PyPoll_output.txt
with open("PyPoll_output.txt",'w') as f:
    print("Election Results",file=f)
    print("---------------------------------------------",file=f)
    print(f"Total Votes:  {counter}",file=f) 
    print("---------------------------------------------",file=f)
    #calulate percentage vote for each candi
    for i in range(4):
        candi_arr[i][1]=candi_arr[i][2]/counter*100
        print(f"{candi_arr[i][0]} :  {candi_arr[i][1]:.3f}% ({candi_arr[i][2]})",file=f)
    print("---------------------------------------------",file=f)
    print(f"Winner     {sorted_NP[3][0]}",file=f)
    print("---------------------------------------------",file=f)