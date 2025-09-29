class Character:
    def __init__(self,health,damage,speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def double_speed(self):
        self.speed *= 2
        
warrior = Character(100,50,10)
ninja = Character(80,40,40)

print(f"Warrior speed: {warrior.speed}")
print(f"Ninja speed: {ninja.speed}")
warrior.double_speed()
print(f"Warrior speed: {warrior.speed}")
print(f"Ninja speed: {ninja.speed}")     

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print("Woof!")

my_dog = Dog("Rex")

print(my_dog.name)   # Rex
my_dog.bark()        # Woof!

class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
        
    def drive(self):
        print("Vroom!")
        
    def info(self):
        print(f"This car is a {self.brand} from {self.year}")

my_car = Car("Toyota",2015)
my_car.drive()
my_car.info()

    