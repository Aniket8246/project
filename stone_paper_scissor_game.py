import random
def gameWin(comp,you):
    if comp =='s':
        if you =='p':
            return True
        elif you == 'c':
            return False
    elif comp =='p':
        if you == 'c':
            return True
        elif you =='s':
            return False
    elif comp =='c':
        if you =='s':
            return True
        elif you =='p':
            return False
print("comp turn : stone(s) paper(p) scissors(c) :")
randNo = random.randint(1,3)
if randNo == 1:
    comp ='s'
elif randNo ==2:
    comp ='p'
elif randNo == 3:
    comp = 'c'

you = input("you turn : stone(s) , paper(p) , scisors(c)")
a = gameWin(comp,you)

print(f"comp choose {comp}  :")
print(f"you choose {you}  :")
if a ==None :
    print("the game is a tie")
elif a:
    print('you win ')
else:
    print("you lose")