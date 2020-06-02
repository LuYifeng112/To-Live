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
