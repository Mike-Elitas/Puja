from User import User


class Bid:
    bidder = User("", 0)
    bidCash = 0

    def __init__(self, bidder, bidCash):
        self.bidder = bidder
        self.bidCash = bidCash

    def getBidder(self):
        return self.bidder

    def getBidCash(self):
        return self.bidCash
