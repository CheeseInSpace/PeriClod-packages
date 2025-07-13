import random
import time

words = ["YOUR TAKING TOO LONG", "YOUR LONG", "YOUR TAKING TOO LONG IS TAKING TOO LONG", "YOUR TAKING TOO TOO", "YOUR TOO TOO", "Hi Didst anyone call Me"]

while True:
    random_word = random.choice(words)
    print(random_word)
    time.sleep(1)