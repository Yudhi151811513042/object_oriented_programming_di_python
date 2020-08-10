class Player:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

class ArgentinaPlayer(Player):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        print('HELLO Argentina')



player2 = ArgentinaPlayer('Messi','94')

print(player2.getName() + ' mempunyai speed ' + player2.getSpeed())
