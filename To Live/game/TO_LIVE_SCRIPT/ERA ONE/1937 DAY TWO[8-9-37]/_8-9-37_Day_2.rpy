define ZZC_nickname_prompt = "What other nicknames did he have?"
label Beijing_chapter_one_Day2_8_9_1937:
    python:
            start = time.time()
            discord_rpc.update_connection()
            discord_rpc.run_callbacks()
            discord_rpc.update_presence(
                **{
                    'details': 'Chapter One: Talk Like Doves',
                    'state':'Peiping-Tientsin',
                    'large_image_key': 'tolive',
                    'start_timestamp': start
                }
            )
            discord_rpc.update_connection()
            discord_rpc.run_callbacks()
    "The blurred sounds merge like a bucket of different paints."
    if fang.RandomCheck("reaction", 2,7):
        reaction neutral "Could that be considered art?"
        logic neutral "It's hard to define \"art\"."
        menu:
            "It is art":
                rhetoric neutral "Art is expression."
                rhetoric neutral "Expression is subjective."
            "That's not art":   
                 rhetoric neutral "Art has substance."
        logic neutral "Interesting."
    "I can't event tell if my eyes are open or closed."
    "I try to adjust my eyes again."
    "It's dark and there aren't any silhouette's even."
    Gh "We're nearing Tientsin."
    "Guo Heng had been awake for some time."
    "Crouching near a box of liquor with a thin carpet as a blanket."
    if fang.RandomCheck("empathy", 2,4):
        empathy neutral "He seems cold."
        empathy neutral "He let you two have the warm ones."
        empathy neutral "Wanna return the favor?"
        logic neutral "He might be able to handle it... can you?"
        logic neutral "Pay attention to health."
        menu:
            "Give Guo Heng your blanket":
                "Guo Heng looks at me weirdly."
                empathy neutral "He doesn't expect this from you."
                empathy neutral "A stranger of two weeks."
                Gh "Are you sure Fang?"
                Gh "It's pretty cold."
                empathy neutral "Push on a bit more."
                menu:
                    "Push on.":
                        Gh "I appreciate your goodwill Fang...{nw}"
                        Gh "but it won't be wise to put you through misery all night."
                        Gh "We'll need you awake to talk to that man we are going to."
                        logic neutral "He has a point."
                        logic neutral "Pay attention to health. You have responsibilities."
                        menu:
                            "Try to convince him (Rhetoric-Medium)":
                                if fang.RandomCheck("rhetoric", 5,7):
                                    fang "and I need you to tell Wang P'u Ch'en to write your letter to Guo He."
                                    fang "You need to stay strong for your brother."
                                    fang "I'm pretty sure I can handle this anyway."
                                    "I could see Guo Heng smile in the dark."
                                    perception neutral "He can't see you."
                                    Gh "You pull my heart strings Fang."
                                    Gh "I'm a worrier for everyone but you've hit the nail on the head."
                                    Gh "My brother is the biggest worry after all."
                                    "I hand him the blanket."
                                    fang "How old is he?"
                                    Gh "Old enough."
                                    Gh "15 now."
                                    "Guo Heng ruffled in the dark as he tucked the blanket around himself."
                                    Gh "I'll return these in a few hours to you so that you won't get sick before our arrival."
                                    fang "Fair."
                                    $ Gh.log("Gave_blanket")
                                else:
                                    Gh "I appreciate it."
                                    "Guo Heng had already cut me off before my argument."
                                    Gh "We're counting on you."
                                    Gh "Stay strong."
                            "Give up on convincing him.":
                                Gh "I have a reputation for being stubborn."
                                Gh "That's why it took my brother a long time to crack my shell so that he could study in Shanghai."
                                "Guo Heng leaned his head against the wire frames leaning up the wall."
                                perception neutral "A soft thud emits from his direction."
                                empathy neutral "He's burned out."
                    "On second thought you're right.":
                        Gh "I thought so."
                        Gh "Don't get sick alright?"
                        Gh "We're counting on you."
                        "Guo Heng leaned back against the cold wire frames lining up the wall of the truck."
            "Keep the warm blanket for yourself":
                pred neutral "Survival of the fittest."
    "Ma Wen was half awake and half asleep."
    "You couldn't tell when he would just jump into a conversation."
    Gh "I can't believe I sent him to Shanghai."
    Gh "He's damn persuasive."
    Mw "How long has he been studying there?"
    Gh "1 year and a half."
    Gh "He's meant to graduate from there."
    Gh "Its a fancy international school."
    Mw "Seems to have surpassed you."
    Gh "That's a good thing."
    "Guo Heng hesitantly stammers for a moment."
    Gh "I'm proud of him after all."
    Mw "Fatherly instincts kicking in eh?"
    Gh "I guess you could call it that."
    "We stare out at the dark night sky lit up by tiny stars and a graceful moon."
    "Guo Heng clears his throat assuming he remembered something to say."
    Gh "Pretty much whatever is left of Hsi-Ku arsenal."
    Mw "They turned that place into a school didn't they?"
    Gh "Yeah."
    Mw "That arsenal would be really handy right now."
    Dy "They're already scuffling I bet."
    "Da-Yu had chimed in after hours to taking front wheel."
    "I wondered what else he heard us talking about."
    Dy "Lord knows what's going to be the outcome."
    Dy "My boss hasn't told me a course of action yet so I continue my job today until I meet him in Shanghai."
    Gh "How long will this take?"
    Gh "5 minutes if all hands are on deck."
    if fang.RandomCheck("rhetoric", 4,5):
        rhetoric neutral "This will get done faster if you help out."
        rhetoric neutral "I don't want to be here too."
    "Ma Wen rolled his eyes."
    "We began to crawl out of the back and lined up with goods."
    Dy "It's right in this establishment."
    "The place was shanty but it was a liquor store."
    "There was a dim dying lantern one one side of the building."
    "A implied lantern was hanging behind the building as well."
    Gh "What are we expecting？"
    Dy "A few drunks."
    Dy "Pecker up we'll be fine."
    "Da-Yu stacked up two grates and heaved them on his chest."
    "He walked ahead of us and began to guide us to where to go."
    Dy "The old fella that runs this place tells me to dump it in his cellar."
    "Da-Yu gently placed the crates on a little stone wall."
    "His hands began to pat the patches of grass near the wall before tugging on a rotten stringy fibres of rope."
    Dy "Got it."
    "Da-Yu heaved as he pulled up a concrete lid."
    Dy "Shit is heavy."
    "Guo Heng looked at me worriedly."
    Gh "You think this looks fishy?"
    "He whispered this to me."
    Mw "Even if it is then shut up."
    Dy "Let me get a torch."
    "Da-Yu jogged back to his truck leaving us to stare at the abyss in the cellar."
    Gh "Looks like a place to trap people and slave them."
    if fang.RandomCheck("empathy", 2,4):
        "Guo Heng spoke with melancholy."
        "it was like he has seen these phenomenons personally."
    else:
        random:
            "Maybe he's just worried about his brother."
            empathy neutral "He's just overworked."
            empathy neutral "He might be stressed out you know."
    Mw "Wouldn't they have crawled out by now?"
    Gh "They could be tied up."
    Gh "Besides who uses a disguised concrete lid for a cellar?"
    Mw "A business that has to hide stock from dangerous drunks on a daily basis."
    Gh "I'm not walking down there."
    Gh "I'll stay near the truck."
    Mw "I'll take the damn dive."
    if Mw.mood == "offended":
        Mw "Not like you will Fang."
        "Ma Wen glared at me."
    "Guo Heng put down his crate on the low stone wall and walked back as Da-Yu came back."
    Dy "What's up with him?"
    Dy "Wants us to keep waiting？"
    Mw "He said he was going to unload the crates and Fang will fetch them while I takes them inside."
    Dy "Made my job easier."
    Dy "Here's the torch by the way."
    Dy "Watch out for stray rats, don't put them at the lowest level cause they get in."
    Dy "Last month my lackey got a bad bite."
    Dy "Maybe a damn snake?"
    "Ma Wen looked at him, a bit shaken."
    "Da-Yu burst out laughing."
    Dy "I'm kidding. I unload alone, only some damn rats."
    "Ma Wen nodded slowly and clutched his crate into his left arm and grabbed the handheld torch."
    "He began to descend the cold stairs."
    if Mw.mood == "Offended":
        Mw "Fuck this shit."
        "He muttered under his breath."
    Gh "Fang!"
    "His voice was faint and distant."
    "I began to take steps back to the truck."
    "Guo Heng looked down at me."
    Gh "Here's a crate."
    "I took it into my arms and began to move back."
    "After 10 minutes of leaving a crate at the mouth of the cellar the work was finished."
    Dy "Glad that's over with."
    Dy "Let's get going now."
    "Ma Wen crawled out of the mouth of the cellar scratching his sculp viciously."
    "He dug his nails into the dirt and climbed out."
    Dy "Find many rats down there?"
    Mw "No."
    Dy "The old guy must have hunted them down."
    Dy "I heard they fetch good prices in other villages."
    if fang.RandomCheck("reaction", 3,6):
        reaction neutral "The starving ones..."
    Mw "Can we just get going?"
    Dy "Sure."
    "Guo Heng was already at the truck and we were ready to trek down to Tsingtao."
    Gh "We should get some good sleep."
    Mw "I agree."
    "Ma Wen looked tired and shaken up from the bugs in the cellar."
    "For a noble... he had good tolerance."
    if fang.RandomCheck("logic", 4,6):
        logic neutral "Why?"
        logic neutral "That is strange isn't it?"
        pred neutral "The world is a harsh place."
        pred neutral "I don't blame him for adjusting to it as it is required."
        logic neutral "Perhaps we are assuming wrongly about how long he has been on his own."
        logic neutral "He could have lied even."
        pred neutral "People have their secrets."
        pred neutral "Watch your back."
    "I sat down in the cold area again."
    Gh "Get some shuteye will you?"
    fang "What else will I do?"
    $ TL_datetime.timepass()
    $ TL_datetime.timepass()
    $ TL_datetime.timepass()
    jump Tsingtao_8_9_37_Dawn


