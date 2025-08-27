class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def use_power(self):
        return f"{self.name} uses {self.power}!"


class TechHero(Superhero):
    def __init__(self, name, power, gadget):
        super().__init__(name, power)
        self.gadget = gadget
    
    def use_gadget(self):
        return f"{self.name} uses {self.gadget}!"


# Create superhero instances
hero1 = Superhero("Superman", "super strength")
hero2 = TechHero("Iron Man", "repulsor beams", "Jarvis AI")

print(hero1.use_power())
print(hero2.use_power())
print(hero2.use_gadget())