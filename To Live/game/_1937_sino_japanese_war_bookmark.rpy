
label Beijing_chapter_one:
if not persistent.history_home_unlocked:
  $ persistent.unlocked_history.append("Home")
  $ persistent.history_home_unlocked = True
un "It is important you answer these questions properly."
un "I will go through them one by one."
un "Do not fret."

scene Ku_house

"My eyes remained firmly shut."
"Uncle Gu Hong-Meng would know what to do."
"Professor Po Yeutarng is quite experienced in dealing with wars."
"After all they both lived through the Manchurian conquest."
"Professor Po Yeutarng wanted to know some information about me to give me advice."

Po "Are you Ready Fang?"

menu:
    "Yes I am Ready.":
        jump Beijing_chapter_one_uncle_interview

    "Please Give me a minute to think.": 
        fang "Please give me a minute to think."
        Po "That's fine,"
        "Normally I would be ready to answer any question coming my way."
        "I never passed up answering a question."
        "Beads of sweat formed on my brow."
        "Summer had just ended so the heat was burning out like some star."
        "I controlled my air-flow and calmed myself down."
        "I can do this."
        fang "I am ready."
        "Uncle Gu looked at me like how a human judges a lamb."
        Gu "Don't overthink it."
        Gu "They won't harm civilians, they didn't back in Dong-bei."
        Gu "Just make sure you can answer their questions."
        jump Beijing_chapter_one_uncle_interview

label Beijing_chapter_one_uncle_interview:

$ msg.msg("You are being interviewed.")
Po "Well Let us start now."
Po "When the Japanese as where you are from it will typically give them a first impression about you."
Po "I know you and your family have moved places over the years so what is your go to hometown."
Po "Where is it most convenient for you to return home so you won't have any difficulty resettling or get bothered by Japanese."

menu:
    "Peiping":

        $ Fang_from_Beijing = True
        $ Japanese_aggression = 3
        $ hometown = _("Peiping")
        fang "I'm from Peiping"
        Gu "I'd suggest you move out of Beijing."
        Gu "Yan'an is swarming with communists otherwise I would have recommended a temporary stay there."
        Gu "My best bet would be to send you to Tsingtao."
        Po "I'd have to be agree with Ku-hsien-sheng"
        Gu "I have a shcolarly friend who can provide you with oppurtunities for work."
        Gu "Tsingtao will be familiar to you."
        Gu "You should also prepare your family to leave for Tsingtao."
        jump Beijing_chapter_one_uncle_interview_intention

    "Nanking":

        $ Fang_from_Nanjing = True
        $ Japanese_aggression = 8
        $ hometown = _("Naking")
        fang "I'm from Nanking"
        Gu "Well, the capital is a good place."
        Gu "Nationalists would fight to the death to keep it safe."
        Gu "I doubt the Japanese would get that far to Nanking anyway."
        Po "I doubt it too. I can't predict how the war will go, but the capital city will be heavily defended."
        Gu "Your hometown seem to be out of harms way and strife."
        Gu "I suggest you go back to your family and try to prepare what to do next."
        jump Beijing_chapter_one_uncle_interview_intention

    "Kwangchow":

        $ Fang_from_Guangzhou = True
        $ Japanese_aggression = 2
        $ hometown = _("Kwangchow")
        fang "I'm from Kwangchow"
        Gu "Under Chen Chi-Tang?"
        Gu "I wonder if he can survive or General Chiang will have to bail him out."
        Gu "I think you're safe there, besides you'll fit in there more that here."
        Gu "Your hometown seem to be out of harms way and strife."
        Gu "I suggest you go back to your family and try to prepare what to do next."
        fang "Guangzhou is under Chiang's direct rule now."
        Gu "Oh really?"
        jump Beijing_chapter_one_uncle_interview_intention

    "Hong-Kong":

        $ Fang_from_hong_kong = True
        $ Japanese_aggression = 1
        $ hometown = _("Hong Kong")
        fang "I'm from Hong-Kong"
        Po "It is a good place."
        Po "The British may be a bit foreign to us mainlanders but at least their territories aren't at risk of being involved in a war."
        Gu "Your hometown seem to be out of harms way and strife."
        Gu "I suggest you go back to your family and try to prepare what to do next."
        jump Beijing_chapter_one_uncle_interview_intention

    "Macau":

        $ Fang_from_Macau = True
        $ Japanese_aggression = 1
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
        jump Beijing_chapter_one_uncle_interview_intention

    "Taiwan":

        $ Fang_from_Taiwan = True
        $ Japanese_aggression = 0
        $ hometown = _("Taiwan")
        fang "I'm from Taiwan"
        Gu "From the foreign devils themself."
        "He chuckles"
        Gu "They won't mess with you then i guess."
        jump Beijing_chapter_one_uncle_interview_intention

