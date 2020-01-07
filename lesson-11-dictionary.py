#
#
# item = kye and value

enemy = {
    'loc_x': '170',
    'loc_y': '90',
    'color': 'yellow',
    'health': '85',
    'name': 'Sergio',
}
print(enemy)

print('Location X is: ' + str(enemy['loc_x']))
print('Location Y is: ' + str(enemy['loc_y']))
print('Name is: ' + str(enemy['name']))

enemy['rank'] = 'Admin'
print(enemy)

#remove item
# del enemy['rank']
# print(enemy)


enemy['loc_x'] = enemy['loc_x'] + 10
enemy['health'] = enemy['health'] - 70
if enemy ['health'] < 80:
    enemy['color'] = 'red'

print(enemy)