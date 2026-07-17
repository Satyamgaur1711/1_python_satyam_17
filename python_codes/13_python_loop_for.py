# try for loop for function and do some bawal

# range funcion i python are used to generate a sequence of numbers. It can be used in for loops to iterate over a sequence of numbers. The syntax for the range function is as follows:
# range(start, stop, step)
# start: The starting number of the sequence (inclusive). Default is 0.
# stop: The ending number of the sequence (exclusive).
# step: The increment between each number in the sequence. Default is 1.      

for i in range(0, 10, 2):
    print(i)
# yaha do do ke intreval me number print hoga 0,2,4,6,8

for satyam in range(100):
    print(satyam*10)

# yaha 100 tak ke number print hoga aur har number ko 10 se multiply karke print karega
# yaha py 100 ko include nahi karega kyuki range function me stop number exclusive hota hai.
tablenumber  = int(input("enter the number for which you want to print the table: "))
for deta in range(1, 11):

    print(f"{tablenumber}*{deta}={deta*tablenumber}")
else:
    print("table printed successfully")