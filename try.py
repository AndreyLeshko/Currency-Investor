import random

my_set = set()
while len(my_set) < 100:
    num = random.randint(1000000, 9999999)
    my_set.add(num)
print(*my_set, sep='\n')