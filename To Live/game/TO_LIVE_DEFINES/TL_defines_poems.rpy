init python:
    class poemdict(object):
        def __init__(self, container):
            self.container = container

        def addpoem(self, poem):
            if poem not in self.container:
                if poem in poem_dict:
                    self.container.append(poem)
                    msg.msg("New poem in Poem Booklet: "+poem)
                else:
                    raise Exception("Mispelt or non-existent poem key being added.")
            else:
                msg.msg(poem+" is already in the Poem Booklet")
        def haspoem(self, poem):
            return poem in self.container

default TL_poem = poemdict(
    container = persistent.unlocked_poem
    )
#Poem
define persistent.agneepath = False
define persistent.tao_water_way = False
define persistent.wjw = False
define persistent.unlocked_poem = []

init -1 python:
    poem_display_desc = ""
    poem_dict = \
    {'Dhammapada': 'Through the round of many births I roamed\nwithout reward,\n without rest,\nseeking the house-builder.\nPainful is birth\n  again and again.\nHouse-builder, you\'re seen!\nYou will not build a house again.\nAll your rafters broken,\nthe ridge pole destroyed,\ngone to the Unformed,\nthe mind has come to the end of craving.\n -Gautama Buddha 3rd Century B.C.E',
     'Tao The Water Way' : 'The best of men is like water;\nWater benefits all things\nAnd does not compete with them.\nIt dwells in (the lowly) places that all disdain –\nWherein it comes near to the Tao.\nIn his dwelling, (the Sage) loves the (lowly) earth;\nIn his heart, he loves what is profound;\nIn his relations with others, he loves kindness;\nIn his poems, he loves sincerity;\nIn government, he loves peace;\nIn business affairs, he loves ability;\nIn hi actions, he loves choosing the right time.\nIt is because he does not contend\nThat he is without reproach.\nLao Tzu Tao Te Ch\'ing Chapter 8',
     'Orally Composed Upon Being Captured' : 'Carrying pebbles in its beak was the utmost folly;\nOver dark waves, tens thousand miles of sorrow.\nIn its solitary flight it never halts in fatigue,\nShamed to follow the seagulls and float[with the tide].\nShades of rich purle, crimson scarlett -\nIt has always been known that these are hard to dye.\nAnother day when the tender blossoms bloom,\nPlease recognise on them the speckles of my blood,\nWith heroic abandon I sing in the market of Yan;\nWith calm and ease I become a prisoner from Chu.\nDraw the blade, what a thrill!\nIts sharpness deserves this fien young head!\nI will preserve only my heart, my soul;\nThe remainder shall be burnt in a kalpa to ashes.\nIts blue ghost lights will never be extinguished -\nNight after night, they will shine upon the Terrace of Yan.\n   -Wang Jingwei [while in prison for an attempted assasination of an Imperial Prince.]'}    