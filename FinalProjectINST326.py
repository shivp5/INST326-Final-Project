# Group Members: Shiv Patel & Nuri Tadayon
# Project Topic: UMD Football Food Vendor Database
#Assignment: INST 326 Final Project 

"""UMD Football Food Vendor Database Final Project.

This program stores simple information about food items, vendors, games,
and sales for UMD football games.
"""

# Class for Food items
class FoodItem: 
    """ Menu items that are sold at a UMD football game."""

    def __init__(self, item_name, item_category, item_price, vendor_name):
        """ Logs a food item."""
        self.item_name = item_name
        self.item_category = item_category
        self.item_price = item_price
        self.vendor_name = vendor_name

# Class for food vendors
class Vendor:
    """ Shows a vendor at a UMD football game."""

    def __init__(self, vendor_name, vendor_location):
        self.vendor_name = vendor_name
        self.vendor_location = vendor_location
        self.vendor_ratings = []

    def add_rating(self, rating):
        """Adds a rating for each of the vendors."""
        self.vendor_ratings.append(rating)

    def average_rating(self):
        """Returns the average vendor rating."""
        if len (self.vendor_ratings) == 0:
            return 0 
        total = 0
        for r in self.vendor_ratings:
            total = total + r
        avg = total / len (self.vendor_ratings)
        return avg 
    
# Class for the game
class FootballGame:
    """ Represents a UMD football game."""

    def __init__(self, opposite_team, game_date):
        self.opposite_team = opposite_team
        self.game_date = game_date

# Class for the purchases
class Purchase:
    """ Shows a purchase made during a UMD football game."""

    def __init__(self, item_sold, vendor_name, game_opponent, amount_sold):
        """ Logs a purchase."""
        self.item_sold = item_sold
        self.vendor_name = vendor_name
        self.game_opponent = game_opponent
        self.amount_sold = amount_sold

class DataManager:
    """ Stores and manages all the data used for the project."""

    def __init__(self):
        """Logs the storage list."""

        self.food_items = []
        self.vendor_list = []
        self.game_list = []
        self.purchase_list = []

    def add_food_item(self, food_item):
        """Adds a food item to the system."""
        self.food_items.append(food_item)

    def add_vendor(self, vendor):
        """ Adds a vendor to the system."""
        self.vendor_list.append(vendor)

    def add_game(self, game):
        """Adds a game to the system."""
        self.game_list.append(game)

    def record_purchase(self, purchase):
        """Records a purchase in the system"""
        self.purchase_list.append(purchase)

    def show_purchases(self): 
        """Prints all the recorded purchases."""
        if len(self.purchase_list) == 0:
            print("No purchases recorded.")
        else:
            for purchase in self.purchase_list:
                print(purchase.item_sold + " - " + purchase.vendor_name + " - " + purchase.game_opponent + " - Quantity: " + str(purchase.amount_sold))

def main():
    """Runs the command-line menu."""

    manager = DataManager()
    checker = True
    while checker:
        print("")
        print("UMD Football Food Vendor Database")
        print("1. Add vendor")
        print("2. Add food item")
        print("3. Add game")
        print("4. Record purchase")
        print("5. Show purchases")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vendor_name = input("Vendor name: ")
            vendor_location = input("Vendor location: ")
            vendor = Vendor(vendor_name, vendor_location)
            manager.add_vendor(vendor)
            print("Vendor added.")

        elif choice == "2":
            item_name = input("Food item name: ")
            item_category = input("Category: ")
            item_price = input("Price: ")
            item_price = float(item_price)
            vendor_name = input("Vendor name: ")
            food = FoodItem(item_name, item_category, item_price, vendor_name)
            manager.add_food_item(food)
            print("Food item added.")

        elif choice == "3":
            opposite_team = input("Opposing team: ")
            game_date = input("Game date: ")
            game = FootballGame(opposite_team, game_date)
            manager.add_game(game)
            print("Game added.")

        elif choice == "4":
            item_sold = input("Item sold: ")
            vendor_name = input("Vendor name: ")
            game_opponent = input("Opponent: ")
            amount_sold = input("Amount sold: ")
            amount_sold = int(amount_sold)
            purchase = Purchase(item_sold, vendor_name, game_opponent, amount_sold)
            manager.record_purchase(purchase)
            print("Purchase recorded.")

        elif choice == "5":
            manager.show_purchases()

        elif choice == "6":
            print("Bye.")
            checker = False 
        else: 
            print("Invalid choice.")

if __name__ == "__main__":
    main()