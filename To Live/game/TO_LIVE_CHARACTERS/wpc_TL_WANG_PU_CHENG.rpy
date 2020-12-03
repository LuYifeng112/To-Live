python:

    import TL_defines_character
init 10:
    default wpc = Char( 
        mood ="Frustrated",
        bond = 0,
        pol = GetMax(wpcPol),
        rel =  GetMax(wpcRel),
        traits = None,
        skillset = None,
        convolog = wpcConvo,
        eventlog = wpcLog
        )
define wpcConvo = [
    ]
define wpcLog = set(
    )

default wpcPol = {
    'fascism':-1,
    'communism':-2,
    'centrism':3,
    'anarchism':-1,
    'conservatism':2,
    'corporatism':0,
    'liberalism':0,
    'libertarianism':0,
    'moralism':5,
    'nationalism':1,
    'progressivism':1
}
default wpcRel = {
    'atheism':-1,
    'buddhism':1,
    'christian':-1,
    'communism':-2,
    'islam':0,
    'shintoism':0,
    'taoism':1,
    'yiguandao':0
}
default wpc_impression = None