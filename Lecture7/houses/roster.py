import csv
from sys import argv
import cs50

def main():
    if len(argv) != 2:
        print("Usage: python roster.py house")
        exit(1)

    # open db
    db = cs50.SQL("sqlite:///students.db")

    results = db.execute("select first, middle, last, birth from students where house = ? order by last asc, first asc", argv[1])
    for result in results:
        if result["middle"] == None:
            print(result["first"], result["last"], "born", result["birth"])
        else:
            print(result["first"], result["middle"], result["last"], "born", result["birth"])


main()