label Tsingtao_8_9_37_Dawn:
    #Sound of guns
    python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Chapter One: Talk Like Doves',
                'state':'Shantung -Tsingtao',
                'large_image_key': 'tolive',
                'start_timestamp': start
            }
        )
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
    "I adjusted my eyes as I began to realize the sounds around me."
    Gh "Fang did you hear that?"
    Gh "Did we cross into some fucking skirmish?"
    Dy "No, we haven't."
    Gh "Why do I hear guns?"
    Dy "Cause we're in Tsingtao and I think there's a fucking raid on some communists."
    Mw "Communists are a pain in the ass."
    "Ma Wen sat up as his eye winced."
    Dy "Anyway I got you to your destination."
    Dy "On my way to Shanghai now."
    Dy "I think I'll get an early leave for a while."
    if fang.RandomCheck("rhetoric", 3,5):
        rhetoric neutral "I won't be coming back."
    Gh "You really want to get off here?"
    "Guo Heng glared at me as Da-Yu swung around from the driver's seat and observed us."
    Dy "Unless you guys are communists...."
    if fang.RandomCheck('rhetoric', 2,3):
        rhetoric neutral "He says this sarcastically."
    Dy "Get out please."
    "Guo Heng looked with slight disbelief at Da-Yu who was much more impeding now."
    Gh "Da-Yu can't you drive us a bit further away from the raid?"
    Dy "The longer I stick here, the more likely an officer will inquire what the hell is happening."
    if fang.RandomCheck("rhetoric", 3, 5):
        rhetoric neutral "It's in everyone's best interest to leave the truck right now."
    #Knocking on glass
    ko "What's happening here?"
    "Da-Yu gave an audible sigh as the officer asked."
    Dy "I'm here to drop off some workers but they're scared of the raid."
    ko "Scared?"
    ko "We're rounding up communists and they're scared of us?"
    Dy "Tell me about it."
    "Da-Yu brought out his cigarette and put in his lip again."
    Dy "Fancy a smoke officer?"
    ko "Sure."
    "The officer took a cigarette from Da-Yu's hand. He was wearing tight leather gloves."
    ko "I don't get why people are scared of us doing our damn job."
    "Da-Yu just shrugged."
    Dy "Take em' off my back will you?"
    ko "Let me give them a tour alright?"
    ko "I need a fare."
    "Da-Yu reached into his glove box and brought out a pack of imported cigarettes."
    Dy "Is this a nice fare?"
    ko "Sure is."
    "The officer slams the side of the truck vehemently."
    ko "Get out of the truck now!"
    "He screeched at us as he commanded us."
    Gh "Fuck."
    "We crawled out of the truck where the officer came up to us three."
    ko "I ain't in charge of this raid."
    ko "Officer Tsai is."
    "The officer points us to a man wearing dark sunglasses and standing with an immaculate uniform staring down a building."
    ko "Up to 50 soldiers have sealed all sides of this shit-hole."
    ko "When anyone is seen near windows, we just shoot."
    ko "We have no fucking clue if they're armed or not but Tsai really wants to bust the door down sooner or later."
    "Guo Heng's eyes widened."
    if fang.RandomCheck("empathy", 3,6):
        empathy neutral "He doesn't want to witness violence."
        empathy neutral "His sorrow is the product of a violent encounter."
        empathy neutral "Look after him."
    "Ma Wen's face had intrigue."
    if Mw.mood == "Offended":
        if fang.RandomCheck("empathy", 5,9):
            empathy neutral "Ma Wen is better at hiding his emotions."
            empathy neutral "He sees the art in deciphering faces."
            empathy neutral "He is only intrigued by this."
            empathy neutral "Hard to tell if afraid at all."
    else:
        if fang.RandomCheck("empathy", 3,7):
            empathy neutral "Ma Wen is better at hiding his emotions."
            empathy neutral "He sees the art in deciphering faces."
            empathy neutral "He is only intrigued by this."
            empathy neutral "Hard to tell if afraid at all."
    "The building was sealed with hungry troops."
    "Their bones were showing in some places."
    ko "Han Fu Ju has made Shandong great."
    ko "He's leading us away from the central government in Kuomintang."
    ko "He's also been talking with the Japanese."
    "The officer seemed to be really confident in a warlord."
    ko "While the {i}guizi{/i} fight with the Nanjing government we are here trading our securities with them."
    ko "He's a true nationalist and I will not hear any bullshit about him."
    "He was holding Me and Wen's necks by the scruff and roughly."
    "Professor Tsai was screaming at his men as they swiftly began to follow instructions."
    "The sounds of gun clicking."
    "Footsteps marching."
    "It was going to start."
    "The officer holding me and Wen had pushed us forward to the side of Lieutenant Tsai."
    Ts "Bring down the door!"
    "He had his arms on his hips as he stared down the building."
    Ts "Kill every fucking communist that fights back."
    Gh "Wouldn't that be a blood bath?"
    "Guo Heng mistakenly uttered."
    "Lieutenant Tsai spat on the ground before turning around."
    Ts "What the fuck are you doing here?"
    ko "They're learning the noble deeds of the Kuomintang."
    Ts "Ain't nothing noble about killing, son."
    Ts "Don't talk like you've fought."
    "The Officer now began to shrivel into his uniform like a turtle."
    Ts "Battlefield will be glad to take you guys."
    Ts "Stuck here with bullshit \"raids\"."
    "Lieutenant Tsai seemed to be pissed off from nearly everything."
    "As he was shouting down the officer a gun shot emerged from the building."
    Ts "Great, who got first blood?"
    ds "What?"
    "A scrawny young soldier about 20 screamed back from inside the building."
    "Lieutenant Tsai spat on the ground again and prepared for a screech."
    Ts "Who hit who?!"
    "Despite being far away the young shoulder shuddered at the might of his voice."
    ds "We hit em Sir!"
    Ts "How many men were there?!"
    "I could see Guo Heng and Ma Wen visibly confused at this whole situation."
    "A weird screeching game between soldiers."
    ds "Don't know sir! We got four teenagers!"
    Ts "Fucking youngsters."
    "He rubbed his mouth before turning back around."
    Ts "Clean out the building!"
    ds "yes Sir!"
    "The young soldier ducked back into the building."
    Ts "This shit is too boring."
    Ts "They don't put up a fight."
    Ts "When there is a trace of a challenge then we send in more physical force, more men, more guns, more power and its too easy."
    "Lieutenant Tsai pulled out a pack of Marlboro smokes."
    if fang.RandomCheck('encyclopedia', 2,5):
        schema neutral "This is a filtered cigarette, which means its marketed to woman mostly."
        schema neutral "Imported items are a gem here and often can fetch you a lot of money or luxury."
    "He slid out a cigarette from the packet and packed it between his lips."
    Ts "Got a light?"
    "He had asked this to the Officer but being in Guo Heng's direction his face spoke terror."
    "The gunshots began to become more and more frequent as screams of soldiers inside the building roared."
    "Screams of soldiers winning."
    Ts "My boys may be skinny as a fucking stick but they get the job done."
    Ts "Corporal Hu have you heard of the situation in Szechewan?"
    "The officer now Corporal Hu shook his head to the side."
    "Officer Tsai patted his hands on the thighs of his uniform as he sat on a nearby chair."
    Ts "This chair makes me feel like a director.{w=0.1} Ya know?"
    "All of us nodded our heads."
    "We all could see it."
    Ts "Szechewan isn't in great shape."
    Ts "My old busted up home is back there in Changsha."
    "He picked up a rifle of some sort and proceeded to start cleaning it."
    if fang.RandomCheck("encyclopedia", 3,5):
        schema neutral "Liu Hsiang is {i}de-facto{/i} leader of Szechewan."
        schema neutral "Too many warlords keep further dividing Szechewan."
        schema neutral "Szechewan is still going through famine in various parts and Liu Hsiang is still consolidating power."
        schema neutral "It was pretty autonomous since the 1911 revolution and it seems to have embraced the warlord period in pushing its autonomy agenda."
        schema neutral "Technically they're autonomous by the National Revolutionary army since..."
        schema neutral "When??"
        schema neutral "You should ask him soon."
        rhetoric neutral "He seems well educated in {i}geo-politics{/i}."
        rhetoric neutral "Ask your questions through him."
    else:
        Ts "Szechewan is also not one warlord state but many smaller defense districts that too many warlords carved up."
        Ts "Liu Hsiang is just the most prominent warlord in Szechewan hence given the title warlord of Szechewan."
    "He rubbed the cloth across the stock of the gun before placing it down again."
    Ts "There's been a famine since last year I've heard."
    Ts "They got the most manpower in their military out of all of us right now."
    Ts "You wanna know how they pulled it off?"
    Ch "Propaganda?"
    "Lieutenant Tsai let out a sigh of despair."
    "It seemed if one thing were to go out of his way he gets fed up."
    Ts "The military of all places has become a haven for the poor."
    Ts "Consistent meals, shelter and benefits from being stand in {i}cannon-fodder{/i}"
    Ts "They flock like ironic doves to the haven and now will be forced to fight against Japan."
    Ts "Hey kids, fly off or we'll make you fight for the NRA({i}National Revolutionary Army{/i})."
    logic neutral "Don't you want to hear more about his story?"
    logic neutral "Your world feels so narrow and limited."
    rhetoric neutral "A brave old soldier with a cranky personality talking with pride about his honors."
    rhetoric neutral "Could he have medals?"
    rhetoric neutral "This man interests you."
    logic neutral "Pick up some learning..."
    menu:
        "Try to learn more about Szechewan. (Rhetoric Medium)":
            if fang.RandomCheck("rhetoric", 4,7):
                "Lieutenant Tsai look down and flicks his cigarette out."
                Ts "At least you sound serious unlike the clowns who I order to listen to me."
                rhetoric neutral "Success!"
                Ts "What do you want to know?"
                Ts "I'm a busy man."
                Ts "Ask me questions until this cigarette runs out."
                "He pout it up to my face. The soft whirls of smoke dancing in the air."
                if fang.RandomCheck("reaction", 1,5):
                    reaction neutral "Like Russian ballet."
                    # if fang.GetMaxPol() == "communism":
                    #     judgement neutral "Just like the beauty of the freedom of its workers."
                    # elif fang.GetMaxPol() == "fascism" or fang.GetMaxPol() == "nationalism":
                    #     judgement neutral "Sadly it has been raped by the injustices of communism."
                    # else:
                    #     pass
                jump TS_convo_2
            else:
                "Lieutenant Tsai looked at me in disbelief."
                Ts "I'm supervising a raid on communist scums."
                Ts "Pardon my french but I don't give enough shits to educate people right now."
                Ts "Now please get out of my sight."
        "get up and leave":
            pass
    Ts "Tell em' corporal."
    "Guo Heng had already backed off around a corner of a building."
    Ch "You don't want to see those bodies with the blood and guts and shit and piss on them."
    Ch "You're young, keep your mind fresh."
    "He taps me on the cheek like a kid."
    if fang.RandomCheck("predatoryinstinct", 1,3):
        pred neutral "What a shithead."
        pred neutral "I'll show him."
    jump WPC_house