label Beijing_chapter_one_uncle_interview_intention:
Po "So what are you doing in Peiping right now?"

menu:
    "Attending school as a student.":
        $ is_student = True
        $ Fang_determination = 3
        $ Fang_intellect = 3
        $ Fang_dexterity = 2
        play sound "sounds/stat_increase/00_stat_increase.ogg"
        "{font=fonts/eng_octin_spraypaint/octin spraypaint a rg.ttf}{color=#4fc1ff}Fang gained 3 Determination; 3 Intellect and 2 Dexterity!{/color}{/font}"
        fang "I came here to actually continue my education."
        fang "I am staying with Uncle Ku since it is close to the facilities."
        Po "I doubt schools will run under foreign occupation."
        "Professor Po gave a faint grin."
        Po "Well classes won't."
        "Professor Po raised his glass of {i}Máotái{/i} and took a sip."
        if not persistent.maotai:
          $ persistent.unlocked.append('Máotái')
          $ persistent.maotai = True
          $ msg.msg("New word added to glossary")
        if persistent.maotai:
          $ msg.msg("This word is in the glossary")
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
        jump Beijing_chapter_one_uncle_interview_religion

    "Working as a scholarly apprentice under my uncle":
        $ is_apprentice = True
        $ Fang_intellect = 3
        $ Fang_dexterity = 3
        play sound "sounds/stat_increase/00_stat_increase.ogg"
        "{font=fonts/eng_octin_spraypaint/octin spraypaint a rg.ttf}{color=#4fc1ff}Fang gained 3 Intellect and 3 Dexterity!{/color}{/font}"
        fang "I am working as an apprentice to my Uncle."
        Gu "The kid is quite dexterous."
        Gu "It's hard to believe he wasn't born without some miracle jade in the mouth story."
        Po "Comments like that will get you in high places."
        fang "Thank you"
        Po "anyway..."
        jump Beijing_chapter_one_uncle_interview_religion

    "Working here to send money back home.":
        $ is_working = True
        $ Fang_determination = 2
        $ inventory.earn(200)
        $ current_money = inventory.money
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
        jump Beijing_chapter_one_uncle_interview_religion

    "Taking a break after military conscription training":
       $ is_free = True
       $ Fang_strength = 3
       $ Fang_determination = 4
       $ Fang_dexterity = 4
       $ inventory.earn(30)
       $ current_money = inventory.money
       play sound "sounds/stat_increase/00_stat_increase.ogg"
       "{font=fonts/eng_octin_spraypaint/octin spraypaint a rg.ttf}{color=#4fc1ff}Fang gained 3 strength; 4 determination; 4 dexterity and 2 wealth!{/color}{/font}"
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
       $ persistent.unlocked.append('Pèifú')
       $ msg.msg("New word added to glossary.")
       "He had raised his {i}Máotái{/i} with both hands to show his appreciation."
       "You should stay away from the military. {w}You're too young for that life.{w=1.0}"
       Po "You're also too young to watch me drink {i}Máotái{/i}"
       "He gave a hearty chuckle. His face was red from the alcohol."
       "He dipped his brush into the little clay pot of abyss-like ink."
       "You couldn't see it spin like water. It was fascinating."
       "He removed the brush and began to scribe onto his piece of paper once again."
       Po "I will lie and state that you were discharged by injury."
       jump Beijing_chapter_one_uncle_interview_religion

