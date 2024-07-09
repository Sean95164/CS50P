import random
n = -1
while n <= 0:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue

answer = random.randint(1,n)
guess = -1

while guess != answer:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue

    if(guess > answer):
        print("Too large!")
    elif(guess < answer):
        print("Too small!")
    else:
        print("Just right!")
