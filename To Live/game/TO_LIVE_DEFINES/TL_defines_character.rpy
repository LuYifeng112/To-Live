# TODO
# Add a Random Check Modifier Ability.
define npercentage = 0
define nskill = 0
default void = __("Anti-Humonculus")
 
 ######  ##     ##    ###    ########     ###     ######  ######## ######## ########   ######
##    ## ##     ##   ## ##   ##     ##   ## ##   ##    ##    ##    ##       ##     ## ##    ##
##       ##     ##  ##   ##  ##     ##  ##   ##  ##          ##    ##       ##     ## ##
##       ######### ##     ## ########  ##     ## ##          ##    ######   ########   ######
##       ##     ## ######### ##   ##   ######### ##          ##    ##       ##   ##         ##
##    ## ##     ## ##     ## ##    ##  ##     ## ##    ##    ##    ##       ##    ##  ##    ##
 ######  ##     ## ##     ## ##     ## ##     ##  ######     ##    ######## ##     ##  ######
#Protagonist
define character.fang = Character(__("Fang Jie"), image="fang", who_color="#3154b5", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="fang")
define character.authority = Character(__("Authority"), image="authority", what_italic=True, who_color="#3154b5", ctc="ctc_blink", ctc_position="nestled")
define character.composure = Character(__("Focus"), image="composure", what_italic=True, who_color="#3154b5", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="fang")
define character.concept = Character(__("Abstraction Compeherension"), image="concept", what_italic=True, who_color="#3154b5", ctc="ctc_blink", ctc_position="nestled")
define character.empathy = Character(__("Empathy"), image="empathy", what_italic=True, who_color="#3154b5", ctc="ctc_blink", ctc_position="nestled")
define character.logic = Character(__("Logic"), image="logic", who_font="fonts/eng_chars/visualcomprehension/Cinzel-Regular.ttf", who_kerning=-1, what_font="fonts/chi_pinyin/Alegreya-Regular.ttf", what_color="#000000", what_italic=True, who_color="#000000", ctc="ctc_blink", ctc_position="nestled")
define character.luck = Character(__("Luck"), image="luck", what_italic=True, who_color="#3154b5", ctc="ctc_blink", ctc_position="nestled")
define character.perception = Character(__("Sensory Perception"), image="perception", what_italic=True, who_color="#3154b5", ctc="ctc_blink", ctc_position="nestled")
define character.pred = Character(__("Predatory Instinct"), image="pred", what_italic=True, who_color="#3154b5", ctc="ctc_blink", ctc_position="nestled", show_always_effect = always_shake(x = 1, y = 1))
define character.rhetoric = Character(__("Rhetorics"), image="rhetoric", what_italic=True, who_color="#3154b5", ctc="ctc_blink", ctc_position="nestled")
define character.judgement = Character(__("Judgement"), image="correction", who_font="fonts/eng_chars/correction/KelmscottRomanNF.ttf", what_font="fonts/chi_pinyin/Alegreya-Regular.ttf", what_italic=True, who_color="#000000", what_color="#000000", ctc="ctc_blink", ctc_position="nestled")
define character.schema = Character(__("Schema"), image="schema", what_italic=True, who_color="#3154b5", ctc="ctc_blink", ctc_position="nestled", show_slow_effect = slow_nonsense, show_slow_effect_delay = 1.0)
define character.reaction = Character(__("Quick Wit"), image="reaction", what_italic=True, who_color="#3154b5", ctc="ctc_blink", ctc_position="nestled")
define character.vice = Character(__("Vice"), image="vice", who_font="fonts/eng_chars/vice/dispose/DISPOSE1.ttf", what_font="fonts/eng_chars/vice/Eutemia.ttf", what_size=50, what_color="#000000", what_italic=True, who_color="#000000", ctc="ctc_blink", ctc_position="nestled", show_always_effect = always_shake(x = 1, y = 1))
define character.visualcomprehension = Character(__("Visual Comprehension"), image="visualcomprehension", what_italic=True, who_font="fonts/eng_chars/visualcomprehension/Cinzel-Regular.ttf", what_font="fonts/eng_chars/visualcomprehension/Caladea-Italic.ttf", what_color="#000000",  who_color="#000000", ctc="ctc_blink", ctc_position="nestled")
define character.void = Character("[void]", ctc="ctc_blink", ctc_position="nestled")

