python:

    import TL_defines_character

default monk = Char( 
    mood ="Thoughtful",
    bond = 1,
    pol = None,
    rel = "Buddhism",
    traits = Monk_traits,
    skillset = None,
    convolog = None,
    eventlog = MonkLog
    )
define Monk_traits = [
    __("Content"),
    __("Devoted"),
    __("Patient"),
    __("Rational"),
    __("Servile"),
    __("Wise")
    ]
define Monkskills = [
    ]
define MonkLog = [
    ]


default monk_impression = None