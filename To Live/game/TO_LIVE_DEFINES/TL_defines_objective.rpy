
init python:
    class Objective(object):
        def __init__(self, name, subtext):
            self.name  = name
            self.subtext = subtext

        def set_obj(self, name):
            SetVariable(self.name, name)

        def set_sub(self, subtext):
            SetVariable(self.subtext, subtext)