from random import randint

answer = randint(1,100)

username = input("Name please? ")
guess = int(input(f"So {username}, what is your choice?: "))
if guess is answer:
  print("Excellent Choice! You got it!")
else :
  print("hmm I don't think so mate")
