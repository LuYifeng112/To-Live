python:

    import TL_defines_character

default Ghe = Char( 
    mood ="Neutral",
    bond = 0,
    pol = None,
    rel = "Christianity",
    traits = GuoHe_traits,
    skillset = GuoHeSkills,
    convolog = GuoHeConvo,
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
    __("Playful"),
    __("Prayful")
    ]
define GuoHeSkills = dict(

    )
define GuoHeConvo = [
    ]
define GuoHeLog = set(
    )

default GHe_impression = None