#### ##    ## ##     ## ######## ##    ## ########  #######  ########  ##    ## 
 ##  ###   ## ##     ## ##       ###   ##    ##    ##     ## ##     ##  ##  ##  
 ##  ####  ## ##     ## ##       ####  ##    ##    ##     ## ##     ##   ####   
 ##  ## ## ## ##     ## ######   ## ## ##    ##    ##     ## ########     ##    
 ##  ##  ####  ##   ##  ##       ##  ####    ##    ##     ## ##   ##      ##    
 ##  ##   ###   ## ##   ##       ##   ###    ##    ##     ## ##    ##     ##    
#### ##    ##    ###    ######## ##    ##    ##     #######  ##     ##    ##    


init python:
    class Item(object):
        def __init__(self, name, weight, value, icon=None, desc=None):
            self.name = name
            self.weight = weight
            self.value = value
            self.icon = icon
            self.desc = desc

    class InvItem(object):
        def __init__(self, item, amount):
            self.item = item
            self.amount = amount

    class Container(object):
        def __init__(self, weight_max, money=100):
            self.inventory = []
            self.weight_max = weight_max
            self.money = money

        def add_item(self, item, amount=1, msge=True):
            if item.weight * amount > self.weight_max - sum(i.item.weight * i.amount for i in self.inventory):
                return('too heavy')
            else:
                if item in [i.item for i in self.inventory]:  # I can't believe I got this line to work with my first try
                    self.inventory[[i.item for i in self.inventory].index(item)].amount += amount   # oh god why
                else:
                    self.inventory.append(InvItem(item, amount))
                    if msge == True:
                        msg.msg(item.name+__(" has been added to Inventory."))
                    elif msge == False:
                        pass
                return('success')

        def has_item(self, item, amount=1, msge=True):
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

        def earn(self, amount, msge=False):
            global current_money
            current_money = self.money + amount
            if msge == True:
                if amount > 0:
                    msg.msg(__("Earned ")+amount+" "+money_loc)
                else:
                    msg.msg(__("Lost ")+amount+" "+money_loc)
            else:
                pass

define fangbag = Container(
    weight_max=12,
    money=100)

define Jade_DESC = __("An Amulet made of Jade. It's precious and pricey and easy to carry around. Beautiful green and serene. This is what hope feels like.")


define Jade = Item(__("Jade Amulet"), weight= 0.3, value=250, desc=Jade_DESC)
#Chapter One
define Peking_admission = Item(__("Peking University Admission paper"), 0.005, 80)
define Red_Lantern = Item(__("Red Lantern"), 0.4, 15)
define Work_Recommendation = Item(__("Cheung's Work Recommendation Document"), 0.005, 10)
define WPC_letter = Item(__("Ku Hong-Meng's Letter to Wang P'u Ch'en"), 0.005, 0)


