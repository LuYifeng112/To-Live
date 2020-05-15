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

#game Time
init:
    default elap = renpy.get_game_runtime()

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
