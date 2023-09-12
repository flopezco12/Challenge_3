import os
import csv
import sys

election_data = os.path.join('Resources', 'election_data.csv')

total_votes = []
candidates = []
list_candidates = []
vote_counter = []

with open(election_data, newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes = row[0]
        candidates= row[2]
        if candidates not in list_candidates:
            list_candidates.append(candidates)
    total_candidates = len(list_candidates)

with open('election_analysis.txt', 'w') as f:
    sys.stdout = f
    print("Election Results")
    print ('------------------------------------')
    print (f"Total Votes: {total_votes}")
    print ('------------------------------------')
    print (f'Candidate: {list_candidates[0]}, Votes: %')
    print (f'Candidate: {list_candidates[1]}, Votes: %')
    print (f'Candidate: {list_candidates[2]}, Votes: %')
    print ('------------------------------------')
    print ('Winner: ')
    print ('------------------------------------')
    sys.stdout = sys.__stdout__
