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

#Mouse Icon
define config.mouse = { 'default' : [ ('GUI/00_cursor.png', 0, 0)] }

#Poem
define persistent.agneepath = False
define persistent.tao_water_way = False
define persistent.unlocked_poem = []

#Glossary
define persistent.unlocked = [] # empty word list
#Historical Events log
define persistent.unlocked_history = [] #Empty hitorical log

#Religion
$ Taoist = False
$ Buddhist = False
$ Christian = False
$ Yiguandao = False

#Health System
$ Fang_health = 100
python:
    if health <= 0:
        renpy.jump(fang_death_monolouge)


#Restart the game from scratch
init python:
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    
#Transition effect 
init:
    $ flash = Fade(.25, 0, .75, color="#fff") #flash effect
    $ noisedissolve = ImageDissolve(im.Tile("00_transitions/00_noise_effect.png"), 1.0, 1) #noise effect
    $ sshake = Shake((0, 0, 0, 0), 0.5, dist=5) #anger shake effect

#Dialogue percentage
init:
    default seen = renpy.count_seen_dialogue_blocks()
    default dialogue = renpy.count_dialogue_blocks()
    default result = seen * 100 / dialogue
$ percent = "Game Progress: [result]%"

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
################################################

image splash ="00_menu_images/slash.jpg"
image mal ="00_menu_images/mel.jpg"
image warn ="00_menu_images/warn.gif"
image sunflower ="00_menu_images/sunflowers.ong"
image darkthought ="00_menu_images/startup2.png"
image dt2 ="00_menu_images/startup 1.png"
image 1937_sino_japanese_war_menu ="00_menu_images/1937_bookmark_intro_splash.png"
image placeholder = "00_background/00_placeholder.png"

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

image ctc_blink:
       "GUI/ctc.png"
       linear 0.5 alpha 1.0
       pause 0.25
       linear 0.5 alpha 0.0
       pause 0.25
       repeat 

style letter_eng is text:
    size 40
    font "fonts/scriptina/SCRIPTIN.ttf"

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
    scene black
    with Pause(1)

    play sound "sounds/menu/logo_sound.ogg"

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    show 1937_sino_japanese_war_menu with dissolve
    with Pause(2)

    show placeholder
    $ renpy.movie_cutscene("00_menu_images/warn.ogv")

    scene black with dissolve
    with Pause(1)

    $ mouse_visible = True
    $ _dismiss_pause = True


    return

    


    #Location Sprites
    image Beijing_location = "00_location_bookmark/00_Beijing_city.jpg"



#MUSIC
define audio.forgetting_beijing = "music/01_forgetting_beijing.ogg"
 


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
label start:
    stop music fadeout 1.0
    $ _dismiss_pause = False
    $ mouse_visible = False
    $ _skipping = False
    show placeholder with dissolve
    with Pause(2)
    play sound "sounds/chapter_bookmarks_sounds/1937_sino_japanese_book_mark_sound.ogg"
    $ renpy.movie_cutscene("00_chapter_bookmark/1937_sino_japanese_war_bookmark.ogv")
    scene black with dissolve
    with Pause(0.5)

    
    play music forgetting_beijing
    play sound "sounds/ambience/1937_Beijing_ambience_steps.ogg"
    show Beijing_location with dissolve
    with Pause (2)
    $ _skipping = True
    scene black with dissolve
    with Pause(3)
    
    $ Sino_Japanese_war_bookmark = True
    $ Fang_jie_age = 16   

    $ mouse_visible = True
    $ _dismiss_pause = True

    jump Beijing_chapter_one 

    return


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
#if not list(set(process_list).intersection(stream_list)):
#    if currentuser != "" and currentuser.lower() != player.lower():
#        "[currentuser] will you struggle once again?"
#if buddhist:
#    "Just agree to struggle by stating \"Agneepath\""
#    $ agree_choice = "Ageneepath"
#if taoist:
#    "Just agree to struggle by stating \"Neidan\""
#    $ agree_choice = "Neidan"
#if christian:
#    "Just agree to struggle by stating \"Resurrection\""
#    $ agree_choice = "Resurrection"
#else:
#    "Just agree to struggle by stating \"I accept\""
#    $ agree_choice = "I accept"

#menu:
#    "[agree_choice]":
#        "Excellant"
#        $ renpy.notify("You are being resurrected")
#        $ recent_save = renpy.newest_slot(r"\d+")


    