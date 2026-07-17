l = int(input("enter a number for which you whant sum of n netural number: "))

def sum(k):
    if k==1:
        return 1
    return sum(k-1)+k

print(sum(l))


# yaha py ek problem hai function ek hazar se jyda khud ko call nahi kar sakta erro aa raha hai maximum recursion depth exceeded in comparison.
# lets try to solve this problem by using a loop instead of recursion.

n = int(input("enter a number for which you whant sum of n netural number: "))
def sumation(k):
    total = 0
    for i in range(1,k+1):
        total += i
    return total
print(sumation(n))