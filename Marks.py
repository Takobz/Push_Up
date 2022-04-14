data_pairs = {}
number_of_pairs = int(input())
key = ''
value = ''

for i in range(0, number_of_pairs):
    key = input()
    value = input()
    data_pairs[key] = value
    
for key, value in data_pairs.items():
    print(key + ':' + value)
