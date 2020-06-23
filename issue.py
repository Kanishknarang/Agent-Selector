#class for creating an issue
class Issue:

    #constructor
    #it initialises all issue attributes
    def __init__(self, discription = "", roles = []):

        self.discription = discription
        self.roles = roles

    #this function gets called when we print an issue object
    def __str__(self):
        return self.discription
