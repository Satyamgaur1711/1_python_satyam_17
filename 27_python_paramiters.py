def good_day(name="tere baap me tuje naam nahi diya kya", ending="tu chutuya hai sale eding kyu nahi diya "):
    print(f" good day {name} {ending}")


naaaam = input("what is your name? ")
khatam = input("what is your ending statment")
if khatam == "" and naaaam == "":
    good_day()
elif khatam == "":
    good_day(naaaam)
elif naaaam == "":
    good_day(ending=khatam)
else:
    good_day(naaaam, khatam)

# agar yaha py ending nahi diya to wo gali


