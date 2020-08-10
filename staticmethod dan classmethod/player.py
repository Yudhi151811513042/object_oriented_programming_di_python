class Player:
    job = 'football player'

    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    #classmethod && staticmethod
    @staticmethod
    def retiredIn(age):
        return str(40 - age)

    @classmethod
    def generalInfo(cls, age):
        return cls.job + ' ini akan pensiun dalam ' +  cls.retiredIn(age) + 'thn'



'''player = Player('Dybala')
print(player.getName())'''
#print('pensiun dalam ' +Player.retiredIn(25) + ' tahun')
print(Player.generalInfo(20))