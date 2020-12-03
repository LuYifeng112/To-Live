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
    $ devlog.info("CHAPTER_1_VOID: CHOICE GUIDANCE -ENDED")
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
    jump CHAPTER_1_HOUSE_ARREST

label CHAPTER_1_HOUSE_ARREST:
    #blink into scene two