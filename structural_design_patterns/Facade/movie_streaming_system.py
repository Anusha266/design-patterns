"""
Problem Statement — Online Movie Streaming System

You are building a simplified Movie Streaming Facade system that hides the complexity of multiple subsystems.

When a user wants to watch a movie, several things happen internally:

AuthenticationSystem  verifies the user.

PaymentSystem  checks subscription or pay-per-view balance.

Instead of making the client call each of these systems individually,
you need to build a MovieStreamingFacade class that simplifies the process.
"""

#subsystem
class AuthenticationSystem:
    def authenticate(self,user):
        print("AUthenticating user :",user)
        return True 

class PaymentSystem:
    def verify_payment(self,user):
        print("verifying payment.. for user",user)
        return True 
    
class RecommendationSystem:
    def recommend(self, movie_name):
        print(f"Recommended movies similar to '{movie_name}': ['movie1', 'movie2', 'Movie3']")

class StreamingServer:
    def start_stream(self, movie_name):
        print(f"Streaming '{movie_name}'... Enjoy your movie!")



class MovieStreamingFacade:
    def __init__(self):
        self.auth_system=AuthenticationSystem()
        self.payment_system=PaymentSystem()
        self.recommend_system=RecommendationSystem()
        self.streaming_server = StreamingServer()

    def watch_movie(self,user,movie_name):
        print("Starting movie request process..")
        if not self.auth_system.authenticate(user):
            print("Authentication failed...")
            return
        if not self.payment_system.verify_payment(user):
            print("Payment verification failed..")
            return 
        
        self.streaming_server.start_stream(movie_name)
        self.recommend_system.recommend(movie_name)
        print("Movie started successfully!!")


#client code    
if __name__ == "__main__":
    movie_facade = MovieStreamingFacade()
    movie_facade.watch_movie("Anshu", "Little Hearts")


'''
Even movie streaming process changed, no need to change client code....Facade layer will take care of it...client will call facade layer only
'''