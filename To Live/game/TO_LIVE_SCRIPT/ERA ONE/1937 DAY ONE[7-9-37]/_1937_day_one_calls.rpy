label CH_1_CHOICE_VOID_GUIDANCE:
    $ devlog.info("CHAPTER_1_VOID: GUIDANCE CHOICE")
    menu:
        "Accept the hand":
            "The cold icy hand of the entity wrapped around my arm like a snake."
            "Thieving me of my energy as I felt myself fall into its grasp."
            void "Never,{w=0.2} bite the hand that {i}feeds{/i} you."
            void "Nonetheless, I will watch your choices with great interest."
            return
        "Reject the hand":
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
        "Satisfying| A sleep that didn't waver the mind. (images/00_character_side_images/character.authority/authority_neutral.png)":
            Po "That would have been good to hear if it wasn't for the fact that you were visibly disturbed in your nap."
            return
        "Strange":
            Po "It sure sounds like it."
            return
        "Uncomforting":
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
    $ mc_name = renpy.input("Please give your alternative name.", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=10)
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
        "Nanking|Home of the Kuomintang, the nationalist military administration committed to preserving Dr Sun's Legacy.\n\nAn urban, peaceful budding metropolis.\n\nA land for hope.( )":
            pass
        "Shanghai|The West's foothold in Asia.\n\nAn urban center akin to Nanking, consisting of heavy trade and port dealings with Britain and the United States.\n\nA blend of a prosperous life that could one day be for the rest of China.( )":
            pass
        "Tsingtao|The legacy of German colonialism in Asia.\n\nA coastal city that is becoming a vital node in the heartland of China's growing economic prowess.\n\nA land of industrious work ethic and thinking.( )":
            pass
        "Kwangchow|The vanguard of Southern Tradition.\n\nA urban and budding metropolis investing in education and academia to further progress China.\n\nBirth of the Kuomintang military administration.\n\nThe land to cultivate a character of erudite. (images/choice_icons/kwangchow_flag.png)":
            pass
        "Hong-Kong|A British fortress in the South East Asia.\n\nA heavily anglicized way of life has been introduced here and culminated an amalgamation of cultures.\n\n A land of skilled documentation and rhetorics presiding over wisdom. ( )":
            pass
        "Macao|A Portuguese landing in the coastal China area.\n\n A place of wonder and awe and enigmatic delights where one can indulge wholeheartedly.\n\n Simply put, a land of embraced vices and risky rewards.( )":
            pass
