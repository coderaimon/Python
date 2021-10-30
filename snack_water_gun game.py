# snack water gun game 
import random

randNum = random.randint(1,3)
if randNum == 1:
    comp = 's'
elif randNum == 2:
    comp = 'w'
elif randNum == 3:
    comp = 'g'
# game structure functioning
def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Computer turn sanck(s) water(w) gun(g):?")
you = input("Your turn sanck(s) water(w) gun(g): ")
result = game(comp, you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

if result == None:
    print("The Game is draw")
elif result:
    print("Congratulations! You win!")
else:
    print("You lose!")

