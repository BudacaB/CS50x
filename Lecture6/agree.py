s = input("Do you agree?\n")

if s.lower() in ["y", "yes"]:
    print("Agreed")
elif s.lower() in ["", "no"]:
    print("Not agreed")