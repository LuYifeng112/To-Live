init python:
    class chaos(object):
        def __init__(self, name, value, death, IsActive):
            self.name = name
            self.value = value
            self.death = death
            self.IsActive = IsActive
    class Char(object):
        def __init__(self, mood, bond, pol, rel, traits, eventlog):
            self.mood = mood
            self.bond = bond
            self.pol = pol
            self.rel = rel
            self.traits = traits
            self.eventlog = eventlog
        def bondp(self, amount):
                self.bond += amount
        def large_dec(self):
            temp_val = renpy.random.randint(4,7)
            self.bond -= temp_val
            msg.msg("Relationship decreased by [temp_val] points.")
        def med_dec(self):
            temp_val = renpy.random.randint(2,5)
            self.bond -= temp_val
        def low_dec(self):
            temp_val = renpy.random.randint(1,3)
            self.bond -= temp_val
        def chardead(self):
            self.mood = None
            self.traits = None

