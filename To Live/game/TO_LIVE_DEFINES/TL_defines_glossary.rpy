init python:
    class glossarydict(object):
        def __init__(self, container):
            self.container = container

        def addword(self, word):
            if word not in self.container:
                if word in glossary_dict:
                    self.container.append(word)
                    msg.msg("New Word in Glossary: "+word)
                else:
                    raise Exception("Mispelt or non-existent key being added.")
            else:
                msg.msg(word+" is already in the glossary")

default TL_glossary = glossarydict(
    container = persistent.unlocked
    )
#Glossary
define persistent.unlocked = [] # empty word list
init -1 python:
    display_desc = ""
    glossary_dict = \
    {__('Maotai'): __('Maotai originated during the Qing Dynasty (1644–1912), when northern Chinese distillers introduced advanced techniques to local processes to create a distinctive type of baijiu. Thereafter Maotai was produced at several local distilleries. During the Chinese Civil War, People\'s Liberation Army forces camped at Maotai and partook of the local liquor. Following the Communist victory in the war, the government consolidated the local distilleries into one state-owned company, Kweichow Moutai (the name is an old romanization of "Guizhou Maotai"). It became a popular drink at state functions and one of the country\'s most popular spirits.'),
     __('Peifu'): __('A form of admiration. Typically used to admire someone\'s efforts or character.'),
     __('Taoism'): __('Taoism is a philosophical or religious tradition of Chinese origin which emphasises living in harmony with the Dao ("the way").'),
     __('Yiguandao') : __('Yiguandao meaning the Consistent Way or Persistent Way, is a Chinese salvationist religious sect that emerged from the Xiantiandao ("Way of Former Heaven") tradition in the late 19th century, in Shandong, to become China\'s most important redemptive society in the 1930s and 1940s, especially during the Japanese invasion. In the 1930s Yiguandao spread rapidly throughout China led by Zhang Tianran, who is the eighteenth patriarch of the Xiantiandao lineage, among thousands of other movements that thrived since the collapse of the Qing dynasty in 1911.'),
     __('Tao Te Ch\'ing') : __('Tao Te Ch\'ing is a Chinese classic text traditionally credited to the 6th-century BC sage Laozi. It is one of the two fundamental for both philosophical and religious Taoism.'),
     __('Confucianism') : __('Confucianism is a system of thought and behavior originating in ancient China. Confucianism developed from what was later called the Hundred Schools of Thought from the teachings of the Chinese philosopher Confucius (551–479 BCE). It formed the basis of Chinese legalism, fillial piety and much of the culture and ways of thinking for Chinese civilisations for over 2000 years.'),
     __('Guizi') : __('Guizi is a pejorative Chinese slang term for foreigners, and has had a history of containing xenophobic connotations. During world war two this was used to refer to the Japanese invaders.'),
     __('Er-Men') : __('Literal Tranlation: Second Door\nIn a traditional Chinese household this is the inner door on must enter after a hallway.'),
     __('Da-Men') : __('Literal Translation: Big Door\n This is the main door that is seen from the outside.'),
     __('Blueshirts Society') : __('This organisation went under many names such as \'Society of the Practice of the Three Principles of the People\', \'Spirit Encouragement Society\', and the \'China Reconstruction Society\'. This organisation was a secret ultranationalist faction that modelled Italian Fascism in the Kuomintang. The Blueshirts Society mainly had influence in the Nationalist Military and key areas such as the capital of the time \'Nanjing\'. The Blueshirts Society slowly dissolved after the end of the Sino-Japanese war for many reasons. It persisted as a Youth organisation known as \'Youth League of the Three principles of the People\'.'),
     __('Tong-pei'): __('Romanized as \"Dong Bei\" this just means north east and generally defines the Manchurian territory. These normally include the provinces of Heilongjiang, Liaoning, Jilin and a portion of Inner Mongolia.'),
     __('Yīnyáng'):__('N/A'),
     __('Siheyuan'):__('N/A'),
     __('Chang San'): __('N/A'),
     __('Ma-Kok'):__('N/A'),
     __('Bai-Jiu'):__('N/A'),
     __('I-Kuan-Tao'):__('N/A')}