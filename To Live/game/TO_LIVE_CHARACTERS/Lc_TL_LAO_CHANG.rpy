python:

    import TL_defines_character

default Lc = Char( 
    mood ="Pondering",
    bond = 2,
    pol = None,
    rel = None,
    traits = LaoChang_traits,
    skillset = None,
    convolog = LaoChangConvo,
    eventlog = LaoChangLog
    )
define LaoChang_traits = [
    __("Content"),
    __("Illiterate"),
    __("Patient"),
    __("Rational"),
    __("Stubborn"),
    __("Uneducated"),
    __("Wise"),
    __("Well-Informed"),
    __("Workaholic")
    ]
define LaoChangSkills = [
    ]
define LaoChangConvo = [
    ]
define LaoChangLog = set(
    )