label Beijing_chapter_one_uncle_interview_religion:
Po "What belief system do you follow?"

menu:
    "Taoism and Confucianism":
       $ Taoist = True
       Po "You seem to be clinging on the old ways."
       "Professor Po sipped his {i}Máotái{/i} lightly before facing me."
       "Bits of his face had manifested a gradient of red."
       Po "I guess the Kuomintang did a good job reinforcing tradition."
       "He sipped one again. {w}{cps=*0.5}As if something was annoying him inside{/cps}."
       Po "Confucianism is a very old principle."
       $ persistent.unlocked.append('Confucianism')
       $ msg.msg("New word added to glossary")
       Po "I...{w}{cps=*2}just don\'t see it going anywhere in the modern era.{/cps}"
       "Uncle Ku looked at him strangely."
       Po "The \"New Life movement\" is an illusion."
       Po "I am not a \"communist\" {w}but I don't like the policies of the nationalists either."
       "Professor Po seemed engrossed with his political beliefs."
       Po "I respect your beliefs {i}Xiǎo Fāng{/i} but...{nw}"
       Po "From a philosophical and political doctrine I dislike the state being an obstacle to modernism."
       Gu "I could agree with that.{nw}"
       Gu "In english they say something along the lines of \"seperation of church and state\"."
       Gu "I believe in Confucianism."
       Gu "It worked for 2000 years why can't it work for another 2000?"
       "Uncle Ku had seemed to have taken offence to Professor Po's anti-Confucian stance."
       fang "I have a neutral atttiude to Confucianism."
       fang "I think some things work and some do not."
       fang "Fillial Piety is one of my core beliefs."
       "Prossor Po smirked."
       Po "The things you say become more interesting as I get more drunk."
       "Professor Po seemed to dip his brush more sloppily and scribe less cautiously."
       "I wondered if he was capable of asking another question."
       jump taoism_breakaway
    "Buddhism":
       $ Buddhist = True
       Po "Ah...{w}{cps=*0.9}A fellow buddhist.{/cps}"
       "Professor Po sipped his {i}Máotái{/i} lightly before facing me."
       "Bits of his face had manifested a gradient of red."
       Po "Have you ever heard of {i}Dhammapada{/i}? {w}{cps=*1.5}the poem of Buddha awakening?{/cps}"
       jump buddhism_breakaway
    "Christianity":
        $ Christian = True
        if Fang_from_hong_kong:
            Po "You being from Hong Kong I wouldn't be suprised at that perspective."
        Po "Do you like listening to hymns?"
        "Professor Po held his {i}Máotái{/i} up to the sunlight where he could see it tinker."
        "I nodded back towards him."
        Po "I love latin choir and hymns."
        Po "It just moves me to the core."

