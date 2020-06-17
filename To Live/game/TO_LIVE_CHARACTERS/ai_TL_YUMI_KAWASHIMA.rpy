python:

    import TL_defines_character

default ai = Char( 
    mood ="Neutral",
    bond = 0,
    pol = "Empire of Japan",
    rel = "Shintoism",
    traits = YumiKawashima_traits,
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
    __("Softed-Hearted"),
    __("Well Educated")
  ]
define YumiKawashimaLog = [
    ]

default AI_impression = None