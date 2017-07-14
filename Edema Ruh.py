import random

print("Welcome to Edema Ruh!")
print("You are escaping the Lady Lackless after she finds out you're of the Edema Ruh.")
print("The guards are after you. Make it across The Eld in your wagons to escape them!")

done = False

horse = 0
thirst = 0
drinks = 3
traveled = 0
guards = -20
caught = traveled - guards

while done == False:
    if thirst >= 4 and thirst < 7:
        print("You are thirsty!")
    elif thirst > 6:
        print("You have died of thirst!")
        input("")
        done = True

    if horse > 5 and horse < 9:
        print("Your horse is getting tired.")
    elif horse > 8:
        print("Your horse has died.")
        input("")
        done = True

    if caught < 15 and caught > 0:
        print("The guards are gaining on you!")
    elif caught <= 0:
        print("The guards have captured you!")
        input("")
        done = True

    if traveled >= 200:
        print("You made it across The Eld! Congratulations!")


    print("\nA. Drink from your waterskin")
    print("B. Continue at moderate speed")
    print("C. Full speed ahead")
    print("D. Rest the horses")
    print("E. Status Check")
    print("F. Quit\n")

    action = input("Choose the letter of the action you would like to perform: ")

    if action.lower() == "f":
        done = True

    elif action.lower() == "e":
        print("\nMiles Traveled: ", traveled)
        print("Drinks in waterskin: ", drinks)
        print("The guards are ", traveled - guards, " miles behind you.\n")

    elif action.lower() == "d":
        horse = 0
        print("Your horse gives you a goofy grin to show its appreciation.")
        guards += random.randrange(7,15)

    elif action.lower() == "c":
        traveled += random.randrange(10,21)
        guards += random.randrange(7,15)
        horse += random.randrange(1,3)
        thirst += 1

        if random.randrange(1,21) == 5:
            print("You found a stream! Your horse is rested, you filled your waterskin, and your thirst has been quenched!")
            thirst = 0
            horse = 0
            drinks = 3

    elif action.lower() == "b":
        traveled += random.randrange(5,13)
        guards += random.randrange(7,15)
        thirst += 1
        horse += 1

        if random.randrange(1,21) == 5:
            print("You found a stream! Your horse is rested, you filled your waterskin, and your thirst has been quenched!")
            thirst = 0
            horse = 0
            drinks = 3

    elif action.lower() == "a":

        if drinks > 0:
            drinks = drinks - 1
            thirst = 0
        elif drink <= 0:
            print("You have no more water.")
