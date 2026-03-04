import numpy as np
game = ["R","P","S"]
rng = np.random.default_rng()
comp =rng.choice(game,1)[0]


player = input("Please enter 'R', 'P', or 'S' (uppercase):")[0]  #only takes in first character

if player== "S" or player=="R" or player=="P":
    if player == comp:
        result ="tie"
    elif player == "S":
        if comp == "R":
            result = "lose"
        else:
            result = "win"
    elif player == "R":
        if comp == "S":
            result = "win"
        else:
            result = "lose" 
    else:
        if comp == "R":
            result = "win"
        else:
            result = "lose"    
    print("Computer plays:"+comp) 

    print("You "+result+"!")
    
else: 

    print("Please try again with the correct input")
   