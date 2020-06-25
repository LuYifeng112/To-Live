python:

    import TL_defines_character

default Ls = Char( 
    mood ="Angry",
    bond = -10,
    pol = "Anti-KMT",
    rel = None,
    traits = LiTsoShih_traits,
    skillset = LiTsoShihSkills,
    eventlog = LiTsoShihLog
    )
define LiTsoShih_traits = [
    __("Angry"),
    __("Anti-Traditionalist"),
    __("Bitter"),
    __("Cunning"),
    __("Educated"),
    __("Frustrated"),
    __("Hate-filled"),
    __("Manipulative"),
    __("Persuasive"),
    __("Protester"),
    __("Wrong-Track")
    ]
define LiTsoShihSkills = dict(
    determination=9,
    dexterity=4,
    equipload=0,
    faith=0,
    forgery=7,           #Special Skill
    hatred=9,            #Special Skill
    improvised_combat=7, #Special Skill
    influence=0,
    intelligence=12,
    lockpicking=4,
    luck=3,
    rhetoric=6,
    strength=4,
    vigor = 3
    )
define LiTsoShihLog = [
    ]

default LS_impression = None