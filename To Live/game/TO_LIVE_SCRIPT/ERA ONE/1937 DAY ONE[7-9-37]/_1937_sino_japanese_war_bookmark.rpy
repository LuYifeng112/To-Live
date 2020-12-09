label Prologue:
    # Video
    $ devlog.info("Prologue: Video")
    jump CHAPTER_1_VOID

label CHAPTER_1_VOID:
    $ devlog.info("CHAPTER_1_VOID_STARTED")
    void "Fang"
    "It whispered."
    "The voice was quiet yet ominous.{w=0.4} One that sent shivers down my spine."
    void "Fang{cps=*0.5}...{/cps}"
    void "The actions of one alone does curtail in big changes."
    void "More-so than you can realize due to a lack of foresight."
    # Beckon out hand
    "The coldness of the hand seemed to greedily absorb my heat."
    "It felt as if my body was cultivating stone out of flesh."
    "A painful paralysis and sense of powerlessness overcame me."
    "One that left me hungered and neglected."
    void "Let me guide you, Fang."
    "The entity formed a malignant smile and looked down towards me."
    "My body shuddered and gazed on through the strange plane of reality I was lying on."
    "{i}Somewhere between a rock and a hard place.{/i}"
    "A world where the sun doesn't shine."
    void "I wish to guide you in your {i}potentiality{/i} for action."
    void "A compatriot in your destiny."
    "I rubbed my head in agony and looked around the hollow landscape."
    "This dream came to beg the same question once more."
    "Expecting one of two answers."
    "Monotonously. Repeatedly."
    "What will I choose this time?"
    "Can I accept the guidance of this \"thing\"?"
    call CH_1_CHOICE_VOID_GUIDANCE
    $ devlog.info("CHAPTER_1_VOID: CHOICE GUIDANCE - ENDED")
    "A cloud of black mist engulfed the entity."
    "Part of me had felt my own essence, perhaps a reflection of self through the entity."
    "Yet however its animosity towards me was questionable."
    "If it was going to be \"challenged\" it needed to be subdued or eradicated from my mind."
    "In between the worlds encompassed in dreams, I lay there in the darkness."
    "A place that wasn't obsolete but more rather a demoralizing void of space and time."
    "Perhaps a limbo?{w=0.2} Just like a waiting place in the afterlife."
    "Everything was here at once."
    "Hopes, dreams, ambitions, weaknesses, failures...{w=0.2} - seemingly with nothing exempted."
    "The only illusion being that the darkness acted as a drape over this \"everything\"."
    "This sensation of \"everything\" was prevalent through my bones and flesh."
    "At this point this recurring dream had cultivated itself as a domestic opponent to my mind.{w=0.2} My sense of autonomy."
    "A harsh reality I was coerced to face."
    "On the other hand, like the countless times I encountered this perverse self reflective critique, I had to make up my mind and leave."
    fang "It's time to wake up now."
    $ devlog.info("CHAPTER_1_VOID ENDED")
    jump CHAPTER_1_HOUSE_ARREST_GREETING

label CHAPTER_1_HOUSE_ARREST_GREETING:
    #blink into scene two
    $ devlog.info("CHAPTER_1_HOUSE_ARREST STARTED")
    show LOCATION_Beijing with dissolve
    with Pause(2)
    scene black with dissolve
    with Pause(2)
    un "Are you awake, Fang?"
    show screen date
    show screen month
    show screen year
    show screen daytime
    if fang.RandomCheck("focus", 9, 12):
        $ fang.convo("Enstrengthened")
        "My eyes darted open as I scanned my surroundings."
        "The fatigue manifesting in my body had dissipated enigmatically along with the closeted dread of melancholia."
        "I turned my head to face Professor Po Yeutarng sitting on a seat opposite to me."
    else:
        "I felt a slight tugging at my shoulders, nudging me to wake up."
        "Despite that, my lethargy overpowered this as my tired body still exuded weakness while regulating my meager motivation."
        "Likewise, my eyes mutinied against my mind as they defiantly refused to open."
        "I pushed my knuckles close in my face and rubbed my eyes out like the kneading of dough."
        "The sensation of my thoughts darting around my head invaded my sensory perception temporarily and rooted itself in the way of my attention."
        "Perhaps the dream was a cruel projection of this fatigue and weakness feasting on my body."
        "I continue to rub my eyes until I can decode the mystery of the silhouette in front of me."
        "As my optics adjusted to the new lighting I finally was able to realize Professor Po Yeutarng sitting opposite me."
    #Eyes open to show Professor Po, sucking in a cigarette.
    "Professor Po is one of the few individuals that began to inhale tobacco."
    if fang.RandomCheck("schema", 6,9):
        schema neutral "This is a growing trend attributed mainly to increasing acidity in chewing tobacco."
        schema neutral "Foreign imports are popular amongst Kuomintang personnel."
    "Also considered a classy fellow by many."
    "But then again, anyone raised in Shanghai would end up that {i}classy{/i}."
    "Professor Po took the liberty of sitting down to initiate a conversation on the controversial issue at hand."
    Po "Good to see you, Fang."
    "I rubbed my eyes and looked around."
    "In the midst of waiting for Professor Po's arrival I had fallen asleep in an uncomfortable chair."
    Po "How was your sleep?"
    call CH_1_CHOICE_HOSUE_ARREST_SLEEP
    $ devlog.info("CHAPTER_1_HOUSE_ARREST: CHOICE SLEEP - ENDED")
    Po "I used to have awful dreams at your age."
    Po "I assume it can be attributed to \"growing up\"."
    if fang.RandomCheck("rhetoric", 2,4):
        rhetoric neutral "Puberty, perhaps?"
    Po "Yet, I guess dreams aren't meant to make sense anyway."
    Po "They're meant to simulate solutions to tangible problems using intangible means."
    Po "Do you understand what I am trying to say?"
    if fang.RandomCheck("rhetoric", 2,4):
        rhetoric neutral "This is a rhetorical question."
    else:
        fang "Sure."
        "Professor Po didn't acknowledge the response as he focused on his documentation."
        if fang.RandomCheck("reaction", 1,3):
            reaction neutral "That was meant to be a rhetorical question."
    if not fang.said("Enstrengthened"):
        Po "From your response you also seem to be quite weakened."
    Po "I hope you take car of yourself, Fang."
    "I flash a smile to Professor Po before speaking out."
    fang "Don't worry. I can handle a lot worse."
    "Professor Po smirked back and continued directing focus to his documents."
    "Meanwhile Uncle Ku gave a face of slight worry."
    "Considering this was occurring in his house, he considered it bad luck despite the {i}near perfect{/i} fengshui of the building."
    "He was a timid, superstitious man in fact,{w=0.2} yet egoistic and stingy."
    "Arguably best described as an amalgamation of traditionalism and conservatism."
    "There was many ways to describe him the more you knew him.{w=0.2} A strange statement to ever describe the person nonetheless."
    "Professor Po gripped the ink pen and looked at me head on."
    "There was a strange aura in the courtyard among the procedure of the interview."
    Po "Keep yourself strong, Fang."
    Po "A lot of things will get thrown in your way while growing up."
    Po "To be honest, for most people the biggest obstacle stems from inside you.{w=0.5} keep that in mind."
    $ devlog.info("CHAPTER_1_HOUSE_ARREST_GREETING ENDED")
    jump CHAPTER_1_HOUSE_ARREST_INTERVIEW

