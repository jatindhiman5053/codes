import random
num = random.randint(1, 101)
print("This Is A Guess Game")
inp = int(input("Please Guess The Number Between 1-100 : "))
game_over = 1
guess = 5
flag=0

while game_over<6:
    if num<inp:
        print("You Guess Too High")
        guess = guess-1
        print(f"You Have left with {guess} guess")
        game_over = game_over + 1

    elif num>inp:
        print("You Guess Too Low")
        guess = guess - 1
        print(f"You Have left with {guess} guess")
        game_over = game_over+1

    elif num==inp:
        print("You Guess Correct Number")
        print("Number of Guesses Used By You Is ", game_over)
        flag=1
        break
    
    if guess>0:
         inp = int(input("Guess Again "))

    
if flag==0:
     print("Game Over !!! You Lost The Game ")
     
    

        
