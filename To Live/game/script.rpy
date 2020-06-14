#define persistent.ironman = False
#Mouse Icon
define config.mouse = { 'default' : [ ('GUI/00_cursor.png', 0, 0)] }

init python:
    splash_notification = __("All dramatisized events, attitudes, characters and political orientations are representations of historical environments and situations do not reflect the beliefs or values of You Yu De Shi Jie or any known affiliates in the production of this visual novel.\nThese situations are presented as a representation of historical attitudes reactions and events and do not intend to harm or offend anyone.\n\nThis game is inspired by Yu Hua's \"To Live\" and uses a fictional character to centre around real historical contexts.")



#starting time var
default timeval = 971937
default pinyin = False
default chapter = 1

#OBJ
default objective = ""
default objective_scr = ""
default subtext = ""



#health
default currenthp = 50
default maxhp = 50
default money_loc = _("Fabi")

default Fang_from_Beijing = False
default Fang_from_Nanjing = False
default Fang_from_Guangzhou = False
default Fang_from_hong_kong = False
default Fang_from_Macau = False
default Fang_from_Taiwan = False

#Religion
define Taoist = False
define Buddhist = False
define Christian = False
define Yiguandao = False
define religions = [ __("Taoism"), __("Buddhism"), __("Christian"), __("Yiguandao"), __("Islam"), __("Shintoism"), __("Communism")]
#character
define is_student = False
define is_apprentice = False
define is_worker = False
define is_free = False
define angst = renpy.random.randint(1,100)
define saucy_thoughts = renpy.random.randint(1,100)

#Promises
define promise_Guo_heng_free_meal = False
define promise_teach_Gh_cantonese = False
define promise_Gh_talk_escape = False
define promise_GH_beer = False

#Transition effect
init:
    $ flash = Fade(.25, 0, .75, color="#fff") #flash effect
    $ noisedissolve = ImageDissolve(im.Tile("00_transitions/00_noise_effect.png"), 1.0, 1) #noise effect
    $ sshake = Shake((0, 0, 0, 0), 0.5, dist=5) #anger shake effect

################################################
python:
        ## test if the file path exists, setting the 'secret_route_unlocked' object if file exists
        if renpy.exists('checkpoints/00_1937_checkpoint_exist.txt'):
            persistant.timing = 0
        if renpy.exists('checkpoints/00_1945_checkpoint_exist.txt'):
            persistant.timing = 1
        if renpy.exists('checkpoints/00_1956_checkpoint_exist.txt'):
            persistant.timing = 2
        if renpy.exists('checkpoints/00_1958_checkpoint_exist.txt'):
            persistant.timing = 3
        if renpy.exists('checkpoints/00_1966_checkpoint_exist.txt'):
            persistant.timing = 4

 ######   ##     ## ####     ######  ######## ##    ## ##       ########  ######
##    ##  ##     ##  ##     ##    ##    ##     ##  ##  ##       ##       ##    ##
##        ##     ##  ##     ##          ##      ####   ##       ##       ##
##   #### ##     ##  ##      ######     ##       ##    ##       ######    ######
##    ##  ##     ##  ##           ##    ##       ##    ##       ##             ##
##    ##  ##     ##  ##     ##    ##    ##       ##    ##       ##       ##    ##
 ######    #######  ####     ######     ##       ##    ######## ########  ######
style datetime is text:
    font "fonts/eng_phat_grunge/PhatGrunge.ttf"

image ctc_blink:
       "GUI/ctc.png"
       linear 0.5 alpha 1.0
       pause 0.25
       linear 0.5 alpha 0.0
       pause 0.25
       repeat

style letter_eng is text:
    size 40
    font "fonts/eng_scriptina/SCRIPTIN.ttf"


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
    with Pause(2)

    $ mouse_visible = True
    $ _dismiss_pause = True
    jump before_main_menu
    return
 ######  ##     ##    ###    ########     ###     ######  ######## ######## ########   ######
##    ## ##     ##   ## ##   ##     ##   ## ##   ##    ##    ##    ##       ##     ## ##    ##
##       ##     ##  ##   ##  ##     ##  ##   ##  ##          ##    ##       ##     ## ##
##       ######### ##     ## ########  ##     ## ##          ##    ######   ########   ######
##       ##     ## ######### ##   ##   ######### ##          ##    ##       ##   ##         ##
##    ## ##     ## ##     ## ##    ##  ##     ## ##    ##    ##    ##       ##    ##  ##    ##
 ######  ##     ## ##     ## ##     ## ##     ##  ######     ##    ######## ##     ##  ######

#Protagonist
define fang = Character(__("Fang Jie"), who_color="#3154b5", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="fang")
define narrator = Character(ctc="ctc_blink", ctc_position="nestled")
define f = Character(__("The Father"), who_color="#fc0335", what_pefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
define m = Character(__("The Mother"), who_color="#0d00ff", what_pefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
define v = Character(__("The Voices"), who_color="#5b5963", what_pefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
#MISC
define un = Character("???",what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
define thought = Character(None, what_italic=True, what_alt="I think, [text]")
define prostitute = Character(__("Chang San Brothel worker"),what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
#1937
define Ab = Character(__("Ah Bai"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ab")
define Am = Character(__("Ah Mei"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Am")
define Ghe = Character(__("Guo He"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ghe")
define Gh = Character(__("Guo Heng"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="gh")
define Gu = Character(__("Ku Hong-Meng"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Gu")
define Lc = Character(__("Lao Chang"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Lc")
define Li = Character(__("Li-Li"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Li")
define Ls = Character(__("Li Tso-Shih"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ls")
define Ly = Character(__("Lady Yang"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ly")
define monk = Character(__("Monk"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="monk")
define Mw = Character(__("Ma Wen"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Mw")
define Po = Character(__("Professor Po Yeutarng"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Po")
define wyx = Character(__("Wang Yue Hsiang"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
define Xw = Character(__("Xiao Wen"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Xw")
define Xwe = Character(__("Xiao Wei"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Xwe")

#1937 Japanese
define ai = Character(__("Yumi"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="ai")
#1945


#1949


#1956


#1958


#1966



   ##    #######   #######  ########    ########   #######   #######  ##    ## ##     ##    ###    ########  ##    ##
 ####   ##     ## ##     ## ##    ##    ##     ## ##     ## ##     ## ##   ##  ###   ###   ## ##   ##     ## ##   ##
   ##   ##     ##        ##     ##      ##     ## ##     ## ##     ## ##  ##   #### ####  ##   ##  ##     ## ##  ##
   ##    ########  #######     ##       ########  ##     ## ##     ## #####    ## ### ## ##     ## ########  #####
   ##          ##        ##   ##        ##     ## ##     ## ##     ## ##  ##   ##     ## ######### ##   ##   ##  ##
   ##   ##     ## ##     ##   ##        ##     ## ##     ## ##     ## ##   ##  ##     ## ##     ## ##    ##  ##   ##
 ######  #######   #######    ##        ########   #######   #######  ##    ## ##     ## ##     ## ##     ## ##    ##
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
                'details': '1937 Sino-Japanese war Bookmark',
                'state': 'Peiping-Ts\'uan Ti hsia Village',
                'large_image_key': 'tolive',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
    python:
        inventory = Inventory()
    if persistent.ironman:
        init python:
            config.has_autosave = True
            config.autosave_slots = 1
            config.autosave_on_choice = True
            config.autosave_on_quit = True
    $ save_name = "Chapter One- Peiping"
    $ _quit_slot = "quitsave"
    $ inventory.earn(100)
    $ current_money = inventory.money
    $currenthp = 50
    $maxhp = 50
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
