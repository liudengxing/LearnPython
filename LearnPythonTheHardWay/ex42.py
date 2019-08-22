class Animals(object):
    pass

class Dog(Animals):

    def __init__(self, name):
        self.name = name


class Cat(Animals):

    def __init__(self, name):
        self.name = name


class Person(object):

    def __init__(self,name):
        self.name = name
        self.pet = None


class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


# There is a dog named Rover
rover = Dog("Rover")

# There is a cat named Satan
satan = Cat("Satan")

# There is a Person named Mary
mary = Person("Mary")

# Satan is Mary's pet
mary.pet = satan

# A Employee named Frank whose salary is 120000
frank = Employee("Frank", 120000)

# frank has a dog , Rever
frank.pet = rover

# flipper is fish
flipper = Fish()

# crouse is salmon
crouse = Salmon()

# harry is halibut
harry = halibut()
