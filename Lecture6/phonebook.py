from sys import exit

people = {
    "EMMA": "555-1234",
    "DAVID": "555-5678",
    "JOE": "555-0102",
    "TEX": "555-0103"
}

if "EMMA" in people:
    print(f"Found {people['EMMA']}")
    exit(0)
print("Not found")
exit(1)