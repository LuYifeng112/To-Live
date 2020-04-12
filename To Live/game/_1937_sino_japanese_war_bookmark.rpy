
label Beijing_chapter_one:

un "It is important you answer these questions properly."
un "I will go through them one by one."
un "Do not fret."

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

$ renpy.notify("You are being interviewed")
Po "Well Let us start now."
Po "When the Japanese as where you are from it will typically give them a first impression about you."
Po "I know you and your family have moved places over the years so what is your go to hometown."
Po "Where is it most convenient for you to return home so you won't have any difficulty resettling or get bothered by Japanese."

menu:
    "Peiping":
        $ Fang_from_Beijing = True
        $ Japanese_aggression = 3
        fang "I'm from Peiping"
        Gu "I'd suggest you move out of Beijing."
        Gu "Yan'an is swarming with communists otherwise I would have recommended a temporary stay there."
        Gu "My best bet would be to send you to Qingdao."
        Po "I'd have to be agree with Gu-hsien-sheng"
        Gu "I have a shcolarly friend who can provide you with oppurtunities for work."
        Gu "Qingdao will be familiar to you."
        Gu "You should also prepare your family to leave for Qingdao."
        jump Beijing_chapter_one_uncle_interview_intention

    "Nanking":
        $ Fang_from_Nanjing = True
        $ Japanese_aggression = 8
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
        fang "I'm from Kwangchow"
        Gu "Under Li Tsung-jen?"
        Gu "I wonder if he can survive or General Chiang will have to bail him out."
        Gu "I think you're safe there, besides you'll fit in there more that here."
        Gu "Your hometown seem to be out of harms way and strife."
        Gu "I suggest you go back to your family and try to prepare what to do next."
        jump Beijing_chapter_one_uncle_interview_intention

    "Hong-Kong":
        $ Fang_from_hong_kong = True
        $ Japanese_aggression = 1
        fang "I'm from Hong-Kong"
        Po "It is a good place."
        Po "The British may be a bit foreign to us mainlanders but at least their territories aren't at risk of being involved in a war."
        Gu "Your hometown seem to be out of harms way and strife."
        Gu "I suggest you go back to your family and try to prepare what to do next."
        jump Beijing_chapter_one_uncle_interview_intention

    "Macau":
        $ Fang_from_Macau = True
        $ Japanese_aggression = 1
        fang "I'm from Macau"
        Gu "A place that won't get thrashed by war."
        Gu "Some people are born lucky I guess."
        Gu "I think it is a safe place that you should consider returning to."
        Gu "Your hometown seem to be out of harms way and strife."
        Gu "I suggest you go back to your family and try to prepare what to do next."
        jump Beijing_chapter_one_uncle_interview_intention

    "Taiwan":
        $ Fang_from_Taiwan = True
        $ Japanese_aggression = 0
        fang "I'm from Taiwan"
        Gu "From the foreign devils themself."
        "He chuckles"
        Gu "They won't mess with you then i guess."
        jump Beijing_chapter_one_uncle_interview_intention

label Beijing_chapter_one_uncle_interview_intention:
Po "So what are you doing in Beijing right now?"

menu:
    "Attending school as a student.":
        $ Fang_determination = 3
        $ Fang_intellect = 3
        $ Fang_dexterity = 2
        play sound "sounds/stat_increase/00_stat_increase.ogg"
        "{font=fonts/eng_octin_spraypaint/octin spraypaint a rg.ttf}{color=#4fc1ff}Fang gained 3 Determination; 3 Intellect and 2 Dexterity!{/color}{/font}"
        fang "I came here to actually continue my education."
        fang "I am staying with Uncle Ku since it is close to the facilities."
        Po "I doubt schools will run under foreign occupation."
        Po "Well classes won't."
        Po "Most students back in Dongbei would just live at the boarding school."
        Po "I think you'll family will need you more."
        jump Beijing_chapter_one_uncle_interview_intention

    "Working as a scholarly apprentice under my uncle":
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
        jump Beijing_chapter_one_uncle_interview_intention
    
    "Working here to send money back home.":
        $ Fang_determination = 2
        $ Fang_wealth = 3
        play sound "sounds/stat_increase/00_stat_increase.ogg"
        "{font=fonts/eng_octin_spraypaint/octin spraypaint a rg.ttf}{color=#4fc1ff}Fang gained 2 determination and 3 wealt!{/color}{/font}"
        Po "what a hardworking kid."
        Gu "I agree."
        Gu "This kind of attitude sculpts heroes and leaders."
        Po "You have probably saved enough now. Have you?"
        fang "yes, it is sufficient I would say."
        Po "That is great to hear"
        jump Beijing_chapter_one_uncle_interview_intention

    "Taking a break after military conscription training":
       $ Fang_strength = 3
       $ Fang_determination = 4
       $ Fang_dexterity = 4
       $ Fang_wealth = 2
       play sound "sounds/stat_increase/00_stat_increase.ogg"
       "{font=fonts/eng_octin_spraypaint/octin spraypaint a rg.ttf}{color=#4fc1ff}Fang gained 3 strength; 4 determination; 4 dexterity and 2 wealth!{/color}{/font}"
       fang "I'm from Hong-Kong"
       jump Beijing_chapter_one_uncle_interview_intention


return