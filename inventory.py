# Course: CS 30
# Period: 4
# Date created: 12/02/20
# Date last modified: 13/02/20
# Name: Maksim Sharoika
# Description: Inventory Test Program
consumables = []
weapons = []

print('--------------------')
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{consumables}'
)
##########
print('--------------------')
##########
print('1. Weapons and consumables picked up!')
weapons.append('knife')
weapons.append('rifle')
consumables.insert(0, 'food')
consumables.insert(0, 'water')
consumables.insert(0, 'bandages')
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{consumables}'
)
##########
print('--------------------')
##########
print('2. You eat some food because you are hungry!')
consumables.pop()
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{consumables}'
)
##########
print('--------------------')
##########
print('3. You relize you dont have any bullets and chuck the gun!')
del weapons[1]
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{consumables}'
)
##########
print('--------------------')
##########
print('4. You stab someone, loose knife gain chunk of flesh')
weapons.remove('knife')
consumables.append('flesh')
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{consumables}'
)
##########
print('--------------------')
##########
print('5. You take a break, and decide to sort your things!')
consumables.sort()
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{consumables}'
)
##########
print('--------------------')
##########
print('6. You dont like that way, so you sort them backwards!')
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{sorted(consumables, reverse = True)}'
)
##########
print('--------------------')
##########
print('7. You like it that way so you keep it like that!')
consumables.reverse()
print(
    'Currents weapons : ' + f'{weapons}'
    f'\n'
    'Current consumables : ' + f'{consumables}'
)
##########
print('--------------------')
##########
print('8. A man asks you how many items you are carrying!')
print('You say: I have ' + f'{len(consumables)}' + ' items.')
##########
print('--------------------')
##########
