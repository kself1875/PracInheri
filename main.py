#  a little multi-level inheritance practice

class Animal():  # this is the base class
    def four_legs(self):  # user-definded function
        print("This animal uses four legs!")
    def has_tail(self):
        print("This animal has a tail!")


class Lion(Animal):  # child class lion inherits from parent class animal
    def food_choice(self):  # user-defined function
        print("The Lion is a carnivore and eats meat!")


class Zebra(Animal):  # child class zebra inherits from parent class animal
    def food_choice(self):  # user-defined function
        print("The zebra is a herbivore!")


lion_1 = Lion()  # object for lion class/object is an instance(real world realization) of a class
lion_1.four_legs()  # .dot notation allows access to the class functions/methods and calls functions/methods
lion_1.has_tail()
lion_1.food_choice()


print("------------------------------------------")


zebra_1 = Zebra()  # object for zebra class/object is an instance(real world realization) of a class
zebra_1.four_legs()  # .dot notation allows access to the class function/methods and calls functions/methods
zebra_1.has_tail()
zebra_1.food_choice()








