init python:
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
        
        def hasTrait(self, trait):
            return trait in self.traits
        
        def addTrait(self, trait):
            self.traits.append(trait)
        
        def log(self, event):
            self.eventlog.append(event)
        
        def hasLog(self, event):
            return event in self.eventlog
        
        def chardead(self):
            self.mood = None
            self.traits = None


