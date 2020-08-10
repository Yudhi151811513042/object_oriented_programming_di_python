class Player:
    name = ''

    def getName(self, name):
        self.name = name
        return self.name

#di luar class
pemain = Player()
pemain2 = Player()
print(pemain.getName('Mbappe'))
print(pemain.getName('Rooney'))
