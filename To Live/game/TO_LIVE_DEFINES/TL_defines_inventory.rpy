#### ##    ## ##     ## ######## ##    ## ########  #######  ########  ##    ## 
 ##  ###   ## ##     ## ##       ###   ##    ##    ##     ## ##     ##  ##  ##  
 ##  ####  ## ##     ## ##       ####  ##    ##    ##     ## ##     ##   ####   
 ##  ## ## ## ##     ## ######   ## ## ##    ##    ##     ## ########     ##    
 ##  ##  ####  ##   ##  ##       ##  ####    ##    ##     ## ##   ##      ##    
 ##  ##   ###   ## ##   ##       ##   ###    ##    ##     ## ##    ##     ##    
#### ##    ##    ###    ######## ##    ##    ##     #######  ##     ##    ##    


init python:
    class Item(object):
        def __init__(self, name, weight, value):
            self.name = name
            self.weight = weight
            self.value = value

    class InvItem(object):
        def __init__(self, item, amount):
            self.item = item
            self.amount = amount

    class Container(object):
        def __init__(self, weight_max, money=100):
            self.inventory = []
            self.weight_max = weight_max
            self.money = money

        def add_item(self, item, amount=1):
            if item.weight * amount > self.weight_max - sum(i.item.weight * i.amount for i in self.inventory):
                return('too heavy')
            else:
                if item in [i.item for i in self.inventory]:  # I can't believe I got this line to work with my first try
                    self.inventory[[i.item for i in self.inventory].index(item)].amount += amount   # oh god why
                else:
                    self.inventory.append(InvItem(item, amount))
                return('success')

        def has_item(self, item, amount=1):
            if item in [i.item for i in self.inventory]:
                if self.inventory[[i.item for i in self.inventory].index(item)].amount >= amount:
                    return(self.inventory[[i.item for i in self.inventory].index(item)].amount)
                else:
                    return(False)
            else:
                return(False)

        def finditem(self, item):
                return(self.inventory[[i.item for i in self.inventory].index(item)])

        def remove_item(self, item, amount=1):
            if self.has_item(item):
                self.finditem(item).amount -= amount
                if self.finditem(item).amount <= 0:
                    self.inventory.pop(self.inventory.index(self.finditem(item)))
                    return('gone')
                else:
                    return('more left')
            else:
                return('not found')

        def inv(self):

            for i in backpack.inventory:
                print(i.item.name)
                print("Weight: "+str(i.item.weight))   ## needs str() because i.item.weight is a number
                print("Number: "+str(i.amount))   ## same here - note that it's i.amount, not i.item.amount!

        def earn(self, amount):
            global current_money
            self.money += amount
            current_money = self.money


python:
    Jade = Item("Jade", 0.5, 250)
    Peking_admission = Item("Peking University Admission paper", 0, 80)
    Work_Recommendation = Item("Cheung's Work Recommendation Document", 0, 10)