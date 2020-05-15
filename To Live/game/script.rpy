
image shards = Snow("00_globals/shard.png")
image heavy_shards = Snow("00_globals/shard.png", max_particiles=500)

#define persistent.ironman = False
#Mouse Icon
define config.mouse = { 'default' : [ ('GUI/00_cursor.png', 0, 0)] }

#starting time var
default timeval = 971937

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
define religions = [ "Taoism", "Buddhism", "Christian", "Yiguandao", "Islam", "Shintoism", "Communism"]
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
    define num = renpy.random.randint(1, 3)
    if persistent.timing ==0:
        image menu_image = "00_menu_images/" + "1937_bookmark_intro_splash_"  + str(num) + ".png"
    $ _dismiss_pause = False
    $ mouse_visible = False
    scene black
    with Pause(4)

    play sound sound_menu_logo
    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    show menu_image with dissolve
    with Pause(2)

    show placeholder
    $ renpy.movie_cutscene("00_menu_images/warn.ogv")
    scene black with dissolve
    with Pause(1)

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
define fang = Character("Fang Jie", who_color="#3154b5", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="fang")
define narrator = Character(ctc="ctc_blink", ctc_position="nestled")
#MISC
define un = Character("???",what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
define thought = Character(None, what_italic=True, what_alt="I think, [text]")
define prostitute = Character("Chang San Brothel worker",what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
#1937
define Ab = Character("Ah Bai", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ab")
define Am = Character("Ah Mei", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Am")
define Ghe = Character("Guo He", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ghe")
define Gh = Character("Guo Heng", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="gh")
define Gu = Character("Ku Hong-Meng", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Gu")
define Lc = Character("Lao Chang", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Lc")
define Li = Character("Li-Li", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Li")
define Ls = Character("Li Tso-Shih", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ls")
define Ly = Character("Lady Yang", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ly")
define Mw = Character("Ma Wen", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Mw")
define Po = Character("Professor Po Yeutarng", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Po")
define wyx = Character("Wang Yue Xiang", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
define Xw = Character("Xiao Wen", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Xw")
define Xwe = Character("Xiao Wei", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Xwe")

#1937 Japanese

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
define phrase = renpy.random.choice(("one", "two", "three", "four", "five"))
if phrase == "one":
    define prologue = _("To have friends come from afar is happiness, is it not?\n -Confucious")
elif phrase == "two":
    define prologue = _("No matter if it is a white cat or a black cat; as long as it can catch mice, it is a good cat.\n -Sichuanese Proverb")
elif phrase == "three":
    define prologue = _("Piercing wind, freezing river of Yi. The hero fords, and he never returns!\n -Jing-Ke (failed Assassin of Emperor Qin Shi Huang")
elif phrase == "four":
    define prologue = _("A journey of a thousand miles begins with a single step.\n -Lao-Tzu")
elif phrase == "five":
    $ prologue = _("Amongst the flowers is a pot of wine\n I pour alone but with no friend at hand\n So I lift the cup to invite the shining moon\n Along with my shadow\n a fellowship of three.\n     -Li Bai")

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


   ##    #######  ##        ########    ########   #######   #######  ##    ## ##     ##    ###    ########  ##    ##
 ####   ##     ## ##    ##  ##          ##     ## ##     ## ##     ## ##   ##  ###   ###   ## ##   ##     ## ##   ##
   ##   ##     ## ##    ##  ##          ##     ## ##     ## ##     ## ##  ##   #### ####  ##   ##  ##     ## ##  ##
   ##    ######## ##    ##  #######     ########  ##     ## ##     ## #####    ## ### ## ##     ## ########  #####
   ##          ## #########       ##    ##     ## ##     ## ##     ## ##  ##   ##     ## ######### ##   ##   ##  ##
   ##   ##     ##       ##  ##    ##    ##     ## ##     ## ##     ## ##   ##  ##     ## ##     ## ##    ##  ##   ##
 ######  #######        ##   ######     ########   #######   #######  ##    ## ##     ## ##     ## ##     ## ##    ##
#label 1945_chinese_civil_war:

    #return



########  ########    ###    ######## ##     ##
##     ## ##         ## ##      ##    ##     ##
##     ## ##        ##   ##     ##    ##     ##
##     ## ######   ##     ##    ##    #########
##     ## ##       #########    ##    ##     ##
##     ## ##       ##     ##    ##    ##     ##
########  ######## ##     ##    ##    ##     ##
label fang_death_monolouge:
scene black with dissolve
with Pause(2)
"Death"
$ renpy.notify("You have passed away.")
"You can feel your body slipping away in the dust."
"Your lungs expelling its final breaths."
"The world is becoming slower...{nw}"
"{fast}or is your life ending faster?{nw}"
"but something burns in you."
"A flame that cannot be extenguished."
return
if buddhist:
    "Just agree to struggle by stating \"Agneepath\""
    $ agree_choice = _("Ageneepath")
elif taoist:
    "Just agree to struggle by stating \"Neidan\""
    $ agree_choice = _("Neidan")
elif christian:
    "Just agree to struggle by stating \"Resurrection\""
    $ agree_choice = _("Resurrection")
else:
    "Just agree to struggle by stating \"I accept\""
    $ agree_choice = _("I accept")

menu:
    "[agree_choice!t]":
        "Excellant"
        $ renpy.notify("You are being resurrected")
        $ recent_save = renpy.newest_slot(r"\d+")


 #######  ##     ## #### ########
##     ## ##     ##  ##     ##
##     ## ##     ##  ##     ##
##     ## ##     ##  ##     ##
##  ## ## ##     ##  ##     ##
##    ##  ##     ##  ##     ##
 ##### ##  #######  ####    ##
