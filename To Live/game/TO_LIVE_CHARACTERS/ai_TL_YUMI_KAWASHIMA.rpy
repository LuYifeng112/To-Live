python:

    import TL_defines_character
init 10:
    default ai = Char( 
        mood ="Neutral",
        bond = 0,
        pol = GetMax(AiPol) ,
        rel = GetMax(AiBelief),
        traits = YumiKawashima_traits,
        skillset = YumiKawashimaSkills,
        convolog = YumiKawashimaConvo,
        eventlog = YumiKawashimaLog
        )
define YumiKawashima_traits = [
    __("Determined"),
    __("Doubtful"),
    __("Indecisive"),
    __("Impulsive"),
    __("Non-Violent"),
    __("Pacifist"),
    __("Persuasive"),
    __("Rational"),
    __("Sensitive"),
    __("Soft-Hearted"),
    __("Well Educated"),
    __("Wise"),
  ]
define YumiKawashimaSkills = dict(
        determination=3,
        cooperativeness=0, #Special Skill
        dexterity=1,
        disguise=0,        #Special Skill
        equipload=4,
        faith=6,
        influence=2,
        intelligence=11,
        lockpicking=0,
        luck=2,
        rhetoric=3,
        strength=2,
        vigor = 0
    )
default AiPol = {
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
default AiBelief = {
    'Atheism':-4,
    'Buddhism':1,
    'Christianity':0,
    'Communism':-6,
    'Islam':-3,
    'Shamanism':1,
    'Shintoism':8,
    'Taoism':0,
    'Yiguandao':0
}
define YumiKawashimaConvo = [
    ]
define YumiKawashimaLog = set(
    )


default AI_impression = None