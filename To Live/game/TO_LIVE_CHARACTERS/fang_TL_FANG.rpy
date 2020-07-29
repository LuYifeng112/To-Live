python:
    import TL_defines_character
    import TL_defines_inventory
default fang = Char( 
    mood =__("Anxious"),
    bond = 0,
    pol = None,
    rel = None,
    traits = FangJie_traits,
    skillset = FangJieSkills,
    convolog = FangJieConvo,
    eventlog = FangJieLog,
    bag = fangbag
    )
define FangPol = {
    'fascism':1,
    'communism':0,
    'centrism':0,
    'anarchism':0,
    'conservatism':0,
    'corporatism':0,
    'liberalism':0,
    'libertarianism':0,
    'moralism':0,
    'nationalism':0,
    'progressivism':0
}
define FangJie_traits = [
    __("Confident"),
   __("Well-Informed"),
   __("Protester"),
   __("Righteous"),
   __("Impulsive"), 
   __("Sensitive"),
   __("Stressed"),
   __("Tolerant"),
   __("Well-Educated")
   ]
define FangJieSkills = dict(
        authority=0,
        composure=2,
        conceptualization=2,
        determination=5,
        dexterity=3,
        empathy=4,
        encyclopedia=6,
        endurance=2,
        faith=4,
        focus=2,
        influence=0,
        judgement=4,
        logic=4,
        luck=2,
        perception=2,
        predatoryinstinct=1,
        psychethreshhold=2,
        rhetoric=4,
        reaction=3,
        strength=4,
        vice=1,
        visualcomprehension=3
    )
define FangJieConvo = [
    ]
define FangJieLog = set(
    )

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