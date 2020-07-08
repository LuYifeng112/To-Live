########     ###    ##    ## ########   #######  ##     ##  ######  
##     ##   ## ##   ###   ## ##     ## ##     ## ###   ### ##    ## 
##     ##  ##   ##  ####  ## ##     ## ##     ## #### #### ##       
########  ##     ## ## ## ## ##     ## ##     ## ## ### ##  ######  
##   ##   ######### ##  #### ##     ## ##     ## ##     ##       ## 
##    ##  ##     ## ##   ### ##     ## ##     ## ##     ## ##    ## 
##     ## ##     ## ##    ## ########   #######  ##     ##  ######  
init python:
    '''
    This is a list of random quotes.
    A global variable chooses it through a renpy.random.choice function.
    '''
    TL_quotes = [
        __("We live in the present,\nwe dream of the future\n and we learn eternal truths from the past.\n -Soong Mei Ling"),
        __("We write our own destiny...\nwe become what we do.\n -Chiang Kai-Shek"),
        __("The sky cannot have two suns.\n -Chiang Kai-Shek"),
        __("If the idea of revolution is to win out,\nit must be through political enlightenment.\nIt is useless to try to impose it by force of arms.\n Sun Yat-Sen"),
        __("The whole world is one family.\n -Sun Yat-Sen"),
        __("Kindness in words creates confidence.\nKindness in thinking creates profoundness.\nKindness in giving creates love.\n -Mao Ze-Dong"),
        __("The people, and the people alone,\n are the motive force in the making of world history.\n -Mao Ze-Dong"),
        __("Politics is war without bloodshed\n while war is politics with bloodshed.\n -Mao Ze-Dong"),
        __("Who are our enemies? Who are our friends?\n This is a question of the first importance for the revolution.\n -Mao Ze-Dong"),
        __("All diplomacy is a continuation of war by other means.\n -Zhou En-Lai"),
        __("No matter if it is a white cat or a black cat;\nas long as it can catch mice,\nit is a good cat.\n -Deng Xiao-Ping"),
        __("Let some people get rich first.\n -Deng Xiao-Ping"),
        __("Give me fifty DC-3s\nand the Japanese can have the Burma Road.\n - Chiang Kai-Shek"),
        __("If imperialism is not banished from the country,\nChina will perish as a nation.\nIf China does not perish, then imperialism cannot remain.\n - Chiang Kai-Shek"),
        __("Politics have no relation to morals.\n -Niccolo Machiavelli"),
        __("The more sand has escaped from the hourglass of our life,\nthe clearer we should see through it.\n -Niccolo Marchiavelli"),
        __("It is better to be feared than loved,\n if you cannot be both.\n -Niccolo Machiavelli"),
        __("The Chinese people have only family and clan solidarity,\nthey do not have national spirit…\nthey are just a heap of loose sand.\n - Sun Yat Sen"),
        __("The rise or fall of Shanghai\nmeans the birth or death of the whole nation.\n -Chiang Kai-Shek"),
        __("Patriotism demands of us sustained sacrifice.\n -Chiang Kai-Shek"),
        __("Dr. Sun Yat-sen, Father of the Republic,\nmade it his great aim in his revolutionary leadership to secure\nfreedom and equality of status for China\namong the nations of the world.\n -Chiang Kai-Shek"),
        __("Human history is in this sense no different from the planet Earth:\nit continues relentlessly on its path,\nwhether at noontime or at midnight.\n -Chen Du-Xiu"),
        __("A journey of a thousand miles begins with a single step.\n -Lao-Tzu"),
        __("Piercing wind,\nfreezing river of Yi.\nThe hero fords,\nand he never returns!\n -Jing-Ke (failed Assassin of Emperor Qin Shi Huang"),
        __("Amongst the flowers is a pot of wine\n I pour alone but with no friend at hand\n So I lift the cup to invite the shining moon\n Along with my shadow\n a fellowship of three.\n -Li Bai")
    ]
    '''
    Similar to the above with random quotes this is more of a visual art thing.
    Instead of displaying text string it will show an image through a global variable of renpy.random.choice function.
    '''
    TL_leader_pic = [
        "country_leader/CHI_chiang_kai_shek.png"
    ]

 ######  ######## ##    ## ##       ########  ######  