label taoism_breakaway:
Gu "{i}Fāng{/i}"
Gu "Did you read the old poems from {i}\"Tao Te Ch\'ing\"{/i}?"
$ persistent.unlocked.append('Tao Te Ch\'ing')
$ msg.msg("New Word added to glossary")
Gu "Would you like to hear a poem from {i}Tao Te Ch\'ing{/i}?"
Gu "{i}Tao the water way{/i}"
menu:
    "Yes" if not persistent.tao_water_way:
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
        $ persistent.unlocked_poem.append('Tao The Water Way')
        $ msg.msg("New poem Unlocked: Tao the Water Way")
        jump beijing_interview_after
    "No" if not persistent.tao_water_way:
        $ not_hear_water_way = True
        fang "I think maybe later.. {w=1}When this interview is finished."
        jump beijing_interview_after
    "No" if persistent.tao_water_way:
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
"I stood up from the uncomfortable chair and approached the shrine."
"It was peaceful to stand before the shrine."
"I wasn't required to announce my presence."
"Part of me was afraid of the new world I had stepped into."
"Will the gods protect me?"
"Thoughts invaded my mind as I looked at the shrine."
"Lúgōuqiáo Shìbiàn had begun only a few days ago."
if not persistent.marco_polo_incident_unlocked:
    $ persistent.unlocked_history.append("1937 Marco-Polo Incident")
    $ persistent.marco_polo_incident_unlocked = True
    $ msg.msg("New event in History Timeline: 1937 Marco-Polo Incident")
else:
    $ msg.msg("Event in History Timeline: 1937 Marco-Polo Incident")
"Uncle Ku ambled out of the guest room with his hands concealed under his robes."
"He grimaced slightly at the situation."
Gu "You might have to wait to attain your visa."
"He seemed to say that calmly."
"Something so important...{w=1} taken so lightly."
fang "That's fine...{w=1} I cant deal with that."
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
fang "Now we have a drunk, a looming war {fast}and what more!" with sshake
"I had lost my composure."
"I could see Uncle Ku's reaction to me lashing out after such a long time."
"Pressure that had built up from everything had finally burst the bottle."
"Uncle Ku looked at me solenmly."
Gu "{cps=*0.35}I'm sorry,{w=1} Fang.{/cps}"
fang "I'm sorry too."
"I turned my back and walked out of the door."
Gu "If there is a air raid just run straight to some air raid shelter."
Gu "If you find a German one, priorotise that."
Gu "The German peoples don't get harassed by {i}guizi{/i}."
if not persistent.guizi:
  $ persistent.unlocked.append('Guizi')
  $ persistent.guizi = True
