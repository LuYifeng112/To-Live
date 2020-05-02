label GH_timed_oppurtunity:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'GH_timed_oppurtunity_slow'
    show screen countdown
    menu:
        "Don't worry I can.":
            hide screen countdown
            fang "I believe in you."
            fang "I can teach you everything you need to know."
            "Guo Heng's face lit up."
            "You could see, a faint shimmer of hope in his eyes."
            "He clasped his hands and bowed."
            Gh "Thank you so much."
            "He kept whispering the words to me."
            "I couldn't comprehend this situation."
            "What was upsetting him."
            "What could language offer him."
            "Why am I involved?"
            "Questions swirled in my head as Guo Heng sat back at the table."
            "He wiped his teary eyes with his dirt painted sleeves."
            Gh "Fang this means so much to me."
            Gh "Sorry for getting so worked up."
            Gh "Stuff like this happens you know."
            return
        "Don't sweat it":
            hide screen countdown
            "I couldn't directly refuse him."
            "I could however console him."
            "I had a feeling he had a sense of self hate for failing his father academically."
            "His father probably worked hard to educate him and now he can't move on from regrets."
            "Guo Heng could only look at me."
            fang "Don't overthink."
            fang "Have a seat."
            "I felt like I was talking to some distraught older brother."
            fang "Have a seat."
            "I urged him once again."
            "Guo Heng glanced at the wooden bench and gradually leveled down to sit on it."
            fang "I don't have confidence to teach."
            fang "I can't be anyone's bastion of hope."
            "Guo Heng listened patiently."
            "I had to make him understand my view."
            Gh "You're very wise Fang."
            "Guo Heng seemed more calm and collected now."
            "He sat as if he didn't go through what he did now."
            "He championed his hiding abilities."
            #Talk abot villagers belittling him 
            return

label GH_timed_oppurtunity_slow:
    "Guo Heng was still teary."
    "My body was frozen."
    "I didn't know how to approach this situation."
    "I have never seen anyone here to emotional."
    "Perhaps I had been{w=1} selfish."
    "Guo Heng wiped his teary wet eyes into his dirt painted ragged sleeves."
    "He clenched his fists and unclenched as he sat back down at the table."
    Gh "Forget it."
    "I could tell his strength was a facade."
    "Something was breaking him into pieces inside."
    "I'm just too selfish to notice."
    fang "I'm sorry Guo-{nw}"
    Gh "Leave it."
    Gh "Don't talk about it."
    "Guo Heng seemed to want to forget about it."
    "I wasn't sure why he had so much self hate for not studying well."
    "Perhaps he felt he failed his father."
    "I wasn't much different as well."
    "He was quite and more collected."
    "I could tell a difference in the atmosphere."
    jump Beijing_1_GH_afterward

label GH_dive_convo:

    return

label GH_first_goodbye:
    "Guo Heng stood up."
    if promise_Guo_heng_free_meal:
        Gh "I hope you come for that meal I promised."
        "He have a cheerful grin to me."
    if promise_teach_Gh_cantonese:
        Gh "I look forward to learning new things."
        "He have a cheerful grin."
    if promise_Gh_talk_escape:
        Gh "I look forward to helping you out if you come to talk tonight."
        "He gave a cheerful grin."
    if promise_GH_beer:
        Gh "Join me for some beer."
        "He pointed to a distilled alcoholic bottle sitting inside his work kitchen."
    return