label CHAPTER_1_HOUSE_ARREST_INTERVIEW:
    $ devlog.info("CHAPTER_1_HOUSE_ARREST_INTERVIEW STARTED")
    Po "Do you know why you are here?"
    "Professor Po slightly tapped his finger on the weak thin documentation he was holding."
    if fang.RandomCheck("rhetoric", 2,5):
        rhetoric neutral "It seems he is trying to jog your memory."
        rhetoric neutral "Roll with it and contribute to the discussion."
    "Can I even remember at this rate?"
    "I dance my fingers against my temple as I ponder."
    if fang.RandomCheck("focus", 2,5):
        focus neutral "Why yes,{w=0.2} the controversy of the Peking university protests."
        fang "Yes, the Peking University protests sparked controversy.{w=0.2} I am here to see the results of my participation in it."
        Po "Correctly said.{w=0.2} Not results per say."
        Po "It's close, I can give you that.{w=0.2} Consider it more so as a consequence."
        if fang.RandomCheck("visualcomprehension", 3, 5):
            visualcomprehension neutral "Inside peripheral vision, Uncle Ku's face strained as if he had eaten a lemon."
    else:
        fang "I am not so sure."
        "Professor Po looked up briefly to observe me."
        if not fang.said("Enstrengthened"):
            Po "Is your health worsening?"
            Po "I really hope it isn't affecting your short term memory."
        else:
            "He emitted a sigh of disappointment mixed in with despair."
        "He winded his body down and rested his face on his knuckles for a second as he began to ponder deeply."
        # CG art
        if fang.RandomCheck("visualcomprehension",1,2):
            "A magnificent pose."
            "Like the resemblance of an inspirited artist."
            "Or perhaps the pinnacle of authoritarian beauty!{w} Voila!"
        Po "We're here to discuss the consequences of the university protests."
        "I ruffle through my hair as I reminisce of my situation and possible consequences."
        "{i}It feels pretty intense.{/i}"
        Po "Get some rest after this interview."
        Po "You seem a little \"over-troubled\"."
        Po "So I suggest you could use it."
        "I replied with a slight nod to Professor Po."
    Po "I take it that you attended some protests organized by students of Peking university."
    Po "These protests were of a contentious nature.{w=0.2} In the sense that they were criticizing the central government."
    Po "Several arrests we made by Kuomintang officers have been unpopular among students but more than necessary for order."
    Po "Per instruction of the administrative department I have to take your thumb print and some questions you'll be answering."
    "Uncle Ku was rubbing his hands in agitation as he failed to contain his stress."
    "By sight alone the clasping of his hands could crush a diamond."
    "It also manifested a sense of guilt in me.{w=0.2} Having to worry an old man like that."
    "Perhaps I was a little selfish."
    Po "Questions first. I will take your thumb print last."
    if fang.RandomCheck("logic", 3,5):
        logic neutral "The ink on the thumb would be harder to wash off if hit got time to dry."
    Po "Please inform me that the following details are correct."
    Po "Your name is Fang Jie.\n {w=0.2}Your date of birth is 11th June 1920.\n {w=0.2}Your current residence is with your guardian {i}Ku Hong-Meng{/i} in Peiping."
    fang "Yes, these are all correct."
    Po "Any extra details to add? Is there any special name that you go by that other people identify you with?"
    call CHAPTER_1_HOUSE_ARREST_NAME
    Po "Alight then,{w=0.2} As far as I am aware you also resided at a different address before you came into your Uncle's custodianship."
    Po "May you enlighten me as to where that was?"
    call CHAPTER_1_HOUSE_ARREST_RESIDENCE
label CHAPTER_1_HOUSE_ARREST_CONTINUED:
    Po "Goo to have that out of the way."