$ msg.msg("New word added to glossary.")
"I had crossed the Er-men."
$ persistent.unlocked.append('Er-men')
$ msg.msg("New word added to glossary.")
"I kept on walking until I passed through the Da-men."
$ persistent.unlocked.append('Da-men')
$ msg.msg("New word added to glossary.")
default activities_left = 3
"Outside was a little garden where my Great Grandfather had planted a Sakura Tree for Sun Yat Sen's new era of the Republic."
"It's a real shame I never even learnt his name despite knowing how well known he was in this local place."
"My great grandfather disliked the Qing as they were Manchus as opposed to the Ming who were a Han Chinese dynasty."
"He had a wealthy wine business which gave him the money to buy a large {i}Siheyuan{/i}"
"The Sakura was planted to mark the growth a new era without the Qing."
"The Sakura plant was also foreign and thus showcased his wealth when he had it planted."
"Everything I ever learnt about him indicated that...{w=1} wealth controlled his choices."
"Sadly he died before he realised how the Republic failed China."
"{cps=*0.4}or the shortlived Empire before the warlord era.{/cps}"
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
"In six months of residing in this district I had a memorised map of the place."
"There were a few facilities I was going to walk past."
"The most interesting was the brothel."
"The sex industry had grown in Manchuria and many boys would talk about it in the alley ways."
"Over here the brothel was something that you should not be seen entering and leaving if you wanted to have a sense of dignity."
"This brothel was known as a {i}Chang San{/i} brothel."
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
prostitute "The ones you talk to aren't here."
"It seemed their sisterhood all shared the same mind like some collective conscious."
prostitute "They tell me, how you blush when they compliment you."
prostitute "Maybe when you're older you can whisk one away and keep her."
"I gave a faint giggle as I felt butterflies in my stomach."
prostitute "Xiao Wen dreams about you, I've heard."
"That took me off guard."
"I could feel my heart pumping and racing."
"It was just embarassing at this point."
prostitute "I think you two would be cute."
prostitute "By the way, my name is Wang Yuelan."
prostitute "If you ever need shelter, just ask Xiao Wen to share the room."
"She laughed as she opened the door and walked inside."
"They were an interesting bunch,{w=1}strange but interesting."
"While I do confess Xiao Wen's attraction, caste was a stigma that would burrow itself deep in me, like some toxic idea or opinion."
"I felt guilty to admit to myself such things."
if saucy_thoughts <= 30:
  "Despite that..."
  "I couldn't help wanting to... {w=1} touch her."
  "Like feel her skin,"
  "Hear her moan."
  "It would keep me up all night until I did something about it."
  "At this point I didn't know when I felt lust for her,{w=2} and when I felt love."
  "She would flirt with me everytime I would pass by and no one else was around."
  "It was intense."
  "Despite that..{w=1}I can't keep thinking so provocatively."
  "I had to come to my senses."
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
$ timeofday = "early afternoon"
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
if Fang_from_Taiwan:
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
elif Fang_from_Macau:
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
elif Fang_from_Guangzhou:
    #TEST!!!
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
    Gh "Teach me some Cantonese some time,{w=1} When I'm off work, preferably."
    menu:
        "Sure":
            $ promise_teach_Gh_cantonese = True
            fang "I don't mind, it would be nice to teach you."
            Gh "Thanks."
            "Guo Heng was strnage that he wanted to learn a dialect he had no practical use for."
            "but then again he might be like those foreigners who see some gem in the language and learn it to keep a sense of that beauty for themselves."

        "Sorry, I can't":
            fang "I am not confident when it comes to teaching."
            "Guo Heng gave a grin and didn't say anything for a while."
            $ renpy.pause(5, hard=True)
            Gh "That's fine."
            Gh "Not all knowledge can be taught."
            "Guo Heng stood up and looked at the wooden table."
            Gh "I can't read or write or accomplish anything."
            Gh "My father sent me to school and I never tried hard."
            Gh "I can barely make out what something says if I'm lucky."
            "There was a looming guilty melancholia lodged in his head."
            Gh "Can you help me read and write at least?"
            "I could see his eyes looking teary."
            "He was ashamed of himself."
            Gh "I don't want to fall behind."
            "He whispered it, so quietly it could float and be carried by the wind indefinately."
            "At this rate I can't make a choice."
            "I have an oppurtunity."
            call GH_timed_oppurtunity
elif Fang_from_Nanjing:
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
elif Fang_from_hong_kong:
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
    menu:
        "No":
            fang "No no no no!"
            fang "I have enough money to pay for a meal myself."
            fang "I think you shouldn't have to treat me for free."
            "We aren't even that close.."
            Gh "you're very adamant , aren't you？"
            Gh "I'm trying to show my hospitability here!"
            "He gave a warm inviting grin."
            Gh "Whenever you feel like it just come up here and it will be on me."
            "I looked up at him."
            Gh "Don't worry,{w=1} I make enough to treat people for free."
        "Yes":
            $ promise_Guo_heng_free_meal = True
            fang "Sure."
            "Guo Heng smirks at me."
            Gh "I hope you aren't fuilt tripping me for free meals."
            fang "Don't worry Heng, I'm not like that."
            fang "You can trust me after meeting me four times."
            Gh "I'm sure you can."
            Gh "Nobody beats me in eatery around here."
            "It seemed Guo Heng took great pride in his line of work."
