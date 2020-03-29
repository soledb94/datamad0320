
# Soldier
import random

class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength 

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health-=damage


#class Viking: 


class Viking(Soldier):
    def __init__(self, name,health, strength):
        self.name=name
        self.health=health
        self.strength=strength 
        
    def attack(self):
        return super().attack()
        
    def receiveDamage(self,damage):
        self.health-=damage
        
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength 

    def attack(self):
        return super().attack()

    def receiveDamage(self,damage):
        self.health-=damage
        
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
            

# War


class War:
    
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
        
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
        

    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
   

    def vikingAttack(self):
        v1=random.choice(self.vikingArmy)
        s1=random.choice(self.saxonArmy)

        v_attack=s1.receiveDamage(v1.attack())
        self.saxomArmy=[s for s in self.saxonArmy if s1.health>0] 
        return v_attack


    def saxonAttack(self):
        s2=random.choice(self.saxonArmy)
        v2=random.choice(self.vikingArmy)

        s_attack=v2.receiveDamage(s2.attack())
        self.vikingArmy=[v for v in self.vikingArmy if v2.health>0] 
        return s_attack

    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        


