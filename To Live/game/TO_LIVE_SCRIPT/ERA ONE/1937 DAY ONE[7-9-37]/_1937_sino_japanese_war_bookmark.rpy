label Beijing_chapter_one:
    if not persistent.history_home_unlocked:
        $ persistent.unlocked_history.append("home")
    na "{size=30}Republic of China - 1937 \n Peiping{/size}"
    no "Are these you memories??{cps=*0.4}!?!?!{cps=*0.6}?!?!{/cps}?!?!{/cps}"
    no "The father calls you."
    $ camera_move(0, 0, 500, rotate=0, duration=10)
    no "WHERE ARE YOU"
    no "SHOW YOURSELF"
    no "SHOW YOURSELF!{cps=*0.4}!!!!{/cps}"
    scene black with flash
    $ fangbag.add_item(Jade, msge=False)
    window auto
    un "Fang"
    un "{cps=*0.4}...{/cps}"
    un "You awake?"
    "The faint figure was only a silhouette in my half opened eyes."
    un "Sounded like you were having a nightmare of some sort."
    "I had waited so long for him to arrive for this interview I had fallen asleep in this god awful uncomfortable chair."
    menu:
        "I'm awake":
            pass
    un "That's good."
    "The silhouette moved around a bit more as I tried to gain focus."
    un "It is important you answer these questions properly."
    un "I will go through them one by one."
    un "Alright?"
    menu:
        "...":
            pass
    un "Do not fret."
    fang "Yes I understand."
    un "Good."
    un "We're here for you."
    un "Let's get this over with."
    "That thought was calming to me."
    "Tough times needed tough people or support."
    "In this case I knew what {i}I{/i} needed."
    "I knew I had screwed up..."
    "Protesting and rebelling."
    "Showing the power of a voice without hope."
    "Of harsh unfiltered criticism."
    "What should I expect?"
    menu:
        "{i}That was my choice; thus my consequence.{/i}":
            pass
        "{i}Justice being punished is just proof of a unjust leadership.{/i}":
            if fang.RandomCheck("rhetoric", 0,1, True, 0.35, True):
                "This gives me a message on authority and power in this country."
                "It's better to not believe in it too much."
                correction neutral "Perhaps it is human nature to be self centered."
                correction neutral "How else is one expected to live in a naturally cruel world?"
                menu:
                    "By cooperating and becoming strong as a group":
                        correction neutral "perhaps so."
                    "You're right. A litte sefishness is necessary.":
                        "But most people tka it too far."
                        "They fail to limit ambition or a desire for inhibition."
                        correction neutral "Maybe..."
                        correction neutral "Maybe not."
                $ fang.addTrait("LightCynical")
            else:
                fang "But if they really want to preserve Dr Sun's legacy they will have to change their ways."
                fang "They will listen one way or the other."
            "I should just focus on getting this interview done."
    scene Ku_house

    "Times are getting intense these days."
    "We are on the edge of total war - {i}again{/i}."
    "I began to adjust my eyes and get used to who was around me."
    "Resting my eyes on the previously known \"Silhouette\" I recognised him as \"Professor Po-YeurtTarng\"."
    "Professor Po Yeutarng is a lawyer who is quite well connected wtih Kuomintang \"Hawks\"."
    "\"Hawks\" in the sense that they perch on your shoulder and are aggressive in every action they take."
    "The Professor's very close with my uncle \"Ku Hong-Meng\"."
    "A scholar who used to work in Peking before he became \"enlightened\" in a lifestyle of spiritual content and cosmic toiling."
    "A full time Taoist in essence."
    "Professor Po Yeutarng on request of Uncle Ku had come to interview me to clear of any charges or suspicions with communist acivity."
    "All three of us knew that I was in no way connected with communists or had any clear sympathies for them."
    "The interview still had to be carried out superficially... just to clear my name."
    "It was also a good oppurunity to evaluate my situation and possible choices."

    Po "Are you Ready Fang?"

    menu:
        "Yes I am Ready.":
            pass
            
        "Please Give me a minute to think.": 
            if fang.RandomCheck("composure", 0, 1, True, 1, False):
                composure "{i}Succeeded in focussing.{/i}"
                $ fang.updateSkill("focus", 1)
                fang "Please give me a minute to think."
                Po "That's fine,"
                "Normally I would be ready to answer any question coming my way."
                "I never passed up answering a question."
                "Beads of sweat formed on my brow."
                "Summer had just ended so the heat was burning out like some star."
                "I controlled my air-flow and calmed myself down."
                "I can do this."
                Po "I don't think you did anything wrong."
                Po "You're young."
                Po "You have this burning fire in you that can't be matched."
                Po "You have to vent it out somewhere."
                Po "Those hawks will let you go..."
                Po "unless they see you have an incentive to believe in communism through traits such as {i}poverty.{/i}"
                Po "Which means that any of the other kids that were protesting and weren't affluent can be suspected more {i}harshly{/i} as \"communists\" due to their economic conditions."
                Po "I'll have to interview them as well."
                Po "I can spot damn communists really well."
                if fang.RandomCheck("visualcomprehension", 2,4, True, 0.35, True):
                    visualcomprehension neutral "I mean you can tell by that patriotic insignia he wears."
                    visualcomprehension neutral "Normally he wears a coat to cover it up or keep the coat resting on his shoulder."
                    logic neutral "Why would he hide it?"
                    visualcomprehension neutral "He's not part of any Kuomintang adminstration based on his job or uniform."
                    visualcomprehension neutral "So you can guess why he wears that at all."
                    "Professor Po wore the insignia of the Kuomintang flag on his arm."
                    "It looked well stitched and taken care of."
                    Po "You spotted that?"
                    Po "Good eye there."
                    visualcomprehension neutral "I know."
                    "Professor Po brushed it lightly."
                    Po "I do this to preserve Dr Sun's legacy."
                    "Professor Po smirked."
                    Po "Unlike that \"Generalissimo\" Chiang."
                    "Professor Po let out a large sigh."
                    Po "Communists are the {i}worst{/i}"
                Po "I hoped they would have lost back in Fusze."
                "Professor Po cursed under his breath as he said this."
            else:
                composure "{i}Failed to focus.{/i}"
                "I tried my best to focus but something kept burning up in me."
                "It was painful to confront my own emotions."
                "The pressure of everything just kept building up."
                "Like a bag of rocks on my back. Like something kept putting in more rocks."
                "{i}Whose burdem am I carrying?{/i}"
                "The flames of stress and neuroticism just growing and expanding."
                "{i}Life feels like a fucking nightmare.{/i}"
                fang "I'm ready."
            
    Po "Well Let us start now."
    Po "The hawks want to know more about you this will information will help you reflect on what you want to do with the looming war."
    Po "War's harsh isn't it?"
    "Professor Po bit his lip and focussed on the blank piece of paper in front of him."
    fang "Yeah it is..."
    Po "Lets start off with being realistic."
    Po "Your hometown."
    Po "What is your background in terms of location?"
    Po "I know you and your family have moved places over the years..."
    Po "It's best to choose what is your go-to \"home\"."
    Po "Where is it most convenient for you to return home? What would your gut feeling say?"
    default stress = 0
    menu:
        "Peiping":

            $ fang.log("Hometown:Peiping")
            $ hometown = _("Peiping")
            fang "I'm from Peiping"
            Gu "I'd suggest you move out of Peiping."
            Gu "I mean the hawks don't care."
            Po "All they'll see is you living in this large house and stereotype you as a capitalist."
            Po "The reason why you should move out is because of the war."
            Po "There have been all sorts of conflcits ocurring on the outskirts of Peiping."
            Po "This place will be levelled down with bombs."
            Gu "Yan'an is swarming with communists otherwise I would have recommended a temporary stay there."
            Gu "My best bet would be to send you to Tsingtao or further south where the Japanese won't be able to fight through."
            Po "I'd have to be agree with Ku-hsien-sheng"
            Gu "I have a shcolarly friends all across the place who can provide you with oppurtunities for work."
            Gu "Tsingtao will be familiar to you."
            Po "Even if they do reach Tsingtao you can always go to Nanking."
            Po "What do you make of it?"
            fang "It's a pending decision."
            Po "That makes sense."
            Po "As of now both armies are mobilisng so there will be a lot of crossfire here at the inception of the war."
            Po "Back in Da-ren when there was conflict I knew that I could possibly be in danger so I had to act quick."
            Po "I buckled down at my boarding school for a few weeks."
            Po "We waited and waited as the food came in slower and slower."
            Po "It was scary but we didn't care about that."
            Po "Everyone wanted to feel a full stomach again."
            Po "Eventually I snuck out and went to the ports."
            Po "I hoarded some stuff and went back to the school."
            Po "Anyway I'll tell the rest a little later."
            Po "We have an \"interview\" here."

        "Nanking":

            $ fang.log("Hometown:Nanjing")
            $ hometown = _("Nanking")
            fang "I'm from Nanking"
            Gu "Well, the capital is a good place."
            Gu "Nationalists would fight to the death to keep it safe."
            Gu "I doubt the Japanese would get that far to Nanking anyway."
            Po "I doubt it too. I can't predict how the war will go, but the capital city will be heavily defended."
            Gu "Your hometown seem to be out of harms way and strife."
            Po "The only issue is that it's close to Shanghai."
            fang "What's wrong with that?"
            Po "It's an international settlement area."
            Po "After the Opium wars and the onset of unequal treaties an international zone was established."
            Po "It's under Kuomintang sovereignty but areas of it are allocated to the French, British etc."
            Po "While the Japanese don't have any legal right that I'm aware of they have an \"unofficial settelemt\" in Kongkew."
            Po "It's called \"Little Tokyo\"."
            Po "That means Shanghai is the gateway to Chinese territory."
            Po "If you're going to be in Nanking you have to be aware of that."
            Po "They might as well just leap frog the legal framework of the Shanghai International Zone."
            Po "War is chaotic and often..."
            Po "Unpredictable."
            "Uncle Ku has listened with extreme curiosity."
            "It seemed this was the first time he had learnt about the legal status of Shanghai."
            fang "That's so interesting."
            Po "I could be a military strategist with this much analytical skill."
            "He gave a dry laugh."
            Po "Anyway lets get going with the questions."

        "Kwangchow":

            $ fang.log("Hometown:Guangzhou")
            $ hometown = _("Kwangchow")
            fang "I'm from Kwangchow"
            Gu "Under Chen Chi-Tang?"
            Gu "I wonder if he can survive or General Chiang will have to bail him out."
            Gu "I think you're safe there, besides you'll fit in there more that here."
            Gu "Your hometown seem to be out of harms way and strife."
            fang "Guangzhou is under Chiang's direct rule now."
            Gu "Oh really?"
            Po "Didn't he take control about a year ago?"
            Po "I'm not so up to date with that."
            fang "Yes that's true."
            Po "The south is diverse isn't it?"
            "Porfessor Po has this rhetoric that made him interesting to listen to."
            Po "Can you speak Cantonese?"
            fang "Yes I can."
            Po "I think it's a beautiful language."
            "Uncle Ku made a smirk."
            Gu "No offense Po-Hsian-Sheng, I prefer Mandarin."
            "Professor Po flashed a surprised face."
            Po "How so?"
            Gu "In Cantonese there are many more tones."
            Gu "Mandarin only has four."
            Gu "I also believe in focussing on a vernacular language."
            Po "Acceptable views I guess."
            Po "But I don't realise how these points prove Cantonese is not a beautiful language."
            Po "The diveristy in tones make it much more rhythmic."
            Gu "To each their own."
            Po "Glad to disagree Ku-hsien-sheng"
            "Professor Po flashed a smile and Uncle Ku teasignly."
            Gu "Let's get on with the questions."

        "Hong-Kong":

            $ fang.log("Hometown:HongKong")
            $ hometown = _("Hong Kong")
            fang "I'm from Hong-Kong"
            Po "It is a good place."
            Po "The British may be a bit foreign to us mainlanders but at least their territories aren't at risk of being involved in a war."
            Gu "Your hometown seem to be out of harms way and strife."
            Po "I take it you are fluent in English?"
            fang "Yes, that is true."
            Po "Do you read the bible in Cantonese as well?"
            fang "Yes we have it in many languages."
            Po "It's nice to learn about the other places in this country."
            Po "It's so diverse."
            Po "Each place seems to teach you something new."
            "I seem to agree with it also."
            "A lot of cities in China are pockets of international influence from Hong-Kong to Macau to Shanghai etc."
            "At times two people in the same country feel alien to each other."
            "No wonder there's so much divisions in our society."
            "So many warlords and independent states."
            Po "Fang!"
            "I sat up quickly and faced Professor Po."
            Po "You dozed out."
            $ stress += 1
            fang "Seems to be a unending habit."
            Po "you'll grow out of it I'm sure."
            Po "I wanted to go to the next question."

        "Macau":

            $ fang.log("Hometown:Macau")
            $ hometown = _("Macau")
            fang "I'm from Macau"
            Gu "A place that won't get thrashed by war."
            Gu "Portugese don't involve themselves in wars."
            Gu "Plus they let Chiense culture flourish unlike the Guizi in Hong Kong."
            "Uncle Ku has a strong bias for Macao, he disliked how the British ran Hong Kong and prefered Portugese ruled Macao."
            Gu "Some people are born lucky I guess."
            Po "Will you go ahead and start gambling?"
            Po "Gambling is like water in Macao. A {i}necessity{/i}."
            "Professor Po gave a laugh about it."
            "Uncle Gu did not approve of gambling but laughed at this joke regardless."
            Gu "I think it is a safe place that you should consider returning to."
            Gu "Your hometown seem to be out of harms way and strife."
            Gu "I suggest you go back to your family and try to prepare what to do next."

        "Taiwan":

            $ fang.log("Hometown:Taiwan")
            $ hometown = _("Taiwan")
            fang "I'm from Taiwan"
            Gu "From the foreign devils themself."
            "He chuckles"
            Gu "They won't mess with you then I guess."
            Po "Out of curiosity..."
            Po "How have the Japanese run Taiwan?"
            menu:
                "Pretty Well":
                    pass
                "I guess alright":
                    pass
                "Not that good":
                    pass



    Po "So what are you doing in Peiping right now?"

    menu:
        "Attending school as a student.":
            $ fang.log("Reason:Student")
            play sound "sounds/stat_increase/00_stat_increase.ogg"
            "{font=fonts/eng_octin_spraypaint/octin spraypaint a rg.ttf}{color=#4fc1ff}Fang gained 3 Determination; 3 Intellect and 2 Dexterity!{/color}{/font}"
            fang "I came here to actually continue my education."
            fang "I am staying with Uncle Ku since it is close to the facilities."
            Po "I doubt schools will run under foreign occupation."
            "Professor Po gave a faint grin."
            Po "Well classes won't."
            "Professor Po raised his glass of {i}Máotái{/i} and took a sip."
            $ TL_glossary.addword('Maotai')
            "He normally didn't drink heavily but Uncle Ku had handed him this as a token of thanks for visiting me."
            "Giving such an expensive drink symbolised Uncle Ku's gratitude."
            Po "Most students back in Dongbei would just live at the boarding school."
            Po "They would not return to their families."
            "He raised the cup of {i}Máotái{/i} to his lips but didn't take a sip. {w}As if something important crossed his mind.{w=1.2}"
            Po "After the first month a few homesick students did in fact return."
            Po "No vandalism, no abusive powers and the old deposed emperor back on a throne."
            Po "Most parents made kids work back on the farms or their old shanty businesses while the Japanese and {i}Kang-te Pu Yi{/i} tried to get the old ways running again."
            "I could make out the sorrow in his face.{nw}"
            "It seemed he made himself remember something he wished to forget."
            Po "So I guess you should head back."
            Po "I think your family will need you more."
            "He looked down at his papers as he dipped the brush back into a clay pot of ink and scribed some details on a creased paper."

        "Working as a scholarly apprentice under my uncle":
            $ fang.log("Reason:Apprentice")
            play sound "sounds/stat_increase/00_stat_increase.ogg"
            "{font=fonts/eng_octin_spraypaint/octin spraypaint a rg.ttf}{color=#4fc1ff}Fang gained 3 Intellect and 3 Dexterity!{/color}{/font}"
            fang "I am working as an apprentice to my Uncle."
            Gu "The kid is quite dexterous."
            Gu "It's hard to believe he wasn't born without some miracle jade in the mouth story."
            Po "Comments like that will get you in high places."
            fang "Thank you"
            Po "anyway..."

        "Working here to send money back home.":
            $ fang.log("Reason:Working")
            $ inventory.earn(200)
            play sound "sounds/stat_increase/00_stat_increase.ogg"
            "{font=fonts/eng_octin_spraypaint/octin spraypaint a rg.ttf}{color=#4fc1ff}Fang gained 2 determination!{/color}{/font}"
            Po "what a hardworking kid."
            Gu "I agree."
            "Uncle Ku nodded with professor Po."
            "They had seemed to be harmonious in their actions.. {w}{cps=*0.5}Like they were parts of the same piece...{/cps}{w=1.2}"
            Gu "This kind of attitude sculpts heroes and leaders."
            Po "You have probably saved enough now. Have you?"
            "Working at Cheung's silkhouse paid off well. It still does"
            "This summer I had saved up enough to return home again."
            fang "yes, it is sufficient I would say."
            Po "That is great to hear"

        "Taking a break after military conscription training":
           $ fang.log("Reason:Military")
           $ inventory.earn(30)
           fang "I'm taking a break from military conscription training."
           Po "How come you weren't enlisted?"
           "Professor Po looks confused as he asks me this question."
           fang "I'm only sixteen years old as of now. I can be trained but I can't be enlisted to fight already."
           Po "Your time of birth is lucky I guess."
           fang "I guess,{w}others were rounded up forcefully and marched to camps in chains."
           "I turn my head towards Uncle Ku"
           fang "Uncle Ku paid off the recruiters."
           "He gives a smile back."
           fang "Thanks to him I don't have to become a war child."
           "Professor Po turns towards Uncle Ku as well."
           Po "{i}Pèifú{/i}{nw}"
           $ TL_glossary.addword("Peifu")
           "He had raised his {i}Máotái{/i} with both hands to show his appreciation."
           $ TL_glossary.addword("Maotai")
           "You should stay away from the military. {w}You're too young for that life."
           Po "You're also too young to watch me drink {i}Máotái{/i}"
           "He gave a hearty chuckle. His face was red from the alcohol."
           "He dipped his brush into the little clay pot of abyss-like ink."
           "You couldn't see it spin like water. It was fascinating."
           "He removed the brush and began to scribe onto his piece of paper once again."
           Po "I will lie and state that you were discharged by injury."

    Po "What belief system do you follow?"

    menu:
        "Taoism and Confucianism":
           $ fang.rel = "Taoism" 
           $ Taoist = True
           Po "You seem to be clinging on the old ways."
           "Professor Po sipped his {i}Máotái{/i} lightly before facing me."
           $ TL_glossary.addword("Maotai")
           "Bits of his face had manifested a gradient of red."
           Po "I guess the Kuomintang did a good job reinforcing tradition."
           "He sipped one again. {w}{cps=*0.5}As if something was annoying him inside{/cps}."
           Po "Confucianism is a very old principle."
           $ TL_glossary.addword("Confucianism")
           Po "I...{w}{cps=*2}just don\'t see it going anywhere in the modern era.{/cps}"
           "Uncle Ku looked at him strangely."
           Po "The \"New Life movement\" is an illusion."
           Po "I am not a \"communist\" {w}but I don't like the policies of the nationalists either."
           "Professor Po seemed engrossed with his political beliefs."
           Po "I respect your beliefs {i}Xiǎo Fāng{/i} but...{nw}"
           Po "From a philosophical and political doctrine I dislike the state being an obstacle to modernism."
           Gu "I could agree with that.{nw}"
           Gu "In english they say something along the lines of \"seperation of church and state\"."
           Gu "Still, I persist, I believe in Confucianism."
           Gu "It worked for 2000 years why can't it work for another 2000?"
           "Uncle Ku had seemed to have taken offence to Professor Po's anti-Confucian stance."
           fang "I have a neutral atttiude to Confucianism."
           fang "I think some things work and some do not."
           fang "Fillial Piety is one of my core beliefs."
           "Prossor Po smirked."
           Po "The things you say become more interesting as I get more drunk."
           "Professor Po seemed to dip his brush more sloppily and scribe less cautiously."
           Po "Fillial Piety..."
           "I hope he didn't broach the subject."
           "The fact that he wasn't sober meant that there was a chance he would bring up a topic I didn't like..."
           Po "But isn't it, like, ummm, uhh..."
           Gu "Lets get back to the itnerview."
           Gu "Now is not the time to discuss such matters."
           Po "bu-{nw}"
           Gu "Come on,"
           Gu "The poor boy has been so patient."
           Gu "Let's not waste his time."
           Gu "It's important to him to leave fast and unite with his family."
           Po "What f-{nw}"
           Gu "Just understand."
           "Uncle Gu had expertly steered the conversation away despite Professor Po's drunk demeanor manifesting."
           "In regards to professor Po, I wondered if he was capable of asking another question."
           "I hope he would have enough capaicity to finish to interview before he became too drunk."
           "Every second I'm here... it feels more dangerous."
           "Perhaps I'm prone to overthinking but I just wanted to leave Peiping."
           "I don't have the strength to persist through violence."
           "Nor do I have time to indulge in my personal family matters."
           "I would have asked Uncle Ku why he ever told Professor Po something that was supposed to be so personal to me."
           "To an extent this did piss me off."
           "Truth is these days things like total war are a biger worry than some petty gossip."
           Po "Fang!"
           if stress >0:
                Po "You dozed off again."
                Po "I used to be like that too."
                Po "I think you retreat into your thoguths a bit don't you?"
                Po "You need to calm down."
                Po "Overthing is bad."
                Po "This was you can think better and clearly."    
           else:
                Po "Stay alert a litte bit longer then you go think about whatever you want."
                Po "I'm doing my best as well."
           Po "Let's keep going."
           Gu "Wait,"
           jump taoism_breakaway
        "Buddhism":
           $ fang.rel = "Buddhism" 
           $ Buddhist = True
           Po "Ah...{w}{cps=*0.9}A fellow buddhist.{/cps}"
           "Professor Po sipped his {i}Máotái{/i} lightly before facing me."
           "Bits of his face had manifested a gradient of red."
           Po "Have you ever heard of {i}Dhammapada{/i}? {w}{cps=*1.5}the poem of Buddha awakening?{/cps}"
           jump buddhism_breakaway
        "Christianity":
            $ fang.rel = "Christianity"
            $ Christian = True
            if fang.hasLog("Hometown:HongKong"):
                Po "You being from Hong Kong I wouldn't be suprised at that perspective."
            Po "Do you like listening to hymns?"
            "Professor Po held his {i}Máotái{/i} up to the sunlight where he could see it tinker."
            "I nodded back towards him."
            Po "I love latin choir and hymns."
            Po "It just moves me to the core."

