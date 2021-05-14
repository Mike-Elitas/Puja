class User:
    name = ""
    credit = 0

    def __init__(self, name):
        self.name = name

    def __init__(self, name, credit):
        self.name = name
        self.credit = credit

    def getName(self):
        return self.name

    def getCredit(self):
        return self.credit

    def incrementCredit(self, cash):
        self.credit = self.credit + cash

    def decreaseCredit(self, cash):
        self.credit = self.credit - cash

    
