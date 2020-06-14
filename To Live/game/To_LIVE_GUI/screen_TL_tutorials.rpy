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

screen lang():
    tag tutorial
    add "#000000"
    textbutton "English" xalign 0.5 yalign 0.3 text_style "langeng":
        action [Language(None), SetField(persistent, "lang", True), renpy.hide_screen('lang')]
    textbutton "简体中文" xalign 0.5 yalign 0.4 text_style "langchisim":
        action [Language("chinesesim"), SetField(persistent, "lang", True), renpy.hide_screen('lang')]
    textbutton "繁體中文" xalign 0.5 yalign 0.5 text_style "langchinese":
        action [Language("chinese"), SetField(persistent, "lang", True), renpy.hide_screen('lang')]
    textbutton "日本語" xalign 0.5 yalign 0.6 text_style "langjap":
        action [Language("japanese"), SetField(persistent, "lang", True), renpy.hide_screen('lang')]