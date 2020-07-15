python:

    import TL_defines_character

default Gu = Char( 
    mood ="Thoughtful",
    bond = 7,
    pol = None,
    rel = "Taoism",
    traits = Ku_HongMeng_traits,
    skillset = None,
    convolog = KuHongMengConvo,
    eventlog = KuHongMengLog
    )
define Ku_HongMeng_traits = [
    __("Calm"),
    __("Stable"),
    __("Reassuring"),
    __("Idealistic"),
    __("Stingy"),
    __("Wise"),
    __("Traditional")
    ]
define KuHongMengSkills = dict(

    )
define KuHongMengConvo = [
    ]
define KuHongMengLog = [
    ]