f = open("file.txt", "r")

deta = f.read()
print(deta)
f.close()
# ye file ko kholega or read karke close kar dega


s = open("file.txt", "w")

write = s.write("satyam gaur is writing the text file")
s.close()
# ye file ko open kargea write mode me or mere string ko overwrite kar dega

k = open("created_by_program.txt", "w")
newfile = k.write("this is created by the programm")
k.close()

# agar ham ko file ko write mode me open karty hai to agar wo file nahi exist kati wo wo create ho jati hai.

