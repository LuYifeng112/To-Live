init python:
    class chapter(object):
        def __init__(self, name, number, specialactions):
            self.name = name
            self.number = number
            self.specialactions = specialactions
    class Char(object):      
        def __init__(self, mood, bond, pol, rel, traits, skillset, convolog, eventlog):
            self.mood = mood
            self.bond = bond
            self.pol = pol
            self.rel = rel
            self.traits = traits
            self.skillset = skillset
            self.convolog = convolog
            self.eventlog = eventlog
        
        def bondp(self, amount):
            self.bond += amount
        
        def hasTrait(self, trait):
            return trait in self.traits
        
        def addTrait(self, trait):
            self.traits.append(trait)

        def removeTrait(self, trait):
            if trait in self.traits:
                self.traits.remove(trait)
            else:
                raise Exception("Invalid Trait Key in \'removeTrait()\' function.")

        def addSkill(self, skill, val):
            self.skillset.update(skill=val)

        def updateSkill(self, skill, val):
            if skill in self.skillset:
                self.skillset[skill] += val
            else:
                raise Exception("Invalid Skill Key or Invalid Skill in Character Skillset for function \'updateSkill()\'.")
    
        def skillval(self, skill):
            if skill in self.skillset:
                return self.skillset.get(skill)
            else:
                raise Exception("Invalid Skill Key for function \'skillval()\'.")

        def convo(self, topic):
            self.convolog.append(topic)

        def said(self, phrase):
            return phrase in self.convolog

        def clearconvo(self):
            self.convolog.clear()

        def log(self, event):
            self.eventlog.append(event)
        
        def hasLog(self, event):
            return event in self.eventlog
        
        def chardead(self):
            self.mood = None
            self.traits = None


######## ########     ###    #### ########  ######     ########  ####  ######  ######## 
   ##    ##     ##   ## ##    ##     ##    ##    ##    ##     ##  ##  ##    ##    ##    
   ##    ##     ##  ##   ##   ##     ##    ##          ##     ##  ##  ##          ##    
   ##    ########  ##     ##  ##     ##     ######     ##     ##  ##  ##          ##    
   ##    ##   ##   #########  ##     ##          ##    ##     ##  ##  ##          ##    
   ##    ##    ##  ##     ##  ##     ##    ##    ##    ##     ##  ##  ##    ##    ##    
   ##    ##     ## ##     ## ####    ##     ######     ########  ####  ######     ##    
'''
Traits are how characters have behaviours that will influence how they interact with other NPCs and the protagonist.
Traits change through events and help characters develop.
Below each trait is listed alphabetically and with their ingame use/effect.
'''
# Angry                             -Hostile conversations
# Anti-Traditionalist               -Dislikes KMT aligned NPC or confucianists, typically communist people.
# Bitter                            -Holds things against people
# Calm                              -Avoids lashing out.
# Content                           -Neutral effect
# Cowardly                          -Will break down if pushed into a dangerous situation. Likes to run away.
# Cunning                           -Sees people as pawns to a goal. Manipulative and lies alot.
# Determined                        -Doesn't give up on ambition. A goal is a goal.
# Devoted                           -Deifies their goals. Mostly for rationally religious people.
# Doubtful                          -Will question NPCs pessimestically.
# Educated                          -Has good rhetoric.
# Emotional                         -Will not always understand rationally.
# Frustrated                        -Avoids people, can't get things done well.
# Gullible                          -Will trust the wrong people. Get NPCs in trouble.
# Hate-Filled                       -Violent, barbaric and will refuse to understand. Revenge based characters.
# Idealistic                        -People with good ideas, not so good execution.
# Illiterate                        -Can only be informed by ear giving written work will not communicate.
# Immature                          -kids or manchilren that don't realize the situation.
# Impulsive                         -if rational - fast decision maker, otherwise these people are just emotionally attached.
# Indecisive                        -they will make someone else make a choice rather than themself.
# Insecure                          -Often psychologically vunerable. Mostly for low esteem type characters.
# Manipulative                      -On par with cunning but not for a goal. Often these people are just self centered and control freaks.
# Naive                             -Similar to gullible, these are for adults and these people typically just are not used to being harsh.
# Non-Violent                       -Similar to pacifist, this one means someone that doesn't use violence in their goals and doesn't stop violence around them.
# Overprotective                    -Someone that guards people close to them. Sacrificial like a saint.
# Pacifist                          -Similar to non-violent this one means that someoe that enforces peace and refuse to use violence or kill.
# Patient                           -Someone that can stand not being communicated to.
# Persuasive                        -This person is good at convincing their cause.
# Playful                           -Someone that needs to recharge their batteries to work best.
# Prayful                           -Someone that needs time to pray and do service to work best.
# Protester                         -Somone that challenges authority.
# rational                          -Thinking logically.
# Reassuring                        -Emotionally supportive
# Rebellious                        -Will have acts of aggression
# Religious                         -Will take offense to heretical talk unless they're rational.
# Righteous                         -Will never stand for injutice. Loses respect for people that commit injustice.
# Self-Controlled                   -Neutral character
# Self-Hating                       -Low self esteem
# Self-Righteous                    -Extreme ideology belief in a quest for justice.
# Sensitive                         -Takes offense easily.
# Servile                           -Will work hard and get things accomplished. Loyal as well.
# Short-Tempered                    -Lets their anger get in the way of their owj progress.
# Stable                            -neutralises the character
# Stingy                            -Hates spending money.
# Stressed                          -Prone to breakdown if stress buildsup.
# Stubborn                          -Will be difficult to convince them to do anything.
# Soft-Hearted                      -Will be overly merciful.
# Suppressed                        -Hateful towarda authority and high influence people.
# Traditional                       -Rejects progressive beliefs.
# Uneducated                        -Has skills outside of academia.                       
# Well Educated                     -Leadership potential
# Well-Informed                     -Up to date with information and communication. 
# Wise                              -Parents a group of people.
# Workaholic                        -Unhealthily dedicated to work even if ineffecient.
# Worrier                           -Focusses on pessimistic remarks
# Wrong-Track                       -Negative Influence
'''
NOTE:
An AI system off of this is yet to be perfected.
I would like to automate learning of player choice habits so that these traits interact with each other automaticlaly and flexibly.
'''

 ######  ##    ## #### ##       ##        ######  ######## ######## 
##    ## ##   ##   ##  ##       ##       ##    ## ##          ##    
##       ##  ##    ##  ##       ##       ##       ##          ##    
 ######  #####     ##  ##       ##        ######  ######      ##    
      ## ##  ##    ##  ##       ##             ## ##          ##    
##    ## ##   ##   ##  ##       ##       ##    ## ##          ##    
 ######  ##    ## #### ######## ########  ######  ########    ##    

###default skill set

# determination
# dexterity
# equipload
# faith
# influence
# intelligence
# lockpicking
# luck
# rhetoric
# strength
# vigor

###Special skills
'''
These are skills that apply to specific characters. Sometimes more than one. 
'''
# cooperativness
# disguise
# forgery
# hatred
# improvised_combat