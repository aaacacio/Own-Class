# Andre Acacio
# A system to collect bugs, fish, and fossils to keep or sell. Based on things you can do in real life, of course

# When you catch or collect something, it could be one of a select possibilities which is why I need to import random
import random

# I create the class which will hold and keep track of everything which changes from each method
class Inventory:
    def __init__(self):
        # Start with blank variables while setting their type
        self.inventory = []
        self.wallet = 0
        self.museum = []

    # For the fossils, I need them to be unspecified until they are assessed 
    def dig_fossil(self):
        self.inventory = self.inventory + ["Fossil"]
    def assess_fossil(self):
        num = 0
        # Here it replaces one of the unidentified fossils and replaces it with a random fossil out of four possibilities
        for item in self.inventory:
            # Only takes in a fossil from inventory
            if item == "Fossil":
                self.inventory[num] = [random.choice(["Amber", "Dino Head", "Diplo Chest", "Spino Tail"])]
                break
            else:
                num += 1

    def catch_bug(self):
        # Similar system but since there's no need for the bug to be assessed, they were combined into one method
        num = 0
        self.inventory = self.inventory + ["Bug"]
        for item in self.inventory:
            if item == "Bug":
                # Needed to switch some variables' names and batch of random choices
                self.inventory[num] = [random.choice(["Moth", "Grasshopper", "Ladybug", "Dragonfly"])]
                break
            else:
                num += 1

    def reel_fish(self):
        # Same as before just different variables
        num = 0
        self.inventory = self.inventory + ["Fish"]
        for item in self.inventory:
            if item == "Fish":
                self.inventory[num] = [random.choice(["Sea Bass", "Carp", "Squid", "Whale Shark"])]
                break
            else:
                num += 1

    # Sell module, must be inputted item as string
    def sell(self, item):
        # Checks if item is in inventory
        if [item] not in self.inventory:
                print(f"You cannot sell the {item}, there are none in your inventory")
        else:
            for i in self.inventory:
                if i == [item]:
                    # Searches for item, removes it, then adds a certain value into wallet
                    self.inventory.remove([item])
                    if [item] == ["Amber"]:
                        self.wallet += 150
                    elif [item] == ["Dino Head"]:
                        self.wallet += 200
                    elif [item] == ["Diplo Chest"]:
                        self.wallet += 300
                    elif [item] == ["Spino Tail"]:
                        self.wallet += 175
                    # You can still sell a fossil even if they aren't assessed
                    elif [item] == ["Fossil"]:
                        self.wallet += 50     
                    if [item] == ["Moth"]:
                        self.wallet += 130
                    elif [item] == ["Grasshopper"]:
                        self.wallet += 600
                    elif [item] == ["Ladybug"]:
                        self.wallet += 200
                    elif [item] == ["Dragonfly"]:
                        self.wallet += 180                
                    elif [item] == ["Sea Bass"]:
                        self.wallet += 400
                    elif [item] == ["Carp"]:
                        self.wallet += 300
                    elif [item] == ["Squid"]:
                        self.wallet += 500
                    elif [item] == ["Whale Shark"]:
                        self.wallet += 13000
                    else:
                        return None

    # Option to release the bug or fish but not fossils
    def release(self, an_item):
        # Checks if the item is in your inventory
        if [an_item] not in self.inventory:
            print(f"You cannot release the {an_item}, there are none in your inventory")
        # Premits fossil and the different kinds from being accepted
        else:
            if an_item == "Amber" or an_item == "Dino Skull" or an_item == "Diplo Chest" or an_item == "Spino Tail" or an_item == "Fossil":
                print(f"You can't release a fossil")
            else:
                self.inventory.remove([an_item])
                print(f"The {an_item} has been released!")

    # Able to donate what is found to the museum 
    def donate(self, item):
        if item not in self.inventory:
            print(f"You cannot donate the {item}, there are none in your inventory")
        elif item == "Fossil":
            print(f"The fossil must be assessed before it can be donated")
        else:
        # Items donated can only be given once
            if item not in self.museum:
                try:
                    self.inventory.remove([item])
                    self.museum += [item]
                except ValueError:
                    print(f"There is no {item} in your inventory")
            else:
                print(f"The {item} is already in the museum")                

    # Returns wallet and/or inventory
    def get_wallet(self):
        print(f"You have ${self.wallet}")
    def get_inv(self):
        # Need to return inventory as a string rather than a list
        Inv = ''
        for i in self.inventory:
            if i == str(i):
                Inv = Inv + str(i) + ", "
            elif i == list(i):
                Inv = Inv + str(i)[2:-2] + ", "
        Inv = Inv[:-2]
        if len(self.inventory) == 0:
            print(f"Your inventory is empty")
        else:
            print(f"Inventory: {Inv}")
    def get_museum(self):
        # Same as requesting museum only changed variable names
        Muse = ''
        for i in self.museum:
            if i == str(i):
                Muse = Muse + str(i) + ", "
            elif i == list(i):
                Muse = Muse + str(i)[2:-2] + ", "
        Muse = Muse[:-2]
        if len(self.museum) == 0:
            print(f"The museum is empty")
        else:
            print(f"Museum: {Muse}")   

        
    def __str__(self):
        return (f"You have {len(self.inventory)} items in your inventory")

# To test code
def main():
    # Calls class
    y = Inventory()
    # Digs two fossils
        # Adds items named "Fossils" to the inventory
    y.dig_fossil()
    y.dig_fossil()
    # But only assesses one to show there can be an unidentified and an identified fossil at once
        # Looks for "Fossil" in inventory and replaces it with a random fossil name  
    y.assess_fossil()

    # Catches multiple bugs
        # Adds a random bug to your inventory
    y.catch_bug()
    y.catch_bug()
    y.catch_bug()
    
    # Catched multiple fish
        # Adds a random fish to your inventory
    y.reel_fish()
    y.reel_fish()

    # Sells items, if there is one in inventory
        # Searches for item provided, removes from wallet, and will but an amount into the waller
    y.sell("Ladybug")
    y.sell("Sea Bass")
    y.sell("Spino Tail")

    # Donates amber, if the user has one and since it's the first use of the donate module, the museum won't have one already
        # Stores it into the self.museum
    y.donate("Amber")
    y.donate("Fossil")

    # If you caught something, you can release it
        # Removes the bug or fish from inventory, unable to do with fossils
    y.release("Squid")

    # Using the three get-methods to look at current statuses
    y.get_inv()
    y.get_wallet()
    y.get_museum()

# From all this, it will return a prompt for the sell, donate or release modules if the action couldn't be completed
# as well as the current inventory, wallet, and museum
    print(y)
        

if __name__ == "__main__":
    main()