label TS_convo_2:
    menu:
        "What's your opinion on Szechewan?" if not Ts.said("opinion"):
            $ Ts.convo("opinion")
            "Lieutenant Tsai rubs his chin as he contemplates."
            Ts "It's my hometown but it's not in great shape."
            Ts "It's dishonorable to back stab your hometown."
            Ts "I think Liu Hsiang has to pull himself together."
            Ts "I also hope they don't rely on throwing men at the enemy rather than bullets. They have a lot of conscripts."
            Ts "Generalissimo Chiang would sort them out.{nw}"
            Ts "Hopefully."
            jump TS_convo_2
        "How did you end up working under Han Fu Ju?" if not Ts.said("backstory"):
            $ Ts.convo("backstory")
            Ts "I used to work the ranks under the previous warlord."
            Ts "The \" most based\" one."
            Ts "He's a lucky bastard."
            Ts "He used to be a bandit that involved himself in conflicts."
            Ts "Somehow during the 1910s he got himself in charge of a division and began to cooperate with the Japanese backed Fengtian clique."
            Ts "Anyway I worked my way up the ranks."
            Ts "I was well educated and smart and what not."
            Ts "I want to stay as a Lieutenant of Artillery."
            Ts "I get paid enough and I don't have to make big choices."
            Ts "Anyways I was young and wanted an easy leader to follow."
            Ts "I was the kind of lad that would be updated with everything."
            "Lieutenant Tsai spat on the ground."
            Ts "The Dogmeat General as I said was pretty \"based\"."
            if fang.RandomCheck("encyclopedia", 1,4):
                schema neutral "Dogmeat General is an interesting nickname."
                schema neutral "Some say it's named after his favourite tonic."
                schema neutral "Others say it's derived from a gambling game he plays often."
                schema neutral "The game in question is {i}Pai-Gow{/i}."
                $ TL_glossary.addword("Pai-Gow")
                schema neutral "This game is also referred to as \"Eating Dog-meat\""
                menu:
                    "That's interesting":
                        schema neutral "Exactly."
                    "What a strange man.":
                        schema neutral "Wait till you hear more about him."
            Ts "I wanted to work under him because of his character."
            Ts "A self made bandit to General who was infamously cool."
            Ts "Sadly the poor fella got shot in 1932 by his nephew."
            Ts "Han Fu-Ju took over his role and began the {i}Han-Liu war{/i}."
            Ts "The fucker won and Shandong is reunited."
            "Lieutenant Tsai gave a sarcastic \"yay\"."
            Ts "I can tell by his eyes he's a coward to the Japanese."
            Ts "He'll give em everything to save his tail."
            Ts "Honestly I became a soldier to help the nationalists not become a chess piece in feudal games."
            Ts "Enough yapping, I'm boring you."
            Ts "What other stuff you got to ask?"
            jump TS_convo_2
        "How prepared is Shandong against Japan?" if not Ts.said("preparation"):
            $ Ts.covo("preparation")
            "Lieutenant Tsai gave a muffled laugh."
            Ts "What are you a fucking spy?"
            Ts "I ain't telling you sensitive things."
            Ts "but you can probably tell just by looking that our armies are built to fight Chinese not foreign technologically superior imperialists."
            Ts "Since you're asking so many question like some interrogator lemme ask some to you as well."
            Ts "What's your opinion of the Kuomintang?"
            menu:
                "The best option from communists and the Japanese.":
                    Ts "Well at least you got some brains."
                "A capitalist system of abuse and corruption.":
                    Ts "Aye, those hawks in government are a pain."
                    Ts "Ruins the name of us honest folk."
                    if fang.RandomCheck("logic", 1,3):
                        logic neutral "He'll probably hold in some loot confiscated from the building."
                "A fragile state without the strength to unite itself and it's people. Food for Japanese.":
                    Ts "Jeez you're more nationalist than the nationalists."
                    if fang.RandomCheck("predatoryinstinct", 2,5):
                        pred neutral "That's life."
            jump TS_convo_2
        "How much war experience you have?" if not Ts.said("experience"):
            $ Ts.convo("experience")
            Ts "Enough to be a fucking general."
            Ts "but I just want to get paid well not tell kids to kill themselves in the middle of a battlefield."
            "He took another drag of his cigarette."
            if fang.RandomCheck("reaction", 3,4):
                visualcomprehension neutral "He looks a bit jittery."
                if fang.RandomCheck("logic", 2,4):
                    logic neutral "Maybe he takes opium?"
                    logic neutral "Or perhaps he's remembering something harsh."
                    schema neutral "People get the shakes when in withdrawal from an addictive substance or when they're ill."
                    logic neutral "That makes sense."
            jump TS_convo_2
        "You don't like Han Fu-Ju?" if not Ts.said("dislike"):
            $ Ts.convo("dislike")
            jump TS_convo_2
        "Tell me more about the Dogmeat General" if not Ts.said("dogmeat") and Ts.said("backstory"):
            $ Ts.convo("dogmeat")
            Ts "That guy is always interesting to talk about."
            "Lieutenant Tsai gave a small chuckle."
            if fang.RandomCheck("empathy", 3,5):
                empathy neutral "He enjoys talking about his \"Idol\"."
            call dogmeat_convo
            jump TS_convo_2
        "I have to go now.":
            $ Ts.clearconvo()
            jump WPC_house


