##     ##    ###    ########  ####    ###    ########  ##       ########  ######  
##     ##   ## ##   ##     ##  ##    ## ##   ##     ## ##       ##       ##    ## 
##     ##  ##   ##  ##     ##  ##   ##   ##  ##     ## ##       ##       ##       
##     ## ##     ## ########   ##  ##     ## ########  ##       ######    ######  
 ##   ##  ######### ##   ##    ##  ######### ##     ## ##       ##             ## 
  ## ##   ##     ## ##    ##   ##  ##     ## ##     ## ##       ##       ##    ## 
   ###    ##     ## ##     ## #### ##     ## ########  ######## ########  ######  

#Max points
init:
    python:
        def max_points(*values):
            return [ i for i, v in enumerate(values) if v == max(values) ]

#Restart the game from scratch
init python:
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)



#Dialogue percentage
init:
    default seen = renpy.count_seen_dialogue_blocks()
    default dialogue = renpy.count_dialogue_blocks()
    default result = seen * 100 / dialogue
$ percent = "Game Progress: [result]%"

#adult scenes
init python:

    # Set the default value.
    if persistent.hentai is None:
        persistent.hentai = False

#Timed menus
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script
init:
    $ timer_range = 0
    $ timer_jump = 0

#DLC stuff
init -3 python:
    persistent.new_era_dlc_installed = False
init -1 python:
    if persistent.new_era_dlc_installed and not persistent.patch_first_time:
        persistent.patch_enabled = True
        persistent.patch_first_time = True
    elif not persistent.patch_installed:
        persistent.patch_first_time = False
        persistent.patch_enabled = False


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

######## ########  ####  ######    ######   ######## ########   ######  
   ##    ##     ##  ##  ##    ##  ##    ##  ##       ##     ## ##    ## 
   ##    ##     ##  ##  ##        ##        ##       ##     ## ##       
   ##    ########   ##  ##   #### ##   #### ######   ########   ######  
   ##    ##   ##    ##  ##    ##  ##    ##  ##       ##   ##         ## 
   ##    ##    ##   ##  ##    ##  ##    ##  ##       ##    ##  ##    ## 
   ##    ##     ## ####  ######    ######   ######## ##     ##  ######  
define recognition = []
init python:
    def recog(name):
            recognition.append(name)
            recog_count = len(recognition)


init -20 python:
    import discord_rpc
    import time

    def readyCallback(current_user):
        print('Our user: {}'.format(current_user))

    def disconnectedCallback(codeno, codemsg):
        print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
            codeno, codemsg
        ))

    def errorCallback(errno, errmsg):
        print('An error occurred! Error {}: {}'.format(
            errno, errmsg
        ))

label before_main_menu:
    python:
        # Note: 'event_name': callback
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('704183975987511348', callbacks=callbacks, log=False)
        start = time.time()
        print(start)
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Main Menu',
                'start_timestamp': start,
                'large_image_key': 'tolive'
            }
        )
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
    return


