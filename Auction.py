from User import User
from Bid import Bid


class Auction:
    auctionedItem = ""
    host = User
    active = False
    bids = []
    if len(bids) > 0:
        highestBid = bids.__getitem__(len(bids) - 1)
    else:
        highestBid = None

    def __init__(self, auctionedItem, host):
        self.auctionedItem = auctionedItem
        self.host = host
        self.host.getAuctions().append(self)
        self.active = True

    def getAuctionedItem(self):
        return self.auctionedItem

    def getHost(self):
        return self.host

    def getStatus(self):
        return self.active

    def getBids(self):
        return self.bids

    def getHighestBid(self):
        return self.highestBid

    def bidding(self, user, cash=None):
        if cash is not None:
            if not self.active:
                print ("Auction is not open")
                return False
            elif user.getCredit() < cash:
                print ("User lacks funds to make this bid")
                return False
            elif user == self.host:
                print ("User can't because he's the owner of the auction")
                return False
            elif len(self.bids) < 1:
                self.bids.append(Bid(user, cash))
                print ("First bid has been sent")
                self.highestBid = self.bids[0]
                return True
            elif cash < Bid.getBidCash(self.bids.__getitem__(len(self.bids) - 1)) - 1:
                print ("The highest bid is higher than this one")
                return False
            else:
                self.bids.append(Bid(user, cash))
                return True
        else:
            if not self.active:
                print ("Auction is not open")
                return False
            elif user.getCredit() < self.highestBid:
                print ("User lacks funds to make this bid")
                return False
            elif user == self.host:
                print ("User can't because he's the owner of the auction")
                return False
            elif len(self.bids) < 1:
                self.bids.append(Bid(user, 1))
                print ("First bid has been sent")
                self.highestBid = self.bids[0]
                return True
            elif user.getCredit() < Bid.getBidCash(self.bids.__getitem__(len(self.bids) - 1)) + 1:
                print ("The highest bid is higher than this one")
                return False
            else:
                self.bids.append(Bid(user, self.highestBid+1))
                return True

    # def bidding(self, user):
    #     if not self.active:
    #         print ("Auction is not open")
    #         return False
    #     elif user.getCredit() < Bid.getBidCash(self.highestBid) + 1:
    #         print ("User lacks funds to make this bid")
    #         return False
    #     elif user == self.host:
    #         print ("User can't because he's the owner of the auction")
    #         return False
    #     elif Bid.getBidCash(self.highestBid) == 0:
    #         self.bids.append(Bid(user, 1))
    #         return True
    #     else:
    #         self.bids.append(Bid(user, Bid.getBidCash(self.highestBid) + 1))
    #         return True

    def execute(self):
        if self.active & len(self.bids) > 0:
            User.decreaseCredit(Bid.getBidder(self.highestBid), Bid.getBidCash(self.highestBid))
            User.incrementCredit(self.host, Bid.getBidCash(self.highestBid))
            return True
        else:
            return False
