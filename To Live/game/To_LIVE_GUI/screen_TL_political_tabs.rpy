default nation = None

screen political_menu():
    tag menu
    default quote = renpy.random.choice(TL_quotes)

    key "K_SPACE" action ShowMenu(main_menu)
    key "K_TAB" action ShowMenu(main_menu)
    key "K_ESCAPE" action Return()
    key "o" action Return()
    key "n" action ShowMenu('guo_map')
    key "1" action ShowMenu('guo_map')
    key "g" action ShowMenu('glossary')
    key "p" action ShowMenu('poems')
    key "l" action ShowMenu('historical_event_log')
    key "2" action ShowMenu('glossary')
    key "3" action ShowMenu('poems')
    key "4" action ShowMenu('historical_event_log')

    add "#141414"

    text "[objective]" xalign 0.05 yalign 0.05 size 20 font "fonts/eng_moria/MoriaCitadel.ttf" at slant
    text "[subtext]" xalign 0.07 yalign 0.15 size 12 font "fonts/eng_moria/MoriaCitadel.ttf" at slant_st
    text "[quote]" xpos 45 yalign 1.1 size 15 font "fonts/eng_moria/MoriaCitadel.ttf" color "#000000" at slant_q
    text "Pause" xalign 0.4 size 55 font "fonts/eng_moria/MoriaCitadel.ttf" at slant_title

    textbutton "National Map" xalign 0.9 yalign 0.45 action ShowMenu('guo_map') at am_map
    textbutton "Historical Event Log" xalign 0.91 yalign 0.55 action ShowMenu('historical_event_log') at am_hist
    textbutton "Character profiles" xalign 0.92 yalign 0.65 at am_ch
    textbutton "Resistance Journal" xalign 0.93 yalign 0.75 at am_res

screen fang_character():
    tag menu
    key "K_SPACE" action ShowMenu(main_menu)
    key "K_TAB" action ShowMenu(main_menu)
    key "K_ESCAPE" action Return()
    key "n" action ShowMenu('guo_map')
    key "1" action ShowMenu('guo_map')
    key "g" action ShowMenu('glossary')
    key "p" action ShowMenu('poems')
    key "l" action ShowMenu('historical_event_log')
    key "2" action ShowMenu('glossary')
    key "3" action ShowMenu('poems')
    key "4" action ShowMenu('historical_event_log')

screen guo(): 
    tag menu
    default vbox_button_is_hovered = False
    key "K_SPACE" action ShowMenu(main_menu)
    key "K_TAB" action ShowMenu(main_menu)
    key "K_ESCAPE" action Return()
    key "n" action ShowMenu('guo_map')
    key "1" action ShowMenu('guo_map')
    key "g" action ShowMenu('glossary')
    key "p" action ShowMenu('poems')
    key "l" action ShowMenu('historical_event_log')
    key "2" action ShowMenu('glossary')
    key "3" action ShowMenu('poems')
    key "4" action ShowMenu('historical_event_log')
    mousearea: #This is to make sure that the list doesn't block info or look ugly unless we want to select a new country
        area (0, 0, 500, 1080)
        hovered SetScreenVariable("vbox_button_is_hovered", True)
        unhovered SetScreenVariable("vbox_button_is_hovered", False)        
    window:
        style "gm_root"
        add "#141414"
    viewport:
        xysize (config.screen_width, config.screen_height)
        child_size (2000, 1100)
        draggable True
        edgescroll (200, 200)
        showif vbox_button_is_hovered:
            vbox spacing 15:
                at fader
                for n in TL_GUO:
                    if n.IsActive:
                        textbutton n.name:
                            action SetVariable("nation", n)
    text "[nation.name]" xalign 0.5 ypos 10 size 40 font "fonts/eng_moria/MoriaCitadel.ttf" at slant_guo_name
    text "[nation.leader]" xalign 0.25 yalign 0.2 size 25 font "fonts/eng_moria/MoriaCitadel.ttf"
    text "[nation.leadersub]" xalign 0.28 yalign 0.25 size 13 font "fonts/eng_moria/MoriaCitadel.ttf"
    text "Government Type: [nation.politicalID]" xalign 0.9 yalign 0.45 size 15 font "fonts/eng_moria/MoriaCitadel.ttf"
    text "Political Alignment: [nation.AlignmentID]" xalign 0.9 yalign 0.5 size 15 font "fonts/eng_moria/MoriaCitadel.ttf" 
    text "Ruling Party: [nation.rulingparty]" xalign 0.9 yalign 0.55 size 15 font "fonts/eng_moria/MoriaCitadel.ttf"
    text "Alliances: [nation.factionID]" xalign 0.9 yalign 0.6 size 15 font "fonts/eng_moria/MoriaCitadel.ttf"  
    add nation.flagimg xalign 0.9 yalign 0.1 at guo_flag_pulse
    vbox xalign 0.3 ypos 300 xsize 600 ysize 1000 box_wrap True:
            text nation.info size 20 font "fonts/chi_wangfonts/wt064.ttf"



