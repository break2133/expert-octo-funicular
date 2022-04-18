from turtle import Turtle


str = "012345678"

str1 = "abc"
str2 = "ABC"

# print(len(str))
# print(str1.capitalize())
# print(str1.upper())
# print(str2.lower())
# print(str.find("1"))

a = True
b = False

class animal:
    def __init__(self, name, eyes=2, leg=4):
        self.name = name
        self.eyes = eyes
        self.leg = leg
    
    def get_animal_inf(self):
        print("%s has %d eyes and %d legs."%(self.name, self.eyes, self.leg))

class dog(animal):
    def __init__(self, name):
        animal.__init__(self, name)

    def get_animal_inf(self):
        print("%s is cute , it has %d eyes and %d legs."%(self.name, self.eyes, self.leg))


class spider(animal):
    def __init__(self, name):
        animal.__init__(self, name, 8, 8)

    def get_animal_inf(self):
        print("%s is terrible , it has %d eyes and %d legs."%(self.name, self.eyes, self.leg))

animal_people = animal("People", 2, 2)
animal_dog_xiaohua = dog("Xiaohua")
animal_spider_parker = spider("Parker")

animal_people.get_animal_inf()
animal_dog_xiaohua.get_animal_inf()
animal_spider_parker.get_animal_inf()

