subject_1 = int(input("Enter you 1 subject number"))
subject_2 = int(input("Enter you 2 subject number"))
subject_3 = int(input("Enter you 3 subject number"))
subject_4 = int(input("Enter you 4 subject number"))

total_mark = subject_1 + subject_2 + subject_3 + subject_4
print("you total mark is :", total_mark)
total_parcentage = (total_mark/400)*(100)


if total_parcentage>=40 and subject_1>=33 and subject_2>=33 and subject_3>=33 and subject_4>=33:
    print("you are pased. good job." , total_parcentage)


else:
    print("fail hai tu bhadwe londiya baz. firse exam de." , total_parcentage)