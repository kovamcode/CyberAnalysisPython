
'''csv_file_path = 'cybersecurity_attacks.csv'


with open(csv_file_path, 'r') as file:
    
    lines = file.readlines()


data = [line.strip().split(',') for line in lines]


for row in data[:5]: 
    print(row)
'''
f = open ('cybersecurity_attacks.csv', 'r')

entire_file = f.read()
print(entire_file)

f.close