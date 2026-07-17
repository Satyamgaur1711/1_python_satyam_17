#  *
# ***
#*****
# for n = 3

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    print(" "*(n-i)+"*"*(1+(i-1)*2))

new_number = int(input("Enter the number of new rows: "))
for l in range(1, new_number+1):
    print(" "*((n-l)*2)  +  "*"*(1+(l-1)*4))
