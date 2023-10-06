import json
import random
import string
from . import game

from channels.generic.websocket import AsyncWebsocketConsumer

player_counter = 0
lobbies = {}

def findLobby():
    for lobbyKey in lobbies:
        lobby = lobbies[lobbyKey]
        if lobby['player_number'] < 2:
            lobby['player_number'] += 1
            return lobby['lobby_id']
    lobby_id = "home_%s" % random_string(10)
    lobbies[lobby_id] = {'game': game.Game(),'lobby_id': lobby_id,'player_number': 1}
    return lobby_id

def random_string(n):
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=n))

class GameConsumer(AsyncWebsocketConsumer):
        
    async def connect(self):
        global player_counter
        
        self.game_id = random_string(10)
        self.lobby_id = findLobby()
        self.game = lobbies[self.lobby_id]['game']
        self.playerNumber = lobbies[self.lobby_id]['player_number']
        player_counter += 1
        print(f'Player Number: {self.playerNumber}')
        print(f'Total Players: {player_counter}')
        print(f'Total Lobbies: {len(lobbies)}')

        if(self.playerNumber == 1):
            print("No players found yet. Waiting for opponent.")
        
        package = {
            'type': 'initalization',
            'player': self.playerNumber,
            'text': self.game.state(),
            'game_id': self.game_id,
            'lobby_number': len(lobbies),
        }
        
        await self.accept()
        await self.send(text_data=json.dumps(package))
        await self.channel_layer.group_add(self.lobby_id, self.game_id)

    async def receive(self, text_data):
        data = json.loads(text_data)
        
        if(data['type'] == 'getData'):
            self.game.run();
            self.game.nextRound();
            package = {
                    'type': 'update',
                    'text': self.game.state(),
            }
            await self.send(text_data=json.dumps(package))
        
        if(data['type'] == 'placeTower'):
            if self.game.towerMap[data['y']][data['x']] != 1 and len(data['name']) != 0:
                self.game.placeTower(data)
            else:
                returnedTower = {}
                for tower in self.game.towers.allTowers():
                    if tower.x == data['x'] * self.game.TILESIZE and tower.y == data['y'] * self.game.TILESIZE:
                        returnedTower = tower
                if bool(returnedTower):
                    package = {
                        'type': 'foundTower',
                        'text': [returnedTower.name, returnedTower.x, returnedTower.y, returnedTower.upgradeLevel],
                    }
                    await self.send(text_data=json.dumps(package))
                else:
                    package = {
                        'type': 'foundTower',
                        'text': ['', 0, 0, 0],
                    }
                    await self.send(text_data=json.dumps(package))
        
        if(data['type'] == 'upgradeTower'):
            if self.game.towerMap[data['y']][data['x']] == 1:
                for tower in self.game.towers.allTowers():
                    if (tower.x / self.game.TILESIZE) == data['x'] and (tower.y / self.game.TILESIZE) == data['y']:
                        tower.upgrade()
                        break
        
        if(data['type'] == 'upgradeBalloon'):
            if self.game.coins - (data['level']**2) * 10 >= 0:
                self.game.coins -= (data['level']**2) * 10
                self.game.upgradeBalloon(data['level'])
        
        if(data['type'] == 'placeBalloon'):
            if self.game.coins - (data['level'] * 10) >= 0:
                self.game.coins -= (data['level']**2) * 10
                self.game.spawnBalloons({
                    'level': data['level'],
                    'speed': 2.1,
                    'number': 10,
                })
            
    async def disconnect(self, code):
        global player_counter
        player_counter-=1
        await self.channel_layer.group_discard(self.lobby_id, self.game_id)