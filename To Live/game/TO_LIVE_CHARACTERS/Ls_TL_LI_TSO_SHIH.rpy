python:

    import TL_defines_character

default Ls = Char( 
    mood ="Angry",
    bond = -10,
    pol = "Anti-KMT",
    rel = None,
    traits = LiTsoShih_traits,
    eventlog = LiTsoShihLog
    )
define LiTsoShih_traits = [
    __("Angry"),
    __("Anti-Traditionalist"),
    __("Bitter"),
    __("Cunning"),
    __("Educated"),
    __("Frustrated"),
    __("Hate-filled"),
    __("Manipulative"),
    __("Persuasive"),
    __("Protester"),
    __("Wrong Track")
    ]
define LiTsoShihLog = [
    ]

default LS_impression = None