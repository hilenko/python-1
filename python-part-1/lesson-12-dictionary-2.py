enemy = {
    'loc_x': '90',
    'loc_y': '90',
    'color': 'yellow',
    'health': '100',
    'name': 'Sergio',
    'images': ['images.jpg', 'images2.jpg', 'images3.jpg']
}

all_enemy = []

for i in range(0,10):
    all_enemy.append(enemy.copy())

for i in all_enemy:
    print(i)

print('================================================================')

all_enemy[4]['health'] = 30
all_enemy[0]['name'] = 'LEXA'
all_enemy[2]['loc_x'] += 10

for i in all_enemy:
    print(i)