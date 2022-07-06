# Import dependencies
import os, csv
from pathlib import Path 

# Assign file location with the pathlib library
csv_file_path = Path("PyPoll", "Resources", "election_data.csv")

# Declare Variables 
total_votes = 0 
Charles_Casper_Stockham_votes = 0
Diana_DeGette_votes = 0
Raymon_Anthony_Doane_votes = 0

# Open csv in default read mode with context manager
with open(csv_file_path,newline="", encoding="utf-8") as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header so we iterate through the actual values
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        # We have four candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Charles Casper Stockham": 
            Charles_Casper_Stockham_votes +=1
        elif row[2] == "Diana DeGette":
            Diana_DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            Raymon_Anthony_Doane_votes +=1

 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Charles_Casper_Stockham_votes, Diana_DeGette_votes, Raymon_Anthony_Doane_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
Charles_Casper_Stockham_percent = (Charles_Casper_Stockham_votes/total_votes) *100
Diana_DeGette_percent = (Diana_DeGette_votes/total_votes) * 100
Raymon_Anthony_Doane_percent = (Raymon_Anthony_Doane_votes/total_votes)* 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
print(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
print(f"Raymon Anthony Doane: {Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")