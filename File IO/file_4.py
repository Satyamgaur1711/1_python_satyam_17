linst = ["i am the best student ", "i am a good coder ", "my roommates are good "]



with open("file.txt", "w") as f:
    f.writelines(linst)
    f.seek(0) # isse ye curcer apne zero position py aa jayega
    print(f.tell()) # ye batayega ke curser kaha py hai.
    f.seek(100) # curser ke position change karne ke iye use hota hai.



