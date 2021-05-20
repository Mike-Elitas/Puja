class Bid:

    def __init__(self, bidder, bidCash):
        self.bidder = bidder
        self.bidCash = bidCash

    def getBidder(self):
        return self.bidder

    def getBidCash(self):
        return self.bidCash
