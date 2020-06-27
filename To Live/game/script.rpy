default persistent.chapter = 1

#OBJ
default objective = ""
default objective_scr = ""
default subtext = ""

 ######  ##     ##    ###    ########     ###     ######  ######## ######## ########   ######
##    ## ##     ##   ## ##   ##     ##   ## ##   ##    ##    ##    ##       ##     ## ##    ##
##       ##     ##  ##   ##  ##     ##  ##   ##  ##          ##    ##       ##     ## ##
##       ######### ##     ## ########  ##     ## ##          ##    ######   ########   ######
##       ##     ## ######### ##   ##   ######### ##          ##    ##       ##   ##         ##
##    ## ##     ## ##     ## ##    ##  ##     ## ##    ##    ##    ##       ##    ##  ##    ##
 ######  ##     ## ##     ## ##     ## ##     ##  ######     ##    ######## ##     ##  ######

#Protagonist
define character.fang = Character(__("Fang Jie"), who_color="#3154b5", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="fang")
define character.narrator = Character(ctc="ctc_blink", ctc_position="nestled")
define character.f = Character(__("The Father"), who_color="#fc0335", what_pefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
define character.m = Character(__("The Mother"), who_color="#0d00ff", what_pefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
define character.v = Character(__("The Voices"), who_color="#5b5963", what_pefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
#MISC
define character.un = Character("???",what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
define character.thought = Character(None, what_italic=True, what_alt="I think, [text]")
define character.prostitute = Character(__("Chang San Brothel worker"),what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
#1937
define character.Ab = Character(__("Ah Bai"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ab")
define character.Am = Character(__("Ah Mei"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Am")
define character.Ghe = Character(__("Guo He"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ghe")
define character.Gh = Character(__("Guo Heng"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="gh")
define character.Gu = Character(__("Ku Hong-Meng"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Gu")
define character.Lc = Character(__("Lao Chang"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Lc")
define character.Li = Character(__("Li-Li"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Li")
define character.Ls = Character(__("Li Tso-Shih"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ls")
define character.Ly = Character(__("Lady Yang"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ly")
define character.monk = Character(__("Monk"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="monk")
define character.Mw = Character(__("Ma Wen"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Mw")
define character.Po = Character(__("Professor Po Yeutarng"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Po")
define character.wpc = Character(__("Wang P'u Ch'en"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="wpc")
define character.wyx = Character(__("Wang Yue Hsiang"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
define character.Xw = Character(__("Xiao Wen"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Xw")
define character.Xwe = Character(__("Xiao Wei"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Xwe")

#1937 Japanese
define ai = Character(__("Yumi"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="ai")

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
    show note
    with Pause(3)
    scene black

    play sound sound_menu_logo
    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    show renpy_cred with dissolve
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
    $ renpy.movie_cutscene("00_chapter_bookmark/1937_sino_japanese_war_bookmark.ogv")
    scene black with dissolve
    with Pause(0.5)
    $ save_name = "Chapter One- Peiping\n Talk Like Doves"
    $ inventory.earn(100)
    $ current_money = inventory.money
    $currenthp = 50
    $maxhp = 50

    play sound ambience_steps
    show Beijing_location with dissolve
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
    jump Beijing_chapter_one
