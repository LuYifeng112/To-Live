python:

    import TL_defines_character

default fang = Char( 
    mood ="Anxious",
    bond = 0,
    pol = None,
    rel = None,
    traits = FangJie_traits,
    skillset = FangJieSkills,
    convolog = FangJieConvo,
    eventlog = FangJieLog
    )
define FangJie_traits = [
   __("Well-Informed"),
   __("Protester"),
   __("Righteous"),
   __("Impulsive"), 
   __("sensitive")
   ]
define FangJieSkills = dict(
        authority=0,
        composure=2,
        conceptualization=2,
        determination=5,
        dexterity=3,
        empathy=4,
        encyclopedia=6,
        equipload=10,
        faith=4,
        focus=2,
        influence=0,
        lockpicking=0,
        logic=4,
        luck=3,
        psychethreshhold=2,
        rhetoric=4,
        reaction=3,
        strength=4,
        stress=0,           #special skill
        vice=1,
        vigor=0,
        visualcomprehension=3
    )
define FangJieConvo = [
    ]
define FangJieLog = [
    ]

#health
default currenthp = 50
default maxhp = 50
default money_loc = _("Fabi")

#Religion
define Taoist = False
define Buddhist = False
define Christian = False
define Yiguandao = False
define religions = [ __("Taoism"), __("Buddhism"), __("Christian"), __("Yiguandao"), __("Islam"), __("Shintoism"), __("Communism")]
#character
define is_student = False
define is_apprentice = False
define is_worker = False
define is_free = False
define angst = renpy.random.randint(1,100)
define saucy_thoughts = renpy.random.randint(1,100)