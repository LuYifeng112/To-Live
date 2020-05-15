#### ##    ## ##     ## ######## ##    ## ########  #######  ########  ##    ## 
 ##  ###   ## ##     ## ##       ###   ##    ##    ##     ## ##     ##  ##  ##  
 ##  ####  ## ##     ## ##       ####  ##    ##    ##     ## ##     ##   ####   
 ##  ## ## ## ##     ## ######   ## ## ##    ##    ##     ## ########     ##    
 ##  ##  ####  ##   ##  ##       ##  ####    ##    ##     ## ##   ##      ##    
 ##  ##   ###   ## ##   ##       ##   ###    ##    ##     ## ##    ##     ##    
#### ##    ##    ###    ######## ##    ##    ##     #######  ##     ##    ##    

#inventory system
init python:
    class Item:
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost

    class Inventory:
        def __init__(self, money=100):
            self.money = money
            self.items = []

        def buy(self, item):
            if self.money >= item.cost:
                self.money -= item.cost
                self.items.append(item)
                return True
            else:
                return False

        def earn(self, amount):
            self.money += amount

        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False

python:
        spaghetti = Item("Spaghetti", 3)
        olives = Item("Olives", 4)
        chocolate = Item("Chocolate", 11)