default nation = None


screen political_menu():
    tag menu
    default quote = renpy.random.choice(TL_quotes)
    default leader = renpy.random.choice(TL_leader_pic)

    key "K_SPACE" action ShowMenu(main_menu)
    key "K_TAB" action ShowMenu(main_menu)
    key "K_ESCAPE" action Return()
    key "o" action Return()
    key "g" action ShowMenu('glossary')
    key "p" action ShowMenu('poems')
    key "2" action ShowMenu('glossary')
    key "3" action ShowMenu('poems')

    add "#141414"

    text "[objective]" xalign 0.05 yalign 0.05 size 20 font "fonts/eng_moria/MoriaCitadel.ttf" at slant antialias True
    text "[subtext]" xalign 0.07 yalign 0.15 size 12 font "fonts/eng_moria/MoriaCitadel.ttf" at slant_st antialias True
    text "[quote]" xpos 45 yalign 1.1 size 15 font "fonts/eng_moria/MoriaCitadel.ttf" color "#FFFFFF" at slant_q antialias True
    text __("Pause") xalign 0.4 size 55 kerning -1 font "fonts/eng_moria/MoriaCitadel.ttf" at slant_title antialias True
    add leader xalign 0.55 yalign 0.45

    if not main_menu:
        textbutton __("Main Menu") xalign 0.3 yalign 0.25 action ShowMenu('main_menu') at ambient_left:
            keyboard_focus True    
        textbutton __("Save Game") xalign 0.3 yalign 0.35 action ShowMenu('save') at ambient_left:
            keyboard_focus True
            keysym "s"
    textbutton __("Dialogue History") xalign 0.3 yalign 0.55 action ShowMenu('history') at ambient_left:
        keyboard_focus True
        keysym "h"
    textbutton __("Load Game") xalign 0.3 yalign 0.45 action ShowMenu('main_menu') at ambient_left:
        keyboard_focus True
    textbutton __("National Map") xalign 0.9 yalign 0.56 action ShowMenu('guo_map') at am_map:
        keyboard_focus True
        keysym "n"
    textbutton __("Historical Event Log") xalign 0.91 yalign 0.65 action ShowMenu('historical_event_log') at am_hist:
        keyboard_focus True
        keysym "l"

define TL_pref_tab = "General"
define _mature = False
define persistant.edgeval = 200
screen TL_pref():
    tag menu
    modal True
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
    window:
        style "gm_root"
        add "#141414"
    add "abyss_snow"
    text __("Settings") xalign 0.5 size 60
    hbox xalign 0.45 yalign 0.1 spacing 100:
        textbutton __("General") keyboard_focus True text_style "TL_pref" action SetVariable("TL_pref_tab","General") at ambient
        textbutton __("Audio") keyboard_focus True text_style "TL_pref" action SetVariable("TL_pref_tab", "Audio") at ambient
        textbutton __("Controls") keyboard_focus True text_style "TL_pref" action SetVariable("TL_pref_tab", "Controls") at ambient
        textbutton __("Map Settings") keyboard_focus True text_style "TL_pref" action SetVariable("TL_pref_tab", "Map") at ambient
        textbutton __("Character Settings") keyboard_focus True text_style "TL_pref" action SetVariable("TL_pref_tab", "Character") at ambient

    showif TL_pref_tab == "General":
        vbox xalign 0.3 yalign 0.25:
            style_prefix "radio"
            label _("Display")
            textbutton _("Window") action Preference("display", "window")
            textbutton _("Fullscreen") action Preference("display", "fullscreen")
        vbox xalign 0.5 yalign 0.25:
            style_prefix "radio"
            label _("Rollback Side")
            textbutton _("Disable") action Preference("rollback side", "disable")
            textbutton _("Left") action Preference("rollback side", "left")
            textbutton _("Right") action Preference("rollback side", "right")
        vbox xalign 0.7 yalign 0.25:
            style_prefix "radio"
            label __("Mature Themes")
            textbutton __("Enable") action SetVariable("_mature",True)
            textbutton __("Disable") action SetVariable("_mature", False)


    showif TL_pref_tab == "Audio":
        vbox xalign 0.2 yalign 0.25:
            if config.has_music:
                label _("Music Volume")

                hbox:
                    bar value Preference("music volume")

            if config.has_sound:

                label _("Sound Volume")

                hbox:
                    bar value Preference("sound volume")

                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)

    showif TL_pref_tab == "Map":
        vbox xalign 0.7 yalign 0.25:
            style_prefix "radio"
            label __("Audio")
            textbutton "No Ocean SFX" action ToggleField(persistent, "_map_ocean_SFX")
            


