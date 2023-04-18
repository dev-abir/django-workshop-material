# classes and inheritance
class Animal:
    num_eyes = 2

    def print_num_eyes(self):
        print("num eyes=", self.num_eyes)


ob = Animal()
ob.print_num_eyes()


class Cat(Animal):
    # print_num_eyes() inherited from Animal
    pass


oggy = Cat()
oggy.print_num_eyes()


# Cat is also an Animal
def double_eyes(animal: Animal):
    print(animal.num_eyes * 2)


double_eyes(Cat())
