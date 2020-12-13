import csv
import cs50

# create empty shows2.db
open("shows3.db", "w").close

# open that file for SQLite
db = cs50.SQL("sqlite:///shows3.db")

# create table
db.execute("create table shows (tconst TEXT, primaryTitle TEXT, startYear NUMERIC, genres TEXT)")

# open title.basics.tsv
with open("/home/bogdan/Downloads/data.tsv", "r") as titles:

    # create DictReader
    reader = csv.DictReader(titles, delimiter="\t")

    for row in reader:

        if row["titleType"] == "tvSeries" and row["isAdult"] == "0":
            
            if row["startYear"] != "\\N":

                startYear = int(row["startYear"])

                if startYear >= 1970:

                    tconst = row["tconst"]
                    primaryTitle = row["primaryTitle"]
                    genres = row["genres"]

                    db.execute("insert into shows (tconst, primaryTitle, startYear, genres) values(?, ?, ?, ?)", 
                    tconst, primaryTitle, startYear, genres)