'''
Description:

There is an AuctionMediator that manages an auction for a particular item.

Multiple Bidders participate in the auction.

Instead of bidders directly communicating or competing, all interactions go through the mediator.

The mediator tracks:

Current highest bid

Notifies all bidders of new highest bid

Declares winner when auction ends
'''
from abc import ABC,abstractmethod

#collegue (Bidder)
class Colleague(ABC):
    def __init__(self,name,mediator):
        self.name=name
        self.amount=0
        self.mediator=mediator
    @abstractmethod
    def bid(self):
        pass 
    @abstractmethod
    def notify(self,bidder_name, amount):
        pass

class AuctionMediator(ABC):
    @abstractmethod
    def register_bidder(self,bidder):
        pass 
    @abstractmethod 
    def place_bid(self,bidder):
        pass
    @abstractmethod
    def announce_winner(self):
        pass

class Auctioneer(AuctionMediator):
    def __init__(self):
        self.bidders=[] 
        self.winner=None 
    def register_bidder(self,bidder:Bidder):
        self.bidders.append(bidder)
    def place_bid(self,bidder):
        if not self.winner or bidder.amount>self.winner.amount:
            self.winner=bidder
        for b in self.bidders:
            if b!=bidder:
                b.notify(bidder.name,bidder.amount)

    def announce_winner(self):
        if not self.winner:
            print("No one bid as of now...")
        else:
            print("Winner is ",self.winner.name,"with amount",self.winner.amount)

    
class Bidder(Colleague):
    def __init__(self,name,mediator):
        super().__init__(name,mediator)
        self.mediator.register_bidder(self)
    
    def bid(self,amount):
        self.amount=amount
        self.mediator.place_bid(self)
    
    def notify(self,bidder_name,amount):
        print(f"Notifying for {self.name}....")
        print(f"Bidder {bidder_name} has bid {amount}.....")



if __name__ == "__main__":
    auction = Auctioneer()

    # Register bidders
    anusha = Bidder("Anusha", auction)
    bhavani = Bidder("bhavani", auction)
    kalyani = Bidder("kalyani", auction)
    kavya = Bidder("kavya", auction)

    # Place bids (in any order)
    anusha.bid(100)
    bhavani.bid(120)
    kalyani.bid(110)
    kavya.bid(150)
    anusha.bid(180)
    bhavani.bid(200)
    kalyani.bid(170)
    kavya.bid(210)

    # Announce final winner
    auction.announce_winner()

