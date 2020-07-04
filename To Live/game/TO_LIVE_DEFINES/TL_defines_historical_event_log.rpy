init python:
    class historydict(object):
        def __init__(self, container):
            self.container = container

        def addevent(self, event):
            if event not in self.container:
                if event in historical_event_log:
                    self.container.append(event)
                    msg.msg("New Event in Historical Event Log: "+event)
                else:
                    raise Exception("Mispelt or non-existent event being logged.")
            else:
                msg.msg(event+" is a logged Historical Event")
        def addhome(self, home):
            self.container.append(home)

default TL_history_log = historydict(
    container = persistent.unlocked_history
    )
#Historical Events log
define persistent.unlocked_history = [] #Empty hitorical log
define persistent.history_home_unlocked = True
init -1 python:
    event_display_desc = ""
    historical_event_log = \
    {'home':'This is the history log.',
    'Marco-Polo Incident': '{size=+20}{a=https://en.wikipedia.org/wiki/Marco_Polo_Bridge_Incident}Marco-Polo Incident{/a}{/size}\nThe Marco Polo Bridge Incident, also known by Lugou Bridge Incident or Double-Seven Incident, was a July 1937 battle between China\'s National Revolutionary Army and the Imperial Japanese Army. It is widely considered to have been the start of the Second Sino-Japanese War.\n The Japanese had crossed the border to conduct military exercises and shots were exchanged between the two sides. Despite a ceasefire being declared the Chinese communist assaults faced by the Japanese commanders lead to orders to continue.'}    