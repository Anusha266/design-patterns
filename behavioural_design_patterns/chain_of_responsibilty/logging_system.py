''' 
Description:

You are building a logging system with multiple levels:

INFO – logs informational messages.

DEBUG – logs debug messages.

ERROR – logs errors.

Each logger decides whether to handle the message.

If a logger cannot handle, it passes it to the next logger in the chain.

The client sends a message, and it traverses the chain automatically.
'''
from abc import ABC,abstractmethod 
INFO =1
DEBUG =2
ERROR=3
class Logger(ABC):
    def __init__(self,level):
        self.level=level
        self.next_logger=None 
    
    def set_next(self,logger:Logger):
        self.next_logger=logger 
        return logger
    
    def log_message(self,level,message):
        if self.level<=level:
            self.write(message)

        if self.next_logger:
            self.next_logger.log_message(level,message) 
    
    @abstractmethod
    def write(self):
        pass 

class ConsoleLogger(Logger):
    def write(self,msg):
        print(f"console logging:{msg}")
class FileLogger(Logger):
    def write(self,msg):
        print(f"File logging:{msg}")
class EmailLogger(Logger):
    def write(self,msg):
        print(f"Email logging:{msg}")



if __name__ == "__main__":
    # Create loggers
    console_logger = ConsoleLogger(INFO)
    file_logger = FileLogger(DEBUG)
    email_logger = EmailLogger(ERROR)

    # Setup the chain: Console -> File -> Email
    console_logger.set_next(file_logger).set_next(email_logger)

    # Send messages of different levels
    print("Sending INFO message:")
    console_logger.log_message(INFO, "User logged in successfully.")

    print("\nSending DEBUG message:")
    console_logger.log_message(DEBUG, "User object created with ID=123.")

    print("\nSending ERROR message:")
    console_logger.log_message(ERROR, "Failed to save user data to database.")
