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
    Po "Good to have that out of the way."
    Po "A hometown says a lot about a person, in-fact."
    "Professor Po taps his finger on the wooden arm rests of the chair."
    Po "I'm from Mukden myself, all the way back in Manchuria."
    if fang.RandomCheck("schema", 2,4):
        schema neutral "Behind enemy lines..."
    Po "I left a few years after the Japanese treatment got worse."
    Po "Which reminds me of a story..."
    random:
        block:
            "Professor Po rested his chin on his clasped hands and thought quietly."
            Po "One of my neighbors was a Manchu who worked as a traditional medic in the area."
            Po "Well the story goes that he gave some rice to some poor malnourished slave laborer to the Japanese."
            Po "News went around when he vomited the food back up and the Japanese caught him."
            Po "They accused the poor soul of \"economic treason\",{w=0.1} whatever that means."
            Po "They levied harsh punishment which pushed his body too far and he died as a result."
            Po "Subsequently his wife taking care of a 1 year old jumped into the river after learning of his death."
            Po "The pitiful medic was broken on hearing this news."
            Po "Who knew that food had a 300% mortality rate?"
            Po "An extreme case for sure.{w=0.1} The message behind it though is much more sinister."
        block:
            "Professor Po ruffled through his hair and sighed."
            Po "On second thought I shouldn't talk about it."
            Po "To summarize it, the Japanese were and {i}are{/i} barbaric through their Bushido codes."
        block:
            "Professor Po leaned back and folded his arms."
            Po "A story too depressing to talk about at the current moment."
            Po "However I will talk about the other parts that were wrecking the system."
            Po "Firstly, Aisin Gioro Pu-Yi the \"emperor\" of Manchukuo practically was a puppet emperor."
            Po "Everyone knew that the Japanese were in control and they slaved a lot of people for their demands."
            Po "Secondly, because of that banditry began to grow in the countryside against the Japanese."
            Po "Women would get raped, elderly were slaughtered and homes were ravaged in the countryside."
            Po "With that much chaos,{w=0.2} I moved to Peiping where I began to serve the central government."
    Po "I'm sure you must have some crazy story from your hometown.{w=0.2} But we got to finish these details."
    Po "A lot of political criminals we apprehend are easy to register because they were wealthy enough to have names and addresses and a record in the archives."
    Po "Most of them are students and we don't take them seriously unless they are engaged in communist activities."
    Po "Peking University seems to pool up with young idealists.{w=0.2} Which isn't strange, I guess, considering this is the home of the new culture movement."
    Po "And by extension the birth of political pluralism."
    Po "That's why Peking university doesn't surprise me when it organizes a protest."
    "Professor Po scratched his chin as he lightly pondered."
    Po "I'm assuming you're a smart lad for landing yourself in a prestigious institution."
    Po "I personally envy you to an extent."
    Po "The major reason for our draconian approach is your involvement with people of \"questionable characteristics\"."
    "Professor Po phrased this in a awkwardly offensive manner.{w=0.2} As to articulate a way of thinking he inherited in the administration."
    Po "These people have been detained in Tientsin with other more threatening \"radicals\"."
    Po "Your friend, {i}Shigeru Toshiyuki{/i} is detained with the others in Tientsin as well."
    Po "I'm sure you understand how his nationality vastly affected our decision to punish him like that compared to you."
    Po "I can't put this lightly, and I realize it will make me sound cruel but I will say it nonetheless."
    Po "We can't trust the Japanese. He might be planning something far more sinister or infiltrating impressionable students, etc."
    "Professor Po rubbed his hands together anxiously to expect my reply."
    if fang.RandomCheck("reaction",3 ,5):
        reaction neutral "Stay calm."
        reaction neutral "Anticipate yourself and correct yourself, accordingly."
    else:
        "I formed a slight frown instinctively which Professor Po quietly picked up on."
        Po "Sorry.{w=1} I'm just following orders."
    Po "Anyway, onto you now."
    Po "You can get thrown in the slammer for one night, or spend two nights on house arrest under supervision from me or my protege."
    "Professor Po turned to face Uncle Ku who had let his dignity drop to resort to begging."
    "A pitiful action which manifested guilt within me."
    Po "Your Uncle has opted for the latter.{w=0.5} I'm sure you would also."
    "Professor Po scanned his surroundings as a faint smile emerged from him."
    Po "In all honesty, I wouldn't mind living in this Siheyuan for two nights."
    "Uncle Ku landed his arm on my shoulder and proudly gripped it all the while beaming a optimistic smile."
    "Professor Po meanwhile leaned back and relaxed as he put himself at ease."
    Po "I guess that adjourns the interview."
    jump CHAPTER_1_HOUSE_ARREST_GH_CONTEXT
