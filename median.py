numbers = []
number = 0
median = 0.0
n = int(input())

for i in range(0, n):
    number = int(input())
    numbers.append(number)

numbers = sorted(numbers)
half = (n//2)
if (n % 2) == 0:
    median = (numbers[half] + numbers[half - 1])/2
else:
    median = numbers[half]
    
print(median)
