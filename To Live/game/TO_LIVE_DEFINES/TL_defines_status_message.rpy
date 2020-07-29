init python:
    import renpy.store as store
    
    class status(store.object):
        def __init__(self, name, image):
            self.name = name
            self.image = image

define status_warning = status("Light Warning", "images/notify_icons/icon.5_02.png")


screen status_show(status=None):
    tag status_mode

    add status.image xalign 0.84 yalign 0.25 size(80,80)
    text status.name xalign 0.99 yalign 0.25 size 35

    timer 5.0 action Return()

screen status_choice(status=None):
    tag status_mode

    add status.image xalign 0.6 yalign 0.25 size(80,80)
    text status.name xalign 0.75 yalign 0.25 size 35

    timer 5.0 action Return()