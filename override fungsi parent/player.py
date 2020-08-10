class Player:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def getSkill(self):
        return 'normal'

class ArgentinaPlayer(Player):
    def getSkill(self):
        return 'cepat'

class BrazilPlayer(Player):
    def getSkill(self):
        return 'samba'
class IndonesiaPlayer(Player):
    pass


player1 = IndonesiaPlayer('Gonzalez', '80')
player2 = ArgentinaPlayer('Messi', '94')

print(player2.getName() + ' mempunyai speed ' + player2.getSpeed() + ' dan skillnya ' + player2.getSkill())
print(player1.getName() + ' mempunyai speed ' + player1.getSpeed() + ' dan skillnya ' + player1.getSkill())
