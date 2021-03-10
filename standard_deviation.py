import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To remove headers from CSV
data = file_data[0]
print(data)
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total+=int(x)
    mean = total/n
    print(mean)
    return mean
#squaring the value
square_list = []
for number in data:
    a = int(number)-mean(data)
    print(str(a))
    a = a**2
    square_list.append(a)
#getting sum
sum = 0
for i in square_list:
    sum = sum+i
#diving sum by total values
result = sum/(len(data)-1)
#getting devation by sqaure root
std_deviation = math.sqrt(result)
print(std_deviation )