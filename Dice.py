import random

def dice_random(num_dice,num_side):
    rolls=[]
    for _ in range(num_dice):
        roll=random.randint(1,num_side)
        rolls.append(roll)
    return rolls


n_d=2
n_s=6
result=dice_random(n_d,n_s)
print(f'The result of rolling{n_d} dice with {n_s}sides each:{result}')
print(sum(result))