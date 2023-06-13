class Plane:

    def __init__(self, wings, should_fly):
        self.wings = wings
        self.should_fly = should_fly

    def show(self):
        print(self.wings, self.should_fly)


class Jet(Plane):

    def __init__(self, wings, should_fly, color):
        Plane.__init__(self, wings, should_fly)
        self.color = color

    def show(self):
        print("The number of wings: ", self.wings)
        print("Should fly: ", self.should_fly)
        print("the color:", self.color)


class Passenger(Plane):

    def __init__(self, wings, should_fly, color):
        Plane.__init__(self, wings, should_fly)
        self.color = color

    def show(self):
        print("The number of wings: ", self.wings)
        print("Should fly: ", self.should_fly)
        print("the color:", self.color)


obj1 = Jet(2, "yes", "white")
obj2 = Jet(2, "yes", "black")
obj1.show()
obj2.show()
obj1 = Passenger(2, "yes", "red")
obj2 = Passenger(2, "yes", "black")
obj1.show()
obj2.show()






