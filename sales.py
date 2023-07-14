class Sales:
    def __init__(self, name, location, company, script):
        self.name = name
        self.location = location
        self.company = company
        self.script = script
    def hook(self, name, company):
        print("Hey", self.name, "this is Dhruv Patel from,", self.company,"Its a pleasure to meet you.")
    def hook2 (self, name, location):
        print("Oh my gosh! I love", self.location, "That's great", self.name)
    def intro(self, name, location, company, script):
        print(self.name, "Can I just borrow 2 minutes of your time. Would that be fair? Just two minutes?")
        print("Thanks", self.name, "Here at", self.company, "we specialize in", self.script, "Now would you be opposed to getting more sales or clients?")
        print("Of course not. It must be your birthday", self.name, "because I got the perfect gift for you today!", "There is about to be a party in", self.location)
    def appointment(self, name):
        print("Now, you would agree that it is important to save time and money for your company, right? And what if you could achieve those goals in a five minute meeting. That would be an extremely important and beneficial meeting, right?")
    def close(self, name, company):
        print(self.name, "You must have won the lottery. Because I can set that quick meeting up for you right now. What do you say", self.name)

company = input("Enter company name: ")
script = input("Enter script: ")
name = input("Hey buddy, Who do I have the pleasure of speaking with today? ")
location = input("Where are you speaking from today, " + name + "? ")

sales = Sales(name, location, company, script)
# Create an instance of the Sales class

# Call the class methods to print the statements
sales.hook(name, company)
sales.hook2(name, location)
sales.intro(name, location, company, script)
sales.appointment(name)
sales.close(name, company)
