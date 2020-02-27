Start Screen (Choose Difficulty)
    1. Easy (24 Turns (0000 - 0600))
    2. Medium (16 Turns (0200 - 0600))
    3. Hard (8 Turn (0400 - 0600))

Weapons = None
Consumables = None
Health = 100
Map = Start middle
Turns = depending Difficulty

END SCREEN = "You failed to escape"

    If difficulty chosen...
        if turns left <= 0, go to END SCREEN
        if health <= 0, go to END SCREEN
            if health > 0, and turns left > 0 go to NEXT TURN

NEXT TURN
    Choose = North, East, South, West or Inv, Use, Map
    If north : move north
    If east : move east
    If south : move south
    If west : move west
        if moved : RNG CODE
    If inv : show inventory (I.e weapons and consumables)
    If map : show map

END TURN
    If move north, east, south, west
        then turns - 1

MAP
    if map
        print MAP

INV CODE
    if inv
        print : weapons + consumables

HEALTH
    if event that removes HEALTH
        health - # of health in event = new health

RNG CODE
    Random Number Generated (1-10)
        if 1 : Battle someone (Y/N if use weapons)
        if 2 : Explore something (Y/N)
        if 3 : Talk to someone (Y/N)
        if 4 : You are found (LOSE)
            only if health <= 50
        if 5 : You find a Weapons
            RNG (1-3)
                1. Rifle
                2. Pistol
                3. Knife
        if 6 : You find a Consumables
            RNG (1-3)
                1. Bandages
                2. Food
                3. Water
        if 7 : You are thirty
            if no water drink puddle
                RNG(1-2)
                    1. You are fine
                    2. You loose Health
        if 8 : You are hungry
            if no food you eat bark
                RNG(1-2)
                    1. You are find
                    2. You loose Health
        if 9 : You fall into a trap
            RNG (1-2) each turn
                1. You get out
                2. Loose a turn, try again
        if 10 : You begin to get tracked
            From now on each turn RNG(1-5)
                if 1-4 all good
                if 5 you go to END SCREEN
