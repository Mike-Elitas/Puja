class User:
    name = ""
    credit = 0
    auctions = []

    def __init__(self, name, credit=None):
        self.name = name
        self.credit = credit

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
