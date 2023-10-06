import math
import random

map = [
    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2],
    [2, 2, 2, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
    [2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

towerMap = [
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

towerData = {
    'cannon': {
        'name':'cannon',
        'range': 90,
        'speed': 1,
        'bullet_size': 5,
        'popping_strength': 1,
        'cost': 250,
        'color': 'red',
        'upgrades': [{
            'faster': [200, 1.50],
            'faster 2': [100, 1.75],
            'even faster': [100, 2.00],
        }],
    },

    'regular': {
        'name':'regular',
        'range': 90,
        'speed': 1,
        'bullet_size': 5,
        'popping_strength': 1,
        'cost': 250,
        'color': 'blue',
        'upgrades': [{
            'faster': [200, 1.50],
            'faster 2': [100, 1.75],
            'even faster': [100, 2.00],
        }],
    },

    'freeze': {
        'name':'freeze',
        'range': 90,
        'speed': 1,
        'bullet_size': 5,
        'popping_strength': 1,
        'cost': 250,
        'color': 'lightblue',
        'upgrades': [{
            'faster': [200, 1.50],
            'faster 2': [100, 1.75],
            'even faster': [100, 2.00],
        }],
    },

    'minigun': {
        'name':'minigun',
        'range': 90,
        'speed': 1,
        'bullet_size': 5,
        'popping_strength': 1,
        'cost': 250,
        'color': 'black',
        'upgrades': [{
            'faster': [200, 1.50],
            'faster 2': [100, 1.75],
            'even faster': [100, 2.00],
        }],
    },

    'tack': {
        'name':'tack',
        'range': 90,
        'speed': 1,
        'bullet_size': 5,
        'popping_strength': 1,
        'cost': 250,
        'color': 'pink',
        'upgrades': [{
            'faster': [200, 1.50],
            'faster 2': [100, 1.75],
            'even faster': [100, 2.00],
        }],
    },
}

balloonData = {
   # Instead of including color data, each balloon object has a level 
   # that is used to find the color on the client
   '1': {'name':'Red Balloon',
        'speed': 1,
        'level': 1,
        'cost': 50,
        'upgrades': [1.50, 1.75, 2.00],
   },
   '2': {'name':'Blue Balloon',
        'speed': 1,
        'level': 1,
        'cost': 50,
        'upgrades': [1.50, 1.75, 2.00],
    },
    '3': {'name':'Green Balloon',
        'speed': 1,
        'level': 3,
        'cost': 50,
        'upgrades': [1.50, 1.75, 2.00],
    },
    '4': {'name':'Yellow Balloon',
        'speed': 1,
        'level': 1,
        'cost': 50,
        'upgrades': [1.50, 1.75, 2.00],
    },
    '5': {'name':'Purple Balloon',
        'speed': 1,
        'level': 3,
        'cost': 50,
        'upgrades': [1.50, 1.75, 2.00],
    },
    '6': {'name':'Purple Balloon',
        'speed': 1,
        'level': 3,
        'cost': 50,
        'upgrades': [1.50, 1.75, 2.00],
    },
    '7': {'name':'Pink Balloon',
        'speed': 1,
        'level': 3,
        'cost': 50,
        'upgrades': [1.50, 1.75, 2.00],
    },
    '8': {'name':'Gray Balloon',
        'speed': 1,
        'level': 3,
        'cost': 50,
        'upgrades': [1.50, 1.75, 2.00],
    },
}

class Game:         

    def __init__(game):

        # Uses game rather than self as the parameter because self is used as the parameter for the inner classes

        game.WIDTH = 704
        game.HEIGHT = 512
        game.TILESIZE = 32
        game.BULLET_SPEED = 0.1
        game.POPPING_POWER = 1
        game.SPAWN_TIME = 0.1
        
        game.balloonsLeftInRound = 0
        game.lives = 200
        game.level = 0
        game.coins = 1000
        game.selectedTower = {}

        game.towerMap = towerMap
        game.balloonData = balloonData
        game.selectedTower = {}
         
        class Balloon:
            def __init__(self, params):
                if params['x'] and params['y']:
                    self.x = math.floor(params['x'] / game.TILESIZE) * game.TILESIZE
                    self.y = math.floor(params['y'] / game.TILESIZE) * game.TILESIZE
                else:
                    self.x = -game.TILESIZE
                    self.y = (2 * game.TILESIZE)

                self.radius = game.TILESIZE / 2
                self.speed = game.balloonData[str(params['level'])]['speed']
                self.direction = 'left'
                self.level = params['level']
                self.id = random.random()
                self.hit = False
                game.balloonsLeftInRound += 1

            def shot(self, value):
                self.hit = value

            def move(self):
                currentTileX = math.floor(self.x / game.TILESIZE)
                currentTileY = math.floor(self.y / game.TILESIZE)
                if currentTileY < (len(map) - 1) and currentTileX < (len(map[0]) - 1):
                    if(currentTileX < 0):
                        self.x += self.speed
                    else:
                        if map[currentTileY][currentTileX + 1] != 1:
                            self.direction = 'down'
                        elif map[currentTileY + 1][currentTileX] != 1:
                            self.direction = 'left'
                        if(self.direction == 'left'):
                            self.x += self.speed
                        elif(self.direction == 'down'):
                            self.y += self.speed
    
        class Balloons:
            def __init__(self):
                self.balloons = []

            def __len__(self):
                return len(self.balloons)
            
            def state(self):
                output = []
                for balloon in self.balloons:
                    output.append([balloon.x, balloon.y, balloon.level]);
                return output
        
            def newBalloon(self, balloonData):
                balloon = Balloon(balloonData);
                self.balloons.append(balloon);
                return balloon

            def allBalloons(self):
                return self.balloons;

            def numberOfBalloons(self):
                return self.balloons.length;

            def checkBalloons(self):
                newBalloons = [];
                for balloon in self.balloons:
                    if math.floor(balloon.x + (balloon.radius * 2)) + 1 >= game.WIDTH:
                            game.lives -= balloon.level;
                            game.balloonsLeftInRound -= 1;
                            if(game.lives < 0):
                                game.lives = 0;
                    else:
                        newBalloons.append(balloon);
                self.balloons = newBalloons;

            def checkCollisions(self):
                newBalloons = []
                currentBullets = game.bullets.allBullets()
                newBullets = []

                if len(self.balloons) > 0:
                    for balloon in self.balloons:
                        newBullets = []
                        for bullet in currentBullets:
                            if balloon.x + (balloon.radius * 2) >= bullet.x and balloon.x <= bullet.x + (bullet.radius * 2) and balloon.y + (balloon.radius * 2) >= bullet.y and balloon.y <= bullet.y + (bullet.radius * 2):
                                game.coins += balloon.level
                                balloon.level -= bullet.poppingPower
                            else:
                                newBullets.append(bullet)
                        currentBullets = newBullets
                        if balloon.level > 0:
                            newBalloons.append(balloon)
                        else:
                            game.balloonsLeftInRound -= 1;
                    self.balloons = newBalloons
                    game.bullets.bullets = newBullets

        class Tower:
            def __init__ (self, towerData):
                self.name = towerData['name']
                self.targetAngle = 0.0
                self.x = towerData['tileX'] * game.TILESIZE
                self.y = towerData['tileY'] * game.TILESIZE
                self.color = towerData['color']
                self.focusX = 0
                self.focusY = 0
                self.newX = 0
                self.newY = 0
                self.scl = 30.0
                self.shootingSpeed = towerData['shootingSpeed']
                self.timer = 30 / towerData['shootingSpeed']
                self.poppingPower = towerData['poppingPower']
                self.id = random.random()

                self.upgradeLevel = 0
                self.upgrades = towerData['upgrades']

                game.towerMap[towerData['tileX']][towerData['tileY']] = 1

                self.cannon = {
                    'x': self.x + 16,
                    'y': self.y + 16
                }

            def upgrade(self):
                index = 0
                for upgrade in self.upgrades[0]:
                    if index == self.upgradeLevel:
                        singleUpgrade = self.upgrades[0][upgrade]
                        if game.coins - singleUpgrade[0] >= 0:
                            if self.shootingSpeed < singleUpgrade[1]:
                                self.shootingSpeed = singleUpgrade[1]
                                game.coins -= singleUpgrade[0]
                                self.upgradeLevel += 1
                                return
                    index += 1
                

            def shoot(self):
                if self.timer < 0:
                    game.bullets.newBullet({
                        'x': self.newX,
                        'y': self.newY,
                        'angle': self.targetAngle,
                        'speed': game.BULLET_SPEED,
                        'poppingPower': self.poppingPower,
                        'color': self.color,
                    })
                    self.timer = 30 / self.shootingSpeed
                self.timer -= 1

            def findNearestBalloon(self):
                closestBalloon = 10 ** 10;
                foundBalloon = False;
                for i in range(0, len(game.balloons.allBalloons())):
                    balloon = game.balloons.allBalloons()[i];
                    x = balloon.x - self.cannon['x'];
                    y = balloon.y - self.cannon['y'];
                    distance = math.sqrt(x * x + y * y)
                    if distance < closestBalloon:
                        foundBalloon = True
                        if balloon.direction == 'left':
                            self.focusX = balloon.x + balloon.radius + (balloon.speed * 5)
                            self.focusY = balloon.y + balloon.radius

                        elif balloon.direction == 'down':
                            self.focusX = balloon.x + balloon.radius
                            self.focusY = balloon.y + balloon.radius + (balloon.speed * 5)

                        closestBalloon = distance;
                    
                self.balloonInRange = foundBalloon;

            def turn(self):
                self.targetAngle = math.atan2(self.focusY - self.cannon['y'], self.focusX - self.cannon['x']);
                self.newX = self.cannon['x'] + math.cos(self.targetAngle) * self.scl;
                self.newY = self.cannon['y'] + math.sin(self.targetAngle) * self.scl;

            def run(self):
                self.findNearestBalloon();
                self.turn();
                if self.balloonInRange:
                    self.shoot();        
    
        class Towers:
            def __init__(self):
                self.towers = []
            
            def state(self):
                output = []
                for tower in self.towers:
                    output.append([round(tower.x, 2),round(tower.y, 2), tower.color, tower.cannon['x'], tower.cannon['y'], tower.newX, tower.newY]);
                return output

            def allTowers(self):
                return self.towers
            
            def newTower(self, towerData):
                tower = Tower(towerData)
                self.towers.append(tower)
                return tower

        class Bullet:
            def __init__(self, bulletData):
                self.x = bulletData['x']
                self.y = bulletData['y']
                self.radius = 5
                self.color = bulletData['color']
                self.angle = bulletData['angle']
                self.speed = bulletData['speed']
                self.scl = 70.0
                self.collision = False
                self.poppingPower = game.POPPING_POWER

            def move(self):
                self.x += (math.cos(self.angle) * self.scl) * self.speed;
                self.y += (math.sin(self.angle) * self.scl) * self.speed;
        
        class Bullets:
            def __init__(self):
                self.bullets = []

            def state(self):
                output = []
                for bullet in self.bullets:
                    output.append([bullet.x, bullet.y, bullet.color, bullet.speed, bullet.angle])
                return output

            def newBullet(self, bulletData):
                bullet = Bullet(bulletData)
                self.bullets.append(bullet)
                return bullet;

            def allBullets(self):
                return self.bullets

            def numberOfBullets(self):
                return self.bullets.length;

            def checkBullets(self):
                output = list(filter(lambda bullet: (
                    bullet.x + bullet.radius < 0 or bullet.x + (bullet.radius * 2) + 2 > game.WIDTH or
                    bullet.y + bullet.radius < 0 or bullet.y + (bullet.radius * 2) + 2 > game.HEIGHT) == False, self.bullets))
                if output != None:
                    self.bullets = output

        game.bullets = Bullets()
        game.balloons = Balloons()
        game.towers = Towers()

    def run(self):
        self.bullets.checkBullets();
        self.balloons.checkBalloons();
        self.balloons.checkCollisions();

        for bullet in self.bullets.allBullets():
            bullet.move()
        for tower in self.towers.allTowers():
            tower.run()
        for balloon in self.balloons.allBalloons():
            balloon.move()

    def spawnBalloons(self, params):
        for i in range(1, params['number'] + 1):
            self.balloons.newBalloon({
                'x': (-i * (2 * self.TILESIZE)),
                'y': 2 * self.TILESIZE,
                'level': params['level'],
                'speed': params['speed']
            })
    
    def nextRound(self):
        if self.balloonsLeftInRound <= 0:
            self.level += 1
            if(self.level == 1):
                self.spawnBalloons({'number': 50, 'level': 1, 'speed': 2})
            elif(self.level == 2):
                self.spawnBalloons({'number': 50, 'level': 2, 'speed': 2})
            elif(self.level == 3):
                self.spawnBalloons({'number': 50, 'level': 3, 'speed': 2})
            elif(self.level == 4):
                self.spawnBalloons({'number': 50, 'level': 4, 'speed': 2})
            else:
                self.spawnBalloons({'number': 100, 'level': 5, 'speed': 2})

    def placeTower(self, data):
        for towerKey in towerData:
            if towerKey == data['name']:
                self.selectedTower = towerData[towerKey]
                break
        if map[data['y']][data['x']] != 1 and self.coins - self.selectedTower['cost'] >= 0:
            self.towers.newTower({
                'name': data['name'],
                'tileX': data['x'],
                'tileY': data['y'],
                'shootingSpeed': self.selectedTower['speed'],
                'poppingPower': self.selectedTower['popping_strength'],
                'color': self.selectedTower['color'],
                'upgrades': self.selectedTower['upgrades']
            })
            self.coins -= self.selectedTower['cost']
            self.selectedTower = {}
            self.towerMap[data['y']][data['x']] = 1

    def upgradeBalloon(self, level):
        currentSpeed = self.balloonData[str(level)]['speed']

        if currentSpeed == self.balloonData[str(level)]['upgrades'][2]:
            return

        newSpeed = self.balloonData[str(level)]['speed'] # at least this speed

        # make change to the stats of balloons with matching level
        for upgrade in self.balloonData[str(level)]['upgrades']:
            if upgrade > currentSpeed:
                self.balloonData[str(level)]['speed'] = upgrade
                newSpeed = upgrade
                break

        # loop through all exisiting balloons of that level
        for balloon in self.balloons.allBalloons():
            if balloon.level == level:
                balloon.speed = newSpeed

    def state(self):
        mainVariablesState = [self.lives, self.level, self.coins, self.selectedTower]
        return [self.balloons.state(), self.towers.state(), self.bullets.state(), mainVariablesState]