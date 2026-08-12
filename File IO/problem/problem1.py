with open("poem.txt") as f:
    r = f.read()
    if("twinkal" in r):
        print("twinkal is present in the poem")
    else:
        print("not present")




