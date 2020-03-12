# Course: CS 30
# Period: 4
# Date created: 9/03/20
# Date last modified: 10/03/20
# Name: Maksim Sharoika
# Description: Game Test Program (Nested Dictionaries)
##########
# Nested dictionary for characters
characters = {"Friendly": {"Prisoner", "Friend", "Escapee"},
              "Aggresive": {"Guard", "Guard Dog"}
              }
##########
# Nested dictionary for inventory
inventory = {"tool": {"Hammer", "Screwdriver"},
             "weapon": {"Gun", "Knife", "Rifle"},
             "item": {"Key", "Bandages"}
             }
##########
# Nested dictionary for locations
locations = {"Barracks": {"direction": "West", "owner": "Guards"},
             "Cells": {"direction": "East", "owner": "Prisoners"}
             }
##########
# Heading for characters
print("---Characters---")
##########
# Loop for the characters and thier behaviors
for behavior in characters:
    characternames = characters[behavior]
    for name in characternames:
        print(f"{name} is {behavior}.")
##########
# Heading for inventory
print("---Inventory---")
##########
# Loop for the invetory and its item types
for itemtypes in inventory:
    itemtype = inventory[itemtypes]
    for itemname in itemtype:
        print(f"{itemname} is a {itemtypes}.")
##########
# Heading for locations
print("---Locations---")
##########
# Loop for the location with its direction and owner.
for location in locations:
    owner = locations[location]["owner"]
    direction = locations[location]["direction"]
    print(f"The {location} are to the {direction} and owned by the {owner}.")
