
init python:
    class Target(object):
        def __init__(self, name, occupation, leadership, desc, portrait):
            self.name = name
            self.occupation = occupation
            self.leadership = leadership
            self.desc = desc
            self.portrait = portrait
    TL_One = []
    TL_target_append = 0
    while TL_target_append < 200:
        TL_One.append(Target("","","","",""))
        #TL_faction.append(faction("", True, False))
        TL_target_append += 1
    TL_One[0] = Target("Masafumi Aruga", "District Commander", "Imperial Army of Japan", "", "")