from User import User
from Bid import Bid


class Auction:
    auctionedItem = ""
    host = User("", 0)
    active = False
    bids = []
    highestBid = Bid(User("", 0), 0)

    def __init__(self, auctionedItem, host):
        self.auctionedItem = auctionedItem
        self.host = host
        self.host.getAuctions().append(self)
        self.active = True
        self.bids = list()

    def getAuctionedItem(self):
        return self.auctionedItem

    def getHost(self):
        return self.host

    def getStatus(self):
        return self.active

    def setStatus(self, status):
        self.active = status

    def getBids(self):
        return self.bids

    def setBids(self, bid):
        self.bids.append(bid)

    def getHighestBid(self):
        return self.highestBid

    def setHighestBid(self, bid):
        self.highestBid = bid

    def bidding(self, user, cash=None):
        if not self.getStatus():
            print("Auction is not open")
            return False
        elif user == self.getHost():
            print("User can't bid because he's the owner of the auction")
            return False
        elif cash is not None:
            if user.getCredit() < cash:
                print("User lacks funds to make this bid")
                return False
            elif len(self.getBids()) < 1:
                self.getBids().append(Bid(user, cash))
                print("First bid has been sent")
                self.setHighestBid(Bid(user, cash))
                return True
            elif cash < self.getHighestBid().getBidCash():
                print("Can't bid beacuse this bid is lower than highest bid")
                return False
            else:
                self.setBids(Bid(user, cash))
                self.setHighestBid(Bid(user, cash))
                print("The bid was done successfully")
        else:
            if user.getCredit() < self.getHighestBid().getBidCash() + 1:
                print("User lacks funds to make this bid")
                return False
            elif len(self.getBids()) < 1:
                self.getBids().append(Bid(user, 1))
                print("First bid has been sent")
                self.setHighestBid(Bid(user, 1))
                return True
            else:
                self.getBids().append(self.getHighestBid().getBidCash() + 1)
                self.setHighestBid(Bid(user, self.getHighestBid().getBidCash() + 1))
                return True


    def execute(self):
        if not self.getStatus() or len(self.getBids()) < 1:
            return False
        else:
            User.decreaseCredit(Bid.getBidder(self.getHighestBid()), Bid.getBidCash(self.getHighestBid()))
            User.incrementCredit(self.getHost(), Bid.getBidCash(self.getHighestBid()))
            self.setStatus(False)
            return True