label CHAPTER_1_HOUSE_ARREST_GH_CONTEXT:
    "Professor Po promptly folded up the thin piece of crinkling paper and placed it insider a book."
    #sfx thud
    "He vehemently closed the book and placed it to the little counter table beside him."
    "All the while propping his foot onto his knees and dangling his head back to stretch."
    if fang.RandomCheck("logic",3,6):
        logic neutral "He's let his hair down.{w=0.2} Hence \"business\" is considered over."
        logic neutral "It's plausible to assume he will remain a friendly guest during house arrest."
    if fang.RandomCheck("empathy",3,6):
        empathy neutral "He takes his work seriously as opposed to his personal life."
        empathy neutral "{cps=*0.5}A two faced man.{/cps}"
    Po "It's a good thing I know your uncle since our academic days in Manchuria."
    "Professor Po glanced at Uncle Ku who had eased himself from his anxiety."
    Po "If another officer had offered this, they would have thrown you in the slammer or violated the sovereignty of your pantry and hospitality."
    Po "That would have been an awkward mess."
    "My mind was constantly buzzing at this predicament."
    "This could have gone {i}a lot{/i} easier if I had known that already."
    Po "As soon as I found out you lived with this geezer I had to come stay at his Siheyuan."
    "Professor Po gave a hearty laugh and let his chest deflate slowly."
    Po "Hong! Have you got any Maotai stored away?"
    "Uncle Ku raised his eyebrow and grinned."
    Ku "I sure can,{w=0.2} Poppy."
    "Uncle Ku gave a smug smile and smirked at Professor Po who likewise grinned at this remark."
    if fang.RandomCheck("rhetoric",3,5):
        rhetoric neutral "Must be an inside joke."
        rhetoric neutral "Perhaps we can find out more about this if we pry a bit into the buried past."
    call CHAPTER_1_HOUSE_ARREST_JOKE
    "Professor Po leaned back and rubbed his chin slightly as he absorbed himself back into thought."
    Po "I forgot to tell you."
    Po "When we talk about \"house arrest\" we are only well... \"supervising\" you."
    Po "You can leave the house as long as a registered officer or personnel is supervising you."
    "Professor Po took a sip of his Maotai and kicked his foot to rest on his thigh, like an aristocrat being photographed."
    Po "As you know, I'm too old and tired to be walking around like this."
    Po "I'm hitting 40 now."
    Po "In your books I existed before the republic and therefore by extension a product of the\"old world\"."
    Po "I just don't show it as much as your Uncle expresses it willingly."
    Ku "..."
    Ku "What are you getting at?"
    Po "What am {i}I{/i} getting at?"
    Po "Let the boy do whatever he wants."
    Po "I'll have Guo Heng supervise him."
    Po "We can catch up on what we've missed out on all these days ago."
    Po "On the other hand, Fang will get to mingle with young Kuomintang rather than suspicious foreigners."
    if fang.RandomCheck("reaction",2,4):
        reaction neutral "He's talking about Shigeru.{w=1} \"Suspicious Foreigner\"."
        reaction neutral "Plus he's hiding his contempt much less."
    if fang.RandomCheck("jugdement",3,6):
        judgement neutral "It's difficult to say how open he wants to be with his opinions."
    "Professor Po gave me a short glance with a malignant smirk."
    Po "I hope you didn't take that personally about your friend back there."
    Po "I don't think like that. In fact the burden of the system thinks this way."
    "Professor Po took another quick sip of Maotai to divert his attention from his crude comment."