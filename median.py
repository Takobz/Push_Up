numbers = []
number = 0
n = int(input())

for i in range(0, n):
    number = int(input())
    numbers.append(number)
    
median = sum(numbers)/2
print(median)
