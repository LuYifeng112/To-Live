python:

    import TL_defines_character

default Gh = Char( 
    mood ="Sonder",
    bond = 1,
    pol = None,
    rel = None,
    traits = GuoHeng_traits,
    skillset = GuoHengSkills,
    convolog = GuoHengConvo,
    eventlog = GuoHengLog
    )
define GuoHeng_traits = [
    __("Insecure"),
    __("Overprotective"),
    __("Stressed"),
    __("Sensitive"),
    __("Workaholic"),
    __("Worrier")
   ]
define GuoHengSkills = [
    ]
define GuoHengConvo = [
    ]
define GuoHengLog = [
    ]

default GH_impression = None

#Promises
define promise_Guo_heng_free_meal = False
define promise_teach_Gh_cantonese = False
define promise_Gh_talk_escape = False
define promise_GH_beer = False