label taoism_breakaway:
Gu "{i}Fang{/i}"
Gu "Did you read the old poems from {i}\"Tao Te Ch\'ing\"{/i}?"
$ TL_glossary.addword("Tao Te Ch\'ing")
Gu "Would you like to hear a poem from {i}Tao Te Ch\'ing{/i}?"
Gu "{i}Tao the water way{/i}"
menu:
    "Yes" if not TL_poem.haspoem("Tao The Water Way"):
        fang "Yes I would like to hear it."
        "Professor Po was now heavily intoxicated and slumping in his chair as he strained to keep focus."
        Gu "I don't think he will ming me reciting a poem of backwards tradition."
        "Uncle Ku smirked at Po."
        Gu "{i}The best of men is like water;{/i}"
        Gu "{i}Water benefits all things{/i}"
        Gu "{i}And does not compete with them.{/i}"
        Gu "{i}It dwells in (the lowly) places that all disdain –{/i}"
        Gu "{i}Wherein it comes near to the Tao.{/i}"
        Gu "{i}In his dwelling, (the Sage) loves the (lowly) earth;{/i}"
        Gu "{i}In his heart, he loves what is profound;{/i}"
        Gu "{i}In his relations with others, he loves kindness;{/i}"
        Gu "{i}In his words, he loves sincerity;{/i}"
        Gu "{i}In government, he loves peace;{/i}"
        Gu "{i}In business affairs, he loves ability;{/i}"
        Gu "{i}In his actions, he loves choosing the right time.{/i}"
        Gu "{i}It is because he does not contend{/i}"
        Gu "{i}That he is without reproach.{/i}"
        $ TL_poem.addpoem("Tao The Water Way")
        fang "That's deep."
        Gu "It's life."
        Gu "I noticed that you overthink a lot."
        Gu "You have to be able to understand yourself if you want to be effecient."
        Gu "So you have to understand your feelings and learn how to protect yourself from bottling up or lashing out."
        fang "Thanks for that."
        Gu "I think everyone needs some calming pep talk."
        fang "I couln't agree less."
        "I looked over to Professor Po who didn't have the strength to clutch his cup properly."
        jump beijing_interview_after
    "No" if not haspoem("Tao The Water Way"):
        $ not_hear_water_way = True
        fang "I think maybe later.. {w=1}When this interview is finished."
        Po "The boy knows his priorities."
        "Professor Po was begining to talk more openly and slurredly."
        fang "Let's go to the next question."
        jump beijing_interview_after
    "No" if haspoem("Tao The Water Way"):
        fang "I already know the poem."
        jump beijing_interview_after

label buddhism_breakaway:

menu:
    "Yes" if persistent.agneepath:
        Po "Well that's great!"
        Po "There are so many out there."
        "Professor Po was beginning to look like he had too much to drink."
        jump beijing_interview_after

    "no" if not persistent.agneepath:
        $ persistent.agneepath = True
        Po "It is a great poem."
        "Professor Po had becoem slightly{cps=*0.2}...{/cps} {w=1}intoxicated by this point."
        "Despite that it seemed that Professor Po was sober enough to recite Buddhist poetry."
        Po "{i}{cps=*0.4}Through the round of many births I roamed{/cps}{/i}{nw}"
        "Professor Po had in fact placed his {i}{font=fonts/chi_pinyin/cpinyin0.ttf}Máotái{/font}{/i} down as he recited this."
        Po "{i}{cps=*0.4}without reward,{w=2} without rest,{/cps}{/i}{nw}"
        Po "{i}{cps=*0.4}seeking the house-builder.{/cps}{/i}{nw}"
        Po "{i}{cps=*0.4}Painful is birth{/cps}{/i}{nw}"
        Po "{i}{cps=*0.4}again & again.{/cps}{/i}{nw}"
        Po "{i}{cps=*0.4}House-builder, you're seen!{/cps}{/i}{nw}"
        Po "{i}{cps=*0.4}You will not build a house again.{/cps}{/i}{nw}"
        Po "{i}{cps=*-0.4}All your rafters broken,{/cps}{/i}{nw}"
        Po "{i}{cps=*0.4}the ridge pole destroyed,{/cps}{/i}{nw}"
        Po "{i}{cps=*0.4}gone to the Unformed{/cps}{cps=*0.2}...{/cps}{/i}{nw}"
        Po "{i}{cps=*0.4}the mind has come to the end of craving.{/cps}{/i}{nw}"
        $ persistent.unlocked_poem.append('Dhammapada')
        $ msg.msg("New poem unlocked:Dhammapada")
        "Professor seemed to become internalized during the recital of this poem."
        "In his red intoxicated face, you could see his expression of grattitude and servility."
        jump beijing_interview_after

label beijing_interview_after:
"Professor Po seemed to increasingly become unable to stay...{w=1.0}sober."
Gu "He might need to take some rest."
Gu "He grew up around the drink."
"Uncle Ku grabbed Professor Po by his arms and mounted him on his back."
"Professor Po only slurred some words as Uncle Ku dragged him to a guest room."
"I guess{w=1.0} the interview will be conducted later."
"I turned my head around to the Taoist Shrine."
"It consisted of a {i}Yīnyáng{/i} emblem,{w=0.5} A candle that possessed a mediocre flame,{w=0.5} and a copy of {i}Tao Te Ch\'ing{/i}."
$ TL_glossary.addword("Yīnyáng")
"I stood up from the uncomfortable chair and approached the shrine."
"It was peaceful to stand before the shrine."
"I wasn't required to announce my presence."
"Part of me was afraid of the new world I had stepped into."
"Will the gods protect me?"
"Thoughts invaded my mind as I looked at the shrine."
if fang.RandomCheck("reaction", 2,4, ):
    correction neutral "But you have to stay focussed."
    correction neutral "Overtinking will not be useful to you this way."
    correction neutral "You should try to calm down and think."
    $ stress -= 1
    $ msg.msg("Stress reduced.")
