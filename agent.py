#a class for creating an Agent
class Agent:

    #constructor
    #it initializes all agent attributes
    def __init__(self, name, is_available, available_since, roles):
        
        self.name = name
        self.is_available = is_available
        self.available_since = available_since
        self.roles = roles

    #when we print the agent object this method gets called
    def __str__(self):
        
        return self.name

    