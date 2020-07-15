python:

    import TL_defines_character

default ai = Char( 
    mood ="Neutral",
    bond = 0,
    pol = "Empire of Japan",
    rel = "Shintoism",
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
    __("Rational"),
    __("Sensitive"),
    __("Soft-Hearted"),
    __("Well Educated")
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
define YumiKawashimaConvo = [
    ]
define YumiKawashimaLog = [
    ]


default AI_impression = None