"Lúgōuqiáo Shìbiàn had begun only a few days ago."
$ TL_history_log.addevent("Marco-Polo Incident")
$ CHI.logevent("1937-7-7: Marco-Polo Incident", False)
$ JAP.logevent("1937-7-7: Marco-Polo Incident", False)
$ PGR.logevent("1937-7-7: Marco-Polo Incident", False)
"Uncle Ku ambled out of the guest room with his hands concealed under his robes."
"He grimaced slightly at the situation."
Gu "I don't know what will come out of this."
"He seemed to say that calmly."
"Something so important...{w=1} taken so lightly."
fang "That's fine...{w=1} I can deal with that."
"Uncle Ku sat down at the shrine and opened Tao Te Ch\'ing."
"He was a commited reader and devotee."
Gu "You should go outside and find something to do."
"I looked back at Uncle Ku."
"He could only sigh."
"That was all he could do."
Gu "{cps=*0.4}Don't worry{/cps}"
Gu "We can get ut of here in time."
"Uncle Ku would reguarly meet in the village centre and talk to elders and intelectuals about current events."
Gu "Japan is mobilising an army, they won't go further than Peiping-Tientsen, {w=1}I've heard."
"Uncle Ku felt hopeless."
"Staring into those eyes felt like lies."
fang "They keep taking from us."
Gu "I know..."
"Uncle Ku didn't believe in violence,{w=1.0} he didn't feel the need to fight back."
fang "Now we have a drunk, a looming war and what more!" with sshake
$ Gu.mood = __("Upset")
$ msg.msg("Ku did not like that.")
"I had lost my composure."
"I could see Uncle Ku's reaction to me lashing out after such a long time."
"Pressure that had built up from everything had finally burst the bottle."
"Uncle Ku looked at me solenmly."
Gu "{cps=*0.4}I'm sorry,{w=1} Fang.{/cps}"
fang "I'm sorry too."
"I turned my back and walked out of the door."
Gu "If there is a air raid just run straight to some air raid shelter."
Gu "If you find a German one, priorotise that."
Gu "The German peoples don't get harassed by {i}guizi{/i}."
$ TL_glossary.addword("Guizi")
"I had crossed the Er-men."
$ TL_glossary.addword("Er-Men")
"I kept on walking until I passed through the Da-men."
$ TL_glossary.addword("Da-Men")
default activities_left = 3
"Outside was a little garden where my Great Grandfather had planted a Sakura Tree for Sun Yat Sen's new era of the Republic."
"It's a real shame I never even learnt his name despite knowing how well known he was in this local place."
"My great grandfather disliked the Qing as they were Manchus as opposed to the Ming who were a Han Chinese dynasty."
"He had a wealthy wine business which gave him the money to buy a large {i}Siheyuan{/i}"
$ TL_glossary.addword("sìhéyuàn")
"The Sakura was planted to mark the growth a new era without the Qing."
"The Sakura plant was also foreign and thus showcased his wealth when he had it planted."
"Everything I ever learnt about him indicated that...{w=1} wealth controlled his choices."
"Sadly he died before he realised how the Republic failed China."
"{cps=*0.45}or the shortlived Empire before the warlord era.{/cps}"
"Beyond the Sakura tree was a pond he had hired workers to build."
"Apart from showing off his wealth he would also use this pond to grow Lotuses."
"He would grow them in bulks and sell them to Buddhists and Buddhist temples in which he would get blessed and make money."
"now..{w=1} he wasn't shallow that he did that for profit."
"He was a devout buddhist."
"He would donate large sums of charity to people in need and temples."
"I kept walking on until the pond came into view."
"Black and white pictures showed budding and blossomed Lotuses on the surface of the water."
"Earlier photos even had swans in them."
"What I saw in front of me was neither."
"The water was brown, murky and thick."
"It was hard to believe anything nice was in there anymore."
"Uncle Ku refused to spend his inheritance money on refurbishing things around the house."
"He dared not indulge in materialism and wealth of any kind."
"He preferred and carried a metaphorical banner of being a rich man in poor clothing."
"I stared at the pathetic pond."
"The pond that gave up on life."
"Gave up on struggling."
Lc "He should have hired people to dig a well." with sshake
"I turned around fast before facing Lao-Chang."
"We called him that because he was an old milkman who didn't want to retire.{nw}"
"Hence the name \"old Chang\"."
fang "I would agree."
fang "That would have been better for the community."
Lc "We have a groundwater well over on the other side that was dug by Ma Wen's father."
Lc "It's near the animals a lot, people are scared that they'll find chicken shit."
fang "Uncle Ku is a miser wearing the mask of Taoism."
Lc "That's your opinion."
Lc "I'm sure if we held a petition he would support it."
fang "Really?"
"I wasn't sure if that would suspend my disbelief."
Lc "Calling him a miser won't do him justice."
Lc "He isn't the kind of person who spends money on themselves."
Lc "He would rather spend it to support others."
"He was old enough to know how everyone functioned in this community."
fang "If you ask him, he will."
"Lao Chang laughed."
Lc "You remind me of your grandpa."
"Lao Chang sat down on the damp grass next to me that faced the miserable pond."
fang "How so?"
Lc "Whenever there was war...{w=1} the fella just got into a bad mood."
Lc "During the northern expedition when Chiang Chieh-shih tried to take back from those warlords.."
Lc "He had a sulky mood for a week."
"Lao Chang dug his hand into the basket tied to his bicycle and took out a rice snack."
Lc "You see. {w=1}His sister was back in Kwangchow where this crazy reunifier was wailing war and unifying cities under his control."
Lc "He wouldn't get any of her letters from kwangchow so he sulked."
"Lao Chang bit into his rice snack and chewed it open mouthed."
Lc "He sent out a lot of letters to."
Lc "I wonder where they went."
"Lao Chang gazed at the shitty pond. Like it was beautiful as my Great-Grandfather had left it."
Lc "Eventually you got this shithole situation where there are so many warlords and everyone wants to crown a new China."
Lc "Who do you think will crown a new China?"
menu:
    "Chiang Chie Shih":
        fang "I think Chiang Chie Shih"
        fang "He has proclaimed central government."
        fang "The warlords even cooperate with him."
        fang "It's more or less if he can centralize power to one form of government."
        Lc "That's a good bet."
        Lc "The national Revolutionary Army rolled over everyone in the Northern Camapaign."
        Lc "If they keep those troops moralised Dr Sun's democracy will come back to us."
    "Wang Ching Wei":
        fang "Chiang Chi Shih seems to be too right wing and authoritarian."
        fang "He doesn't cooperate with appeasing the Japanese or the warlords."
        fang "Personally Wang Ching Wei's left Kuomintang will be more liked by foreign nations."
        Lc "The left Kuomintang are an interesting bunch."
        Lc "I can't read so I never get much info about politics."
        fang "Wang Ching Wei was close with Dr Sun in the first republic."
        fang "He lost the power struggle in the Kuomintang to Chiang Chie Shih."
        fang "I think he thinks well."
        Lc "I think he's a bit too crazy for the Guizi."
        Lc "He prefers to appease a rising colonial power."
        Lc "That's basically feeding a pig a little snack so it won't eat a lot."
        fang "I guess, I understand what you mean."
        Lc "Plus Wang doesn't ever cooperate with Chiang, I think Wang will leave and form his own little thing like he did back in Wuhan."
        fang "I think so too."
        Lc "Ever since he failed with cooperating with the Yan'an communists, he's becoming more and more right wing."
        Lc "Ever since the republic was established, the biggest worry is extremism."
        "Lao Chang took a bit out of his rice snack."
        Lc "Everyone is thinking \"What form of government is fit to rule 460 million people?\"."
        Lc "Then they all start shooting each other."
        "Lao Chang gives a hearty laugh at this satirical joke he made."
        "I grin in response."
        fang "but I think we should at least appease until our military is ready to right Japan."
        fang "I don't know if full scale war will happen from the Marco-Polo bridge incident..{w=1}but it is imminent.{nw}"
        fang "That's for sure."
        Lc "I guess, it's depressing we got to live through this."
    "Li Tsung-Jen":
        fang "I think Li Tsung-Jen"
        Lc "The Kwanghsi leader?"
        fang "He and  Pai Ch'ung-hsi were the ones that captured Beijing."
        fang "I think they have quite an influence over the central government."
        fang "I wouldn't be suprised if Li Tsung-Jen was reinstated as a general and rose up the ranks in Chiang's government."
        Lc "He is quite capable."
        Lc "I like how he works."
    "Mao Tse-Tung":
        fang "The communists were supposed to be kicked out of Yan'an."
        fang "After Chang Hsueh-liang took Chiang hostage to focus on the Japanese they stopped attacking the communists."
        fang "Now that they are thriving and gaining support I think they have a chance after the war to seize victory against an unstabke governmnet."
        fang "I'm no communist, but I think when all this ends, Mao's face will be on the Tiananmen Square."
        Lc "His rhetoric is good also."
        "Lao Chang pulled out some grass as he munched on another bite of his rice snack."
        Lc "Those poor peasants want land, freedom and empowerment."
        Lc "The communist revolution gives them that oppurtunity."
        fang "How do you know so much about the communists?"
        "Lao Chang munched on his snack and turned to face me."
        Lc "The village center always tells what they're up to so he can undermine them and their anti-buddhist, anti-taoist philosophies."
        Lc "It looks like foolish advertising to me."
        "Lao Chang took another bite from his rice snack."
        Lc "I think I'm happy giving milk to people everyday."
        Lc "My ribs might be showing a lot, but my good deeds will grant me something good in my next life."
        Lc "Even if there isn't a next life at least I'll be happy in this one."
        Lc "Who knows maybe my hard work will pay off and I'll live in a palace of gold even."
        "Lao Chang gave a dry hearty laugh."
    "I don't know":
        fang "I don't know."
        fang "Normally I don't engage in politics so much."
        Lc "Eh?"
        Lc "That's fine."
        Lc "I don't have an interest."
        Lc "If I know anything about politics it's because Guo Heng's father always shouts about it in the village center over some tea."
        Lc "He's an avid historian who sits at home all day like your Uncle and does scholary stuff."
        "Lao Chang takes a bit from rice snack."
        Lc "but I get you. Don't stick your head into that stuff too much."
"Lao Chang stood up and patted off the back of his pants that had attracted clumps of damp soil."
Lc "I gotta get going."
Lc "Wanna buy a bottle of milk?"
Lc "You can take it home early."
fang "No thanks, I don't have cash."
fang "Uncle Ku will pay for it at the doorstep."
Lc "I guess that suits it."
"Lao Chang grabbed the handles of his makeshift bike and pushed it around."
"THe odd thing about Lao Chang was that he would have a bike he would never ride."
"He would just use the basket and push it for ease."
"Since he was twice the age of Uncle Ku it made sense."
"The bicycle was also too small for him. {w=1}I would have assumed that this was something thrown away by the child of some wealthy family who grew out of the bike."
"I observed Lao Chang walk off in the distance, pushing his bike and the flicking the rusted bell that wouldn't make any sound. {w=1}That was because there was nothing for it to strike against."
"I turned and began to walk the other way."
"It was a five minute walk away from the village center."
"Most young boys or able men would not be welcome there."
"This was because young or able men would get kidnapped by the Kuomintang army and chained and walked down to military headquarters to forcefully enlist."
"These days the reports of Kuomintang barging and taking had gone down."
"My shoes rubbed in the dirt pass as I ambled on."
"In 2 weekss of residing in this district I had started to memorise a map of the place."
"There were a few facilities I was going to walk past."
"The most interesting was the brothel."
"The sex industry had grown in Manchuria and many boys would talk about it in the alley ways."
"Over here the brothel was something that you should not be seen entering and leaving if you wanted to have a sense of dignity."
"This brothel was known as a {i}Chang San{/i} brothel."
$ TL_glossary.addword("Chang San")
"It was like an artistic form of prostituition in which the prositute would play the lyre, do calligraphy and do paintings."
"I think it was a progressive way to humanise prostitutes."
"Personally I have never interacted with a prosititute."
"Nor do I have a good enough reason to."
"I just don't understand their stigma in society."
"Many of the girls are of varying ages from 13 to early 40s."
"The place was not regulated much with ramapnt bribing and blackmail."
prostitute "Hey Fang!"
"I turned to see her sitting in a chair outside the door."
fang "Hey"
"I did a faint wave."
prostitute "Is that a wave?"
prostitute "Relax, {w=1}waving back to me won't make me pounce on you."
"She crossed her arms and smiled at me."
prostitute "I have my principles."
"She grinned."
"I didn't know how to respond to her."
"All I could give her was an awkward grin."
"She giggled at my response."
prostitute "Hard to believe{cps=*0.4}...{/cps}{w=1}Some {i}whore{/i} has a sense of principle. Right?"
"I looked at the ground."
"At this point I had trouble making any form of eye contact."
prostitute "Don't feel bad, little brother."
prostitute "I mean, my rules are I don't drink,{w=1} I don't smoke and I don't condone violence."
"She leaned back on her chair against the chipped brick blocks."
prostitute "I have a band of sisters to look after. People in my situation."
"I couldn't keep being judged like this."
"I felt a need to spit it out."
fang "I don't see whatever you're doing as a bad thing."
"I interrupted her mid sentence."
"She gave a strange look."
prostitute "Litte brother, if some alleyboy said those words to me, I'd think it's some ploy for pity lovemaking."
prostitute "I know my stigma,{cps=*1.2} don't pity me..{/cps}"
"She was still in a good mood for some odd reason."
prostitute "You know, the conflict happening up there doesn't bother me."
prostitute "If the Japanese do take over, we will just be required to service their soldiers instead."
"She closed her eyes to laugh at herself."
prostitute "I mean the industry is booming in Dong-bei, so things around here will change I guess."
fang "Alley boys told you right?"
prostitute "I mean who else will?"
prostitute "it's nice talking to a non-pervert for once."
prostitute "It's amazing how people can have fruitful conversations if you give them a chance. Right Fang?"
fang "Right."
"How did she know my name?"
fang "How do you know my name?"
prostitute "The other girls you flirt with when they sit outside told me so."
"I felt my face go red."
prostitute "You talk better to the ones your age."
prostitute "I'm only a few years your senior. {w=1}A solid 19 year old."
prostitute "You're disappointed. Aren't you?"
"She was teasing me."
prostitute "By the way, my name is Wang Yuelan."
prostitute "If you ever need shelter, just ask {i}Xiao Wen{/i} to share the room."
"She laughed as she opened the door and walked inside."
if fang.RandomCheck("rhetoric", 3,4, True, 0.35, True):
    rhetoric "She's implying you should use their services if you need shelter."
    rhetoric "After all you will {b}stay the night{/b} there by any way."
    vice neutral "Well would you?"
    menu:
        "I don't indulge in such vices.":
            vice neutral "Playing good guy?"
            vice neutral "What a bore."
            vice neutral "I guess it's your \"choice\"."
        "Maybe when I'm more \"curious\".":
            vice neutral "Vice would be proud to hear \"this\"."
            vice neutral "It's human to have such desires."
