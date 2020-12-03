python:

    import TL_defines_character
init 10:
    default Gh = Char( 
        mood ="Sonder",
        bond = 1,
        pol = GetMax(GhPol),
        rel = GetMax(GhRel),
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
default GhPol = {
    'fascism':-2,
    'communism':-1,
    'centrism':2,
    'anarchism':-1,
    'conservatism':1,
    'corporatism':0,
    'liberalism':0,
    'libertarianism':0,
    'moralism':2,
    'nationalism':1,
    'progressivism':0
}
default GhRel = {
    'atheism':2,
    'buddhism':1,
    'christian':0,
    'communism':-2,
    'islam':0,
    'shintoism':0,
    'taoism':0,
    'yiguandao':0
}
define GuoHengSkills = [
    ]
define GuoHengConvo = [
    ]
define GuoHengLog = set(
    )

default GH_impression = None

#Promises
define promise_Guo_heng_free_meal = False
define promise_teach_Gh_cantonese = False
define promise_Gh_talk_escape = False
define promise_GH_beer = False