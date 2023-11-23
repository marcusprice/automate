import math
import random

MIN = 0
MAX = 20
random_number = math.floor(random.random() * (MAX - MIN)) + MIN
attempts = 1

print("Guess a number between " + str(MIN) + " and " + str(MAX))
i = int(input())

while i != random_number:
    if int(i) > random_number:
        print("too high, try again")
    else:
        print("too low, try again")

    i = int(input())
    attempts += 1

print("Correct, it was " + str(i))
print("Total attempts: "+ str(attempts))
