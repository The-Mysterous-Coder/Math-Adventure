
answer = input("Would you like to play? (yes/no) ")

if answer.lower().strip() == "yes":
    
    answer = input("\nYou were voted to get food for your tribe you are in a nuclear wasteland after WW3 where will you go first (left/right) \n\nif you would like to go left do the problem -4 x 2 to move left and do -20 / 5 to move right (hint: follow the rules of add/subtracting/multiplying/dividing integers) ").lower().strip()

    if answer == "-8":
        answer = input("\nYou go to the left and see a small pit to the left, a path that continues straight, and a cut into the forest to the right")
    elif answer == "-4":
        answer = input("\nYou go to the right and encounter a Monster what do you do (ignore/attack) \n\n If you would like to ignore do -45/-2 if you would like to attack then do 23 + -3 ")
        if answer == "22.5":
            answer = input("fgfgfgfg")
    else:
        print("\nYou trip and choke on a Skittle.Game Over")

        
        
    
else:
    print("That's to bad!")
