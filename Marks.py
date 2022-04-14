data_pairs = {}
number_of_pairs = int(input())
key = ''
value = ''

for i in range(0, number_of_pairs):
    key = input()
    value = input()
    data_pairs[key] = value
    
sorted_data = sorted(data_pairs.items())   
    
for key, value in sorted_data:
    print(key + ':' + value)
