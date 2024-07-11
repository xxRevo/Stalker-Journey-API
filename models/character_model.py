"""
class Trait:
    def __init__(self,applied_effects=None,injuries=None,traits=None):
        self.applied_effects
"""
class Character:
    def __init__(self,name,hp,radiation,inventory=None,trait=None):
        self.name = name
        self.hp = hp
        self.radiation = radiation
        self.inventory = Inventory()
        self.trait = Trait()
    
    def get(self):
        return self.name, self.hp, self.radiation, self.inventory