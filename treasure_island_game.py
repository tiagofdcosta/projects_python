
print(r'''
           _.====.._
         ,:._       ~-_
             `\        ~-_
               | _  _  |  `.
             ,/ /_)/ | |    ~-_
    -..__..-''  \_ \_\ `_      ~~-.._Tiago Costa_..----..
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print()

where_go = input("Where do you want to go? 'left' or 'right'\n").lower()
if where_go == "left":
    print("Nice, good choice.\nWe found a bit of water")
    water = input("Do you prefer 'swim' or wait a 'boat'\n").lower()
    if water == "swim":
        print("WoOoOoOW.. you´re like Mickel Phelps.\nNow, in the island we found a big house")
        door = input ("The house have a 3 doors: 'Red' - 'Green' - 'White'\nChoose one!\n").lower()
        if door == "red":
            print("OHH NOOOO... FIRE. GAME OVER!")
        elif door == "green":
            print("Today its your day!")
            print("==== YOU WIN ====")
            print("** Congratulations **")
        elif door == "white":
            print("OHH NOOOO...The devil coming. GAME OVER")
        else:
            print("This door dont exist, sorry. GAME OVER!")
    else:
        print("The boat exploded. GAME OVER!")
else:
    print("Nooooo, the right side its not good. GAME OVER!")
