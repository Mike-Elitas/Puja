from Auction import Auction
from User import User
from Bid import Bid
u1 = User("Toni", 100)
u2 = User("Pep", 150)
u3 = User("Enric", 300)
users = [u1, u2, u3]
# a1 = Auction("Cellphone", u1)
# print(a1.bidding(u2, 100))
# print(a1.bidding(u3, 50))
# print(Bid.getBidCash(a1.getHighestBid()))
# a1.execute()
# a1.bidding(u3, 200)
a2 = Auction("3D Printer", u2)
a2.bidding(u3)
a2.execute()
print ("")
for x in users:
    print (x.getName())
    print(x.getCredit())
    print ("")
for x in users:
    print(x.getName())
    print(x.getAuctions())

    print ("")
