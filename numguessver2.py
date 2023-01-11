from random import randint
from time import sleep

ans = randint(1,100)
print(ans)
tryok = 1
tryok2 = 1
tryok3 =1
tryok4 = 1
tryok5 = 1
totaltry=1
point = 0
allow =5
allow2=10
allow3=15
allow4=20
allow5=25
username = input("Name please? ")

##1st try
while tryok <= allow:
  guess = int(input(f"So {username}, what will be your choice?: ({tryok}번째 시도입니다)"))
  tryok += 1
  if guess == ans:
    tryok -=1
    print (f"Wow ok you got it. You attempted {tryok} time(s) ")
    totaltry += 1
    point += 20
    print("Your total points= ", point)
    break
  elif guess> ans:
    hint = ("hint : ↓")
    print(hint)
  elif guess < ans:
    hint = ("hint : ↑")
    print(hint)
if tryok >= 5:
  print("5번 끝!!")
  print("Your total points= ", point)
  print("***********************")
  sleep(1)
  print("***********************")
  sleep(1)
  print("***********************")
  sleep(1)
  print("2번째 게임을 시작합니다")  

##2nd try
ans = randint(1,100)
print(ans)
while tryok2 <= allow2:
  guess = int(input(f"[2/5]Best luck {username}, what will be your choice?: ({tryok2}번째 시도입니다)"))
  tryok2 += 1
  if guess == ans:
    tryok2 -= 1
    print (f"Wow ok you got it. You attempted {tryok2} time(s) ")
    totaltry += 1
    point += 20
    print("Your total points= ", point)
    break
  elif guess> ans:
    hint = ("hint : ↓")
    print(hint)
  elif guess < ans:
    hint = ("hint : ↑")
    print(hint)
if tryok2 >= 5:
  print("5번 끝!!")
  print("Your total points= ", point)
  print("***********************")
  sleep(1)
  print("***********************")
  sleep(1)
  print("***********************")
  sleep(1)
  print("3번째 게임을 시작합니다")  

##3rd time
ans = randint(1,100)
print(ans)
while tryok3 <= allow3:
  guess = int(input(f"[3/5]Heyyy {username}, what will be your choice?: ({tryok3}번째 시도입니다)"))
  tryok3 += 1
  if guess == ans:
    tryok3 -=1
    print (f"Wow ok you got it. You attempted {tryok3} time(s) ")
    totaltry += 1
    point += 20
    print("Your total points= ", point)
    break
  elif guess> ans:
    hint = ("hint : ↓")
    print(hint)
  elif guess < ans:
    hint = ("hint : ↑")
    print(hint)
if tryok3 >= 5:
  print("5번 끝!!")
  print("Your total points= ", point)
  print("***********************")
  sleep(1)
  print("***********************")
  sleep(1)
  print("***********************")
  sleep(1)
  print("4번째 게임을 시작합니다")  

##4th time
ans = randint(1,100)
print(ans)
while tryok4 <= allow4:
  guess = int(input(f"[4/5] {username}, what will be your choice?: ({tryok4}번째 시도입니다)"))
  tryok4 += 1
  if guess == ans:
    tryok4 -=1
    print (f"Wow ok you got it. You attempted {tryok4} time(s) ")
    totaltry += 1
    point += 20
    print("Your total points= ", point)
    break
  elif guess> ans:
    hint = ("hint : ↓")
    print(hint)
  elif guess < ans:
    hint = ("hint : ↑")
    print(hint)
if tryok4 >= 5:
  print("5번 끝!!")
  print("Your total points= ", point)
  print("***********************")
  sleep(1)
  print("***********************")
  sleep(1)
  print("***********************")
  sleep(1)
  print("5번째 게임을 시작합니다")  

##5th time
ans = randint(1,100)
print(ans)
while tryok5 <= allow5:
  guess = int(input(f"[5/5] {username}, what will be your choice?: ({tryok5}번째 시도입니다)"))
  tryok5 += 1
  if guess == ans:
    tryok5 -=1
    print (f"Wow ok you got it. You attempted {tryok5} time(s) ")
    totaltry += 1
    point += 20
    print("Your total points= ", point)
    break
  elif guess> ans:
    hint = ("hint : ↓")
    print(hint)
  elif guess < ans:
    hint = ("hint : ↑")
    print(hint)
if tryok5 >= 5:
  print("5번 끝!!")
  print("Your total points= ", point)
  print("***********************")
  sleep(1)
  print("***********************")
  sleep(1)
  print("***********************")
  sleep(1)




if totaltry >= 5 and point == 100:
  print("5/5 You genius!")
elif totaltry >= 5 and point ==80:
  print("4/5 Not bad at all")
elif totaltry >= 5 and point == 0: 
  print("0/5 You lame ass hell")