"Interesting indeed."
"They were an interesting bunch,{w=1} strange but interesting."
"I kept on walking along the dirt path."
"The ambient noises from the brothel faded away with my distance."
"I kept walking on."
"Each step one by one."
"The next facility I would see would be the winery my Great Grandpa owned."
"Uncle Ku had sold it when he inherited it from his father."
"Uncle Ku didn't want to support himself by destroying the lives of addicts."
"At first he kept it out of operation."
"It would sit there 5-6 years...{w=1}undisturbed."
"Then officials would come and start ordering him to do something productive with that land and facilities."
"After a few months he sold it off to some businessman from Shanghai who wished to expand their winery business."
"Now I walk past it and just look at how many cycles this building has experienced."
"I was never told why this building was built intially, since my Great Grandfather just decided to occupy this empty place for good business."
"His father ran a little business from his home.{w=1}So my Great Grandpa decided what to do,"
"He moved all his stuff there and took care of it."
"Eventually people began to think this abandoned building didn't host any curse or haunted by any angry spirits."
"Some wealthy people like the Ma family invested in the winery and it grew bigger."
"In about 3 years the bulding had been expanded to four times its intial size."
"Over 70 people worked here for good pay."
"My Great Grandpa built an expensive Siheyuan and began to live lavishly like the Ma family."
"He died believing resourcefulness and willpower outperforms fate."
"I would get told all about this from the locals like Lao Chang or Ah-Mei the educated daughter of a noble family residing here."
"Eventually passing the collosal winery I began to see the village centre in sight."
"It wasn't a centre where you would assume it was a meeting spot."
"It was a noodle shop run by the Guo family."
"Everyone would come and eat there once in a while and that became the de-facto village centre."
"It was run by two brothers around my age."
"The older was Guo Heng, who took over the shop when his father passed away from a stroke two years ago."
"He raised his younger brother to learn to cook as well."
"Eventually they got their skills developed and Guo Heng got to send his brother \"Guo He\" to school."
"I have met Guo Heng only a few times,{w=0.5} but he is very interesting to talk to."
"He has developed a passion for making all kinds of noodles."
"Last time I visited him he showed me his father's recipe that had been handed down for god knows how long."
"He offered to employ me to his noodle shop if I ever needed a place to work."
"Despite being 23 years old Guo Heng was arguably graying from his stress.{w=1} Something he always loved joking about with the other villagers."
"The noodle shop even had a banner which would ostentaciously show off its wealth and success."
"In short, if there was any celebration, meeting, or festival, Guo's noodle shop was the place."
"Mostly because it was the most central and most convenint for everyone to meet at."
"I passed through and entered the store."
"Guo Heng had sat on a table and was appying a dirty rag to wipe the sweat off his face."
"The summer sun was strong and it didn't help he cooked behind a fire all day."
"Guo Heng seemed to age faster everytime I visited him."
"His body had become more built and skinny while his face became browner with more wrinkles."
"His hair had remained the same, {w=1}Little whisks of grey popping out once in an occassional spot."
"Guo Heng looked up at me with his brown eyes that resembled foreign manufactured chocolate."
Gh "Fang!{w=1}{nw}"
"I sat down opposite on the same table he was sitting at."
fang "Hey, Heng"
"It was midday and the sun was now forcing its heated will on us like spears."
$ TL_datetime.timepass()
"At the highest point in the sky, a false inferno had formed."
fang "You must hate the sun so much if you go through this everyday."
"Guo Heng gave a smirk and dabbed his white dirtied rag on his face."
"His shirt had wet patches near his armpits and chest."
Gh "I think its fair."
fang "How is this fair?"
"Guo Heng was quite wise because the elders would gather here and include him in philosophical talks."
Gh "There are two things in this world which are fair."
Gh "THese two things never judge...{w=1}never discriminate."
"He dabbed the cloth on his face again."
Gh "The first is death. In this world God and the Devil may judge you, but death will come for you, no matter how good,{w=1}how bad, or whatever you are."
Gh "Death doesn't pick favourites."
Gh "The Second is the sun."
Gh "For Aeons the Sun had given light regardless of the morality of the creature receiving it."
Gh "The sun when it's too hot will feel this way to everyone."
Gh "If the sun isn't judging than whatever the sun does,{w=1}is fair."
fang "You really learn some interesting stuff from those elders."
Gh "I know right."
Gh "They don't have anything to do, so i give them discounted noodles and educate myself."
"I looked up at the sky"
"It was clear and cloudless."
fang "Don't you get worried about the Japanese?"
"Heng looked up to the sky."
Gh "I heard they're readying air raid shelters because the Japanese are mobilsing for a full attack."
Gh "Maybe I'll have to learn to cook Ramen."
fang "What about your younger brother?"
Gh "I'm planning to send him to Nanking where he will be safer."
"Heng dabbed the cloth on his face again."
"His hair had beads of sweat bouncing but never dropping off."
fang "Really?"
Gh "It's a good idea to evacuate before they start fighting."
Gh "Ma Wen told me that the Shanghai International Zone would become a passage of entrance for the Japanese."
Gh "He advised me not to send Guo He to Shanghai."
Gh "Hence I chose Nanking."
Gh "The Japanese would probably confiscate the shop and make me do work without profit."
fang "That is true."
fang "I'm from [hometown!t]"
if fang.hasLog("Hometown:Taiwan"):
    fang "I can't go back to Taiwan."
    fang "They won't believe me since I'm crossing over from the Mainland."
    fang "I won't see my family till the end of the war."
    Gh "I get your pain."
    Gh "I think you should go to Nanking."
    Gh "THat way Guo He is safe with you."
    fang "You really think so?"
    "Guo Heng gave a slight nod."
    "He was willowed and his left leg had to limp."
    "I could see why he couldn't leave as easily as he said it."
    Gh "So why did you leave Taiwan in te first place?"
    fang "because I was able to."
    fang "I just wanted to keep in touch with my history."
    "Guo Heng nodded."
    Gh "Which part of Taiwan are you from?"
    fang "Taipei, the capital of the province."
    Gh "Have you ever been to Kaohshiung?"
    fang "No, I haven't."
    Gh "I heard it's quite prosperous."
    fang "Me too."
    fang "What about Uncle Ku?"
    Gh "You should talk to him."
    Gh "I'm not sure if he'll go with you."
    fang "yeah, I guess I will have to talk to him about it."
    Gh "Want to talk about it later tonight?"
    menu:
        "I might consider it.":
            $ promise_Gh_talk_escape = True
            fang "I think it's a good idea."

        "I don't think so.":
            fang "I don't know about this idea."
    jump GH_main_convo
elif fang.hasLog("Hometown:Macau"):
    Gh "Gambling is like water there.{w=1}Isn't it?"
    "It seems everybody had this stereotype."
    fang "I never grew up around the casinos."
    Gh "I guess that's a good thing."
    Gh "What is it like there?"
    Gh "I never hear much about it."
    fang "It's two Islands with lots of ships."
    fang "You never see an empty shoreline..{w=1}Like ever."
    fang "Even in 1930 when the world was hit by the Great Depression, ships were still fishing."
    fang "Fishing is a big thing there."
    "Guo Heng listened to what I said with interest."
    fang "The name was a language barrier between the locals and the Portugese arrivers."
    fang "When asked what this place was called the locals told them {i}Ma-kok{/i}."
    $ TL_glossary.addword("Ma-Kok")
    fang "Do you know why?"
    "Guo Heng shook his head."
    fang "A-Ma is the goddess that looked after the harbor and the waters of \"Macau\"."
    fang "They had a well known temple built with her after A-Ma."
    fang "To put it short,{w=1} They thought that the Portugese were asking the name of the Temple which was {i}Ma-Kok{/i} at the time."
    "Guo Heng seemed stunned from all of this."
    Gh "That's the same story with Japan."
    "We both laughed as he mentioned it."
    fang "I also forgot to tell you,"
    "Guo Heng settled back down again."
    fang "The portugese also imported labour from its colonies in India so Sikh Policeman are common there."
    fang "THey have a reputation for being bearded and burly."
    "I began to think what else to tell him."
    fang "Everything else is the same as everywhere else in China."
    "Guo Heng nodded."
    Gh "Does Macao have a dialect like Peiping?"
    fang "Yeah, we have Patua."
    Gh "Can you speak Patua?"
    fang "A bit."
    fang "My family can, but I was never taught it. I was only taught Mandarin."
    fang "If I return, I plan to learn it."
    Gh "It's nice to keep in touch with your ancestral tongue."
    Gh "My family have lived here for generations."
    Gh "The Peiping Dialect is in my blood."
    Gh "Sorry if you don't understand what we say, force of habit."
    fang "It's fine. I'm getting used to it."
    Gh "Is your dialect a mix of Portugese and Cantonese?"
    "I nod to him."
    Gh "Thats good."
    jump GH_main_convo
elif fang.hasLog("Hometown:Guangzhou"):
    Gh "Kwangchow is an interesting place."
    Gh "By the way, what has the political situation been for Kwangchow like?"
    fang "hmmm"
    fang "It's gone from Chen Chi-Tang to direct rule under Chiang Chie-Shih."
    fang "So I guess it's united with the central government."
    Gh "That's good to hear."
    Gh "Do you speak the language of Canton?"
    fang "Of course."
    "Guo Heng nods at me."
    Gh "I would have learnt it if I had the chance."
    Gh "How did you learn Mandarin?"
    fang "My parents made me learn the national language."
    fang "They wanted me to be able to communicate in the national language."
    "Guo Heng nods to me."
    fang "Did you know that the founding fathers of the Republic had a debate on the National Language?"
    "Guo Heng shakes his head."
    Gh "No."
    fang "Cantonese lost by one vote.There was an odd number of people in the room. Mandarin became official by one vote."
    "Guo Heng's eyes widened."
    Gh "I would speak Cantonese?"
    fang "Eventually, the central government can't enforce the national language yet, not with the threat of war shadowing them."
    fang "If you recite ancient poetry in Cantonese then it rhymes more than if you would have used Mandarin."
    fang "People have been researching languages and it seems that Mandarin came around under the Mongol rule which was 700 years ago."
    fang "Cantonese has been estimated to be much older. Like 1900 Years or something."
    fang "Don't quote me on it, but what do you think?"
    "Guo Heng dabbed his face with the rag."
    "He was thinking deeply."
    Gh "It makes sense to me, I think everyone should keep their ancestral tongue with them."
    "Guo Heng flashed a smile."
    Gh "Can you say something in Cantonese right now?"
    rhetoric "How much {b}do{/b} you remember?"
    rhetoric "It's become rusty hasn't it?"
    menu:
        "I'll show you alright.":
            rhetoric "Well show me if you want to so bad."
            if fang.RandomCheck("rhetorics", 5,7):
                fang "{i}gwai ngam ngaan{/i}"
                rhetoric "Congrats on your native tongue."
                Gh "Wow, it really sounds nothing like Mandarin."
                Gh "Crazy how diverse this country is."
                fang "I know."
                Gh "Crazier to think one vote chose what language I'm speaking now."
            else:
                fang ""
        "Maybe you're right.":
            rhetoric "Brush up on your cantonese before you try anything stupid."
            rhetoric "It's your mother tongue anyway."
    jump GH_main_convo
elif fang.hasLog("Hometown:Nanjing"):
    Gh "The capital itself."
    Gh "What is it like there?"
    "Guo Heng applied the rag to his sweaty face again."
    fang "Nanking in it's name means \"Southern Capital\"."
    fang "The first time it ruled a united China was in the Ming Dynasty."
    fang "It's a nice place to live overall."
    fang "It has a powerful inland port and it's close to Shanghai."
    fang "If you're rich then you're like a foreigner.{w=1} You dress pretty or look handsome."
    fang "There's a lot of people there and you even have western Churches propped up in some places of the city."
    fang "Due to these churches, chinese children of Christian believers learn English well and proficiently."
    "Guo Heng looked at me bewildered."
    Gh "Can you speak English?"
    "He looked so excited for some reason."
    fang "A bit,{w=1} I can communicate a good amount with some American residents."
    Gh "What other kind sof foreigners are there in Nanking?"
    "I sat back and thought a little."
    fang "You have German businessmen from the German Reich with their families that settle her to manage German businesses in China."
    fang "Some German military officiers also train Chinese troops, like General Alexander von Falkenhausen."
    fang "He is the military advisor to Chiang Chieh-Shih for their joint military reform program."
    fang "You have Japanese people too, who initially settled in the Japanese sector of Shanghai and moved to Nanking but you don't see them around too often."
    fang "Other europeans are rare to see, apart from some British who do business with Americans."
    Gh "I guess Nanking is becoming a global city."
    fang "I'd say the same thing."
    Gh "At least foreigners are cooperating rather than invading us.{w=1} Apart from Japan."
    "Guo Heng cursed under his breath."
    "He dabbed the rag once again."
    Gh "Is there anything special in the capital city of the republic?"
    fang "There is a statue of Chiang Chieh-Shih in the middle of the city."
    Gh "What about Dr Sun?"
    fang "He doesn't need a statue."
    fang "He has a big Mausoleum called \"Sun Yat-sen Mausoleum\" which I think gives his legacy justice."
    Gh "What's in the Mausoleum now?"
    fang "A marble sarcophagus."
    fang "and a ceiling with the Kuomintang sun stretching above."
    jump GH_main_convo
