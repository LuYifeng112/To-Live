

screen hpbar():
    text "HP: [currenthp]/[maxhp]" xalign 0.9 yalign 0.05 size 10 style datetime at cd_transform
    bar:
        bar_vertical True
        value currenthp
        range maxhp
        xalign 0.15
        yalign 0.15
        xysize(25, 200)


screen moneycount():
    text "[money_loc]: [current_money]" xalign 0.9 yalign 0.15 style datetime

screen objective():
    text "[objective_scr]" xalign 0.5 yalign 0.1 size 40 font "fonts/eng_moria/MoriaCitadel.ttf" at fader
    text "[subtext]" xalign 0.5 yalign 0.5 size 20 font "fonts/eng_moria/MoriaCitadel.ttf" at fader