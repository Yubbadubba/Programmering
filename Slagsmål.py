import random

class Fighter:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
1
def attack(attacker, defender):
    damage = random.randint(5, 10)  # Slumpar skada mellan 5 och 10
    defender.hp -= damage
    print(f"{attacker.name} slår {defender.name} för {damage} skada!") #skriver ut hur mycket dmg figthers gör

def fight(fighter_a, fighter_b):
    turn = random.choice([fighter_a, fighter_b])  #det slumpar vem som attackerar så A inte alltid vinner
    while fighter_a.hp > 0 and fighter_b.hp > 0: # kontrollerar om fighter a fortfarande lever
        attack(fighter_a, fighter_b)
        if fighter_b.hp > 0:  # kontrollerar om fighter b fortfarande lever
            attack(fighter_b, fighter_a)
        print(f"{fighter_a.name} HP: {fighter_a.hp}, {fighter_b.name} HP: {fighter_b.hp}\n") #Skriver ut HP kvar på fighters

    # Bestäm vem som vinner
    if fighter_a.hp <= 0 and fighter_b.hp <= 0:
        print("Det blev oavgjort!")
    elif fighter_a.hp <= 0:
        print(f"{fighter_b.name} Fighter B vinner!")
    else:
        print(f"{fighter_a.name} Fighter A vinner!")

# Skapa fighters
fighter_a = Fighter("Kämpare A", 50)
fighter_b = Fighter("Kämpare B", 52)

# Starta slagsmålet
fight(fighter_a, fighter_b)
