style datetime is text:
    font "fonts/eng_phat_grunge/PhatGrunge.ttf"

define _datetime = True

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
        if _datetime:
            showif TL_datetime.return_day() == i:
                text "[i]/" size 50 xalign 0.91 yalign 0.03 style "datetime"  at cd_transform
screen month():
    for i in range(1, 13):
        if _datetime:
            showif TL_datetime.return_month() == i:
                text "[i]/" size 50 xalign 0.94 yalign 0.03 style "datetime"  at cd_transform
screen year():
    for i in range(1900, 2000):
        if _datetime:
            showif TL_datetime.return_year() == i:
                text "[i]" size 75 xalign 0.99 yalign 0.01 style "datetime"  at cd_transform_skew
screen daytime():
    if _datetime:
    
        showif TL_datetime.return_daytime() == "Late Morning":
            text __("Late Morning") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
        elif TL_datetime.return_daytime() == "Early Afternoon":
            text __("Early Afternoon") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
        elif TL_datetime.return_daytime() == "Late Afternoon":
            text __("Late Afternoon") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
        elif TL_datetime.return_daytime() == "Dusk":
            text __("Dusk") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
        elif TL_datetime.return_daytime() == "Early Night":
            text __("Early Night") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
        elif TL_datetime.return_daytime() == "Late Night":
            text __("Late Night") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
        elif TL_datetime.return_daytime() == "Midnight":
            text __("Midnight") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
        elif TL_datetime.return_daytime() == "Dawn":
            text __("Dawn") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform
        elif TL_datetime.return_daytime() == "Early Morning":
            text __("Early Morning") size 35 xalign 0.97 yalign 0.15 style "datetime" at cd_transform