elif fang.hasLog("Hometown:HongKong"):
    Gh "In Pu Tong Hua we call it \"Xiang Gang\"."
    fang "That's something new I guess."
    Gh "What are the British like there?"
    fang "They segregate themselves from us."
    fang "The most interaction I see is from horny sailors in the coastal nightclubs and bars."
    fang "The stumble along the street and puke while they take some girl home for the night."
    "Guo Heng gave a disapproving nod as heheard this."
    fang "They do have good schools and insituitions. I learnt English there and read the Holy Bible in Cantonese."
    Gh "They translated the bible into Cantonese?"
    "I give him a light nod."
    Gh "That's amazing."
    fang "I was shocked as well."
    fang "They made me read the whole thing."
    Gh "Oh I see."
    Gh "Did you like it?"
    menu:
        "Yes":
            fang "Yes I did like it."
            Gh "How long did it take to finish it？"
            fang "A few years."
            Gh "Was it that long?"
            fang "I read it many times from front cover to back cover over my schooling years."
            fang "but I never understood it."
            fang "It took me a few years to understand the concept."
            Gh "In God's eyes all humans are born as a fool."
            "I silently nod to him."
            Gh "I thin there is some higher power."
            Gh "I don't think its sentient."
            Gh "The closest thing I consider a God is the good old sun."
            "Guo Heng grimaced as the rays of sunlight painted his face."

        "No":
            fang "To be honest...{w=1} I didn't really."
            Gh "That's fine."
            Gh "Not everything is for everyone."
            Gh "I normally just keep to myself."
            Gh "Sometimes I want to live like Lao Chang."
            Gh "He loves delivering milk."
            Gh "but most people like him at one point had to learn to love their situation."
            Gh "I will also,{w=1} Some noodle-maker with a small shop, I will learn to love this place more."
    "There was some strange silence."
    "Awkward and ominous."
    "Guo Heng looks at me with a grin."
    Gh "Want something to eat later?"
    Gh "Its on me."
    fang "No thanks but I appreciate the hospitality."
    "Guo heng gave a beaming smile at this."
    Gh "How much got on you?"
    fang "[current_money] Fabi."
    Gh "How about I give you a discount?"
    jump GH_main_convo
elif fang.hasLog("Hometown:Peiping"):
    fang "I am from Peiping."
    "Technically in between Tientsin and Peiping."
    Gh "But you seem new to this place."
    "He was right."
    "For only two weeks I had stayed here with Uncle Ku."
    "I felt I couldn't fit in."
    "I never knew why..."
    menu:
        "Come up with some reasons":
            if fang.RandomCheck("conceptualization", 2,4, True, 0.35, False):
                fang "There's two reasons to explain that."
                fang "Firstly my family has a habit of moving across China for different jobs and oppurutunities."
                fang "Secondly all my experience of Peiping was South of it where you could consider it a part of Tientsen.{w=1} So I guess overall I lack much experience if any about living in Peiping."
            else:
                "Failed to come up with a reason."
                fang "I don't know why I don't fit in here."
        "I don\'t know why I can't fit in here":
            pass
    Gh "I see then."
    Gh "If you need any help anytime..."
    Gh "I'm here and I'll teach you the ropes of anything."
    fang "Thanks."
    fang "That means a lot to me here."
    Gh "I mean you're a guest in our village."
    Gh "We have to look after you."
    fang "Again.{w=1} Thanks."
    Gh "On a separate note...{w=0.5} Have you ever drank some {i}Bai-Jiu{/i}?"
    $ TL_glossary.addword("Báijiǔ")
    Gh "Your Great Grandpa's factory sells the good stuff to us, sometimes to some Japanese as well on the other side."
    Gh "You should try it."
    vice neutral "Try it Fang."
    vice neutral "Embrace your desires once in a while."
    menu:
        "Sure, I'll try":
            fang "Surely it can't be that bad."
            Gh "You got a good spirit in you."
            "Guo Heng went and got out two bottles."
            "Short and stout with a long neck."
            "I would wonder how much alcohol were stored in them at all."
            Gh "Doesn't look like much eh?"
            Gh "What it fails in volume it makes up for in substance."
            Gh "This is some hard stuff you know?"
            fang "I guess."
            composure "Could you actually drink this?"
            menu:
                "Who knows? I guess I'll have to find out.":
                    composure "Good Luck then."
                    vice neutral "Just do it."
                    fang "Bottoms up."
                    jump GH_drinking_9_7_20
                "probably not but we'll see to that.":
                    composure "You believe in yourself an awful lot."
                    vice neutral "Time to unplug the {b}ambrosia{/b}."
                    fang "Cheers!"
                    jump GH_drinking_9_7_20
                "No, so why am I doing this?":
                    logic neutral "Because of your arrogance and need for social acceptance."
                    composure "Harsh way to put it but it's true."
                    vice neutral "What a fucking bore."
                    fang "I don't if I can drink {i}hard stuff{/i}."
                    "Guo Heng looks up at me."
                    Gh "I only call it that because I don't drink strong stuff that much."
                    Gh "It's hard for you but I've gotten used to it."
                    vice neutral "Do it."
                    logic neutral "Think for a minute and convince him."
                    menu:
                        "Convince him: {b}Rheotorics hard{/b}":
                            if fang.RandomCheck("rhetoric", 6,8):
                                fang "I really don't want to drink."
                                fang "I don't want Uncle Ku catching my breath reeking of alcohol."
                                Gh "Understandable."
                                Gh "I wouldn't want my old man catching me drinking as well."
                                Gh "Just hand the bottle here."
                                Gh "I'll get it down also."
                            else:
                                fang "I can't drink this."
                                Gh "Why?"
                                fang "Religious reasons..."
                                "Guo Heng raised his brow at me."
                                Gh "Why did you agree in the first place?"
                                fang "I don't know...."
                                Gh "Come on just drink up."
                                vice neutral "He got you. The world has got you."
                                $ fang.convo("FailedConvinceDrink")
                                jump GH_drinking_9_7_20
                        "Drink up: {b}Composure hard{/b}":
                            jump GH_drinking_9_7_20
        "No thanks, I'm fine":
            fang "I don't feel like drinking."
            Gh "Ah well, that's fine."
            Gh "I respect that."
            Gh "If you need to talk about stuff in your mind just find me after your shift."
            "Guo Heng wiped the rag across his forehead."
            Gh "You probably need to find a way to get out of here."
            Gh "I'm here to help with that."
            fang "I Know..."
            "Guo Heng really just wanted his brother out of harms way{w=1} which must be the reason why he is trying to support me going away from Peiping."
            jump GH_main_convo
label GH_drinking_9_7_20:
if fang.RandomCheck("endurance", 5,8):
    "It invades my mouth."
    "The bitter taste is masked with it's antique flavour."
    "It chugs down my throat where it burns."
    "I resist the temptation and the strong fumes in my nose."
    "I finally put down the empty bottle and unbutton some top buttons as my chest feels fiery."
    Gh "I didn't think you'd be able to take it."
    fang "Why?"
    if fang.said("FailedConvinceDrink"):
        Gh "After that hilarious failed attempt at \"Religious Reasons\" I guess."
    else:
        Gh "I just had a feeling."
    Gh "You probably just couldn't predict if your body could take it right?"
    fang "I guess you're right."
    jump GH_main_convo
else:
    "it invades my mouth."
    "The bitter taste it masked with a aggressive flavour."
    "I could feel an inferno form in my throat and chest."
    "The fumes occupying my nose aggressively."
    "I could feel my stomach lurge and my tongue spasm."
    "I bend over and spit it out."
    "As I spit it out I feel sick to the core from the strong tase."
    Gh "You alright?"
    fang "I guess."
    "I wipe the alcohol off of my chin."
    Gh "That was how my first experience went as well."
    if fang.RandomCheck("rhetoric", 3,5):
        rhetoric "He's speaking the truth."
    Gh "I started to drink after my old man left the world."
    Gh "Alchol seems like a friend in grief."
    Gh "Honestly it's a whole lot more abusive than that."
    fang "I guess you're right."
    jump GH_main_convo
label GH_main_convo:
Gh "How's house arrest been?"
fang "It's been fine."
fang "I've managed to learn more about my \"ancestral land\"."
fang "Sadly I can't stay here for long."
Gh "Why so?"
fang "There's a war going to start."
Gh "I guess that makes sense."


label Beijing_1_GH_afterward:
    "There was nothing to say."
    "It was a bit awkward but it was difficult to articulate conversation."
    "I don't have in the slightest an idea of what to do."
    menu:
        "Keep conversing with Guo Heng.":
            $ activities_left = 2
            jump GH_dive_convo

        "Take leave":
            fang "I think its time I get moving."
            fang "I have a pending interview to undergo."
            fang "He should be coming to conduct it soon."
            "Guo Heng rubbed the rag on his face."
            Gh "I have to work anyway."
            Gh "It was nice to talk with you Fang."

label GH_Beijing_busy:
    "Guo Heng put down his sweat rag."
    "The sun was piercing through his thin ragged shirt."
    "You could see how the sweat now made the shirt a paint to his canvas of a skin."
    Gh "No offense Fang,"
    Gh "I have work now."
    Gh "I can't afford always taking a break."
    Gh "It takes time to make preparations for a meal."
    "I grinned at him as well."
    "It was pleasant."
    "Guo Heng was now slaving away in his kitchen once again."
    "I stood up and walked outside and began to think."
    "Visiting the village temple was an opportunity to calm myself down and think about life."
    "I'd often get to sit and think."
    "It was almost as quite as the libraries in Peking University."
    "The temple wasn't far from Guo's noddle shop."
    "I began to amble to my destination."
    "The temple had been around since the inception of the village."
    "It was the oldest unchanged object in this whole place."
    "It is rumored that the village was built by rich landowning elites in the Ming dynasty."
    "It would make sense to see why this village is prosperous more than most."
    "Apart from that there is also a gilded reputation of this place."
    "It is prosperous but on the backs of laborers and rural wanderers or military deserters."
    "People like {i}Ma Shih{/i} often hired these desperate people for cheap and made them do things well beyond their pay."
    "It's no rumor that a few times a month the newly hired workers on his farm are either hospitalized or were seen running away."
    "Lao Chang used to work for Ma Shih's father who was a complete opposite in fact."
    "Lao Chang deifies that man because of him Lao Chang had a place to stay and never felt an empty stomach for 15 or so years."
    "Then he died and his cheap cruel son took over the farm and made it much more sinister."
    "Its a thought that keeps me up at night."
    "Maybe it's why these poor dis-empowered people turn to communism."
    "After all why defend something that oppresses you?"
    "As I keep walking, other thoughts amble into my mind."
    if fang.hasLog("Hometown:Peiping"):
        "This temple in front of me."
        "Its the only temple I've been to in a commitment sense."
        "I've been living with Uncle Ku here for about 2 weeks to be closer to Peking university and to reconnect with the \"Ancestral land\"."
        "Apart from house arrest as well for protesting."
        "I did not have much experience with temples in my life."
        "I would read books on temples."
        "From the grandest ones, to the oldest ones, to the abandoned ones."
        "The one that stuck out most were..."
        menu:
            "The Grandest ones":
                pass
            "The Oldest Ones":
                pass
            "The abandoned Ones":
                pass
    elif fang.hasLog("Hometown:Nanjing"):
        ""
    elif fang.hasLog("Hometown:Guangzhou"):
        ""
    elif fang.hasLog("Hometown:Macau"):
        "In Macau the Ma Kok temple is beautiful."
        "It brings me back to the beautiful days of being in Macau."
        "Tonnes of boats, kind Portuguese, Patua families."
        "Life was safer..."
        "If I had stayed in Macau and gotten a chance to attend a school in Portugal I wonder where I would be now."
        "Would I be criticizing Salazar?"
        "Become an activist for the Spanish civil war?"
        "God knows."
        "I sure as hell wouldn't be out here on the front line of a total war between two stubborn nations."
        "While Peking university is prestigious and honorable I would have wanted something better."
        "Something less pathetic than this option in life."
        "I didn't hate my \"Ancestral Land\" just that I didn't feel safe on it."
        "If I had tried to phrase this a neutral as I could Uncle Ku would be prepared to raise his fist."
        "To Uncle Ku, his rule was simple."
        "Principles first...{w}people second."
        "My heart longed for Macau."
        "It was a guilty feeling nonetheless."
    elif fang.hasLog("Hometown:Taiwan"):
        ""  
    elif fang.hasLog("Hometown:HongKong"):
        "Back in Hong Kong my experience with temples were different."
        if Buddhist:
            "The Po Lin monastery was a real piece of work."
            "Before 1924 everyone just called it \"the big hut\"."
            "The monastery has 3 statues of Buddha."
            "The three status represent states of time."
            "The Past."
            "The Present."
            "And of course the future."
            "It's a beautiful message."
            "The big hut also houses a lot of great Buddhist scriptures."
            "A place of true interest."
        elif Taoist:
            "The Man-Mo temple was beautiful."
            "Man-Mo temples typically worship the god of civil and literature."
            "{i}Man-Cheong{/i}"
            "There are several of these types of temples back in Hong Kong."
            "I guess this explains why my essay writing skills became good enough to come to Peking University."
            "Most of the time I don't mind what the religious affiliation of a temple is."
            "I typically find them comforting."
            "It's like a place to heal wounds."
            "To think."
            "One tough days a visit to the temple typically just clears all my stress."
            "For me a visit it like meditating."
        elif Christian:
            "Normally I would attend churches."
            "Alongside that I would attend temples."
            "I would spend time walking around Buddhist or Taoist temples."
            "Anything temple I came across."
            "It was calming."
            "Something about it attracted me to it."
            "Most of the time I was allowed this when i was young."
            "As I got older they became more strict about this sort of stuff."
            "Beliefs grow on you with age."
            "Like hairs on your skin."
            "For some reason that did not apply to me."
    "I knelt down and kept my eyes closed."
    "I was so calm I could hear my own heartbeat."
    $ msg.msg("You feel calm")
    $ stress = 0
    monk "How are you feeling?"
    "I opened my eyes once more."
    monk "You seem much more calm than when you entered this place."
    if Buddhist:
        "A monk wearing the orange robes was standing in front of me with a gentle smile."
    elif Taoist:
        "A monk wearing the Taoist robes was standing in front of me with a inviting smile."
    monk "I'm glad to see that."
    "The monk turns around and orders a temple worker something in a foreign language."
    monk "Don't take offense to that."
    monk "I speak in my dialect."
    monk "I just told him to bring you some water."
    monk "This temple is just as much of a house for me and him."
    monk "That's why all visitors are treated as guests."
    monk "I would just like to request we do not entertain ourselves to discussion here."
    monk "It's a place of worship."
    fang "Ah.. Sure."
    monk "Thanks for understanding."
    "I follow the Monk into a small room."
    if buddhist:
        monk "That room there is my {i}Parivena.{/i}"
    elif taoist:
        monk "That room there is my quarters."
    else:
        monk "That room there is my cell."
    monk "This place was donated to by Ma-Shih."
    monk "I'm happy that he is so generous to us."
    monk "That man I asked to get water for you used to work for Ma-Shih."
    monk "He took refuge here 2 winters ago."
    monk "Ma-Shih fearing for his existence gave colossal donations to the temple as a result."
    monk "I wonder if such acts bear one fruit."
    monk "What would you think?"
    menu:
        "People fear ruining their eternal afterlife.":
            $ monk.log("MONK_CONVO_1_fear_afterlife")
            fang "People do the wrong thing and try to make up for it."
            fang "I feel they don't realize it's better to just avoid doing the wrong thing."
            monk "Of course, I would agree with that."
            monk "Yet I could argue that the money from Ma-Shih to the temple allows that man to live safely and comfortably."
        "People are naturally selfish.":
            $ monk.log("MONK_CONVO_1_Cynical")
            fang "They seem to act in self interest a lot of the time."
            fang "I think it's not fair that one can be cruel and then expect to be free from their consequence."
            monk "You aren't wrong there."
            monk "But did you ever think he gave up something that enabled him material power? A portion of wealth?"
        "In the end it doesn't matter, it's better to live nicer when alive.":
            $ monk.log("MONK_CONVO_1_nihilism")
            fang "Death is absolute so who really knows the meaning of justice in the afterlife?"
            fang "Maybe people get judged differently from what we comprehend."
            monk "I like that point of yours."

    monk "Such thoughts shouldn't plague ones mind."
    monk "Allowing things to be carried on your shoulders mentally is what creates the burden and worrying we want to run away from."
    monk "I don't know your story."
    monk "I don't know why you came in here looking so upset before your \"prayer\"."
    monk "I'm glad you have subdued your frustrations."
    monk "but you must learn to control them at will."
    "The temple servant strolled in with a glass of water."
    "I assume they had to use the temple well to get the water which would explain the wait."
    monk "Do you recognize him?"
    "I looked over at the fresh face of the temple servant."
    fang "I'm afraid not."
    monk "He is Ma-Wen. The son of Ma-Shih."
    Mw "Namaste."
    "He did a slight bow as he did this."
    Mw "Have some water to drink."
    fang "Sure.. Thank you."
    Mw "You're welcome."
    "I picked up the glass of water and drank it down to drown my sense of surprise."
    Mw "Don't drink so fast."
    "Ma Wen took a seat on the same bench as the Monk."
    Mw "It's true, I am Ma-Shih's son."
    $ Mw.log("Met_MW_TEMPLE")
    jump MW_CONVO_1
