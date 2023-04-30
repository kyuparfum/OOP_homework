# 동물
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def shout(self):
        print("동물의 울음소리")
        
class Dog(Animal):   
    def shout(self):
        print(f"안녕 나는 {self.name}고 {self.age}살. 울음소리는 와아아아아아아알")
        
class Cat(Animal):
    def shout(self):
        print(f"안녕 나는 {self.name}고 {self.age}살. 울음소리는 야아아아아아옹")

my_dog = Dog("단풍이", 3)
my_dog.shout()
my_cat = Cat("고양이 이름은 어렵다", 2)
my_cat.shout()