##    ##    ##     ##  ##  ##       ##       ##    ## 
##          ##      ####   ##       ##       ##       
 ######     ##       ##    ##       ######    ######  
      ##    ##       ##    ##       ##             ## 
##    ##    ##       ##    ##       ##       ##    ## 
 ######     ##       ##    ######## ########  ######  
style MapText is button:
    activate_sound "sounds/menu/select_flip.ogg"
style MapText is text:
    antialias True 
    color "#000000" 
    hover_color "#FF0000" 
    size 20 
    kerning -2
    # size 25
    # kerning -1
translate chinesesim style MapText:
    activate_sound "sounds/menu/select_flip.ogg"
    font"fonts/chi_cities/MaShanZheng-Regular.ttf"
    kerning -1
translate korean style MapText:
    activate_sound "sounds/menu/select_flip.ogg"
    size 25
    kerning -2
    font "fonts/kor_songmyung/SongMyung-Regular.ttf"
    language "korean-with-spaces"
translate japanese style MapText:
    activate_sound "sounds/menu/select_flip.ogg"
    size 25
    kerning -1
    font "fonts/jap_mincho/SawarabiMincho-Regular.ttf"
    language "japanese-normal"
translate russian style MapText:
    activate_sound "sounds/menu/select_flip.ogg"
    size 25
    kerning -1
    font "fonts/rus_roboto/RobotoSlab-Regular.ttf"


style GuoHeader is text:
    size 40 
    color "#e0e0e0" 
    font "fonts/eng_moria/MoriaCitadel.ttf"
    kerning 3
    antialias True
translate chinesesim style GuoHeader:
    antialias True
    kerning 2
    font "fonts/chi_cities/MaShanZheng-Regular.ttf"
    color "#e0e0e0"
    size 60
translate chinese style GuoHeader:
    antialias True
    kerning 2
    font "fonts/chi_weidong/wts11.ttf"
    color "#848783"
    size 60


style GuoLeader is text:
    size 25 
    color "#e0e0e0" 
    font "fonts/eng_moria/MoriaCitadel.ttf"
    kerning 2
    antialias True   
translate chinese style GuoLeader:
    antialias True
    font "fonts/chi_weidong/wts11.ttf"
    color "#848783"
    size 45
translate chinesesim style GuoLeader:
    antialias True
    font "fonts/chi_cities/MaShanZheng-Regular.ttf"
    color "#e0e0e0"
    size 45


style GuoLeaderSub is text:
    size 13 
    color "#e0e0e0" 
    font "fonts/eng_moria/MoriaCitadel.ttf"
    kerning 0.5
    antialias True
translate chinese style GuoLeaderSub:
    antialias True
    font "fonts/chi_weidong/wts11.ttf"
    color "#e0e0e0"
    size 30
translate chinesesim style GuoLeaderSub:
    antialias True
    font "fonts/chi_cities/MaShanZheng-Regular.ttf"
    color "#e0e0e0"
    size 30


style GuoText is text:
    size 15 
    color "#e0e0e0" 
    font "fonts/eng_moria/MoriaCitadel.ttf"
    antialias True
translate chinese style GuoText:
    antialias True
    font "fonts/chi_weidong/wts11.ttf"
    color "#e0e0e0"
    size 40
translate chiensesim style GuoText:
    antialias True
    font "fonts/chi_cities/MaShanZheng-Regular.ttf"
    color "#e0e0e0"
    size 40 

style TL_pref is text:
    antialias True
    color "#d4d4d4"
    hover_color "#e3e3e3"
    selected_color "#fc1919"

style TL_PrefObjective is text:
    antialias True
    size 20 
    font "fonts/eng_moria/MoriaCitadel.ttf" 
    antialias True

style TL_PrefSubtext is text:
    antialias True
    size 12 
    font "fonts/eng_moria/MoriaCitadel.ttf"