label MW_CONVO_1:
    menu:
        "Why hasn't he taken you back yet?" if not Mw.said("TakenYouBack"):
            $ Mw.convo("TakenYouBack")
            Mw "I thought he wouldn't care."
            Mw "He's the type who doesn't bother anyway."
            Mw "He did try, he sent some servants to convince me but I refused."
            Mw "Did he lack the capacity to walk his own two feet to talk to me?"
            Mw "After sending more people to talk to me and I keep refusing..."
            Mw "He just gave up."
            Mw "Just like that. In three days."
            Mw "To be fair he lasted longer than I expected in trying to commit to his \"family\"."
            Mw "He just donated lump sums of money so I could \"live comfortably\"."
            Mw "I think it's his superstitions playing on his guilt."
            Mw "That or.."
            Mw "He just wants to remind me that I'm still depending on him."
            Mw "I don't think he'll ever walk on his own two feet and respectfully ask me to return."
            jump MW_CONVO_1
        "Why did you of all people run away?" if not Mw.said("RunAway"):
            $ Mw.convo("RunAway")
            Mw "Just because I lived lavishly and didn't have to struggle for anything did not mean I wanted to live with some narcissist."
            Mw "His attitude, behavior, constant escaping of laborers."
            Mw "It builds up in your head."
            Mw "In defiance of his controlling personality I just walked out."
            Mw "Sometimes it's that simple to send a message to someone that dense."
            jump MW_CONVO_1
        "What will you plan on doing further on?" if not Mw.said("FurtherPlans"):
            $ Mw.convo("FurtherPlans")
            Mw "Anything that keeps me away from him."
            Mw "I'm trying not to use bad language to talk about that man after I picked up this new life."
            Mw "If I could still curse, you wouldn't hear the end of it."
            Mw "In the end, I can do anything I want."
            Mw "I have a whole life ahead of me."
            Mw "Becoming a farmer or a peasant for all I care."
            Mw "As long I never see his face ever again I don't mind what I'm doing."
            jump MW_CONVO_1      
        "What about the rest of your family?" if not Mw.said("Family"):
            $ Mw.convo("Family")
            Mw "My mother died a few winters back."
            Mw "The only place I see her are in my dreams."
            Mw "I feel like it's punishment for not mourning her death for three years."
            Mw "That was my responsibility as her son."
            Mw "As for my siblings..."
            Mw "They can go their own way."
            Mw "They'll soon realize how toxic their \"Oh so precious father\" is."
            Mw "I know they'll do that."
            jump MW_CONVO_1
        "What happened to your mother?" if not Mw.said("AskMother") and Mw.said("Family"):
            $ Mw.convo("AskMother")
            Mw "I don't want to talk about it."
            Mw "It's personal."
            $ Mw.mood = "Offended"
            $ Mw.bondp(-1)
            $ Mw.log("CONVO_1_MW_Mother")
            $ msg.msg("Ma-Wen didn't like that.")
            menu:
                "I'm sorry" if fang.RandomCheck("empathy", 3,6, True, 0.35, True):
                    fang "I'm sorry."
                    "Ma Wen didn't budge from my offense."
                    Mw "Forget it."
                "...":
                    "What could I say."
                    "It felt too awkward..."
            empathy neutral "Apologizing wouldn't have done anything anyway."
            empathy neutral "He will use this against you."
            empathy neutral "He tends to hide grudges."
            jump MW_CONVO_1
        "Was leaving behind so much wealth worth it?" if not Mw.said("Wealth"):
            $ Mw.convo("Wealth")
            if Mw.said("RunAway"):
                Mw "Didn't you hear what I said?"
                Mw "Money doesn't feel nice when there's a narcissist pissing you off every second."
                Mw "Pay more attention when I'm talking."
                $ Mw.mood = "Offended"
                $ Mw.bondp(-1)
                $ MW_CONVO_1_attention = True
                $ Mw.log("CONVO_1_MW_Lacked_Attention")
                $ msg.msg("Ma-Wen didn't like that.")
            else:
                Mw "I wouldn't think twice if I had to do it again."
                Mw "Life is much better off without him."
                Mw "Wealth doesn't necessarily bring happiness now does it?"
            jump MW_CONVO_1
        ">> So the temple is your new life?":
            pass
$ Mw.clearconvo()
Mw "Yeah."
Mw "I probably won't get an inheritance either."
Mw "Nothing to return to."
Mw "So I'm going to try and live a good life wherever I may be."
monk "Quite the story."
monk "I don't judge people so I took him in."
monk "Different lives don't matter as long there is mutual respect."
monk "When he came here, he was just like you."
monk "Everyone has a struggle."
monk "Listening to others will ease that feeling that no-one understands your burdens."
monk "Stories are a window to empathy."
"Ma Wen sat there unmoving."
"He seemed eerily... stolid."
monk "I'm here to talk if you want."
monk "What about you Ma-Wen?"
"Ma Wen looks up from the floor."
Mw "I shoud attend to some duties."
monk "I guess that's alright."
if Mw.mood == "Offended":
    "Ma Wen abruptly stands up and leaves the room."
    "I could hear his heavy rapid footsteps hit the wooden floors until he stormed into the next room."
    "I didn't realise I had angered him so much."
    if Mw.hasLog("CONVO_1_MW_mother"):
        monk "He's still hung up on the death of his mother."
        monk "He was close to her."
        monk "I don't even know what happened to his mother."
        monk "He only talks of fond moments."
    if Mw.hasLog("CONVO_1_MW_Lacked_Attention"):
        fang "I should have also paid attention I guess."
        fang "He was talking about something personal and I kept digging the wrong places."
    $ MW_impression = __("Bad First Impression")
    $ Mw.log("Bad_FI")
else:
    "Ma Wen ambled out the door."
    "Despite that I could still feel his cloud of melancholy."
    $ MW_impression = __("Netural First Impression")
$ msg.msg("You made a [MW_impression] on Ma-Wen")
monk "Don't overthink it."
monk "It will take time for him to come to terms with these feelings."
monk "Self hate is a poison in which time is its antidote."
fang "I guess I can agree with that."
"The Monk retreats back into his mind to think for a moment."
monk "You've only been around here for two weeks right?"
fang "Yes, that's right."
monk "Why are you here?"
fang "There's too many reasons for that."
monk "Will you walk South?"
fang "I'm not sure about that."
fang "I don't want to drop everything and run."
fang "I don't want to get caught in crossfire."
fang "Or enslaved by the army."
monk "All fair crticisms."
monk "I can't disagree with that."
monk "Have you talked to Ku Hsien-Sheng?"
fang "No I have not yet..."
monk "I have a good feeling about you."
monk "I feel the same way about Ma-Wen."
monk "I won't be moving an inch from here."
monk "That is my personal choice."
monk "You..."
"The monk looked at the ground for a second."
monk "You're young."
monk "You don't deserve to get invovled in this."
monk "You have a whole life ahead of you."
monk "Every choice you make counts."
$ TL_datetime.timepass()
$ msg.msg("You made a good impression on the Monk.")
monk "If you don't mind can you help me out with some serivce preparations?"
monk "It will be best to give Ma-Wen a rest for today."
"I stand up and thank the Monk for his hospitality."
"He doesn't reply but retort with a smile."
"I walk past the rooms and the deity room to the outside wind."
"The wind was gentle and inviting as I stood and absorbed it's chilled sensations."
""
jump KU_farewell

label KU_farewell:
"I seemed to have a lot of work left."
"Normally I would be in the urban districts of Peiping where you could see people from all places gather."
"Even the Japanese across the Marco-Polo Bridge."
"I would attend Peiping university so I could work abroad."
"Strangely my dreams seem to force me to run away from my current situation."
"I begin to walk back home as my books are there."
"How would I confront Uncle Ku?"
"I felt like I has strained things again."
"Part of me always does this."
"Part of me always blames me for blaming myself for things outside of my control."
"I realize I always dwell on such trivial matters."
"It's strange really."
"I guess this walk didn't get me anything."
"I felt my leather shoes grind the dust as I ambled."
"Is my education even a priority?"
"{i}I should be evacuating... right?{/i}"
"The Chang San Brothel was now in view again."
"Chang San was not even its name, it was just a type of brothel."
"I never bothered asking the name anyway."
"Was it important to know its name?"
"I began to speed-walk at this rate."
"The wine factory that was supposed to be starting up soon will now be left decrepit."
"I wonder what the soldiers would do to it when they occupy it."
"Yue-Lan has already expressed what the soldiers would do with the brothel under occupation."
"It didn't strike me as surprising in any sense."
"They would probably start up the factory with some volunteers and drink till they drop."
"I kept on walking for what felt like 10 minutes until the pathetic pond came back into view."
"The pond in my eyes resembled an animal that was wounded and in pain."
"Like it needed to be put out of its misery."
"It would also be a breeding ground for ill stuff."
"The water is brown and god knows that is swimming in there."
"I gaze away and walk back in through the Da-men."
"I couldn't hear Uncle Ku doing anything at the alter."
"I wonder if he is home."
"I have to find my books and start reading."
"I chose courses in law at Peking university."
"I seemed to have a strong sense of civil justice since I was young."
"When you're a kid and you feel like the leadership has failed you then you grow up wanting that to change."
"Perhaps my determination to change a faulty system came from a hatred of its failures."
"I can't even understand my own intentions for such ambitions but I persist."
"I reject the alternate options."
"I dragged a book off of the shelf and put it on my table."
"One day I wish I could become part of this system and hopefully steer it towards a path for the better."
"Time to study."
$ TL_datetime.timepass()
scene black with fade
with Pause(3)
"I recited the final quotes and notes to cement them in my head."
"Studying like this has helped me become more calm."
"It's all I have these days."
"Working towards more work."
"{i}I'm such a workaholic{/i}"
"Uncle Ku still hasn't come back even despite the fact I had studied to just above an hour."
"I wonder if he was called to a meeting."
"Surely I would meet them on the way to Guo's shop."
"Perhaps he was talking with some workers on building air raid shelters."
"Uncle Ku is well connected with people in high places, perhaps an officer informed him to undertake responsibility to dig air raid shelters."
"After all they might start bombing any day soon when they're mobilized."
"The thought of war..."
"It still haunts me."
"Will people be able to keep their sanity after witnessing near death, bloodshed and regular bombing?"
"In all honesty I have doubts on my capacity to handle the terrors of war."
"I'm not some mythological hero who can fight till their last breath."
"I just didn't want to be involved in this."
"{i}Is that why I want to run away?{/i}"
"{i}If Uncle Ku and Professor Po realized this then this support for escaping further south makes sense.{/i}"
"Beijing may be the resident of my ancestors but I have to face reality."
Gu "Fang?"
"I sat up not expecting him to enter the house so silently."
if stress > 1:
    Gu "Ever since this whole conflict broken out I have noticed you are much more...{i}stressed{/i}"
    Gu "Not just about the hawks."
    Gu "I know it was my fault for getting the professor drunk and I'm sorry for that."
    Gu "I honestly intend to help you."
    fang "..."
else:
    Gu "What are you hung up about?"
    Gu "The hawks?"
    Gu "The communist accusations?"
    "Uncle Ku sat in silence for a few seconds before manifesting an idea."
Gu "You're hung up on Li aren't you?"
fang "I'm not."
fang "It does make me guilty."
fang "But what can I do?"
fang "If he was in my place he wouldn't be doing anything for me either."
Gu "I'm not here to pinpoint whose fault it is that Li is in prison."
fang "I know."
Gu "Did you even visit him?"
fang "I don't want to raise suspicions that I really am in kahoots with treasonous activity."
Gu "He was your friend."
Gu "Could you do that to a friend?"
fang "Would I want to put my life in danger further?"
Gu "And let him suffer?"
Gu "You're going to make him grow to hate you."
fang "My hands are tied."
fang "What can I do?"
Gu "The professor has already left."
Gu "He said the questions he asked what enough to write a statement on you that could get you out."
Gu "I guess you're out of the trouble now aren't you."
Gu "Maybe do something similar for your friend."
Gu "Don't throw your friend into a hole."
menu:
    "Don't worry. I know the right thing to do.":
        $ fang.log("Promise_HELP_LS")
        $ Gu.bondp(1)
        fang "I won't stab him in the back like that."
        fang "I'll try and help him out when I have time."
        "Uncle Ku gave a pleasant smile upon hearing this."
        "By the way..."
    "There are bigger things to worry about right now.":
        $ fang.log("n_Promise_HELP_LS")
        $ Gu.bondp(-1)
        fang "I do realize the situation we are all in."
        fang "I'm afraid my hands are tied."
        fang "We have to try and move out of this place."
        fang "We have to walk south away from this barrage."
