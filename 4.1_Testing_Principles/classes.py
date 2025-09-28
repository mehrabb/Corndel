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
