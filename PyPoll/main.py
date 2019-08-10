import os
import csv
import sys

def writeout(output_text):

    # Display output to the terminal and store it in an output file
    print(output_text)
    output_report.write(output_text + "\n")


# Initialize Variables
election_data_csv_path = "election_data.csv"
candidates = []
candidate = ""
vote_candidate = ""
winner = ""
max_votes = 0
total_candidate_votes = 0

# Open the Output Report for Writing
output_report = open("VoteCount.txt", 'w')

# Scan the list to count the total number of votes and identify all candidates
with open(election_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Initialize Variables
    total_votes = 0

    # Skip the header row
    next(csv_reader)

    # Read through each row of data after the header
    for row in csv_reader:

        total_votes += 1
        candidate = row[2]
        if not candidate in candidates:
           candidates.append(candidate)

# Count votes per candidate and Print Results

writeout("Election Results")

writeout("----------------------------")
writeout(f"Total Votes: {total_votes}")
writeout("----------------------------")

for candidate in candidates:

    with open(election_data_csv_path, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")

        # Skip the header row
        next(csv_reader)

        # Read through all the votes

        total_candidate_votes = 0

        for row in csv_reader:

            vote_candidate = row[2]
            if vote_candidate == candidate:
                total_candidate_votes += 1

        if total_candidate_votes >= max_votes:
            if total_candidate_votes == max_votes:
                writeout(f"WE HAVE A TIE BETWEEN {candidate} and {vote_candidate}")
                winner = "TIE"
            else:
                winner = candidate
                max_votes = total_candidate_votes

        writeout(f"{candidate}: {(total_candidate_votes/total_votes * 100):.3f}% ({total_candidate_votes})")

writeout("----------------------------")
writeout(f"Winner: {winner}")
writeout("----------------------------")
