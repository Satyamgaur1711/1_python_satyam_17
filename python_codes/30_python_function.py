l = ["gaur", "is", "very", "easy", "to", "learn", "and", "fun", "use", "to"]

def remove(word):
    for item in l:
        if item == word:
            l.remove(word)
    return l

a = remove(input("Enter the word you want to remove: "))
print(a)



def re_move(sabd):
    for saman in l:
        if saman == sabd:
            l.remove(sabd)
    return l

b = re_move(input("Enter the word you want to remove: "))
print(b)