screen guo(): 
    tag menu
    modal True
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
    imagebutton:
        idle "gui/button_return_icon.png"
        hover "gui/button_return_icon_hovered.png"
        xalign 0.9 yalign 0.05
        action Return()
    add "abyss_snow"
    mousearea: #This is to make sure that the list doesn't block info or look ugly unless we want to select a new country
        area (0, 0, 500, 1080)
        hovered SetScreenVariable("vbox_button_is_hovered", True)
        unhovered SetScreenVariable("vbox_button_is_hovered", False)        
    window:
        style "gm_root"
        add "#141414"
    viewport:
        xpos 0 ypos 110 xsize 300 ysize 700
        draggable True
        mousewheel True
        pagekeys True
        edgescroll (130, 130)
        showif vbox_button_is_hovered:
            vbox spacing 15:
                at fader
                for n in TL_GUO:
                    if n.IsActive:
                        textbutton n.name:
                            keyboard_focus True
                            action SetVariable("nation", n)                    
    text [nation.name] xalign 0.5 ypos 10 at slant_guo_name:
        if _preferences.language == None: 
            size 40 
            color "#e0e0e0" 
            font "fonts/eng_moria/MoriaCitadel.ttf"
            kerning 3
            antialias True
        if _preferences.language == "chinesesim":
            style "chinesesim_header"
        elif _preferences.language == "chinese":
            style "chinese_header"
    text [nation.leader] xalign 0.25 yalign 0.2:
        if _preferences.language == None:
            size 25 
            color "#e0e0e0" 
            font "fonts/eng_moria/MoriaCitadel.ttf"
            kerning 2
            antialias True
        if _preferences.language == "chinesesim":
            style "chinesesim_leader"
        elif _preferences.language == "chinese":
            style "chinese_leader"
    text [nation.leadersub] xalign 0.28 yalign 0.25:
        if _preferences.language == None:
            size 13 
            color "#e0e0e0" 
            font "fonts/eng_moria/MoriaCitadel.ttf"
            kerning 0.5
            antialias True
        if _preferences.language == "chinesesim":
            style "chinesesim_sub"
        elif _preferences.language == "chinese":
            style "chiense_sub"
    text [__("Government Type:")]+[nation.politicalID] xalign 0.9 yalign 0.45:
        if _preferences.language == None:
            size 15 
            color "#e0e0e0" 
            font "fonts/eng_moria/MoriaCitadel.ttf"
            antialias True
        if _preferences.language == "chinesesim":
            style "chinesesim_text"
        elif _preferences.language == "chinese":
            style "chinese_text"
    text [__("Political Alignment:")]+[nation.AlignmentID] xalign 0.9 yalign 0.5:
        if _preferences.language == None:
            size 15 
            color "#e0e0e0" 
            font "fonts/eng_moria/MoriaCitadel.ttf"
            antialias True
        if _preferences.language == "chinesesim":
            style "chinesesim_text"
        elif _preferences.language == "chinese":
            style "chinese_text"
    text [__("Ruling Party:")]+[nation.rulingparty] xalign 0.9 yalign 0.55: 
        if _preferences.language == None:
            size 15 
            color "#e0e0e0" 
            font "fonts/eng_moria/MoriaCitadel.ttf"
            antialias True
        if _preferences.language == "chinesesim":
            style "chinesesim_text"
        elif _preferences.language == "chinese":
            style "chinese_text"
    text [__("Alliances:")]+[nation.factionID] xalign 0.9 yalign 0.6:
        if _preferences.language == None:
            size 15 
            color "#e0e0e0" 
            font "fonts/eng_moria/MoriaCitadel.ttf"
            antialias True
        if _preferences.language == "chinesesim":
            style "chinesesim_text"
        elif _preferences.language == "chinese":
            style "chinese_text"
    add nation.flagimg xalign 0.9 yalign 0.1 at guo_flag_pulse
    imagebutton:
        idle "gui/button_return_icon.png"
        hover "gui/button_return_icon_hovered.png"
        xalign 0.96
        action Return()
    vbox xalign 0.3 ypos 300 xsize 600 ysize 1000 box_wrap True:
            text nation.info size 20 font "fonts/chi_genkai/Genkaimincho.ttf":
                if _preferences.language == "chinesesim":
                    font "fonts/chi_cities/MaShanZheng-Regular.ttf"


