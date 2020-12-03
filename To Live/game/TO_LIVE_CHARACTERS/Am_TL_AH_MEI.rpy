python:

    import TL_defines_character
init 10:
    default Am = Char( 
        mood ="Agitated",
        bond = 0,
        pol = GetMax(AmPol),
        rel = GetMax(AmBelief),
        traits = None,
        skillset = None,
        convolog = AhMeiConvo,
        eventlog = AhMeiLog
        )

default AmPol = {
    'Fascism':3,
    'Communism':-2,
    'Centrism':1,
    'Anarchism':-4,
    'Conservatism':0,
    'Corporatism':0,
    'Liberalism':0,
    'Libertarianism':0,
    'Moralism':1,
    'Nationalism':4,
    'Progressivism':0
}
default AmBelief = {
    'Atheism':-1,
    'Buddhism':4,
    'Christianity':0,
    'Communism':-2,
    'Islam':0,
    'Shamanism':1,
    'Shintoism':0,
    'Taoism':1,
    'Yiguandao':-1
}
define AhMeiConvo = [
    ]
define AhMeiLog = set(
    )


default Am_impression = None