import random
from time import sleep

min = 1
max = 6

print ("Rolling the dices...")
sleep(1)
print ("The values are....")
sleep(1)
print (random.randint(min, max))
sleep(1)
print ("would you like to roll again")

if input() == 'yes':
    print ("Rolling the dices...")
    sleep(1)
    print ("The values are....")
    sleep(1)
    print (random.randint(min, max))
    sleep(1)
    print ("would you like to roll again")
