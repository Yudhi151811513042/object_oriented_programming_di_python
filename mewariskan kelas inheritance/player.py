class Player:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

class ArgentinaPlayer(Player):
    def setAge(self, age):
        self.age = age
        return self.age



player2 = ArgentinaPlayer('Messi', '94')

print(player2.getName() + ' umurnya ' + player2.setAge('35') + ' dan mempunyai speed ' + player2.getSpeed())