if promise_Gh_talk_escape:
    fang "Today I talked with Guo Heng on this."
    fang "A bunch of people are planning on walking down south."
else:
    fang "I've been thinking about it."
    fang "We should walk south far away from the conflict."
Gu "Are you crazy?"
Gu "Why would you want to do that?"
fang "To stay safe!"
fang "Why else would I want to escape a bloodbath?"
Gu "You are telling me that I should leave my land like food on a platter for some invaders?"
fang "If it means that we will live for another sunrise.."
fang "then YES!"
"Uncle Ku had a look of disbelief painted on his face."
Gu "Are you out of your mind?"
"How the hell should I approach this?"
menu:
    "They aren't like how they were in Manchuria.":
        fang "They aren't like how they were back in Manchuria!"
        fang "THey're planning a total war!"
        fang "Just think goddammit!"
        "Uncle Ku's eye twitched at hearing this."
        fang "This time they want everything."
        fang "They'll use whatever force necessary."
        fang "I may have been too young to remember anything about what happened in Manchuria."
        fang "But I know I sure as am not that stupid to stand upright and courageously unarmed against some imperial thugs."
        fang "We have to make concrete decisions now."
    "Listen to yourself!":                       
        fang "Do you honestly in your own right mind think that standing upright while they carry guns will change anything?"
        fang "It may be nihilistic but"
        fang "In this scenario it's realistic."
        fang "We have to make concrete decisions now."
menu:
    "I'm leaving for South whether you like it or not":
        fang "I'm afraid I will have to go to [hometown]."
        fang "I know this might be harsh but I don't want to leave you behind at all costs."
        fang "That is why I need you to come with me."
        if fang.hasLog("Hometown:Peiping"):
            fang "Didn't you say at the interview that you knew a scholarly friend back in Tsingtao?"
        else:
            fang "Correct me if I'm wrong but isn't there some friend in Qingdao you can contact?"
        Gu "Fang."
        Gu "I accept your goodwill and honest intentions for my safety."
        Gu "I also have some disagreements."
    "It will be better if you could come.":
        if fang.RandomCheck("rhetoric", 5,7):
            rhetoric "{b}Challenge Successful{/b}"
            rhetoric "Uncle Ku won't budge knowing his \"stubbornness\"."
            rhetoric "It would be best to leave him without drama."
            rhetoric "Talking to him maturely could allow us to have a better head-start on departure."
            "I guess you're right on that part."
            fang "It would be better if you came with me."
            menu:
                "If you can't then at least farewell on a good note":
                    $ devtool.critical("KU_farewell_convo - GOOD_NOTE")
                    pass
                "I'll respect your choices but you'll have to respect mine.":
                    $ devtool.critical("KU_farewell_convo - MUTUAL_RESPECT")
                    pass
            $ fang.log("KU_farewell_convo")
if not fang.hasLog("KU_farewell_convo"):
    Gu "You got accepted into Peking university."
    Gu "You joined a protest about things that matter to you and to you only."
    Gu "Now you are forcing my own hand to your will."
    Gu "Have you noticed how self-entitled you are?"
    Gu "You've only been here two weeks and I'm starting to see a controlling trait of yours emerging."
    Gu "Fang you don't need to be {i}this{/i} rash."
    $ Gu.bondp(-1)
    Gu "I'm sorry."
    Gu "I may be that old traditional thinking fundamentalist."
    Gu "But my choices will remain my choices."
    Gu "You can leave."
    "Uncle Ku sat on the guest bed."
    Gu "I don't have any hard feelings from what is a natural response to fear and danger."
    Gu "Out of goodwill I can help prepare you."
else:
    $ devtool.critical("KU_farewell_convo_branch")
    pass
menu:
    "Thank you.":
        pass
if is_student:
    Gu "Since you were a student you didn't earn much did you?"
    Gu "Take 200 Fabi."
    $ inventory.earn(200)
    $ msg.msg("You received 200 Fabi.")
if is_worker:
    Gu "You worked already haven't you?"
    Gu "I don't think you'll need much from me."
    Gu "Take a 50."
    $ inventory.earn(50)
    $ msg.msg("You received 50 Fabi.")
if is_apprentice:
    Gu "As an apprentice I always feel I didn't pay you enough."
    Gu "Take this."
    $ inventory.earn(400)
    $ msg.msg("You received 400 Fabi.")
if is_free:
    Gu "You were forced into training without pay."
    Gu "At least you had food and shelter there."
    Gu "Here's 300."
    $ inventory.earn(300)
    $ msg.msg("You received 300 Fabi.")
Gu "Keep your admission papers with you."
Gu "Peking university might move during wartime like any other kind of business."
Gu "Even after the war when it returns it will be nice to have your spot guaranteed."
$ fangbag.add_item(Peking_admission)
"Uncle Ku scratched his head as he thought."
Gu "Do you still have the work recommendation letter from Cheung?"
if fang.RandomCheck("rhetoric", 0,1): 
    rhetoric "A rhetorical question."
Gu "Keep that with you."
Gu "If you could find some kind hearted foreigner to work for then most of your tantrums will go silent."
$ fangbag.add_item(Work_Recommendation)
Gu "You should go to Tsingtao."
Gu "Over there I have an academic colleague by the name of Wang P'u Ch'en"
Gu "He's quite rich. Rich as me I would say."
Gu "He has a wife who is referred to as \"Lady Wang\"."
Gu "Her full name is Wang Yue Hsiang but don't ever refer to her with that."
Gu "I will write a letter to him explaining him to take you in for as long as you need to be dependent on him or leave further south."
Gu "After all he owes me."
menu:
    "Why?":
        pass
Gu "I sponsored his education and accommodation with my house and inherited wealth."
Gu "His success today is due to my input."
Gu "Since he owes me he can't turn you away."
Gu "I doubt he would have turned you away even if he didn't owe me."
Gu "This sort of goodwill comes in handy down the line you see."
"Uncle Ku kept on dabbing the brush in ink and sliding it elegantly across a piece of paper approximately the size of a table-top world map."
Gu "By the way Fang."
Gu "Have you heard of {i}I Kuan-Tao{/i}?"
$ TL_glossary.addword("I-Kuan-Tao")
menu:
    "No" if not persistent.yikuantao:
        $ persistent.yikuantao = True
        Gu "It's a sect of a larger religious movement that gained popularity after the fall of the Empire."
        Gu "I Kuan-Tao is a belief of salvation of the individual and of society."
    "Yes" if persistent.yikuantao:
        Gu "Good."
Gu "Wang P'u Ch'en is actually studying about the sect."
Gu "I need to tell you two things in regards to it."
Gu "First you need to stay away from that sect."
Gu "By that I mean don't believe in what they tell you."
Gu "Besides you might get sucked into more obscure and shadowy organizations."
Gu "Secondly if you can help Wang P'u Ch'en gain insight into the organization then you can prolong your stay with him indefinitely by paying him with \"intel\"."
Gu "Provided you don't fall victim to their lies."
Gu "Wang P'u Ch'en is eying them carefully."
Gu "I put down in this letter than you might be willing to help him out on learning about it in exchange for living space."
Gu "When you reach there make your own choices."
Gu "Here you go."
$ fangbag.add_item(WPC_letter)
Gu "I forgot to tell you."
Gu "Professor Po will stay in contact also."
Gu "He'll use his connections to help you out if you need help."
Gu "Just keep track of how much you {i}owe{/i} him."
Gu "Let me walk you off tonight."
Gu "God knows what will come out of this war."
Gu "When the war ends feel free to come back here."
Gu "Or go wherever else you want."
Gu "I'll keep sending letters to you in Tsingtao unless the Japanese begin intercepting them."
Gu "If you do decide to go further south then inform me so that I can keep in contact."
Gu "Do you have a torch or anything?"
Gu "It's pretty dark out there."
menu:
    "No":
        pass
Gu "I don't have any lanterns around."
Gu "Will you be able to make it still?"
fang "Sure, I can."
fang "Thanks for everything."
"Uncle Ku gave a faint smile."
"Something you don't normally expect from him."
"It was nice I guess to be sent of with a smile."
if not fang.hasLog("KU_farewell_convo"):
    "even if I did speak to him like that."
    "I hope it didn't leave any hard feelings."
jump DayOneEarlyNight

label DayOneEarlyNight:
fang "Time to meet Guo Heng again."
if fang.hasLog("PackedUp"):
    if fang.hasLog("Promise_HELP_LS"):
        "I should also go meet with Li-Tso-Shih on the way to Tsingtao."
        "I wonder how he feels towards me."
        "Would he have that warm friendship? Or has it rotted away after the arrests?"
        "I've heard he was being kept somewhere in Tientsin which was not too far and on the way to Tsingtao."
        "I was not aware why he was transferred from Peking to Tientsin during police custody."
        "Maybe he was perceived more seriously because of his ethnic background."
        "Li Tso-Shih was my friend and classmate at Peking."
        "He was from Amdo and his family originates from the Ngolok people who are fighting the Kuomintang."
        "He has personal reasons to fight against the republic."
        "After entertaining my thoughts I decided to snap out of it."
        "I should focus on my task at hand."
    elif not fang.hasLog("Promise_HELP_LS"):
        "It might be harsh to leave my friend out to dry."
        "What else can I do."
        "Everyone is trying to save their skin."
        "I have my own personal reasons to fight moral dilemmas."
        "I have to focus on getting to Tsingtao."
    "I was prepared to leave tonight."
    "With Uncle Ku's help I was prepared to face the challenges of a struggling republic at war."
    "I could talk with Guo Heng and leave out tonight."
else:
    "I might have to make a choice on a whim tonight."
    "I could plan it out with Guo Heng and quickly pack to go on ahead."
    "I would still need to talk to Uncle Ku about this."
    "I should try to make him leave with us to Tsingtao for the timebeing."
    "Then we can make more long term decisions about how to go up against the war."
    "Besides with Uncle Ku on our side the financial aspect of the group will be fixed."
"By now the sun was setting."
"Darkness was slowly invading the battlefield of the sky."
"This scenery was strangely cathartic."
"I wonder how many days it will take to experience this tranquil atmosphere once again."
"I absorbed the sweet image into my memory."
"I began to walk down that path I had walked down a few times today."
"Objects becoming more and more like silhouettes."
"I kept walking ahead."
"I had to rush ahead to Guo Heng's shop."
"I was under the impression that Guo Heng would know what was to be done next."
"At night sneaking past the Chang San is bad news."
"If anyone sees me like this..."
"{i}boy, the rumour's won't stop{/i}"
"You could see the windows of the Brothel had candlelights in some rooms and electricity in some others."
"Grunts and moans also leaked through the window."
"God knows how many unloyal men were in there."
"I squinter off of the dirt path into the darker edges of the trees shielding me from the moonlight."
if fang.RandomCheck("vice", 0,5):
    menu:
        "Peak at who enters and leaves.":
            vice neutral "Look at them enjoying themselves."
            vice neutral "Don't {b}you{/b} ever feel the need for that desire?"
            vice neutral "Instead you hide and watch other people wear their vices like their skin."
            vice neutral "Pathetic but rewarding."
            vice neutral "Don't keep dreaming."
            vice neutral "It calls you..."
        "Move on towards Guo's shop":
            pass
"Guo Heng's shop is in the distance and he has a few lanterns lit."
"I hurriedly sneak over while trying to avoid tripping up on anything."
"It was a few minutes away if I had to sneak."
"I kept my eyes on the lanterns."
"My eyesight could not make out what characters were painted on his lanterns but they shone bright."
"Like the end of a dark hopeless tunnel."
"Guo Heng's lantern felt like... {i}hope{/i}."
"I keep my breath under control and made sure to keep my feet stable."
"Skidding down the bank of dirt I regained my balance and reached Guo Heng's shop."
"Guo Heng signalled something to me using his hands."
if fang.RandomCheck("conceptualization", 2,4):
    concept "He's telling you to come over but quietly."
"I kept going until I was within talking range."
Gh "Glad you made it Fang."
fang "Same here."
"Guo Heng's shop had padlocks on every door and boards nailed into any open window like entrance as well."
Gh "It's got to go Fang."
Gh "It'll probably be blown up by the time I get back but at least my brother will be safe."
Gh "Plus I saved up enough in the last 6 months."
"Guo heng scans around the lantern lit shop."
"I wasn't the only one there."
Gh "This is Ma-Wen."
fang "I know him."
if Mw.mood == "Offended":
    Mw "Oh I know this guy alright."
    "Ma Wen sarcastically imitiates me."
    if Mw.hasLog("CONVO_1_MW_Lacked_Attention"):
        Mw "Same guy that couldn't listen straight."
        Mw "Same guy that will accompany us away from this place?"
    if Mw.hasLog("CONVO_1_MW_Mother"):
        Mw "Is this guy going to also ask us about our dead loved ones along the way?"
    Gh "Wen you need to calm down."
    fang "What happened between you and Fang?"
    menu:
        "I made some mistakes":
            Mw "Sure you did."
            Mw "Just get this straight."
            Gh "Jeez stop Wen!"
            "Ma Wen looked Guo Heng vehemently."
            "He turned his gaze back to me."
            Mw "We got issues."
            Mw "and... I'll hold them against you."
        "...":
            Mw "You were so nosy before weren't you?"
            Mw "Wonder what got your tongue?"
            "Ma-Wen cursed under his breath."
            if fang.RandomCheck("perception", 2,4):
                perception "He called you asshat."
                pred "Smack him."
            Mw "Just know that"
            Mw "I'm holding it against you."
else:
    Mw "Nice to see you again."
    fang "Same here."
fang "you're leaving with us also?"
"Ma Wen look into the lunar skies beyond."
Mw "The monk urged me to go."
Mw "He said I got a whole life ahead of me."
Mw "Plus he pretty much kicked me out for that."
"Guo Heng had been watching us two talk it out."
if Mw.mood == "Offended":
    Gh "Some history between you two."
else:
    Gh "Good to see we all know each other then."
