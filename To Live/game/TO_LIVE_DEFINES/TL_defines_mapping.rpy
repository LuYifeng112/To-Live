##     ##    ###    ########  ##      ##  #######  ########  ##    ## 
###   ###   ## ##   ##     ## ##  ##  ## ##     ## ##     ## ##   ##  
#### ####  ##   ##  ##     ## ##  ##  ## ##     ## ##     ## ##  ##   
## ### ## ##     ## ########  ##  ##  ## ##     ## ########  #####    
##     ## ######### ##        ##  ##  ## ##     ## ##   ##   ##  ##   
##     ## ##     ## ##        ##  ##  ## ##     ## ##    ##  ##   ##  
##     ## ##     ## ##         ###  ###   #######  ##     ## ##    ## 
init -10 python:          
    class GuoPlace(object):
        def __init__(self, x, y, name, IsActive, country, ID):
            self.x = x
            self.y = y
            self.name = name
            self.IsActive = IsActive
            self.country = country
            self.ID = ID
            
    class Nation(object):
        def __init__(self, name, ID, leader, politicalID, AlignmentID, rulingparty, factionID, stability, warsupport):
            self.name = name
            self.ID = ID
            self.leader = leader
            self.politicalID = politicalID
            self.AlignmentID = AlignmentID
            self.rulingparty = rulingparty
            self.factionID = factionID
            self.stability = stability
            self.warsupport = warsupport

    TL_GUO_loc = []
    TL_GUO = []
    t = 0
    while t < 50:
        TL_GUO_loc.append(GuoPlace(0,0,"", False, "",""))
        TL_GUO.append(Nation("","","","","","","",0,0))
        t += 1

    TL_GUO_loc[0] = GuoPlace(2819, 2023, "Kwangchow", True, "Republic of China", "ROC")
    TL_GUO_loc[1] = GuoPlace(2888, 2062, "Hong Kong", True, "United Kingdom", "ENG")
    TL_GUO_loc[2] = GuoPlace(2826, 2069, "Macau", True, "Portugese Republic", "POR")
    TL_GUO_loc[3] = GuoPlace(2565, 2167, "Kwang-Chow Wan", True, "French Republic", "FRA")
    TL_GUO_loc[4] = GuoPlace(3436, 1392, "Shanghai", True, "Republic of China (Interntional Settlement)", "CHI")
    TL_GUO_loc[5] = GuoPlace(3262, 1341, "NanKing", True, "Republic of China", "CHI")
    TL_GUO_loc[6] = GuoPlace(4040, 2230, "Peiping", True, "Republic of China", "CHI")
    TL_GUO_loc[7] = GuoPlace(3276, 1805, "Foochow", True, "Republic of China", "CHI")
    TL_GUO_loc[8] = GuoPlace(3450, 1492, "Ning-Po", True, "Republic of China", "CHI")
    TL_GUO_loc[9] = GuoPlace(3042, 1556, "Nan-Kang", True, "Republic of China", "CHI")
    TL_GUO_loc[10] = GuoPlace(3087, 1462, "An-King", True, "Republic of China", "CHI")




    
    TL_GUO[0] = Nation("Republic of China", "ROC", "Chiang Chie Shih", "Conservative Junta", "Central Government of Kuomintang", "Kuomintang", "Allied Front", 40, 50)
    TL_GUO[1] = Nation("People's Liberation Army", "PRC", "Mao Tse-Tung", "Marxist Guerillas", "Chinese Soviet Republic", "Chung-kuo Kung-ch'an-tang", "Allied Front", 30, 30)
    TL_GUO[2] = Nation("Empire of Japan", "JAP", "Emperor Hirohito", "Fascist Monarchy", "Co-Prosperity Sphere", "Tohokai", "Co-Properity Sphere", 60, 90)
    TL_GUO[3] = Nation("Empire of Manchukuo", "MAN", "Aisin Gioro Pu-Yi", "Fascist Puppet Monarchy", "Co-Prosperity Sphere", "Manchōwkuó Hsiéhehuì", "Co-Prosperity Sphere", 70, 70)
    TL_GUO[4] = Nation("Reorganized National Government of the Republic of China", "RNG", "Wang Ching-Wei", "Fascist Puppet State", "Co-Prosperity Sphere", "Left Kuomintang", "Co-Prosperity Sphere", 40, 30)
    TL_GUO[5] = Nation("Shaanxi Clique", "SHX", "Yan HsiShan", "Conservative Junta", "Central Government of Kuomintang", "Kuomintang", "Allied Front", 40, 50)
    TL_GUO[6] = Nation("Xi Bei San Ma", "XSM", "Ma Bu Fang", "Conservative Junta", "Central Government of Kuomintang", "Kuomintang", "Allied Front", 40, 50)
    TL_GUO[7] = Nation("KwangHsi Clique", "GXC", "Li Tsun-Jen", "Conservative Junta", "Central Government of Kuomintang", "Kuomintang", "Allied Front", 40, 50)
    TL_GUO[8] = Nation("Yunnan Clique", "YUN", "Lung Yun", "Conservative Junta", "Central Government of Kuomintang", "Kuomintang", "Allied Front", 40, 50)