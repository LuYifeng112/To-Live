init:
    python:
        def max_points(*values):
            return [ i for i, v in enumerate(values) if v == max(values) ]
init:
    config.mouse = { 'default' : [ ('GUI/00_cursor.png', 0, 0)] }

python:
    if health <= 0:
        renpy.jump(fang_death_monolouge)

init python:
    import random
    import subprocess
    import os



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
define fang = Character("Fang Jie", who_color="#3154b5", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
define narrator = Character(ctc="ctc_blink", ctc_position="nestled")
#MISC
define un = Character("???",what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")

#1937
define Gu = Character("Ku Hong-Meng", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled") 
define Po = Character("Professor Po Yeutarng", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")

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
    
    $ _dismiss_pause = False
    $ mouse_visible = False
    show placeholder
    play sound "sounds/chapter_bookmarks_sounds/1937_sino_japanese_book_mark_sound.ogg"
    $ renpy.movie_cutscene("00_chapter_bookmark/1937_sino_japanese_war_bookmark.ogv")
    scene black with dissolve
    with Pause(0.5)

    
    play music forgetting_beijing
    play sound "sounds/ambience/1937_Beijing_ambience_steps.ogg"
    show Beijing_location with dissolve
    with Pause (2)

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


    