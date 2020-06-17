python:

    import TL_defines_character

default Ghe = Char( 
    mood ="Neutral",
    bond = 0,
    pol = None,
    rel = "Christianity",
    traits = GuoHe_traits,
    eventlog = GuoHeLog
    )
define GuoHe_traits = [
    __("Cowardly"),
    __("Doubtful"),
    __("Emotional"),
    __("Gullible"),
    __("Indecisive"),
    __("Immature"),
    __("Naive"),
    __("Prayful")
    ]

define GuoHeLog = [
    ]

default GHe_impression = None