screen guo_map():
    tag menu
    key "K_SPACE" action ShowMenu(main_menu)
    key "K_TAB" action ShowMenu(main_menu)
    key "K_ESCAPE" action Return()
    key "5" action ShowMenu ('guo')
    key "n" action Return()
    key "1" action Return()
    key "g" action ShowMenu('glossary')
    key "p" action ShowMenu('poems')
    key "l" action ShowMenu('historical_event_log')
    key "2" action ShowMenu('glossary')
    key "3" action ShowMenu('poems')
    key "4" action ShowMenu('historical_event_log')
    viewport:
        xysize (config.screen_width, config.screen_height)
        child_size (4040, 2230)
        if show_beijing:
            xinitial 2300
            yinitial 500
        else:
            xinitial 2300
            yinitial 500
        draggable True
        edgescroll (700, 700)
        add "maps/GUO_map.png"
        for q in TL_GUO_loc:
            if q.IsActive:
                for n in TL_GUO:
                    if n.ID ==q.ID:
                        $ act = SetVariable('nation', n)
                button:
                    xpos q.x
                    ypos q.y
                    text q.name color "#000000" hover_color "#FF0000" size 20
                    action [act, Show('guo')]



transform pulse_button:
    linear .25 zoom 1.25
    linear .25 zoom 1.0
    repeat

screen tutmap():
    tag tutorial
    modal True

    add "00_keyboard_prompts/Dark/Keyboard_Black_N.png" xalign 0.2 yalign 0.3 at pulse_button
    add "00_background/00_tint.png"

    key "n" action [ShowMenu('guo_map')]



screen glossary():
    default show_return = False
    default return_button_img = renpy.random.randint(1,3)
    key "g" action [Return()]
    key "2" action [Return()]
    key "K_ESCAPE" action Return()
    key "n" action ShowMenu('guo_map')
    key "p" action ShowMenu('poems')
    key "l" action ShowMenu('historical_event_log')
    key "1" action ShowMenu('guo_map')
    key "3" action ShowMenu('poems')
    key "4" action ShowMenu('historical_event_log')
    tag menu
    window:
        style "gm_root"
        add "#000c" 
    text "Glossary" size 40 xalign 0.5 ypos 20
    timer 3.0 action [SetScreenVariable("show_return", True)]
    showif show_return:
        showif return_button_img ==1:
            add "00_keyboard_prompts/Dark/Keyboard_Black_2.png" xalign 0.9 yalign 0.1 at fader
        showif return_button_img ==2:
            add "00_keyboard_prompts/Dark/Keyboard_Black_G.png" xalign 0.9 yalign 0.1 at fader
        showif return_button_img ==3:
            add "00_keyboard_prompts/Dark/Keyboard_Black_Esc.png" xalign 0.9 yalign 0.1 at fader
    hbox spacing 200:
        viewport:
            xpos 50 ypos 100 xsize 300 ysize 500
            #child_size (None, 4000)
            scrollbars "vertical"
            spacing 5
            draggable True
            mousewheel True
            arrowkeys True
            add "#000c"
            vbox spacing 20:
            # loop over persistent here
                for word in sorted(persistent.unlocked):
                    textbutton word:
                           action SetVariable("display_desc", word)
        vbox ypos 100 xsize 650 ysize 500 box_wrap True:
            text glossary_dict.get(display_desc, "")


screen poems():
    key "p" action Return()
    key "3" action Return()
    key "K_ESCAPE" action Return()
    key "n" action ShowMenu('guo_map')
    key "g" action ShowMenu('glossary')
    key "l" action ShowMenu('historical_event_log')
    key "1" action ShowMenu('guo_map')
    key "2" action ShowMenu('glossary')
    key "4" action ShowMenu('historical_event_log')
    tag menu
    window:
        style "gm_root"
        add "#000c" 
    text "Poems" size 40 xalign 0.5 ypos 20
    hbox spacing 200:
        viewport:
            xpos 50 ypos 100 xsize 300 ysize 500
            child_size (None, 4000)
            scrollbars "vertical"
            spacing 5
            draggable True
            mousewheel True
            arrowkeys True
            vbox spacing 20:
                # use sorted(glossary_dict.keys()) instead of glossary_dict
                # to arrange the terms in alphabetic order
                for poem in sorted(persistent.unlocked_poem):
                    textbutton poem:
                        action SetVariable("poem_display_desc", poem)
        vbox ypos 100 xsize 650 ysize 500 box_wrap True:
            text poem_dict.get(poem_display_desc, "")


default event_display_bg = 0

image historical_event_background = ConditionSwitch(
    "event_display_bg == 1", "history_log_bgs/Marco_polo_bridge_bg.png",
    "True", "history_log_bgs/default_history_bg.png")

screen historical_event_log():
    tag menu
    key "l" action Return()
    key "4" action Return()
    key "K_ESCAPE" action Return()
    key "n" action ShowMenu('guo_map')
    key "g" action ShowMenu('glossary')
    key "p" action ShowMenu('poems')
    key "1" action ShowMenu('guo_map')
    key "2" action ShowMenu('glossary')
    key "3" action ShowMenu('poems')
    window:
        style "gm_root"
        add "historical_event_background"
    text "Historical Events" size 40 xalign 0.5 ypos 20
    hbox spacing 200:
        viewport:
            xpos 50 ypos 100 xsize 300 ysize 500
            child_size (None, 4000)
            scrollbars "vertical"
            spacing 5
            draggable True
            mousewheel True
            arrowkeys True
            vbox spacing 20:
                for  num,event in enumerate(persistent.unlocked_history):
                    textbutton event:
                        action [SetVariable("event_display_desc", event), SetVariable("event_display_bg", num)]
                        selected event_display_desc == event and event_display_bg == num
                        sensitive event_display_desc != event and event_display_bg != num
        vbox ypos 100 xsize 650 ysize 500 box_wrap True:
            text historical_event_log.get(event_display_desc, "")