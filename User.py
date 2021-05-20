class User:

    def __init__(self, name, credit=None):
        self.name = name
        self.credit = credit
        self.auctions = list()

    def getName(self):
        return self.name

    def getCredit(self):
        return self.credit

    def getAuctions(self):
        return self.auctions

    def incrementCredit(self, cash):
        self.credit = self.credit + cash

    def decreaseCredit(self, cash):
        self.credit = self.credit - cash
