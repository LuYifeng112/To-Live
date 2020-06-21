init python:
    month = 7
    date = 9
    year = 1937
    timeofday = "Late Morning"

style datetime is text:
    font "fonts/eng_phat_grunge/PhatGrunge.ttf"

define dayperiods = [ "Late Morning", "early afternoon", "dusk", "early night", "late night", "midnight", "early morning" ]

transform cd_transform:
    on appear:
        alpha 1.0
    on show:
        zoom .75
        linear .25 zoom 1.0 alpha 1.0
    on hide:
        linear .25 zoom 1.25 alpha 0.0

transform cd_transform_skew:
    on appear:
        alpha 1.0
        rotate 330
    on show:
        zoom .75
        linear .25 zoom 1.0 alpha 1.0
    on hide:
        linear .25 zoom 1.25 alpha 0.0

screen date():
    for i in range(1, 32):
        showif date == i:
            text "[i]/" size 50 xalign 0.91 yalign 0.03 style "datetime"  at cd_transform
screen month():
    for i in range(1, 13):
        showif month == i:
            text "[i]/" size 50 xalign 0.94 yalign 0.03 style "datetime"  at cd_transform
screen year():
    for i in range(1900, 2000):
        showif year == i:
            text "[i]" size 75 xalign 0.99 yalign 0.01 style "datetime"  at cd_transform_skew
screen daytime():

    showif timeofday == "Late Morning":
        text __("Late Morning") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
    elif timeofday == "early afternoon":
        text __("Early Afternoon") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
    elif timeofday == "late afternoon":
        text __("Late Afternoon") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
    elif timeofday == "dusk":
        text __("Dusk") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
    elif timeofday == "early night":
        text __("Early Night") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
    elif timeofday == "late night":
        text __("Late Night") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
    elif timeofday == "midnight":
        text __("Midnight") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
    elif timeofday == "dawn":
        text __("Dawn") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
    elif timeofday == "early morning":
        text __("Early Morning") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform