from Auction import Auction
from User import User

u1 = User("Toni", 100)
u2 = User("Pep", 150)
u3 = User("Enric", 300)
users = [u1, u2, u3]
a1 = Auction("Cellphone", u1)
a1.bidding(u2, 100)
print ("")
a1.viewHighestBid()
print ("")
a1.bidding(u3, 50)
print("")
a1.viewHighestBid()
print("")
a1.execute()
a1.bidding(u3, 200)
print("")
a2 = Auction("3D Printer", u2)
a2.bidding(u3)
print("")
a2.bidding(u1)
print("")
a2.execute()
for x in users:
    print(x.getName())
    print(str(x.getCredit()) + "$")
    print("")
for x in users:
    print(x.getName())
    if len(x.auctions) == 0:
        print("No auctioned items.")
    else:
        for y in x.auctions:
            print("Auctioned item: " + str(y.getAuctionedItem()))
    print("")