label dogmeat_convo:
    menu:
        "What is Dogmeat General's real name?" if not Ts.said("name"):
            $ Ts.convo("name")
            "Lieutenant Tsai rubbed his chin for a second."
            Ts "{i}Chang Tsung-Ch'ang{/i} I believe"
            jump dogmeat_convo
        "[ZZC_nickname_prompt]" if not Ts.said("nicknames"):
            if not Ts.said("lemme think"):
                $ Ts.convo("lemme think")
                "Lieutenant Tsai thought for a few seconds."
                Ts "Holy shit there were a lot of names."
                Ts "Lemme think."
            call dogmeat_convo_nicknames
            jump dogmeat_convo
        "What's he most remembered for?" if not Ts.said("legacy"):
            $ Ts.convo("legacy")
            jump dogmeat_convo
        "Did you ever meet him?" if not Ts.said("contact"):
            $ Ts.convo("contact")
            Ts "No."
            "He took a drag of his cigarette."
            Ts "Bummer."
            jump dogmeat_convo
        ">> That's enough about him.":
            Ts "I guess so."
            return


label WPC_house_map:
    "I caught up to Guo Heng around the block where he and Ma Wen were waiting arms crossed."
    Gh "We should get going."
    Mw "How far away is the house?"
    menu:
        "Try to remember (focus-medium)":
            if fang.RandomCheck("composure", 4,7):
                composure "It's in your head."
                composure "A day's walk on foot, a few hours by rickshaw."
                composure "It is in Shipei district."
                $ fang.log("WPC_house")
                jump WPC_route
        "Find a map of Qingdao":
            pass
    Gh "Lets find a map then."
    "Ma Wen gave a sigh."
    Gh "Where should we look?"
    Mw "We should ask the locals."
    
label WPC_route:
    Gh "Good we should get going."
    Mw "Shouldn't we just take a {i}rickshaw?{/i}"
    "Guo Heng bites his lip."
    if fang.RandomCheck("empthy", 4,9):
        empathy neutral "He's low on cash."
        $ fang.log("GH_low_cash")
        menu:
            "Don't worry, I'll cover it. (80 Fabi)":
                $ Gh.bondp(1)
                $ Gh.log("CoveredRickshawFee")
                $ msg.msg("Guo Heng will remember that.")
            "Do Nothing.":
                $ Gh.mood = "Upset"

