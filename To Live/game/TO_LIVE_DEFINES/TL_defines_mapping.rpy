##     ##    ###    ########  ##      ##  #######  ########  ##    ## 
###   ###   ## ##   ##     ## ##  ##  ## ##     ## ##     ## ##   ##  
#### ####  ##   ##  ##     ## ##  ##  ## ##     ## ##     ## ##  ##   
## ### ## ##     ## ########  ##  ##  ## ##     ## ########  #####    
##     ## ######### ##        ##  ##  ## ##     ## ##   ##   ##  ##   
##     ## ##     ## ##        ##  ##  ## ##     ## ##    ##  ##   ##  
##     ## ##     ## ##         ###  ###   #######  ##     ## ##    ## 
default show_beijing  = True
init -10 python:          
    class GuoPlace(object):
        def __init__(self, x, y, name, IsActive, country, ID, Port, Capital):
            self.x = x
            self.y = y
            self.name = name
            self.IsActive = IsActive
            self.country = country
            self.ID = ID
            self.Port = Port
            self.Capital = Capital 

            
    class Nation(object):
        def __init__(self, name, ID, leader, leadersub, politicalID, AlignmentID, rulingparty, factionID, stability, warsupport, IsActive, flagimg, info):
            self.name = name
            self.ID = ID
            self.leader = leader
            self.leadersub = leadersub
            self.politicalID = politicalID
            self.AlignmentID = AlignmentID
            self.rulingparty = rulingparty
            self.factionID = factionID
            self.stability = stability
            self.warsupport = warsupport
            self.IsActive = IsActive
            self.flagimg = flagimg
            self.info = info
    TL_GUO_loc = []
    TL_GUO = []
    t = 0
    while t < 50:
        TL_GUO_loc.append(GuoPlace(0,0,"", False, "","", False, False))
        TL_GUO.append(Nation("","","","","","","","",0,0, False, "",""))
        #TL_faction.append(faction("", True, False))
        t += 1

    TL_GUO_loc[0] = GuoPlace(2819, 2023, "Kwangchow", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[1] = GuoPlace(2888, 2062, "Hong Kong", True, TL_GUO[17], "ENG", True, False)
    TL_GUO_loc[2] = GuoPlace(2826, 2069, "Macau", True, TL_GUO[18], "POR", True, False)
    TL_GUO_loc[3] = GuoPlace(2565, 2167, "Kwang-Chow Wan", True, TL_GUO[19], "FRA", True, False)
    TL_GUO_loc[4] = GuoPlace(3436, 1392, "Shanghai", True, TL_GUO[0], "CHI",True, False)
    TL_GUO_loc[5] = GuoPlace(3262, 1341, "NanKing", True, TL_GUO[0], "CHI", False, True)
    TL_GUO_loc[6] = GuoPlace(4040, 2230, "Peiping", True, TL_GUO[0], "CHI", False, True)
    TL_GUO_loc[7] = GuoPlace(3276, 1805, "Foochow", True, TL_GUO[0], "CHI", True, False)
    TL_GUO_loc[8] = GuoPlace(3450, 1492, "Ning-Po", True, TL_GUO[0], "CHI", True, False)
    TL_GUO_loc[9] = GuoPlace(3042, 1556, "Nan-Kang", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[10] = GuoPlace(3087, 1462, "An-King", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[11] = GuoPlace(3037, 840, "Tientsin", True, TL_GUO[0], "CHI", False, True)
    TL_GUO_loc[12] = GuoPlace(3291, 1022, "Tsingtao", True, TL_GUO[9], "SDC", False, True)
    TL_GUO_loc[13] = GuoPlace(3297, 925, "Wei-Hai-Wei", True, TL_GUO[9], "SDC", False, True) 
    TL_GUO_loc[14] = GuoPlace(3325, 827, "Port Arthur", True, TL_GUO[2], "JAP", True, False)
    TL_GUO_loc[15] = GuoPlace(2013, 775, "Peiping", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[16] = GuoPlace(3336, 1400, "Soochow", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[17] = GuoPlace(3443, 1600, "Tai Ping", True, TL_GUO[0], "CHI", True, False)
    TL_GUO_loc[18] = GuoPlace(3187, 1884, "Chang Chow", True, TL_GUO[0], "CHI", True, False)






    #Civil War
    TL_GUO[0] = Nation("Republic of China", "CHI", "Chiang Chie Shih", "Generalissimo President of the Republic", "Conservative Junta", "Central Government of Kuomintang", "Kuomintang", "Allied Front", 40, 50, True, "country_flags/CHI.png", "The Republic of China was established on Janurary 1st 1912 after the Xinhai Revolution which overthrew the Qing dynasty. It was de-facto dissolved during the warlord era until in 1921 the Kuomintang established a rival government in Canton. Chiang Chieh Shih who came into power through a military coup began a northern expedition to capture cities fro warlords and proclaim a central government to unite China under. Many foreign nations recognised the Nationalist government as the legitimate unified government of China, even the Soviet Union which supported the Chinese communists. After the Nanjing decades of the 1930s the Republic was weak and thrown into constant war of unification and resistance against foreign powers such as Japan.")
    TL_GUO[1] = Nation("Chinese Soviet Republic", "PRC", "Mao Tse-Tung", "Revolutionary Marxist Leader", "Marxist Guerillas", "International Marxism", "Chung-kuo Kung-ch'an-tang", "Allied Front", 30, 30, True, "country_flags/PRC_1937.png", "" )
    #CO-Propserity Sphere
    TL_GUO[2] = Nation("Empire of Japan", "JAP", "Emperor Hirohito", "Emperor of Japan", "Fascist Monarchy", "Co-Prosperity Sphere", "Tohokai", "Co-Properity Sphere", 60, 90, True, "country_flags/JAP.png", "")
    TL_GUO[3] = Nation("Empire of Manchukuo", "MAN", "Aisin Gioro Pu-Yi","Collaborationist Emperor of Manchukuo", "Fascist Puppet Monarchy", "Co-Prosperity Sphere", "Manchōwkuó Hsiéhehuì", "Co-Prosperity Sphere", 70, 70, True, "country_flags/MAN.png", "")
    TL_GUO[4] = Nation("Reorganized National Government of the Republic of China", "RNG", "Wang Ching-Wei","Japanese Collaborationist Dictator", "Fascist Puppet State", "Co-Prosperity Sphere", "Left Kuomintang", "Co-Prosperity Sphere", 40, 30, False, "country_flags/RNG.png", "")
    #Warlord Cliques
    TL_GUO[5] = Nation("Shaanxi Clique", "SHX", "Yan HsiShan", "Warlord", "Conservative Junta", "Central Government of Kuomintang", "Kuomintang", "Allied Front", 40, 50, True, "country_flags/SHX.png", "")
    TL_GUO[6] = Nation("Hsi Bei San Ma", "XSM", "Ma Bu Fang", "Warlord", "Conservative Junta", "Central Government of Kuomintang", "Kuomintang", "Allied Front", 40, 50, True, "country_flags/XSM.png", "")
    TL_GUO[7] = Nation("KwangHsi Clique", "GXC", "Li Tsun-Jen", "Warlord", "Conservative Junta", "Central Government of Kuomintang", "Kuomintang", "Allied Front", 40, 50, True, "country_flags/GXC.png", "")
    TL_GUO[8] = Nation("Yunnan Clique", "YUN", "Lung Yun", "Warlord", "Conservative Junta", "Central Government of Kuomintang", "Kuomintang", "Allied Front", 40, 50, True, "country_flags/YUN.png", "")
    TL_GUO[9] = Nation("Shandong Clique", "SDC", "Chang Tsung-ch'ang", "Warlord", "Conservative Junta", "Central Government of Kuomintang", "Kuomintang", "Allied Front", 40, 50, True, "country_flags/SDC.png", "")
    TL_GUO[10] = Nation("Hunan Clique", "HNC", "Chang Chih Chung", "Warlord", "Conservative Junta", "Central Government of Kuomintang", "Kuomintang", "Allied Front", 40, 50, True, "country_flags/HNC.png", "")
    TL_GUO[11] = Nation("Szechewan Clique", "SHC", "Liu Hsiang", "Warlord", "Conservative Junta", "Central Government of Kuomintang", "Kuomintang", "Allied Front", 40, 50, True, "country_flags/SHC.png", "")
    TL_GUO[12] = Nation("Sikang Clique", "SKC", "Liu Wen Hui", "Warlord", "Conservative Junta", "Central Government of Kuomintang", "Kuomintang", "Allied Front", 40, 50, True, "country_flags/SKC.png", "")
    TL_GUO[13] = Nation("Sinkiang Clique", "SIK", "ShengShih Ts'ai", "Warlord", "Soviet Junta", "Internationale & Central Government of Kuomintang", "Kuomintang", "Allied Front", 25, 30, True, "country_flags/SIK.png", "")
    TL_GUO[14] = Nation("Kingdom of Tibet", "TIB", "Tenzin Gyatso", "Warlord", "Monastic Monarchy", "Non-Aligned", "Dalai Lama", "No Faction", 40, 40, True, "country_flags/TIB.png", "")
    TL_GUO[15] = Nation("East Hopeh autonomous\nanti-communism council", "EHA", "Yin-Ju-Keng", "Japanese Collaborationist Dictator", "Buffer State", "Co-Prosperity Sphere", "East Hopei Autonomous Government", "Co-Prosperity Sphere", 50, 60, True, "country_flags/EHA.png", "")
    TL_GUO[16] = Nation("Mongol United\nAutonomous Government", "MEN", "Prince Demchugdongrub", "Japanese Collaborationist Dictator", "Fascist Puppet State", "Co-Prosperity Sphere", "Mongol Military Government", "Co-Prosperity Sphere", 50, 60, True, "country_flags/MEN.png", "")
    #European Colonies
    TL_GUO[17] = Nation("United Kingdom", "ENG", "Neville Chamberlain", "Prime Minister of United Kingdom", "Imperial Federation", "League of Nations", "Conservative Party", "Anglo-French Alliance", 70, 50, True, "country_flags/ENG.png", "")
    TL_GUO[18] = Nation("Portugese Republic", "POR", "Antonio de Oliveira Salazar", "Prime Minister of Portugal", "Authoritarian Republic", "Estada Novo", "Uniao Nacional", "No Faction", 70, 40, True, "country_flags/POR.png", "")
    TL_GUO[19] = Nation("French Republic", "FRA", "Camille Chautemps","Prime Minister of France", "Democratic Republic", "League of Nations", "Parti radical", "Anglo-French Alliance", 80, 70, True, "country_flags/FRA.png", "")
    TL_GUO[20] = Nation("Union of\nSoviet Socialist Republics", "SOV", "Josef Stalin","General Secretary of the Communist Party of the Soviet Union", "Marxist Dictatorship", "International Marxism", "Kommunisticheskaya partiya\nSovetskogo Soyuza", "Comintern", 60, 70, True, "country_flags/SOV.png", "")

    