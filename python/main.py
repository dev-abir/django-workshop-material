# python = dynamic (runtime type check)
roll = 56
ACCL_G = 9.8  # m/s^2
print(roll + ACCL_G)
print()

# conditional branching
age = 56

if age >= 18:
    print("adult")
elif age >= 60:
    print("senior citizen")
else:
    print("tu POGO dekh!")

# loops
# for (int i = 0; i< 5; i++)
for i in range(5):
    print("for loop", i)
print()


i = 0
while i < 5:
    print("while loop", i, end=", ")
    # i++ won't work
    i += 1
print()
print()


# strings
name = "Steve"
print(name, len(name), name.replace("e", "u"))
print("1" + "1")
# [start_idx:end_idx:step]
print("name[1]", name[1])
print("name[2:]", name[2:])  # name[2:len(name)]
print("name[:2]", name[:2])  # name[0:2]
print("name[:]", name[:])  # name[0:len(name)]
print()


# Robert Frost
stanza = "The woods are lovely, dark and deep,\nBut I have promises to keep..."

stanza = """
The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep."""

print(stanza)
print()


for c in name:
    print(c, end=", ")
print()
print()

# lists (arrays)
a = ["a", "boy"]
b = [89, "hello from Mars!", "D"]

c = a + b

print(a[1])
print(b)
print(c)
print(b[1:])  # similar to strings
print()


# functions
def increment(number):
    print(number + 1)


increment(56)
print()

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


# dictionaries
video = {
    "title": "kuch bhi daal do yaha",
    "length": 2.45,
    4: 90,
    (56, 89): "g",
    # [7, 6]: 45, (list is not hashable)
}

print(video[4])


# using import and dynamic HTML
# pip install Jinja2
from jinja2 import Template

name = "Abir"
skeleton_html = "<h1>Hello {{ name }}!</h1>"
t = Template(skeleton_html)
with open("a.html", "w") as f:
    f.write(t.render(name=name))


# assignment: input a number n and print pattern...
