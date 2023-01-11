from random import shuffle, choice, randint

result = {
    'stay_to_win':0,
    'move_to_win':0,
}

doors = [0,0,1] #0:goat, 1:car
for x in range(1000):
    shuffle(doors)
    user_choice = choice(doors)
    if user_choice == 0:
        result ['move_to_win'] += 1
    else:
        result['stay_to_win'] += 1
print(result)