define persistent._map_audio = True
define persistent._map_ocean_SFX = True
screen guo_map():
    tag menu
    key "K_SPACE" action ShowMenu(main_menu)
    key "K_TAB" action ShowMenu(main_menu)
    key "K_ESCAPE" action Return()
    key "5" action ShowMenu ('guo')
    key "n" action Return()
    key "1" action Return()
    key "o" action ShowMenu('political_menu')
    key "g" action ShowMenu('glossary')
    key "p" action ShowMenu('poems')
    key "l" action ShowMenu('historical_event_log')
    key "2" action ShowMenu('glossary')
    key "3" action ShowMenu('poems')
    key "4" action ShowMenu('historical_event_log')
    viewport:
        xysize (config.screen_width, config.screen_height)
        child_size (4040, 2230)
        if persistent._map_audio == True and persistent._map_ocean_SFX == True:
            mousearea: # For dyanmic sounds
                focus_mask "GUO_FOCUS_OP"
                hovered [ Play("sound", "sounds/map/ambient_seaside.ogg", loop=True)]
                unhovered [Stop("sound",fadeout=2.5)]
        if show_beijing:
            xinitial 2300
            yinitial 500
        else:
            xinitial 2300
            yinitial 500
        draggable True
        edgescroll (350, 350)
        add "maps/GUO_map.png"
        for q in TL_GUO_loc:
            $ nx = q.x +5
            $ ny = q.y -12
            if q.IsActive:
                for n in TL_GUO:
                    if n.ID == q.ID:
                        $ act = SetVariable('nation', n)
                button:
                    xpos nx
                    ypos ny
                    sensitive n_map != False
                    keyboard_focus True
                    text q.name antialias True color "#000000" hover_color "#FF0000" size 20 kerning -2 style "mapon" at ambient:
                        if _preferences.language == "chinesesim":
                            style "mapon_zg"
                        elif _preferences.language == "chinese":
                            style mapon_tw
                        elif _preferences.language == "korean":
                            style "mapon_kr"
                        elif _preferences.language == "russian":
                            style "mapon_rs"
                        elif _preferences.language == "japanese":
                            style "mapon_jp"
                    action [act, Stop("sound", fadeout=2.5), Show('guo')]
                if not q.Port and not q.Capital:
                    add "gui/map_bullet.png" xpos q.x ypos q.y
                if q.Port and not q.Capital:
                    add "gui/map_port.png" xpos q.x ypos q.y
                if q.Capital and not q.Port:
                    add "gui/map_bullet_capital.png" xpos q.x ypos q.y
                if q.Capital and q.Port:
                    add "gui/map_bullet_capital.png" xpos q.x ypos q.y
    on "show":
        action Play("notify", "sounds/menu/select_flip.ogg", loop=False)
    on "hide":
        action Stop("music", fadeout=2.5)
                    
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
    text __("Glossary") size 40 xalign 0.5 ypos 20
    timer 3.0 action [SetScreenVariable("show_return", True)]
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
                    button:
                        text word:
                            style "TL_menu"
                        action SetVariable("display_desc", word)
        vbox ypos 100 xsize 650 ysize 500 box_wrap True:
            text glossary_dict.get(display_desc, ""):
                style "TL_menu"


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
                for poem in sorted(persistent.unlocked_poem):
                    button:
                        text poem style "TL_menu"
                        action SetVariable("poem_display_desc", poem)
        vbox ypos 100 xsize 650 ysize 500 box_wrap True:
            text poem_dict.get(poem_display_desc, ""):
                style "TL_menu"


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
    text __("Historical Events") size 40 xalign 0.5 ypos 20
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
                    button:
                        text event:
                            style "TL_menu"
                        action [SetVariable("event_display_desc", event), SetVariable("event_display_bg", num)]
                        selected event_display_desc == event and event_display_bg == num
                        sensitive event_display_desc != event and event_display_bg != num
        vbox ypos 100 xsize 650 ysize 500 box_wrap True:
            text historical_event_log.get(event_display_desc, ""):
                style "TL_menu"