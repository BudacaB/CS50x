import csv
from sys import argv
import cs50

def main():
    if len(argv) != 2:
        print("Usage: python import.py data.csv")
        exit(1)

    # open db
    db = cs50.SQL("sqlite:///students.db")

    # open and read file
    with open(argv[1], "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        
        for row in reader:
            nameSplit = row["name"].split()
            if len(nameSplit) == 2:
                firstName = nameSplit[0]
                middleName = None
                lastName = nameSplit[1]
            else:
                firstName = nameSplit[0]
                middleName = nameSplit[1]
                lastName = nameSplit[2]
            house = row["house"]
            birth = row["birth"]
            db.execute("insert into students (first, middle, last, house, birth) values(?, ?, ?, ?, ?)", 
                    firstName, middleName, lastName, house, birth)

main()