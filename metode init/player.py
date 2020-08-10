class Player:
    name  = ''
    speed = ''

    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed


player = Player('Dybala', '86')
player2 = Player('Messi', '94')
print(player.getName() + ' punya speed ' + player.getSpeed())
print(player2.getName() + ' punya speed ' + player2.getSpeed())