elif Fang_from_Beijing:
    fang "I am from Peiping."
    Gh "But you seem new to this place."
    "He was right."
    "Despite the six months I had stayed here with Uncle Ku."
    "I couldn't fit in."
    "I never knew why..."
    fang "There's two reasons to explain that."
    fang "Firstly my family has a habit of moving across China for different jobs and oppurutunities."
    fang "Secondly all my experience of Peiping was South of it where you could consider it a part of Tientsen.{w=1} So I guess overall I lack much experience if any about living in Peiping."
    Gh "I see then."
    Gh "If you need any help anytime..."
    Gh "I'm here and I'll teach you the ropes of anything."
    fang "Thanks."
    fang "That means a lot to me here."
    Gh "I mean you're a guest in our village."
    Gh "We have to look after you."
    fang "Again.{w=1} Thanks."
    Gh "On a separate note...{w=0.5} Have you ever drank some {i}Bai-Jiu{/i}?"
    Gh "Your Great Grandpa's factory sells the good stuff to us, sometimes to some Japanese as well on the other side."
    Gh "You should try it."
    menu:
        "Sure, I'll try":
            $ promise_GH_beer = True
            fang "Surely it can't be that bad."
            Gh "You got a good spirit in you."
            Gh "Unfortunately my work day isn't over{w=1} and I won't cook while I'm not sober."
            Gh "Meet me up tonight for a drink and we can talk about whatever is on our minds."
            Gh "Especially in regards to the start of a war."

        "No thanks, I'm fine":
            $ promise_Gh_talk_escape = True
            fang "I don't feel like drinking."
            Gh "Ah well, that's fine."
            Gh "I respect that."
            Gh "If you need to talk about stuff in your mind just find me after your shift."
            "Guo Heng wiped the rag across his forehead."
            Gh "You probably need to find a way to get out of here."
            Gh "I'm here to help with that."
            fang "I Know..."
            "Guo Heng really just wanted his brother out of harms way{w=1} which must be the reason why he is trying to support me going away from Peiping."



label Beijing_1_GH_afterward:
    "There was nothing to say."
    "It was a bit awkward but it was difficult to articulate conversation."
    "I don't have in the slightest an idea of what to do."
    $ timer_jump = "GH_Beijing_busy"
    show screen countdown
    menu:
        "Keep conversing with Guo Heng.":
            hide countdown
            $ activities_left = 2
            jump GH_dive_convo

        "Take leave":
            hide countdown
            fang "I think its time I get moving."
            fang "I have a pending interview to undergo."
            fang "He should be coming to conduct it soon."
            "Guo Heng rubbed the rag on his face."
            Gh "I have to work anyway."
            Gh "It was nice to talk with you Fang."
            call GH_first_goodbye

label GH_Beijing_busy:
    "Guo Heng put down his sweat rag."
    "The sun was piercing through his thin ragged shirt."
    "You could see how the sweat now made the shirt a paint to his canvas of a skin."
    Gh "No offence Fang,"
    Gh "I have work now."
    Gh "I can't afford always taking a break."
    Gh "It takes time to make preparations for a meal."
    call GH_first_goodbye
    "I grinned at him as well."
    "It was pleasant."
    "Guo Heng was now slaving away in his kitchen once again."
    "I stood up and walked outside and began to think."
    menu:
        "Catch up on work for school." if is_student:
            $ activities_left += -1
            "I seemed to have a lot of work left."
            "Normally I would be in the urban districts of Peiping where you could see people from all places gather."
            "Even the Japanese across the Marco-Polo Bridge."
            "I would attend Peiping university so I could work abroad."
            "Strangely my dreams seem to force me to run away from my current situation."
            "I begin to walk back home as my books are there."

        "Go to Cheung's silk-house to work" if is_working:
            $ activities_left += -1
            "Uncle Cheung's silk house was an extraordinary beauty."
            "The type poets die away trying to express on paper."
            "In the house full of buckling wooden levers and rods were colorful rags hanging down like the dress of an angel."
            "A lake of dye would sit in the middle where one would use it to well...{nw}"
            "dye clothes."
            "Uncle Cheung's silk house wasn't too far from Guo Heng's shop."
            "It was on the way back home but diverging from the brothel."

        "Visit Shuang-lin temple":
            $ activities_left += -1
            call templevisit
        "Go home":
            call confirm_day_1_go_home
        


return
