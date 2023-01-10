from random import randint
from time import sleep

ans = randint(1,100)
print(ans)

username = input("Name please? ")
guess = int(input(f"So {username}, what will be your choice?: "))

if guess > ans:
  hint= ("hint : ↓")
elif guess < ans:
  hint = ("hint : ↑")

while guess != ans:
  print("Hell no ERGGGGGGGGGGGGGGG")
  sleep(1)
  print(hint)
  guessagain = int(input("One more?"))
  if guessagain > ans:
      hint = ("hint : ↓")
  elif guessagain < ans:
      hint = ("hint : ↑")
  elif guessagain is ans:
    sleep(1)
    print("FINALLYY")
    break
