from User import User
from Bid import Bid


class Auction:
    auctionedItem = ""
    host = User
    active = False
    bids = [Bid]
    highestBid = Bid

    def __init__(self, auctionedItem, host, active):
        self.auctionedItem = auctionedItem
        self.host = host
        self.active = active

    def getAuctionedItem(self):
        return self.auctionedItem

    def getHost(self):
        return self.host

    def getStatus(self):
        return self.active

    def getBids(self):
        return self.bids

    def getHighestBid(self):
        return self.bids.__getitem__(len(self.bids) - 1)
