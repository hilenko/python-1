import json

filename = 'user_settings.txt'
myfile = open(filename, mode='w', encoding='latin-1')

player1 = {
    'playername': 'Donald Thurnat',
    'score': 1,
    'awards': ['NY', 'NV', 'RO']
}

player2 = {
    'playername': 'Robert Joy',
    'score': 5,
    'awards': ['TX', 'WI', 'MI']
}

all_players = []
all_players.append(player1)
all_players.append(player2)

# =======SAVE IN JSON
json.dump(all_players,  myfile)
myfile.close()

# ========LOAD BY JSON
myfile = open(filename, mode='r', encoding='latin-1')
json_data = json.load(myfile)

for user in json_data:
    print('player name is: ' + str((user)['playername']))
    print('player score is: ' + str((user)['score']))
    print('player awards 1 is: ' + str((user)['awards'][0]))
    print('player awards 2 is: ' + str((user)['awards'][1]))
    print('player awards 3 is: ' + str((user)['awards'][2]))

    print('\n\n\t=====================')

