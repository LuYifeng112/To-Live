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
        determination=5,
        dexterity=3,
        equipload=10,
        faith=4,
        influence=0,
        intelligence=10,
        lockpicking=0,
        luck=4,
        rhetoric=4,
        strength=4,
        stress=0,           #special skill
        vigor = 0
    )
define FangJieConvo = [
    ]
define FangJieLog = [
    ]

#health
default currenthp = 50
default maxhp = 50
default money_loc = _("Fabi")

default Fang_from_Beijing = False
default Fang_from_Nanjing = False
default Fang_from_Guangzhou = False
default Fang_from_hong_kong = False
default Fang_from_Macau = False
default Fang_from_Taiwan = False

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