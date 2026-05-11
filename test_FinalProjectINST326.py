# Group Members: Shiv Patel & Nuri Tadayon
# Test File for FinalProjectINST326.py

from FinalProjectINST326 import Vendor, FoodItem, FootballGame, Purchase, DataManager

def test_vendor_rating():
    # creates a vendor 
    vendor = Vendor("Test Vendor", "Section A")

    # adds vendor ratings
    vendor.add_rating(4)
    vendor.add_rating(6)

    # find the average vendor rating
    avg = vendor.average_rating()

    # check if the average vendor rating is correct
    assert avg == 5

def test_add_vendor():
    # creates manager
    manager = DataManager()

    # creates vendor
    vendor = Vendor("Pizza Stall", "Section 9")

    # add vendor
    manager.add_vendor(vendor)

    # checks if vendor was added
    assert len(manager.vendor_list) == 1

def test_add_food_item():
    # creates manager
    manager = DataManager()

    # creates food items
    food = FoodItem("Hot Dog", "Snack", 6.0, "HotDog Stall")

    # adds food items
    manager.add_food_item(food)

    # checks if it was added
    assert len(manager.food_items) == 1

def test_add_game():
    # creates manager
    manager = DataManager()

    # creates game
    game = FootballGame("Rutgers", "09/15/2025")

    # adds game
    manager.add_game(game)

    # checks if game was added
    assert len(manager.game_list) == 1

def test_record_purchase():
    # creates manager
    manager = DataManager()

    # creates purchase
    purchase = Purchase("Burger", "Burger Stand", "Ohio State", 10)

    # records purchase
    manager.record_purchase(purchase)

    # checks if purchase was recorded
    assert len(manager.purchase_list) == 1

def test_sales_by_game_total_Score():
    # creates manager
    manager = DataManager()

    # creates purchases 
    p1 = Purchase("Burger", "Vendor1", "Ohio State", 5)
    p2 = Purchase("Hot Dog", "Vendor2", "Ohio State", 4)

    # records purchases 
    manager.record_purchase(p1)
    manager.record_purchase(p2)

    # manually calculates total
    total = 0
    for purchase in manager.purchase_list:
        if purchase.game_opponent == "Ohio State":
            total = total + purchase.amount_sold

    # check if total is correct 
    assert total == 9

def test_top_selling_item_logic():
    # creates manager
    manager = DataManager()

    # adds purchases
    p1 = Purchase("Hot Dog", "Vendor 1", "Rutgers", 4)
    p2 = Purchase("Hot Dog", "Vendor1", "Rutgers", 3)
    p3 = Purchase("Burger", "Vendor2", "Michigan", 2)

    manager.record_purchase(p1)
    manager.record_purchase(p2)
    manager.record_purchase(p3)

    # counts the sales manually
    sales = {}
    for purchase in manager.purchase_list:
        if purchase.item_sold in sales:
            sales[purchase.item_sold] = sales[purchase.item_sold] + purchase.amount_sold
        else:
            sales[purchase.item_sold] = purchase.amount_sold

    # finds the top item
    best_item = ""
    best_amount = 0

    for item in sales:
        if sales[item] > best_amount:
            best_amount = sales[item]
            best_item = item

    # checks the result
    assert best_item == "Hot Dog"