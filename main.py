print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ / _` / __| | | | '__/ _  / __| |/ _` | '_  / _` |
| |_| | |  __/ (_| __  |_| | | |  __/ __  | (_| | | | | (_| |
 __|_|  ___|__,_|___/__,_|_|  ___|_|___/_|__,_|_| |_|__,_|
 
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a crossroad. Where do you want to go?\n    Type 'left' or 'right'\n")

choice = input()

if choice == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.\n   Type 'wait' to wait for the boat."
          "Type 'swim' to swim towards the island.\n")
    choice = input()
    if choice == 'wait':
        print("You've arrived at the island unharmed. There is a house with three doors.\n   One red, one yellow and"
              " one blue. Which color do you choose?\n")
        choice = input()
        if choice == 'yellow':
            print("Congratulations!! You found the treasure!.")
        else:
            if choice == 'red':
                print("You've entered a room full of mosquitoes. You've died from blood loss!.")
            else:
                print("You've entered the deep sea!. Oops! you've exploded, painting the sea red due to internal pressure.")
    else:
        print("You tried to swim, but u dont have enough stamina!. You've Died.")
else:
    print("Siikeeee!!! wrong choice!. You've died from a crashing meteor. Your existence is now disintegrated.")
