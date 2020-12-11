label CH_1_CHOICE_VOID_GUIDANCE:
    $ devlog.info("CHAPTER_1_VOID: GUIDANCE CHOICE")
    menu:
        "Accept the hand|...  (images/choice_icons/00_default.png)":
            "The cold icy hand of the entity wrapped around my arm like a snake."
            "Thieving me of my energy as I felt myself fall into its grasp."
            void "Never,{w=0.2} bite the hand that {i}feeds{/i} you."
            void "Nonetheless, I will watch your choices with great interest."
            return
        "Reject the hand|...  (images/choice_icons/00_default.png)":
            "The cold icy hand of the entity dissipated into a dark mist that lost itself into the hollow reality."
            "Running away, to someplace I wouldn't want to be aware of, {w=0.2} or even curious of."
            void "Your fear drives me away..."
            void "Yet I will never go away."
            void "Lest, you choose to challenge my domain in your mind.{w=0.2} Through cooperation or confrontation."
            void "My presence is unchallenged."
            void "Ultimately, my domain is preserved."
            return
label CH_1_CHOICE_HOSUE_ARREST_SLEEP:
    $ devlog.info("CHAPTER_1_HOUSE_ARREST: SLEEP CHOICE")
    menu:
        "Satisfying| A sleep that didn't waver the mind.  (images/choice_icons/00_default.png)":
            Po "That would have been good to hear if it wasn't for the fact that you were visibly disturbed in your nap."
            return
        "Strange.  (images/choice_icons/00_default.png)":
            Po "It sure sounds like it."
            return
        "Uncomforting.  (images/choice_icons/00_default.png)":
            Po "I can tell."
            return

label CHAPTER_1_HOUSE_ARREST_NAME:
    $ devlog.info("CHAPTER_1_HOUSE_ARREST_NAME CALLED")
    menu:
        "No, no other names.":
            label CHAPTER_HOUSE_ARREST_NAME_RETURN:
                Po "Well ok, that's fine then."
                return
        "Yes, I do.":
            jump CHAPTER_1_HOUSE_ARREST_NAME_SUB

