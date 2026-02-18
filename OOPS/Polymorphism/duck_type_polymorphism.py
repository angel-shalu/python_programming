class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

class Human:
    def speak(self):
        print("Hello")

def make_sound(obj):
    obj.speak()   # koi type check nahi

make_sound(Dog())
make_sound(Cat())
make_sound(Human())


# ====================================================================================
class my_cls1:
    def my_func(self):
        print("1. Sing a song")

class my_cls2:
    def my_func(self):
        print("2. Play the game")
        
class my_cls3:
    def my_func(self):
        print("3. Eat the food")

def func(obj):
    obj.my_func()   # koi type check nahi


l = [my_cls1(), my_cls2(), my_cls3()]
for i in l:
    # print(i)
    func(i)
    
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

class Human:
    def speak(self):
        print("Hello")

def make_sound(obj):
    obj.speak()   # koi type check nahi

make_sound(Dog())
make_sound(Cat())
make_sound(Human())


# ====================================================================================
class my_cls1:
    def my_func(self):
        print("1. Sing a song")

class my_cls2:
    def my_func(self):
        print("2. Play the game")
        
class my_cls3:
    def my_func(self):
        print("3. Eat the food")

def func(obj):
    obj.my_func()   # koi type check nahi


l = [my_cls1(), my_cls2(), my_cls3()]
for i in l:
    # print(i)
    func(i)
    
