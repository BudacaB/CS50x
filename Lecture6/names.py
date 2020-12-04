from sys import exit

names = ["EMMA", "DAVID", "JOE", "TEX"]

if "EMMA" in names:
    print("Found")
    exit(0)
print("Not found")
exit(1)