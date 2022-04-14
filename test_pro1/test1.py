from asyncio.windows_events import NULL
from re import A
from unicodedata import name


a = 123
b = "hello"
c = " world"

# print(b[-4:-1])

def get_sum(p1, p2):
    return p1 + p2


# print(get_sum(b, c))

class person:
    def __init__(self, name, son_class):
        self.name = name
        self.son_class = son_class
    
    def get_self(self):
        return self.name
    
    def get_son(self):
        return self.son_class.name

son = person("王小明", NULL)
father = person("王明", son)


print(father.get_self())
# print(father.get_son())

print("------------------")

print(son.get_self())
print(son.get_son())

