class Player:

    def __init__(self,name):
        self.name = name
        self.__age = '23' #permanen tidak bisa diganti

    def getName(self):
        return self.name

    def getAge(self):
        return self.__age

class ArgentinaPlayer(Player):
    pass

player = ArgentinaPlayer('Dybala')
print(player.getAge() + ' - ' + player.getName())