label CHAPTER_1_HOUSE_ARREST_NAME_SUB:
    if not fang.said("Po_note"):
        Po "Please tell me then and I'll make a note of it."
        $ fang.convo("Po_note")
    $ mc_name = renpy.input("Please give your alternative name.", allow=" -'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=10)
    call CHAPTER_1_HOUSE_ARREST_NAME_CHECK
    $ mc_name.strip()
    if mc_name == "":
        jump CHAPTER_HOUSE_ARREST_NAME_RETURN
    else:
        judgement neutral "Are you sure you want to put down this alternative name?"
        menu:
            "Yes.":
                $ fang.forget("Po_note")
                Po "Ok then, I see."
            "No":
                jump CHAPTER_1_HOUSE_ARREST_NAME_SUB
            "Forget the alternative name":
                jump CHAPTER_HOUSE_ARREST_NAME_RETURN

label CHAPTER_1_HOUSE_ARREST_NAME_CHECK:
    if mc_name == "":
        random:
            block:
                Po "Its bad luck to live through life without a name you know?"
                Po "Anyway if it isn't a hassle, I can put your name down as Fang Jie."
                return
            block:
                Po "All of my sisters never had a name.{w=0.2} It was strange."
                Po "They were all referred to by their birth order."
                Po "You know \"Er Jie\", \"Si Jie\", etc."
                return    
    return
label CHAPTER_1_HOUSE_ARREST_RESIDENCE:
    menu:
        "Nanking|Home of the Kuomintang, the nationalist military administration committed to preserving Dr Sun's Legacy.\n\nAn urban, peaceful budding metropolis.\n\nA land for hope. (images/choice_icons/00_default.png)":
            $ fang.updateSkill("faith", 1)
            $ fang.updateSkill("psychethreshhold", 1)
            $ fang.hometown = "NK"
            "Nanking"
            return
        "Shanghai|The West's foothold in Asia.\n\nAn urban center akin to Nanking, consisting of heavy trade and port dealings with Britain and the United States.\n\nA blend of a prosperous and social life that could one day be for the rest of China. (images/choice_icons/00_default.png)":
            $ fang.updateSkill("influence", 1)
            $ fang.updateSkill("empathy", 1)
            $ fang.hometown = "SH"
            "Shanghai"
            return
        "Tsingtao|The legacy of German colonialism in Asia.\n\nA coastal city that is becoming a vital node in the heartland of China's growing economic prowess.\n\nA land of industrious work ethic and thinking. (images/choice_icons/00_default.png)":
            $ fang.updateSkill("determination", 1)
            $ fang.updateSkill("endurance", 1)
            $ fang.hometown = "QD"
            "Tsingtao"
            return
        "Kwangchow|The vanguard of Southern Tradition.\n\nA urban and budding metropolis investing in education and academia to further progress China.\n\nBirth of the Kuomintang military administration.\n\nThe land to cultivate a character of erudite. (images/choice_icons/kwangchow_flag.png)":
            $ fang.updateSkill("logic", 1)
            $ fang.updateSkill("schema", 1)
            $ fang.hometown = "GZ"
            "Kwangchow"
            return
        "Hong-Kong|A British fortress in the South East Asia.\n\nA heavily anglicized way of life has been introduced here and culminated an amalgamation of cultures.\n\n A land of skilled documentation and rhetorics presiding over wisdom. (images/choice_icons/00_default.png)":
            $ fang.updateSkill("dexterity", 1)
            $ fang.updateSkill("rhetoric", 1)
            $ fang.hometown = "HK"
            "Hong-Kong"
            return
        "Macao|A Portuguese landing in the coastal China area.\n\n A place of wonder and awe and enigmatic delights where one can indulge wholeheartedly.\n\n Simply put, a land of embraced vices and risky rewards. (images/choice_icons/00_default.png)":
            $ fang.updateSkill("vice", 1)
            $ fang.updateSkill("focus", -1)
            $ fang.hometown = "MC"
            "Macao"
            return
label CHAPTER_1_HOUSE_ARREST_JOKE:
    menu:
        "\"Where did you get the name Poppy?\"|Poppies are the direct result of ravaged landscapes which scatter their seeds.\n\nUltimately a symbol of the cruel aftermath of war.\n\nThe curiosity is overwhelming to find out the inception of this peculiar nickname. (images/choice_icons/00_default.png)":
            "Professor Po looked at me momentarily and closed his eyes."
            "Uncle Ku quietly placed a cup of Maotai on the adjacent table next to his chair."
            Po "Back when the Kwantung army took over Manchuria and set up Manchukuo, the league of nations set up a committee to investigate the incident."
            Po "It was known as the Lytton committee.{w=0.5} They were sent to investigate the validity of Japanese justification for their invasion."
            Po "Which by the way despite the bullshit was obviously not justified."
            if fang.RandomCheck("schema", 5,9):
                schema neutral "The Kwantung army was the name given to the Japanese military that acted independent of of the civilian government."
                schema neutral "Its operations mainly consisted in Manchuria."
                schema neutral "The Lytton committee was a 5 man investigation team from several western countries."
                schema neutral "The committee also concluded after one year of investigations that Japan was an aggressor."
                schema neutral "Arguably, the first nail in the coffin for the declining authority of the League of Nations."
            Po "I was an assistant for one of the translators who co-operated with them.{w=0.2} Due to fact they were all westerners."
            "Professor Po paused monetarily to sip from his cup and smack his lips from the strong concentrated batch of Maotai."
            Po "Eventually my master gave me an English name to use because {i}Po Yeurt-Tarng{/i} was too difficult for a foreigner to remember."
            Po "He gave me the name \"Poppy\".{w=0.5} A symbol of peace and a legacy of war."
            Po "I couldn't tell if it was a girls name or boys name, but since I don't meet many foreigners that isn't something to bother about."
            Po "By the way, the report didn't do so much because when it was shown before the international community, Japan metaphorically slapped their face by walking out."
        "Never-mind. Just let it be.|Inside jokes lose their value when spread around to others.\n\nHumor forms through relationships and bonds and it feels \"off\" to dig them up.\n\nKnowing about it won't claw my sleep away or dissatisfy my curiosity. Its better to just leave it. (images/choice_icons/00_default.png)":
            pass
    return