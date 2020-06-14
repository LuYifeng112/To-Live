#Glossary
define persistent.unlocked = [] # empty word list

#checkpoints
define persistent.maotai = False
define persistent.Peifu = False
define persistent.Taoism = False
define persistent.Yiguandao = False
define persistent.Taoteching = False
define persistent.confucianism = False
define persistent.guizi = False
define persistent.ermen = False
define persistent.damen = False
define persistent.dongbei = False
init -1 python:
    display_desc = ""
    glossary_dict = \
    {'Máotái': 'Maotai originated during the Qing Dynasty (1644–1912), when northern Chinese distillers introduced advanced techniques to local processes to create a distinctive type of baijiu. Thereafter Maotai was produced at several local distilleries. During the Chinese Civil War, People\'s Liberation Army forces camped at Maotai and partook of the local liquor. Following the Communist victory in the war, the government consolidated the local distilleries into one state-owned company, Kweichow Moutai (the name is an old romanization of "Guizhou Maotai"). It became a popular drink at state functions and one of the country\'s most popular spirits.',
     'Pèifú': 'A form of admiration.',
     'Taoism': 'Taoism is a philosophical or religious tradition of Chinese origin which emphasises living in harmony with the Dao ("the way").',
     'Yiguandao' : 'Yiguandao meaning the Consistent Way or Persistent Way, is a Chinese salvationist religious sect that emerged from the Xiantiandao ("Way of Former Heaven") tradition in the late 19th century, in Shandong, to become China\'s most important redemptive society in the 1930s and 1940s, especially during the Japanese invasion. In the 1930s Yiguandao spread rapidly throughout China led by Zhang Tianran, who is the eighteenth patriarch of the Xiantiandao lineage, among thousands of other movements that thrived since the collapse of the Qing dynasty in 1911.',
     'Tao Te Ch\'ing' : 'Tao Te Ch\'ing is a Chinese classic text traditionally credited to the 6th-century BC sage Laozi. It is one of the two fundamental for both philosophical and religious Taoism.',
     'Confucianism' : 'Confucianism is a system of thought and behavior originating in ancient China. Confucianism developed from what was later called the Hundred Schools of Thought from the teachings of the Chinese philosopher Confucius (551–479 BCE). It formed the basis of Chinese legalism, fillial piety and much of the culture and ways of thinking for Chinese civilisations for over 2000 years.',
     'Guizi' : 'Guizi is a pejorative Chinese slang term for foreigners, and has had a history of containing xenophobic connotations. During world war two this was used to refer to the Japanese invaders.',
     'Er-men' : 'Literal Tranlation: Second Door\nIn a traditional Chinese household this is the inner door on must enter after a hallway.',
     'Da-men' : 'Literal Translation: Big Door\n This is the main door that is seen from the outside.',
     'Blueshirts Society' : 'This organisation went under many names such as \'Society of the Practice of the Three Principles of the People\', \'Spirit Encouragement Society\', and the \'China Reconstruction Society\'. This organisation was a secret ultranationalist faction that modelled Italian Fascism in the Kuomintang. The Blueshirts Society mainly had influence in the Nationalist Military and key areas such as the capital of the time \'Nanjing\'. The Blueshirts Society slowly dissolved after the end of the Sino-Japanese war for many reasons. It persisted as a Youth organisation known as \'Youth League of the Three principles of the People\'.',
     'Tong-pei': 'Romanized as \"Dong Bei\" this just means north east and generally defines the Manchurian territory.'}