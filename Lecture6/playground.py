import csv
import operator
from sys import argv

def main():
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # open and read files
    csvfile = open(argv[1], "r")
    reader = csv.DictReader(csvfile)
    file = open(argv[2], "r")
    text = file.read()

    # get number of nucleotides
    numOfNucleotides = len(reader.fieldnames) - 1

    # get matches
    findings = find_matches(reader, text)

    # get match
    keyList = [ k for k in findings.keys() if findings[k] == numOfNucleotides ]
    if len(keyList) != 0:
        print(keyList[0])
    else:
        print("No match")

    # close files
    csvfile.close()
    file.close()

# https://code-maven.com/slides/python/is-number
def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True

def find_matches(reader, text):
    findings = {}
    for row in reader:
        for key, value in row.items():
            if not is_int(row[key]):
                name = row[key]
                findings[row[key]] = 0
            for i in reversed(range(0, 100)):
                if operator.contains(text, key * i) and is_int(row[key]):
                    if int(row[key]) == i:
                        findings[name] += 1
                    break
    return findings



main()