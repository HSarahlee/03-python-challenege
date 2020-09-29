import os
import csv

election_csv = os.path.join("..", "Resources", "election_data.csv")

Candidate_List = []
Candidates_from_data = []
Candidate_percent = []
Candidate_vote = []
Total = 0
count_individuals = 0



with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")    
    next(csvreader, None)
    
    for row in csvreader:
        Candidates_from_data.append(row[2])
        Total += 1

    for x in set(Candidates_from_data):
        Candidate_List.append(x)
        Candidate_vote.append(Candidates_from_data.count(x))
        winner = Candidate_List[Candidate_vote.index(max(Candidate_vote))]
       
        
        
      
       
Candidate_1 = round((Candidate_vote[0])/Total *100, 3)
Candidate_2 = round((Candidate_vote[1])/Total *100, 3)
Candidate_3 = round((Candidate_vote[2])/Total *100, 3)
Candidate_4 = round((Candidate_vote[3])/Total *100, 3)



print("--------------------------------------")
print("Election Results")
print("--------------------------------------")
print("Total Votes: "+ str(Total))

print("--------------------------------------")

print(str(Candidate_List[0]) + ": " + str(Candidate_1) + "00%" + " (" + str(Candidate_vote[0]) + ")")
print(str(Candidate_List[1]) + ": " + str(Candidate_2) + "00%" + " (" + str(Candidate_vote[1]) + ")")
print(str(Candidate_List[2]) + ": " + str(Candidate_3) + "00%" + " (" + str(Candidate_vote[2]) + ")")
print(str(Candidate_List[3]) + ": " + str(Candidate_4) + "00%" + " (" + str(Candidate_vote[3]) + ")")
print("--------------------------------------")
print("Winner: " + str(winner))
print("--------------------------------------")



election_csv = os.path.join('..', 'Analysis', 'Analysis_PyPoll.txt')
with open(election_csv, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(["--------------------------------------"])
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["--------------------------------------"])
    csvwriter.writerow(["Total Votes: "+ str(Total)])
    csvwriter.writerow(["--------------------------------------"])

    csvwriter.writerow([str(Candidate_List[0]) + ": " + str(Candidate_1) + "00%" + " (" + str(Candidate_vote[0]) + ")"])
    csvwriter.writerow([str(Candidate_List[1]) + ": " + str(Candidate_2) + "00%" + " (" + str(Candidate_vote[1]) + ")"])
    csvwriter.writerow([str(Candidate_List[2]) + ": " + str(Candidate_3) + "00%" + " (" + str(Candidate_vote[2]) + ")"])
    csvwriter.writerow([str(Candidate_List[3]) + ": " + str(Candidate_4) + "00%" + " (" + str(Candidate_vote[3]) + ")"])
    csvwriter.writerow(["--------------------------------------"])
    csvwriter.writerow(["Winner: " + str(winner)])
    csvwriter.writerow(["--------------------------------------"])





   