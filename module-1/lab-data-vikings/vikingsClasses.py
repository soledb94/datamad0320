
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength 

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health-=damage


class Viking(Soldier):
    def __init__(self, name,health, strength):
        self.name=name
        self.health=health
        self.strength=strength 
        
    def attack(self):
        super().attack()
        
    def receiveDamage(self,damage):
        self.health-=damage
        
        if self.health>1:
            return f"{self.name} has received {damage} points of damage"
        if self.health<=0:
            return f"{self.name} has died in act of combat"
        
    def battle_cry(self):
        return "Odin Owns You All!"



#class Viking:

    #pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass


