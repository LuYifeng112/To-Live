define dogmeat_names = ['monster', 'Lanky General','Old Eighty-Six', 'Three Don\'t knows', '72-Cannon Chang', 'Chang of Shantung', 'Great General of Justice and Might']
label dogmeat_convo_nicknames:
    if not len(dogmeat_names) == 0:
        $ current_ZZC_nickname = renpy.random.choice(dogmeat_names)
        if current_ZZC_nickname == "monster":
            $ dogmeat_names.remove('monster')
            $ ZZC_nickname_prompt = "What other nickname did the \"Monster\" have?"
            Ts "One of his nicknames was monster"
            Ts "Why should I know why?"
            Ts "He was a rowdy bandit who became a general."
            Ts "He wasn't going to be a angel."
            return
        elif current_ZZC_nickname == "Lanky General":
            $ dogmeat_names.remove("Lanky General")
            $ ZZC_nickname_prompt = "Lanky general? eh? What else..."
            Ts "Sometimes folks that thinks he's too extreme call him Lanky general."
            Ts "It's just petty offense to a dead man now."
            return
        elif current_ZZC_nickname == "Old Eighty-Six":
            $ dogmeat_names.remove("Old Eighty-Six")
            $ ZZC_nickname_prompt = "That's quite the story about 86. Anything else?"
            "Lieutenant Tsai cupped his mouth with his hand."
            Ts "Should I really tell you?"
            Ts "It ain't pretty..."
            menu:
                "Tell me":
                    "Lieutenant Tsai let out a audible sigh."
                    Ts "These are rumors and gossip maybe even a joke."
                    Ts "Apparently his cock was as long as 86 Mexican coins."
                    vice neutral "What a story."
                    concept neutral "Don't even think about it."
                    visualcomprehension "I don't event know..."
                    "It felt a bit like shock and horror."
                    Ts "I warned ya kid."
                    fang "I know"
                "Don't tell me":
                    $ ZZC_nickname_prompt = "Apart from 86 what else?"
                    Ts "Good."
                    Ts "Wasn't planning to anyway."
            return
        elif current_ZZC_nickname == "Three Don\'t knows":
            $ dogmeat_names.remove("Three Don\'t knows")
            $ ZZC_nickname_prompt = "Any other nicknames you don't know?"
            return
        elif current_ZZC_nickname == "72-Cannon Chang":
            $ dogmeat_names.remove("72-Cannon Chang")
            $ ZZC_nickname_prompt = "Any other names you can fire off?"
            Ts "72-Cannon Chang."
            fang "Is there any story behind it?"
            Ts "Not that I know of."
            Ts "Couldn't bother finding out as well."
            return
        elif current_ZZC_nickname == "Chang of Shantung":
            $ dogmeat_names.remove("Chang of Shantung")
            $ ZZC_nickname_prompt = "Any other famed titles?"
            Ts "Ah yes."
            Ts "Chang of Shantung."
            Ts "Foreign media calls him that because of his character."
            Ts "It inflated his pride alright."
            return
        elif current_ZZC_nickname == "Great General of Justice and Might":
            $ dogmeat_names.remove("Great General of Justice and Might")
            $ ZZC_nickname_prompt = "Any other bravado names?"
            Ts "Great General of Justice and Might"
            "he looked at me with a smirk."
            Ts "You can probably tell the story behind that one."
            return
    else:
        $ Ts.convo("nicknames")
        Ts "Nah no more."
        Ts "Kid I love doing this but I don't think there is anymore nicknames."
        Ts "At least not in my damn memory."
        return