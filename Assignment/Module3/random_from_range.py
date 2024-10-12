import random
start_number=int(input('Enter First Number: '))
last_number=int(input('Enter Last Number: '))
myrange=range(start_number,last_number)
random_item=random.choice(myrange)
print(random_item)