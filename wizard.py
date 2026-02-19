import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = random.randint(10, 20)
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.boost_turns = 0

    def kamikaze(self, opponent):
        damage = self.health
        opponent.health = int(opponent.health * 0.25)
        self.health = 0
        print(f"{self.name} performs a kamikaze attack on {opponent.name}! The warrior has been eliminated in the process. {opponent.name} has lost 75% of their current health!")

    def battle_boost(self):
        self.attack_power = int(self.attack_power * 1.5)
        self.boost_turns = 2
        print(f"{self.name} uses Battle Boost! Attack power increased by 50% for the next 2 attacks!")


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.decoy = False


    def curse(self, opponent):
        opponent.attack_power = int(opponent.attack_power * 0.9)
        print(f"{self.name} casts a curse on {opponent.name}! All future attacks from {opponent.name} will be reduced by 10%! ")

    def decoy_produced(self):
        self.decoy = True
        print(f"{self.name} has created a magical decoy! The next attack will be redirected to the decoy, which will take the damage instead!")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=10)
        self.evading = False

    def quick_shot(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        total_damage = int(damage * 1.75)
        opponent.health -= total_damage        
        print(f"{self.name} attacks {opponent.name} for {total_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def evade(self):
        self.evading = True
        print(f"{self.name} has evaded the next attack!")


# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=30)
        self.shielding = False

    def holy_strike(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        total_damage = int(damage * 1.5)
        opponent.health -= total_damage        
        print(f"{self.name} attacks {opponent.name} for {total_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def divine_shield(self):
        self.shielding = True
        print(f"{self.name} has activated Divine Shield! Incoming damage will be deflected back 15% to the attacker.")


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

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
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Archer):
              print("1. Quick Shot")
              print("2. Evade")
              attack_choice = input("Choose attack method: ")
              if attack_choice == '1':
                  player.quick_shot(wizard)
              elif attack_choice == '2':
                  player.evade()
            elif isinstance(player, Paladin):
              print("1. Holy Strike")
              print("2. Divine Shield")
              attack_choice = input("Choose attack method: ")
              if attack_choice == '1':
                  player.holy_strike(wizard)
              elif attack_choice == '2':
                  player.divine_shield()
            elif isinstance(player, Mage):
              print("1. Curse")
              print("2. Decoy")
              attack_choice = input("Choose attack method: ")
              if attack_choice == '1':
                  player.curse(wizard)
              elif attack_choice == '2':
                  player.decoy_produced()
            elif isinstance(player, Warrior):
              print("1. Battle Boost")
              print("2. Kamikaze")
              attack_choice = input("Choose attack method: ")
              if attack_choice == '1':
                  player.battle_boost()
              elif attack_choice == '2':
                  player.kamikaze(wizard)
            else:
                  print("Invalid option")
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")
        if wizard.health > 0:
            if isinstance(player, Warrior) and player.boost_turns > 0:
                player.boost_turns -= 1
                if player.boost_turns == 0:
                    print(f"{player.name}'s Battle Boost has been depleted.")
                    player.attack_power = 25
            wizard.regenerate()
            if hasattr(player, 'evading') and player.evading:
                print(f"{player.name} evaded the attack!")
                player.evading = False
            elif hasattr(player, 'decoy') and player.decoy:
                print(f"{player.name}'s decoy takes the hit instead!")
                player.decoy = False
            elif hasattr(player, 'shielding') and player.shielding:
                damage = int(wizard.attack_power * 0.15)
                wizard.health -= damage
                print(f"{player.name} deflected {damage} damage back to {wizard.name}!")
                player.shielding = False
            else:
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