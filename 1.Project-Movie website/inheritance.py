class Parent():
    def __init__(self, last_name, eye_color):
        print "Parent Constructord Called"
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print "last_name " + self.last_name
        print "eye_color " + self.eye_color

        
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print "Child Constructor Called"
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self): # method override
        #print "last_name " + self.last_name
        #print "eye_color " + self.eye_color
        Parent.show_info(self)
        print "number_of_toys " + str(self.number_of_toys)

miley_cyrus = Child("Cyrus", "Blue", 5)
print miley_cyrus.last_name
print miley_cyrus.number_of_toys
miley_cyrus.show_info()


