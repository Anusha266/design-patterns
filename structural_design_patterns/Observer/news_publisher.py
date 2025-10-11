'''
A NewsPublisher (subject) sends news updates.

Multiple Subscribers (observers) receive notifications.

Subscribers can subscribe/unsubscribe at runtime.
'''

#interface - observable
from abc import ABC,abstractmethod
class NewsObservableInterface(ABC):
    @abstractmethod
    def subscribe():
        pass
    @abstractmethod
    def unsubscribe():
        pass
    @abstractmethod
    def notify():
        pass 

#observer interface
class ObserverInterface(ABC):
    @abstractmethod
    def update(self):
        pass

#concreate observable
class NewsObservable(NewsObservableInterface):
    def __init__(self):
        self.observers=[]
    
    def subscribe(self,observer:ObserverInterface):
        self.observers.append(observer)
        print(observer.name," user subscribed")
    
    def unsubscribe(self,observer:ObserverInterface):
        self.observers.remove(observer)
        print(observer.name," user unsubscribed")

    def notify(self):
        for observer in self.observers:
            observer.update()
        
#concrete observers
class EmailSubscriber(ObserverInterface):
    def __init__(self):
        self.name="email"
    def update(self):
        print("Received notification through email")

class SMSSubscriber(ObserverInterface):
    def __init__(self):
        self.name="SMS"
    def update(self):
        print("Received notification through SMS")

#client code 

if __name__=='__main__':
    news_observable= NewsObservable()
    email_subscriber = EmailSubscriber()
    news_observable.subscribe(email_subscriber)
    news_observable.notify()
    sms_subscriber= SMSSubscriber()
    news_observable.subscribe(sms_subscriber)
    news_observable.notify()
    news_observable.unsubscribe(email_subscriber)
    news_observable.notify()


