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
    __("Disciplined"),
    __("Dreamer"),
    __("Overprotective"),
    __("Prudent"),
    __("Workaholic"),
    ]
default GhPol = {
    'fascism':-2,
    'communism':-7,
    'centrism':0,
    'anarchism':-5,
    'conservatism':3,
    'corporatism':1,
    'liberalism':0,
    'libertarianism':0,
    'moralism':4,
    'nationalism':4,
    'progressivism':1
}
default GhRel = {
    'atheism':5,
    'buddhism':0,
    'christian':0,
    'communism':-5,
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