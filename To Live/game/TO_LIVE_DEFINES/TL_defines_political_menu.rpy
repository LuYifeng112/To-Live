
init python:
    TL_quotes = [
        "We live in the present,\nwe dream of the future\n and we learn eternal truths from the past.\n -Soong Mei Ling",
        "We write our own destiny...\nwe become what we do.\n -Chiang Kai-Shek",
        "The sky cannot have two suns.\n -Chiang Kai-Shek",
        "If the idea of revolution is to win out,\nit must be through political enlightenment.\nIt is useless to try to impose it by force of arms.\n Sun Yat-Sen",
        "The whole world is one family.\n -Sun Yat-Sen",
        "Kindness in words creates confidence.\nKindness in thinking creates profoundness.\nKindness in giving creates love.\n -Mao Ze-Dong",
        "The people, and the people alone,\n are the motive force in the making of world history.\n -Mao Ze-Dong",
        "Politics is war without bloodshed\n while war is politics with bloodshed.\n -Mao Ze-Dong",
        "Who are our enemies? Who are our friends?\n This is a question of the first importance for the revolution.\n -Mao Ze-Dong",
        "All diplomacy is a continuation of war by other means.\n -Zhou En-Lai",
        "No matter if it is a white cat or a black cat;\nas long as it can catch mice,\nit is a good cat.\n -Deng Xiao-Ping",
        "Let some people get rich first.\n -Deng Xiao-Ping",
        "Give me fifty DC-3s\nand the Japanese can have the Burma Road.\n - Chiang Kai-Shek",
        "If imperialism is not banished from the country,\nChina will perish as a nation.\nIf China does not perish, then imperialism cannot remain.\n - Chiang Kai-Shek",
        "Politics have no relation to morals.\n -Niccolo Machiavelli",
        "The more sand has escaped from the hourglass of our life,\nthe clearer we should see through it.\n -Niccolo Marchiavelli",
        "It is better to be feared than loved,\n if you cannot be both.\n -Niccolo Machiavelli",
        "The Chinese people have only family and clan solidarity,\nthey do not have national spirit…\nthey are just a heap of loose sand.\n - Sun Yat Sen",
        "The rise or fall of Shanghai\nmeans the birth or death of the whole nation.\n -Chiang Kai-Shek",
        "Patriotism demands of us sustained sacrifice.\n -Chiang Kai-Shek",
        "Dr. Sun Yat-sen, Father of the Republic,\nmade it his great aim in his revolutionary leadership to secure\nfreedom and equality of status for China\namong the nations of the world.\n -Chiang Kai-Shek",
        "Human history is in this sense no different from the planet Earth:\nit continues relentlessly on its path,\nwhether at noontime or at midnight.\n -Chen Du-Xiu",
        "A journey of a thousand miles begins with a single step.\n -Lao-Tzu",
        "Piercing wind,\nfreezing river of Yi.\nThe hero fords,\nand he never returns!\n -Jing-Ke (failed Assassin of Emperor Qin Shi Huang"
        "Amongst the flowers is a pot of wine\n I pour alone but with no friend at hand\n So I lift the cup to invite the shining moon\n Along with my shadow\n a fellowship of three.\n -Li Bai"
    ]

    def P_quote(x):
       x = renpy.random.choice(TL_quotes)

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
