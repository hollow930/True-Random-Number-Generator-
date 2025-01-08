from random_number import random_number
import matplotlib.pyplot as plt
from collections import Counter

randomList = []

for i in range(100000):
    print(i)
    randomList.append(random_number(1000))

print(randomList)
frequency = Counter(randomList)

x = list(frequency.keys())  
y = list(frequency.values())  

plt.bar(x, y)
plt.xlabel('Numbers')
plt.ylabel('Frequency')
plt.title('Frequency of Numbers in the List')
plt.show()