style TL_PrefQuote is text:
    antialias True
    size 15 
    font "fonts/eng_moria/MoriaCitadel.ttf" 
    color "#FFFFFF"

style TL_PrefPause is text:
    size 55 
    kerning -1 
    font "fonts/eng_moria/MoriaCitadel.ttf"
    antialias True
style TL_menu is text:
    font "fonts/chi_pinyin/Alegreya-Regular.ttf"
    antialias True
    kerning -1
# style TL_pref is button:
#     activate_sound "sounds/menu/select_flip.ogg"
######## ########     ###    ##    ##  ######  ########  #######  ########  ##     ##  ######  
   ##    ##     ##   ## ##   ###   ## ##    ## ##       ##     ## ##     ## ###   ### ##    ## 
   ##    ##     ##  ##   ##  ####  ## ##       ##       ##     ## ##     ## #### #### ##       
   ##    ########  ##     ## ## ## ##  ######  ######   ##     ## ########  ## ### ##  ######  
   ##    ##   ##   ######### ##  ####       ## ##       ##     ## ##   ##   ##     ##       ## 
   ##    ##    ##  ##     ## ##   ### ##    ## ##       ##     ## ##    ##  ##     ## ##    ## 
   ##    ##     ## ##     ## ##    ##  ######  ##        #######  ##     ## ##     ##  ######  

#Menu
transform slant:
    subpixel True
    on show:
        rotate 330
    on idle:
        linear 4.5 yalign 0.09
        linear 5.0 yalign 0.11
        repeat
transform slant_st:
    subpixel True
    on show:
        rotate 330
    on idle:
        linear 4.5 yalign 0.14
        linear 5.0 yalign 0.15
        repeat

transform slant_title:
    on show:
        rotate 355
        yoffset -10

transform slant_q:
    subpixel True
    linear 10 rotate 10
    linear 10 rotate -10
    repeat

transform slant_a:
    on show:
        rotate 350

transform ambient_left:
    rotate 15
    subpixel True
    on hover:
        linear .15 zoom 1.25
    on idle:
        linear .25 zoom 1.0
        block:
            linear 5 yoffset -10
            linear 5 yoffset 10
            repeat
transform ambient:
    subpixel True
    on hover:
        linear .15 zoom 1.25
    on idle:
        linear .25 zoom 1.0

transform am_hist:
    yalign 0.55
    rotate 345
    subpixel True
    on hover:
        linear .15 zoom 1.25
    on idle:
        linear .25 zoom 1.0     
        linear 5 yalign 0.54
        linear 5 yalign 0.56
        repeat
transform am_ch:
    yalign 0.65
    rotate 345
    subpixel True
    on hover:
        linear .15 zoom 1.25
    on idle:
        linear .25 zoom 1.0 
        linear 4.9 yalign 0.64
        linear 4.9 yalign 0.66
        repeat
transform am_map:
    yalign 0.45
    rotate 345
    subpixel True
    on hover:
        linear .15 zoom 1.25
    on idle:
        linear .25 zoom 1.0 
        linear 5 yalign 0.44
        linear 4.9 yalign 0.46
        repeat
transform am_res:
    yalign 0.75
    rotate 345
    subpixel True
    on hover:
        linear .15 zoom 1.25
    on idle:
        linear .25 zoom 1.0 
        linear 5 yalign 0.74
        linear 4.95 yalign 0.76
        repeat



#Country pages
transform slant_guo_name:
    subpixel True
    #rotate 355
    block:
        linear 4.5 yoffset -10
        linear 5.0 yoffset 10
        repeat
transform slant_guo_name_d:
    subpixel True
    linear 0.2
    block:
        linear 4.5 yoffset -10
        linear 5.0 yoffset 10
        repeat
transform guo_flag_pulse:
    subpixel True
    block:
        linear 10 rotate -10
        linear 10 zoom 1.1
    block:
        linear 10 rotate 10
        linear 10 zoom 1
    repeat
transform vbox_slidein:
    subpixel True
    xoffset -50
    block:
        linear 1.0 alpha 1.0
        linear 3.0 xoffset 0