Gh "Here's the plan right."
Gh "Da-Yu is out back with a truck."
Gh "He does deliveries for my supplies."
Gh "Bring stuff from as far as Ning-Po to over here in Peiping."
Gh "It's not his job but he makes a good ammount of money on the side by doing people favours."
Gh "His boss hasn't caught him since all his side business stuff is en-route."
Gh "Anyway Da-Yu says that passengers should chip in their shares depending on how far we are going to decide to go."
Mw "I don't give a shit how far we go."
"Guo Heng eyes him nervously as his vision darts back to me."
Gh "What about you Fang?"
if fang.hasLog("Promise_HELP_LS"):
    fang "I'll need to drop off at Tianjin for a quick talk to a friend of mine."
    Gh "You mean he'll come with us?"
    fang "No, probably not."
    Gh "Why?"
    fang "He's locked up and in custody."
    Gh "Why do you need to see him then?"
    menu:
        "He's my friend":
            pass
        "I made a promise to someone":
            pass
    Gh "Either way we can't stay there for too long."
    Gh "It will be dawn or ealier when we reach there."
    Gh "You think they'll let you in?"
    if Mw.mood == "Offended":
        Mw "Why the fuck do we got to play by his tunes?"
        Gh "Cause you don't have any tunes."
        Gh "{i}\"I don't give a shit how far we go\"{/i}"
        "Ma Wen went quiet on this."
        fang "Back to the topic..."
    fang "I think they will."
    "After all my name has been cleared..."
    "After that I have a stop..."
fang "Tsingtao"
Gh "Why Tsingtao?"
fang "My uncle Ku has a friend there who is indebt to him."
fang "I have a written notice from my Uncle to take me in his hospitality while the war doesn't reach the Shandong province."
Gh "Depends how fast troops strorm through Hopeh."
Mw "The Japanese are better than us anyway."
Gh "Why say that?"
Mw "Hav you seen the state of our army?"
Mw "They got to kidnap and chain men to force them to serve."
Mw "The republic is a fucking failure, that's what."
"Ma Wen cynically stated this."
"A cigarette would have fit this persona more."
Gh "What about us two?"
if Mw.mood == "Offended":
    Mw "He's going to abandon us."
    Mw "Big guy here has his rich uncle take care of everything for him."
    Mw "Not a worry in the world for us two right?"
    "Guo Heng began to look visibly annoyed at this rate."
    Gh "Wen, can you just shut up for a moment."
fang "I can try to find space for you guys."
Gh "You would?"
if Mw.mood == "Offended":
    Mw "Lip service shit."
    Mw "Like hell you'll find us someplace to stay."
    "Guo Heng clenched his fist and breathed in deeply."
fang "Wang P'u Ch'en is quite influential there."
fang "I think he can pull some strings for you guys."
Gh "I still think we won't be there for very long."
Gh "Besides I need to get to Guo He in Shanghai."
Mw "Plus that damn cult of I-Kuan-Tao is there."
Mw "Doing their weird cult shit and whatever."
Gh "That too."
fang "Well we can get some letters sent to Guo He in Tsingtao."
fang "Wang P'u Ch'en can write something for you anyway."
"Guo Heng's face lit up at this."
"He seemed elated at this."
if Mw.mood == "Offended":
    Mw "Don't think I'll forgive you over this kind shit."
    "GUo Heng had already left around back for Da-Yu's truck."
    "I'm imagening how annoyed Ma Wen's toxic mood had made him feel."
    fang "Let's just get to the damn truck at least."
    "Ma Wen gives a heavy sigh and follows me to the truck."
else:
    "Guo Heng then gets up and stretches before walking out to the back where the truck should be."
    Mw "Moment of truth?"
    fang "I guess so."
    fang "Let's go talk to Da-Yu."
"I walk ahead into a dimly lit area behind the shop."
Dy "Tientsin, Tsingtao and Shanghai?"
Dy "What are you all scouring the coast for?"
Gh "We all have plans I guess."
Mw "I just don't want to die in the middle of a shootout."
"Da-Yu smirks at Ma Wen."
Dy "I like how this one speaks."
if Mw.mood == "Offended":
    Gh "Sure you will."
    "It was too dark to see but I bet Guo Heng rolled his eyes."
Gh "That's Ma Wen."
"He points to me."
Gh "That's Fang."
Dy "Just Fang?"
fang "Just Fang for now."
"Da-Yu shook a box of cigarettes and bit down on a roll."
Dy "Any of you want to try?"
Mw "Aren't they crazy expensive?"
"Da-Yu brought out a foreign imported lighter up to his roll clamped between his lips."
"Flicking the box till it beamed with life."
Dy "They're expensive cause' they're classy."
"Guo Heng have a small nod."
"Ma Wen stared at him blankly."
Gh "How much do we all chip in?"
Dy "I'm stopping up at Tientsin for a delivery."
if fang.hasLog("Promise_HELP_LS"):
    Dy "Your friend here can get off as well but only for 30 minutes."
    "Da-Yu looked at his pocketwatch in his pocket."
else:
    Dy "So that means it en-route so no need to pay for that."
    Dy "Makes everything else cheaper now? Doesn't it?"
    "Da-Yu took another puff of his classy cigarette."
    "{i}How could he afford such expensive stuff?{/i}"
Dy "Then you all want to go to Tsingtao for a few days."
Dy "If I drop you all off there then chip in 80 Fabi."
Gh "That much?"
Dy "The shit that runs this."
"Da-Yu points to the truck."
Dy "The shit that runs this{fast} is subsidized by my employers like crazy."
Dy "Lowest I'm going."
Mw "I only got 50 on me."
Dy "Get these two to help you out."
Dy "If you all went to Shanghai-Nanjing area then boy your wallets would be dry."
Dy "Anyway time to chip in."
menu:
    "Pay Ma-Wen's chip":
        $ Mw.log("Paid_MW_chip")
        $ Mw.bondp(1)
        $ msg.msg("Ma Wen will remember that.")
        $ fangbag.earn(-80)
        fang "I can."
        if Mw.mood == "Offeded":
            "Ma Wen looks at me for a second with a neutral face."
            "It was strange."
            Mw "Thanks."
            "He said it without a tone."
            rhetoric "Eerie."
            correction neutral "Agreed."
        else:
            Mw "Really?"
            fang "Sure, why not?"
            Mw "Ma Wen looked glumly before Da-Yu took the bill into his hand."
    "Let Guo Heng pay for Ma-Wen":
        Gh "Let me pay for him."
        if Mw.mood == "Offended":
            "Ma Wen looks at me with his arms crossed."
            "His eyes send a message to me."
            if fang.RandomCheck("conceptualization",2,4):
                concept "He expected this type of behaviour from you."
                concept "Maybe he thought {b}you{/b} didn't keep grudges?"
                concept "Did this prove him right or wrong?"
            else:
                "What he said will remain a mystery to you."
        else:
            "Guo Heng passed a thin stack of small notes to Da-Yu."
            "Ma Wen guiltilly watched ahead."
        "Da-Yu took the bills Guo Heng."
Dy "Well that settles it."
Dy "Congrats on a chance at new life."
"He opens the door and hops in."
Dy "I envy you guys."
Gh "Why?"
Dy "You get to feel the cool breeze and open air space around it."
Mw "We're going to be in the back?"
if fang.RandomCheck("rhetoric", 2,4):
    rhetoric "He means \"Are you fucking serious?\"."
Dy "It's not that bad."
Dy "Like I said.. I really do envy you."
Dy "Very few people get to experience moving on the road in a {i}vehicle{/i}"
"He takes a puff of his cigarette again," 
Dy "and even fewer while watching what they leave behind."
Dy "When I start this thing up give this place a formal farewell."
Dy "Who knows what will happen to it or you."
"What a depressing thought."
"I walk around to the back with Guo Heng and Ma Wen."
"It's dark and full of stock."
if fang.RandomCheck("logic", 2,4):
    logic neutral "{i}Maybe he sneaks stuff from his deliveries?{/i}"
    logic neutral "A packet of cigarettes or maybe that pocketwatch would take a year or so to earn."
    logic neutral "That wouldn't explain why his clothes are so western."
    logic neutral "He'd been caught and fired by now."
    menu:
        "There's another reason":
            pass
Gh "Get on Fang."
if Mw.mood == "Offended":
    "Ma Wen still looked pissed."
    "He just stared me down from atop of the open backdoor of the truck."
"I grab the cold bars at the side of the back and hop on."
Gh "Surreal?"
fang "Yeah"
"Ma Wen just lies against the wall of the truck and stares up at the black roof."
"{i}To a new life{/i}"

$ TL_datetime.timepass()

if not fang.hasLog("Promise_HELP_LS"):
    jump Beijing_chapter_one_Day2_8_9_1937
else:
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
    Gh "Fang, get up."
    "I try to adjust my eyes again."
    "It's dark and there aren't any silhouette's even."
    Gh "We're nearing Tientsin."
    Gh "Pretty much whatever is left of Hsi-Ku arsenal."
    Mw "They turned that place into a school didn't they?"
    "Ma-Wen slept in a way in which you couldn't tell if he was {i}actually{/i} awake."
    "At least he looked peaceful."
    Gh "Yeah."
    Mw "That arsenal would be really handy right now."
    Dy "30 minute stopover."
    "I rub my eyes and look over as the empty street."
    fang "It's too dark to go out."
    if Mw.mood == "Offended":
        Mw "Just go and get your shit done."
        Mw "We don't wanna be bombarded any minute now."
    Dy "We passed a skirmish a while bacm while you all were napping."
    Dy "At least an area reported to be hosting one."
    Dy "Didn't see or hear anything."
    Gh "Unsettling..."
    Dy "We just unloaded a whole deck of alcohol into a dogdy cellar while you slept."
    Dy "Up ahead I know some headquarters where you can get some information on that \"friend\" of yours."
    "This street was lit up with a few lanterns unlike the other roads we had been crossing throughout the night."
    Mw "It seems we're in town."
    Gh "I think it's the Kuomintang officers inspecting people or capturing them for forced consription."
    Gh "We shouldn't let them see us."
    Mw "You're right."
    if Mw.mood == "Offended":
        Mw "I'm in no fucking mood for war."
        Mw "Or taking some lives that I've never met or had beef with."
        "Me and Guo Heng looked at Ma Wen curiously."
        "He glanced at us and leaned back."
        Mw "What?"
        Mw "I'd rather shoot my dad."
        "Guo Heng visibly winced on hearing this."
    Mw "I don't involve myself with this noble crusade."
    if fang.RandomCheck("perception", 3,5):
        Mw "Fuck Bushido,{w=0.1} Japanese pigs."
        rhetoric neutral "That's pretty racist."
        rhetoric neutral "Is it personal? {w=0.5}or is he a left sympathiser?"
        perception neutral "He whispers this expecing the wind to whisk it away into the night sky never to be heard again."
        perception neutral "Seems he was wrong."
        if fang.RandomCheck("conceptualization", 1,5):
            concept "What do you make of this?"
            menu:
                "They're all pigs taking our lands for money!":
                    "Ma Wen is right!"
                    "They want our vast resources to power themselves and their economic interests!"
                    "They really are pigs that graze in the wrong {i}place{/i}."
                    concept "Imperialism and capitalism is the problem for this aggression."
                "They'll run the country better than these incompetent bureaucrats.":
                    "The current government is so incompetent and unprepared for war."
                    "They divide the nation and make a joke of democracy."
                    "A powerful military and a strict authority need to unite this fractured country."
                    concept "Fascism will fix our problems. They wil unite us under order."
                "It's better to not form extreme opinions right now.":
                    "Differing views can divide the cooperation between our group."
                    "We need to brush aside our differences."
                    concept "There's no incentive to pick a side."
                "I don't know what to make of this":
                    "All this political rhetoric and demagogic thought is confusing."
                    "Makes my head spin to focus on this any longer."
                    "Forget it."
                    concept "Politics is too much. Focus on what matters."
    Mw "Will you guys ever participate in this bullshit?"
    Gh "Why would I orphan my brother? I have a reason to live."
    if Mw.mood == "Ofended":
        Mw "What about you? A coward? Some shitty wise martyr?"
    else:
        Mw "What about you Fang? What do you make of this?"
    menu:
        "I would fight.":
            if Mw.mood == "Offended":
                Mw "Why? Cause you like hurting people?"
                "Guo Heng just kept gazing at us two."
                if fang.RandomCheck("empathy", 2,5):
                    empathy neutral "He's getting tired of this."
                    empathy neutral "You two need to patch up."
            else:
                Gh "Why?"
                Gh "All that bloodshed?"
                if fang.RandomCheck("empathy", 3,6):
                    empathy neutral "He's not a coward."
                    empathy neutral "All he cares about is his brother."
            menu:
                "I want to defend the people I love":
                    $ FangIdeologyStats[conservatism] +=1
                    if Mw.mood == "Offended":
                        "Ma Wen leans back."
                        "His rib cage relaxes as he sighs."
                        if RandomCheck("empathy", 5,9):
                            empathy neutral "He relates to {b}you{/b}."
                        else:
                            "He hates me."
                            logic neutral "it could be he thinks you're giving lip service for your character."                            
                "I won't hand over my country to some fascists":
                    $ FangIdeologyStats[nationalism] +=1
                    Gh "Do you really love what's going on here?"
                    Mw "It's chaos."
                    if RandomCheck("rhetoric", 3,7):
                        pass
                "I want to experience killing someone.":
                    $ FangIdeologyStats[progressivism] -=1
                    $ FangIdeologyStats[moralism] -=1
                    $ Mw.bondp(-1)
                    $ msg.msg("Ma Wen will remember that.")
                    $ msg.msg("Guo Heng will remember that.")
                "I have personal reasons.":
                    pass
        "I wouldn't fight.":
            if Mw.mood == "Offended":
                Mw "Probably cause you're a coward right?"
                "Guo Heng made a faint smile that you could make out in the dark."
            else:
                Mw "Why? Something about your beliefs?"
            menu:
                "I'm not some slave to capitalist interests":
                    $ FangIdeologyStats[communism] +=1
                "This fight doesn't concern me":
                    $ FangIdeologyStats[centrism] +=1
                "I can't take someone's life":
                    $ FangIdeologyStats[progressivism] +=1
                    if Mw.mood == "Offended":
                        $ Mw.log("FangIsMoral")
                        $ Mw.bondp(1)
                        if RandomCheck("empathy", 4,7):
                            empathy neutral "Ma Wen respects that."

                "I can't handle the stress of those situations":
                    $ FangIdeologyStats[moralism] +=1
                "It's against my Buddhist principles.":
                    pass
                "It's against my Beliefs":
                    pass
                "I have personal reasons.":
                    pass 