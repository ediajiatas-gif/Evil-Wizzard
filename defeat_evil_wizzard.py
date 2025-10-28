# Base Character class
import random
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def special_ability(self, opponent):
        special_damage = int(self.attack_power*1.5)
        opponent.health -= special_damage
        print(f"{self.name} activates special ability and attacks {opponent.name} for {special_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def heal(self):
        heal_amount = random.randint(10,20)
        self.health += heal_amount
        if self.health > self.max_health:
            self.heal = self.max_health 
        print(f"{self.name} has used heal! Health is now: {self.health}")
    
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} slashes {opponent.name} with sword for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def special_ability(self, opponent):
        special_damage = int(self.attack_power*1.5)
        opponent.health -= special_damage
        print(f"SPECIAL ABILITY ACTIVATED! {self.name} calls upon the heavens to unleash a lightning-charged sword strike! {opponent.name} for {special_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def heal(self):
        heal_amount = random.randint(10,20)
        self.health += heal_amount
        if self.health > self.max_health:
            self.heal = self.max_health 
        print(f"{self.name} has used heal! Health is now: {self.health}")
    
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
            
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        
    def attack(self, opponent):
        elements = ["fire", "ice", "lighting", "shadow"]
        element = random.choice(elements)
        opponent.health -= self.attack_power
        print(f"{self.name} conjures a {element} blast, hitting {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def special_ability(self, opponent):
        special_damage = int(self.attack_power*1.2)
        opponent.health -= special_damage
        print(f"SPECIAL ABILITY ACTIVATED! {self.name} unleashes Inferno Blast, engulfing {opponent.name} in flames for {special_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def heal(self):
        heal_amount = random.randint(15,30)
        self.health += heal_amount
        print(f"{self.name} has used heal! Health is now: {self.health}")
    
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
    
    def attack(self, opponent):
        evil_elements = ["shadow bolt", "life drain", "poison"]
        evil_element = random.choice(evil_elements)
        opponent.health -= self.attack_power
        print(f"{self.name} conjures a {evil_element} blast, hitting {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def special_ability(self, opponent):
        special_damage = int(self.attack_power*2.8)
        opponent.health -= special_damage
        print(f"SPECIAL ABILITY ACTIVATED! {self.name} raises the UNDEAD, skeletons and spirts attack {opponent.name} with relentless attacks causing {special_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def heal(self):
        heal_amount = random.randint(15,30)
        self.health += heal_amount
        if self.health > self.max_health:
            self.heal = self.max_health 
        print(f"{self.name} has used heal! Health is now: {self.health}")
    
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def regenerate(self):
        self.health += 10
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
    
    def attack(self, opponent):
        print(f"{self.name} shoots arrow at enemy {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def special_ability(self, opponent):
        special_damage = int(self.attack_power*1.5)
        opponent.health -= special_damage
        print(f"SPECIAL ABILITY ACTIVATED! {self.name} uses ARROW STORM! Arrows fall from the sky piercing {opponent.name} for {special_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def heal(self):
        heal_amount = random.randint(10,20)
        self.health += heal_amount
        if self.health > self.max_health:
            self.heal = self.max_health 
        print(f"{self.name} has used heal! Health is now: {self.health}")
    
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=40)
        
    def attack(self, opponent):
        print(f"{self.name} uses Holy Strike against {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def special_ability(self, opponent):
        special_damage = int(self.attack_power*1.4)
        opponent.health -= special_damage
        print(f"SPECIAL ABILITY ACTIVATED! {self.name} calls upon the heavens to strike {opponent.name} with unstoppable divine wrath! {opponent.name} takes {special_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def heal(self):
        heal_amount = random.randint(10,20)
        self.health += heal_amount
        if self.health > self.max_health:
            self.heal = self.max_health 
        print(f"{self.name} has used heal! Health is now: {self.health}")
    
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") #Potential Class Add on
    print("4. Paladin")  #Potential Class Add on

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal (Randomized amount of heal points!)")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()