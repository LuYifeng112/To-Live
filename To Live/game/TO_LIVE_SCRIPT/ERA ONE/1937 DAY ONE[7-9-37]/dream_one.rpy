label dream_one:
    "I feel light."
    "I feel as if there's no weight in me."
    "Like something scraped me from the inside to become hollow."
    "Everything is dark."
    "But I don't feel alone."
    v "Absolution."
    "The voices kept murmuring."
    "Gossiping about me."
    "I could feel it."
    f "It's true,{w=0.5}urchin."
    f "They all just gossip about you."
    f "How pathetic you are."
    f "How weak you are."
    f "You're failure to face reality."
    f "Your desire to run away from your responsibility."
    v "Failure."
    f "Did you ever stop and consider anyone else in your life apart from yourself?"
    menu:
        "Yes":
            fang "Of course I have!"
            f "Saying is one thing."
            f "Doing is another."
            f "Your actions so far only prove your selfishness."

        "No":
            fang "Is there a reason to place something else before my own sense of self?"
            f "That is a answer you will discover yourself."
    f "I do not exist to guide you."
    f "My reasons for my actions are beyond materialized concepts."
    f "The mother pities you urchin."
    f "I do not."
    f "I will remind you of your sins."
    f "from this day on the choices you make."
    f "the actions you take"
    f "they will be observed."
    f "Will you choose to dirty your hands?"
    f "Will you save and defend people?"
    f "You are alone."
    f "You will be alone."
    f "You will be judged every moment."
label dream_one_convo:
    menu:
        "What are you?" if not whatisfather:
            $ whatisfather = True
            f "Something you can't comprehend."
            f "I may be a part of you."
            f "An incarnation of your guilt, self hate or frustrations."
            f "I may be a passing thought."
            f "I may be the essence of your character with autonomy."
            f "You will have to define me."
            jump dream_one_convo
        
