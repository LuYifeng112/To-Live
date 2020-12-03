default persistent.chapter = 1

default chapter_name = __("Merantau")

 ######  ########  ##          ###     ######  ##     ##  ######   ######  ########  ######## ######## ##    ##
##    ## ##     ## ##         ## ##   ##    ## ##     ## ##    ## ##    ## ##     ## ##       ##       ###   ##
##       ##     ## ##        ##   ##  ##       ##     ## ##       ##       ##     ## ##       ##       ####  ##
 ######  ########  ##       ##     ##  ######  #########  ######  ##       ########  ######   ######   ## ## ##
      ## ##        ##       #########       ## ##     ##       ## ##       ##   ##   ##       ##       ##  ####
##    ## ##        ##       ##     ## ##    ## ##     ## ##    ## ##    ## ##    ##  ##       ##       ##   ###
 ######  ##        ######## ##     ##  ######  ##     ##  ######   ######  ##     ## ######## ######## ##    ##
label splashscreen:
    $ _dismiss_pause = False
    $ mouse_visible = False
    if not persistent.menu_note == True:
        show MENU_note
        with Pause(3)
    else:
        pass
        
    scene black

    play sound menu_sound_logo
    show MENU_YYDSJ_logo with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    show MENU_RENPY with dissolve
    with Pause(2)

    show placeholder
    $ renpy.movie_cutscene("00_menu_images/warn.ogv")
    scene black with dissolve
    with Pause(1)

    $ mouse_visible = True
    $ _dismiss_pause = True
    jump before_main_menu

 ######  ########    ###    ########  ######## 
##    ##    ##      ## ##   ##     ##    ##    
##          ##     ##   ##  ##     ##    ##    
 ######     ##    ##     ## ########     ##    
      ##    ##    ######### ##   ##      ##    
##    ##    ##    ##     ## ##    ##     ##    
 ######     ##    ##     ## ##     ##    ##    
label start:
    window hide
    python:
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('601663968288833536', callbacks=callbacks, log=False)
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Chapter One: Talk Like Doves',
                'state': 'Peiping-Ts\'uan Ti hsia Village',
                'large_image_key': 'tolive',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
    python:
        inventory = Container(100)
    if persistent.ironman:
        python:
            config.has_autosave = True
            config.autosave_slots = 1
            config.autosave_on_choice = True
            config.autosave_on_quit = True
    $ _quit_slot = "quitsave"

    jump Sino_Japanese_bookmark_chapter_one_splash

   ##    #######   #######  ########    ########   #######   #######  ##    ## ##     ##    ###    ########  ##    ##
 ####   ##     ## ##     ## ##    ##    ##     ## ##     ## ##     ## ##   ##  ###   ###   ## ##   ##     ## ##   ##
   ##   ##     ##        ##     ##      ##     ## ##     ## ##     ## ##  ##   #### ####  ##   ##  ##     ## ##  ##
   ##    ########  #######     ##       ########  ##     ## ##     ## #####    ## ### ## ##     ## ########  #####
   ##          ##        ##   ##        ##     ## ##     ## ##     ## ##  ##   ##     ## ######### ##   ##   ##  ##
   ##   ##     ## ##     ##   ##        ##     ## ##     ## ##     ## ##   ##  ##     ## ##     ## ##    ##  ##   ##
 ######  #######   #######    ##        ########   #######   #######  ##    ## ##     ## ##     ## ##     ## ##    ##

label Sino_Japanese_bookmark_chapter_one_splash:
    stop music fadeout 1.0
    $ _dismiss_pause = False
    $ mouse_visible = False
    $ _skipping = False
    $ quick_menu = False
    show placeholder with dissolve
    with Pause(2)
    play sound chapter_1937
    $ renpy.movie_cutscene("00_bookmark_chapter/1937_sino_japanese_war_bookmark.ogv")
    scene black with dissolve
    with Pause(0.5)
    $ save_name = __("Chapter One- Peiping\n [chapter_name]")
    $ inventory.earn(100)
    $ current_money = inventory.money
    $currenthp = 50
    $maxhp = 50

    play sound ambience_steps
    show LOCATION_Beijing with dissolve
    with Pause (2)
    $ _skipping = True
    scene black with dissolve
    with Pause(3)
    $ quick_menu = True

    $ Sino_Japanese_war_bookmark = True
    show screen date
    show screen month
    show screen year
    show screen daytime

    $ mouse_visible = True
    $ _dismiss_pause = True
    jump Prologue


label checkpoint:
    $ renpy.save("1-1")
    return