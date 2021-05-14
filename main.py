from Auction import Auction
from User import User
from Bid import Bid
u1 = User("Toni", 100)
u2 = User("Pep", 150)
u3 = User("Enric", 300)
users = [u1, u2, u3]
a1 = Auction("Cellphone", u1)
print(a1.bidding(u2, 100))
print(a1.bidding(u3, 50))
print(Bid.getBidCash(a1.getHighestBid()))
print("")
print (len(a1.getBids()))
print a1.getStatus()
print(a1.execute())
print(a1.bidding(u3, 200))
print("\n\n")
a2 = Auction("3D Printer", u2)
print (a2.bidding(u3))
print (a2.bidding(u1))
print ("")
print (len(a2.getBids()))
print a2.getStatus()
a2.setStatus(False)
print (a2.execute())
print ("")
for x in users:
    print (x.getName())
    print(x.getCredit())
    print ("")
for x in users:
    print(x.getName())
    print(x.getAuctions())

    print ("")
