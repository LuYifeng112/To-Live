#Transition effect
init:
    $ flash = Fade(.25, 0, .75, color="#fff") #flash effect
    $ noisedissolve = ImageDissolve(im.Tile("00_transitions/00_noise_effect.png"), 1.0, 1) #noise effect


#game Time
init:
    default elap = renpy.get_game_runtime()

init 2 python:
    def speaker_change_callback(event, interact=True, **kwargs):
        global _speaker_changed, _last_last_say_who
        if event=="begin":
            _speaker_changed = (_last_say_who != _last_last_say_who)
            _last_last_say_who = _last_say_who
    config.all_character_callbacks.append(speaker_change_callback)

default _speaker_changed = False
default _last_last_say_who = ""
