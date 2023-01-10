from random import randint
from time import sleep

answer = randint(1,100)

##for debugging
print(answer)

username = input("Name please? ")
guess = int(input(f"So {username}, what is your choice?: "))

#compare answer with user's guess



if guess > ans:
  hint= ("hint : ↓")
elif guess < ans:
  hint = ("hint : ↑")

if guess == answer:
    print("************************")
    sleep(1)
    print("************************")
    sleep(1)
    print("Excellent Choice! You got it!")
elif guess != answer:
    print(hint, "ERGGGGGGGG!!!!!!! YOU STUPID"