define character.narrator = Character(ctc="ctc_blink", ctc_position="nestled")
init 9999:
    define na = Character(None, show_slow_effect = slow_nonsense, show_slow_effect_delay = 1.0, kind=centered)
    define no = Character(None, show_always_effect = always_shake(x = 1, y = 1), kind=centered, show_layer='master')
#MISC
define character.un = Character("???",what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
#1937
define character.Ab = Character(__("Ah Bai"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ab")
define character.Am = Character(__("Ah Mei"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Am")
define character.Ch = Character(__("Corporal Hu"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
define character.Dy = Character(__("Da-Yu"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Dy")
define character.Ghe = Character(__("Guo He"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ghe")
define character.Gh = Character(__("Guo Heng"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="gh")
define character.Ku = Character(__("Ku Hong-Meng"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Gu")
define character.Lc = Character(__("Lao Chang"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Lc")
define character.Li = Character(__("Li-Li"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Li")
define character.Ls = Character(__("Li Tso-Shih"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ls")
define character.Ly = Character(__("Lady Yang"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Ly")
define character.monk = Character(__("Monk"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="monk")
define character.Mw = Character(__("Ma Wen"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Mw")
define character.Po = Character(__("Professor Po Yeutarng"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Po")
define character.Ts = Character(__("Liutenant Tsai"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
define character.wpc = Character(__("Wang P'u Ch'en"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="wpc")
define character.wyx = Character(__("Wang Yue Hsiang"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
define character.Xw = Character(__("Xiao Wen"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Xw")
define character.Xwe = Character(__("Xiao Wei"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="Xwe")

#1937 Japanese
define ai = Character(__("Yumi"), what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled", voice_tag="ai")

init python:
    import renpy.store as store
    from collections import Counter
    def WeightedChoice(choices):
        """ 
        @param choices: A list of (choice, weight) tuples. Returns a random
        choice (using renpy.random as the random number generator)
        """
        totalweight = 0.0
        for choice, weight in choices:
            totalweight += weight
        randval = renpy.random.random() * totalweight
        for choice, weight in choices:
            if randval <= weight:
                return choice
            else:
                randval -= weight

    class Char(store.object):  
        hometown=None    
        def __init__(self, mood, bond, pol, rel, traits, skillset, convolog, eventlog, bag=None):
            self.mood = mood
            self.bond = bond
            self.pol = pol
            self.rel = rel
            self.traits = traits
            self.skillset = skillset 
            self.convolog = convolog
            self.eventlog = eventlog
            self.bag = bag

        def setmood(self, moodname, responsibility=True):
            self.mood = moodname
            IsResponsible[self.mood] = responsibility

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

        def updateSkill(self, skill, val, msge=True):
            if skill in self.skillset:
                self.skillset[skill] += val
                devlog.info(str(skill)+" increased by:"+str(val)+" to: "+str(self.skillset[skill]))
                if msge==True:
                    if val == 1:
                        msg.msg(SkillsetDictionary[str(skill)]+" increased by 1 point to level "+str(self.skillset[skill]))
                    else:
                        msg.msg(SkillsetDictionary[str(skill)]+" increased by "+str(val)+" points to level "+str(self.skillset[skill]))
            else:
                raise Exception("Invalid Skill Key or Invalid Skill in Character Skillset for function \'updateSkill()\'.")
    
        def skillval(self, skill):
            if skill in self.skillset:
                return self.skillset.get(skill)
            else:
                raise Exception("Invalid Skill Key for function \'skillval()\'.")
        def convo(self, topic, event=False):
            devlog.info("New conversation: "+str(topic))
            self.convolog.append(topic)
            if event == True:
                self.eventlog.add(topic)

        def said(self, phrase):
            devlog.info("Checked for "+str(phrase)+" in conversation.")
            return phrase in self.convolog

        def forget(self, phrase):
            try:
                self.convolog.remove(phrase)
                devlog.info(phrase+" has been forotten.")
            except:
                devlog.info("forgetting "+phrase+" has been excepted.")

        def clearconvo(self):
            devlog.info("Conversation has been cleared.")
            self.convolog.clear()
        
        def log(self, event):
            self.eventlog.add(event)

        def hasLog(self, event):
            if event in self.eventlog:
                return True
            else:
                return False

        def RandomCheck(self, skill, x, y, sound=True, vol=0.35, msge=True):
            if skill in self.skillset.keys():
                global temp_val
                temp_val = self.skillset[skill] + self.skillset["luck"]
                opposition = renpy.random.randint(x, y)
                test = WeightedChoice([("Success", temp_val),
                                ("Failure", opposition)])
                if test == "Success":
                    if sound == True:
                        renpy.music.set_volume(vol, delay=0, channel='skills') 
                        renpy.play("sounds/menu/00_checksuccess.ogg", channel="skills")
                    if msge == True:
                        msg.msg(SkillsetDictionary[skill]+" challenge success.")
                    devlog.info(str(skill)+" success in the difficulty of "+str(x)+"-"+str(y))
                    return True

                elif test == "Failure":
                    if sound == True:
                        renpy.music.set_volume(vol, delay=0, channel='skills') 
                        renpy.play("sounds/menu/00_checkfail.ogg", channel="skills")
                    if msge == True:
                        msg.msg(SkillsetDictionary[skill]+" challenge failed.")
                    devlog.info(SkillsetDictionary[skill]+" failure in the difficulty of "+str(x)+"-"+str(y))
                    return False
            else:
                raise Exception("Invalid Skill Key for function RandomCheck.")

init python:
    def GetMax(d):
        r = max(d.values())
        key = [k for k,v in d.items() if v == r]
        if len(key) == 2:
            sentence = " and ".join(key)
        else:
            sentence = " ,".join(key)
        foo = len(key)
        if foo == 1:
            return max(d, key=lambda key: d[key])
        else:
            return "Mixed views"+" ("+sentence+")"
 ######   ########     ###    ########  ##     ## ####  ######   ######  
##    ##  ##     ##   ## ##   ##     ## ##     ##  ##  ##    ## ##    ## 
##        ##     ##  ##   ##  ##     ## ##     ##  ##  ##       ##       
##   #### ########  ##     ## ########  #########  ##  ##        ######  
##    ##  ##   ##   ######### ##        ##     ##  ##  ##             ## 
##    ##  ##    ##  ##     ## ##        ##     ##  ##  ##    ## ##    ## 
 ######   ##     ## ##     ## ##        ##     ## ####  ######   ######  
'''
The side images for each character.
'''
transform change_transform(old, new):
    contains:
        old
        yalign 1.0
        xpos 0.0 xanchor 0.0
        linear 0.2 xanchor 1.0
    contains:
        new
        yalign 1.0
        xpos 0.0 xanchor 1.0
        linear 0.2 xanchor 0.0

define config.side_image_change_transform = change_transform
style default:
    antialias True
image side vice neutral:
    "images/00_character_side_images/character.vice/vice_neutral.png"
    size(300, 300)
    zoom 1.1
image side correction neutral:
    "images/00_character_side_images/character.correction/correction_neutral.png"
    size(300, 300)
    zoom 1.1
image side visualcomprehension neutral:
    "images/00_character_side_images/character.visualcomphrehension/visualcomprehension_neutral.png"
    size(300, 300)
    zoom 1.1
image side logic neutral:
    "images/00_character_side_images/character.logic/logic_neutral.png"
    size(300, 300)
    zoom 1.1
image side rhetoric neutral:
    "images/00_character_side_images/character.rhetoric/rhetoric_neutral.png"
    size(300, 300)
    zoom 1.1
image side perception neutral:
    "images/00_character_side_images/character.perception/perception_neutral.png"
    size(300, 300)
    zoom 1.1
image side empathy neutral:
    "images/00_character_side_images/character.empathy/empathy_neutral.png"
    size(300,300)
    zoom 1.1
image side pred neutral:
    "images/00_character_side_images/character.pred/pred_neutral.png"
    size(300,300)
    zoom 1.1
image side schema neutral:
    "images/00_character_side_images/character.schema/schema_neutral.png"
    size(300,300)
    zoom 1.1
image side reaction neutral:
    "images/00_character_side_images/character.reaction/reaction_neutral.png"
    size(300,300)
    zoom 1.1
image authoritycheck:
    ConditionSwitch(
        "fang.pol == None", "images/00_character_side_images/character.authority/authority_neutral.png",
        "fang.pol == 'KMT' ", "images/00_character_side_images/character.authority/authority_neutral.png",
        "fang.pol == 'PRC' ", "images/00_character_side_images/character.authority/authority_neutral_com.png")
image side authority neutral:
    'authoritycheck'
    size(300,300)
    zoom 1.1
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

### Interactive SkillSet

# Authority
# Composure
# Coneptualisation
# Empathy
# Schema
# Logic
# Luck
# Rhetoric
# Judgement
# Vice
# Visual-Comprehension

### Default skill set

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
