python:
    import TL_defines_character
    import TL_defines_inventory
init 10:
    default fang = Char( 
        mood =__("Anxious"),
        bond = 0,
        pol = GetMax(FangPol),
        rel = GetMax(FangRel),
        traits = FangJie_traits,
        skillset = FangJieSkills,
        convolog = FangJieConvo,
        eventlog = FangJieLog,
        bag = fangbag
        )
default FangPol = {
    'fascism':0,
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
default FangRel = {
    'atheism':0,
    'buddhism':0,
    'christian':0,
    'communism':-2,
    'islam':0,
    'shintoism':0,
    'taoism':0,
    'yiguandao':0
}
define FangJie_traits = [
    __("Confident"),
   __("Well-Informed"),
   __("Protester"),
   __("Righteous"),
   __("Impulsive"),
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
        schema=6,
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

define religions = [ __("Taoism"), __("Buddhism"), __("Christian"), __("Yiguandao"), __("Islam"), __("Shintoism"), __("Communism")]
#character
default mc_name = "Fang Jie"