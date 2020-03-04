# Course: CS 30
# Period: 4
# Date created: 12/02/20
# Date last modified: 04/03/20
# Name: Maksim Sharoika
# Description: Inventory Test Program
##########
# Creating the lists for the inventory.
consumables = []
weapons = []
##########
# Seperation line.
print('--------------------')
##########
# Saying the items that are in the inventory at start.
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{consumables}'
)
##########
# Seperation line.
print('--------------------')
##########
# Appending and inserting weapons and consumables into inventory.
print('1. Weapons and consumables picked up!')
weapons.append('knife')
weapons.append('rifle')
consumables.insert(0, 'food')
consumables.insert(0, 'water')
consumables.insert(0, 'bandages')
# Using a loop to print out the items that are being used.
print(f'Current weapons : ')
for w in weapons:
    print(f" - {w}")
print(f'Current consumables : ')
for c in consumables:
    print(f' - {c}')
##########
# Seperation line.
print('--------------------')
##########
# Removing an item from the list using the pop() command.
print('2. You eat some food because you are hungry!')
consumables.pop()
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{consumables}'
)
##########
# Seperation line.
print('--------------------')
##########
# Removing an item from the list using the del command.
print('3. You relize you dont have any bullets and chuck the gun!')
del weapons[1]
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{consumables}'
)
##########
# Seperation line.
print('--------------------')
##########
# Removing an item from the list using the remove command, adding via append.
print('4. You stab someone, loose knife gain chunk of flesh')
weapons.remove('knife')
consumables.append('flesh')
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{consumables}'
)
##########
# Seperation line.
print('--------------------')
##########
# Sorting the items in the correct order.
print('5. You take a break, and decide to sort your things!')
consumables.sort()
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{consumables}'
)
##########
# Seperation line.
print('--------------------')
##########
# Sorting the items in the reverse order via sorted command.
print('6. You dont like that way, so you sort them backwards!')
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{sorted(consumables, reverse = True)}'
)
##########
# Seperation line.
print('--------------------')
##########
# Sorting the items in the reverse order via reverse command.
print('7. You like it that way so you keep it like that!')
consumables.reverse()
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{consumables}'
)
##########
# Seperation line.
# Using the len() command to say the number in the list.
print('--------------------')
##########
print('8. A man asks you how many items you are carrying!')
print('You say: I have ' + f'{len(consumables) + len(weapons)}' + ' items.')
##########
# Seperation line.
print('--------------------')
##########
# You pick up two new items
weapons.insert(0, 'Sledgehammer')
consumables.insert(0, 'Mac & Cheese')
print('8. A man asks you how many items you are carrying!')
print('You picked up ' + f'{consumables[0]}' + 'and a ' + f'{weapons[0]}')
##########
print('--------------------')
##########
