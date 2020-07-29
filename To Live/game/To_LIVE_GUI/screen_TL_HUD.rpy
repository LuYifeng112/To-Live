

screen hpbar():
    text __("HP: [currenthp]/[maxhp]") xalign 0.9 yalign 0.05 size 10 style datetime at cd_transform
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

screen invdisplay():

    ## screen stuff here ##
    add "#141414"
    hbox:    ## horizontal box arranges all elements next to each other
        for i in fangbag.inventory:    ## iterates through all inventory items
            vbox:   ## vertical box displays the data of each element in one column
                text i.item.name
                text __("Weight: ")+str(i.item.weight)   ## needs str() because i.item.weight is a number
                text __("Number: ")+str(i.amount)   ## same here - note that it's i.amount, not i.item.amount!