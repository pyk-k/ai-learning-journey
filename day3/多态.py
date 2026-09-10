class animal:
    def speak(self):
        print("不会叫")

class dog(animal):
    def speak(self):
        print("wowowo")

class cat(animal):
    def speak(self):
        print("miaomiao")

class danesour(animal):
    def speak(self):
        print("wooooo")

def gain(animals):
    animals.speak()

Dog = dog()
Cat = cat()
Danesour = danesour()

gain(Danesour)
gain(Dog)
gain(Cat)