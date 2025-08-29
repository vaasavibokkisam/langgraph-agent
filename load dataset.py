import json

# Load dataset
with open("dataset.json", "r") as f:
    dataset = json.load(f)

print("Loaded Tickets:\n")
for ticket in dataset:
    print(ticket)
