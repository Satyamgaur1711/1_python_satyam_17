# span detection program by stary gaur...
key1 = "make a lot of money"
key2 = "subscribe"
key3 = "click this"
key4 = "buy"

comment = input("Enter you comment what you want.")

if key1 in comment or key2 in comment or key3 in comment or key4 in comment:
    print("this is span message/comment" , comment)
else:
    print("this message is noraml:  " , comment)