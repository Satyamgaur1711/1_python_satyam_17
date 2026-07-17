listnumber  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for satyam in range(18):
    print(listnumber[satyam])
for i in listnumber:
    print(i)

name = "satyam gaur"
for i in name:
    print(i)

dict1 = {"satyam": 100, "shivam": 200, "satyarth": 300, "rajit":400}

print(dict1["satyam"])  # This will raise a KeyError because "satyam" is not a key in the dictionary
print(dict1.get("aman")) # This will return None because "aman" is not a key in the dictionary
for i in dict1:
    print(f"{i}: {dict1.get(i)}")
