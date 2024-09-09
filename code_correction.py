# Task 1
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    #else:
        #pass
elif place == "cave":
    action2 = input("light a torch or proceed in the dark? ")
    if action2 == "light a torch":
        print("Light it up!")
    elif action2 == "proceed in the dark":
        print("Watch your steps!")
    else:
        pass
else:
    pass
    # print("Just go home!")  - removed from task 2, replaced with PASS
    # print("You found a hidden treasure!") removed from task 1

# Task 2 - changes were made above for task 2

# Task 3

