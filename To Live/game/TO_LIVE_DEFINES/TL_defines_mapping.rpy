###  ##      ##  #######  ########  ##    ## 
###   ###   ## ##   ##     ## ##  ##  ## ##     ## ##     ## ##   ##  
#### ####  ##   ##  ##     ## ##  ##  ## ##     ## ##     ## ##  ##   
## ### ## ##     ## ########  ##  ##  ## ##     ## ########  #####    
##     ## ######### ##        ##  ##  ## ##     ## ##   ##   ##  ##   
##     ## ##     ## ##        ##  ##  ## ##     ## ##    ##  ##   ##  
##     ## ##     ## ##         ###  ###   #######  ##     ## ##    ## 
default show_beijing  = True
default n_map = True

init -10 python:          
    class GuoPlace(object):
        '''
        This is the class that creates map coordinate for the map.
        - It consists of X,Y coordinates for placement.
        - The city name that will be displayed in the text button.
        - Whether that city is visible or accessible to show the country.
        - A country specific ID that has to be the same as the Nation class.
        - Port and Capital jus set map point visuals.
        '''
        def __init__(self, x, y, name, IsActive, ID, Port, Capital):
            self.x = x
            self.y = y
            self.name = name
            self.IsActive = IsActive
            self.ID = ID
            self.Port = Port
            self.Capital = Capital
        def deact(self):
            self.IsActive = False
    class Guoflavour(object):
        def __init__(self, x, y, name, IsActive, strength, icon):
            self.x = x
            self.y = y
            self.name = name
            self.IsActive = IsActive
            self.strength = strength 
            self.icon = icon
    
    class Province(object):
        def __init__(self, x, y, name, ID, ProvinceID):
            self.x = x
            self.y = y
            self.name = name 
            self.ID = ID
            self.ProvinceID = ProvinceID

    class Nation(object):
        '''
        How countries are displayed. These are containers for information.
        '''
        def __init__(self, name, ID, leader, leadersub, politicalID, AlignmentID, rulingparty, factionID, IsActive, dead, flagimg, log, info):
            self.name = name                    #THe official name of the country.
            self.ID = ID                        #A shortened ID to compare to the map point ID. This is a link.
            self.leader = leader                
            self.leadersub = leadersub          #The position of the leader of the country.
            self.politicalID = politicalID      #Form of ideology and government.
            self.AlignmentID = AlignmentID      #Which power does it align itself to? or ideology.
            self.rulingparty = rulingparty      
            self.factionID = factionID
            self.IsActive = IsActive
            self.dead = dead                    #Dead countries will display but you can track changes across time.
            self.flagimg = flagimg
            self.log = log
            self.info = info

        def activate(self):
            self.isActive = True
            devlog.info("Activated Country")
        def dead(self):
            self.dead = True

        def setname(self, setname):
            self.name = setname

        def setleader(self, boss):
            self.leader = boss

        def flag(self, flag):
            self.flagimg = flag

        def getleadername(self):
            global leader
            leader = self.leader

    TL_GUO_loc = []
    TL_GUO = []
    TL_map_flavour = []
    TL_Provinces = []
    t = 0
    while t < 200:
        TL_GUO_loc.append(GuoPlace(0,0,"",False, "", False, False))
        TL_GUO.append(Nation("", "", "", "", "", "", "", "", False, False, "", "", ""))
        TL_map_flavour.append(Guoflavour(0,0,"", False, 0, ""))
        TL_Provinces.append(Province(0,0,"", "",""))
        t += 1

         ######  #### ######## #### ########  ######  
        ##    ##  ##     ##     ##  ##       ##    ## 
        ##        ##     ##     ##  ##       ##       
        ##        ##     ##     ##  ######    ######  
        ##        ##     ##     ##  ##             ## 
        ##    ##  ##     ##     ##  ##       ##    ## 
         ######  ####    ##    #### ########  ######  
    '''
    These two defines play around with map button sensitivity.
    If we want to disable looking up the owner for a city say for a quiz then we can toggle it with these two function.
    '''  
    def mapon():
        n_map = True
    def mapoff():
        n_map = False 
    '''
    A list of indexed class objects for cities.
    '''
    TL_GUO_loc[0] = GuoPlace(2819, 2010, __("Kwangchow"), True, "CHI", False, False)
    TL_GUO_loc[1] = GuoPlace(2888, 2062, __("Hong Kong"), True, "ENG", True, False)
    TL_GUO_loc[2] = GuoPlace(2826, 2069, __("Macau"), True, "POR", True, False)
    TL_GUO_loc[3] = GuoPlace(2565, 2167, __("Kwang-Chow Wan"), True, "FRA", True, False)
    TL_GUO_loc[4] = GuoPlace(3436, 1392, __("Shanghai"), True, "CHI",True, False)
    TL_GUO_loc[5] = GuoPlace(3262, 1341, __("Nanking"), True, "CHI", False, True)
    TL_GUO_loc[6] = GuoPlace(2519, 2046, __("Yulin"), True, "GXC", False, False)
    TL_GUO_loc[7] = GuoPlace(3276, 1805, __("Foochow"), True, "CHI", True, False)
    TL_GUO_loc[8] = GuoPlace(3450, 1492, __("Ning-Po"), True, "CHI", True, False)
    TL_GUO_loc[9] = GuoPlace(3042, 1556, __("Nan-Kang"), True, "CHI", False, False)
    TL_GUO_loc[10] = GuoPlace(3087, 1462, __("An-King"), True, "CHI", False, False)
    TL_GUO_loc[11] = GuoPlace(3037, 840, __("Tientsin"), True, "CHI", True, False)
    TL_GUO_loc[12] = GuoPlace(3291, 1022, __("Tsingtao"), True, "SDC", True, False)
    TL_GUO_loc[13] = GuoPlace(3399, 927, __("Wei-Hai-Wei"), True, "SDC", True, False) 
    TL_GUO_loc[14] = GuoPlace(3325, 827, __("Da-ren"), True, "JAP", True, False)
    TL_GUO_loc[15] = GuoPlace(3013, 775, __("Peiping"), True, "CHI", False, False)
    TL_GUO_loc[16] = GuoPlace(3336, 1400, __("Soochow"), True, "CHI", False, False)
    TL_GUO_loc[17] = GuoPlace(3443, 1600, __("Tai Ping"), True, "CHI", True, False)
    TL_GUO_loc[18] = GuoPlace(3187, 1884, __("Chang Chow"), True, "CHI", True, False)
    TL_GUO_loc[19] = GuoPlace(2448, 1139, __("Sian"), True, "PRC", False, False)
    TL_GUO_loc[20] = GuoPlace(3415, 1972, __("Kaohshiung"), True, "JAP", True, False)
    TL_GUO_loc[21] = GuoPlace(3493,1825, __("Taipei"), True, "JAP", True, False)
    TL_GUO_loc[22] = GuoPlace(3440, 591, __("Mukden"), True, "MAN", False, True)
    TL_GUO_loc[23] = GuoPlace(3326, 931, __("Yantai"), True, "SDC", True, False)
    TL_GUO_loc[24] = GuoPlace(3185, 999, __("Weifang"), True, "SDC", False, False)
    TL_GUO_loc[25] = GuoPlace(3138, 1111, __("Lini"), True, "SDC", False, False)
    TL_GUO_loc[26] = GuoPlace(3185, 1100, __("Tsining"), True, "SDC", False, False)
    TL_GUO_loc[27] = GuoPlace(2910, 869, __("Paoting"), True, "CHI", False, False)
    TL_GUO_loc[28] = GuoPlace(3295, 1247, __("Yancheng"), True, "CHI", False, False)
    TL_GUO_loc[29] = GuoPlace(2845, 931, __("Shihkiachwuang"), True, "CHI", False, False)
    TL_GUO_loc[30] = GuoPlace(3219, 1157, __("Lianyun"), True, "CHI", False, False)
    TL_GUO_loc[31] = GuoPlace(3443, 1577, __("Taichow"), True, "CHI", True, False)
    TL_GUO_loc[32] = GuoPlace(3390, 1631, __("Wenchow"), True, "CHI", True, False)
    TL_GUO_loc[33] = GuoPlace(2861, 2036, __("Tungkuan"), True, "CHI", False, False)
    TL_GUO_loc[34] = GuoPlace(2680, 2098, __("Yuengkong"), True, "CHI", False, False)
    TL_GUO_loc[35] = GuoPlace(2984, 2021, __("Swabue"), True, "CHI", False, False)
    TL_GUO_loc[36] = GuoPlace(2909, 1727, __("Kian"), True, "CHI", False, False)
    TL_GUO_loc[37] = GuoPlace(3300, 1556, __("Kingwha"), True, "CHI", False, False)
    TL_GUO_loc[38] = GuoPlace(2937, 1186, __("Shangkiu"), True, "CHI", False, False)
    TL_GUO_loc[39] = GuoPlace(2715, 1291, __("Nanyang"), True, "CHI", False, False)
    TL_GUO_loc[40] = GuoPlace(2703, 938, __("Taiyuan"), True, "SHX", False, True)
    TL_GUO_loc[41] = GuoPlace(2611, 1068, __("Linfen"), True, "SHX", False, False)
    TL_GUO_loc[42] = GuoPlace(2752, 773, __("Tatung"), True, "SHX", False, False)
    TL_GUO_loc[43] = GuoPlace(2683, 1375, __("Siangyang"), True, "CHI", False, False)
    TL_GUO_loc[44] = GuoPlace(2814, 1452, __("Siaokan"), True, "CHI", False, False)
    TL_GUO_loc[45] = GuoPlace(2606, 1462, __("Yicheng"), True, "CHI", False, False)
    TL_GUO_loc[46] = GuoPlace(2735, 1728, __("Hengyang"), True, "HNC", False, False)
    TL_GUO_loc[47] = GuoPlace(2521, 1679, __("Hwaihwa"), True, "HNC", False, False)
    TL_GUO_loc[48] = GuoPlace(2354, 1914, __("Hochi"), True, "GXC", False, False)
    TL_GUO_loc[49] = GuoPlace(2845, 2018, __("kweikang"), True, "GXC", True, False)
    TL_GUO_loc[50] = GuoPlace(2453, 2102, __("Pakhoi"), True, "GXC", True, False)
    TL_GUO_loc[51] = GuoPlace(2278, 1681, __("Tsunyi"), True, "CHI", False, False)
    TL_GUO_loc[52] = GuoPlace(2170, 1586, __("Luchow"), True, "SHC",False, False)
    TL_GUO_loc[53] = GuoPlace(2237, 1376, __("Bachung"), True, "SHC", False, False)
    TL_GUO_loc[54] = GuoPlace(2482, 1054, __("Fusze"), True, "PRC", False, True)
    TL_GUO_loc[55] = GuoPlace(2498, 812, __("Ordos"), True, "SHX", False, False)
    TL_GUO_loc[56] = GuoPlace(2337, 714, __("Bayan Nur"), True, "SHX", False, False)
    TL_GUO_loc[57] = GuoPlace(2266, 890, __("Yuchwan"), True, "XSM", False, False)
    TL_GUO_loc[58] = GuoPlace(2227, 858, __("Axla"), True, "XSM", False, False)
    TL_GUO_loc[59] = GuoPlace(2215, 1165, __("Tenshui"), True, "XSM", False, False)
    TL_GUO_loc[60] = GuoPlace(2076, 1049, __("Lanchow"), True, "XSM", False, False)
    TL_GUO_loc[61] = GuoPlace(2008, 900, __("Wuwei"), True, "XSM", False, False)
    TL_GUO_loc[62] = GuoPlace(1727, 756, __("Kiuquan"), True, "XSM", False, False)
    TL_GUO_loc[63] = GuoPlace(1676, 831, __("Deqen"), True, "XSM", False, False)
    TL_GUO_loc[64] = GuoPlace(1740, 2002, __("Puerh"), True, "YUN", False, False)
    TL_GUO_loc[65] = GuoPlace(3246, 1858, __("Chinchew"), True, "CHI", False, False)
    TL_GUO_loc[66] = GuoPlace(3153, 1766, __("Sanming"), True, "CHI", False, False)
    TL_GUO_loc[67] = GuoPlace(3193, 753, __("Chinwangtao"), True, "MAN", False, False)
    TL_GUO_loc[68] = GuoPlace(3262, 697, __("Hulutao"), True, "MAN", False, False)
    TL_GUO_loc[69] = GuoPlace(3381, 681, __("Yingkow"), True, "MAN", False, False)
    TL_GUO_loc[70] = GuoPlace(3141, 637, __("Chaoyang"), True, "MAN", False, False)
    TL_GUO_loc[71] = GuoPlace(3115, 586, __("Chifeng"), True, "MAN", False, False)
    TL_GUO_loc[72] = GuoPlace(3533, 429, __("Hsinking"), True, "MAN", False, False)
    TL_GUO_loc[73] = GuoPlace(3321, 483, __("Tungliao"), True, "MAN", False, False)
    TL_GUO_loc[74] = GuoPlace(3147, 74, __("Hulun Buir"), True, "MAN", False, False)
    TL_GUO_loc[75] = GuoPlace(2960, 86, __("Manchowli"), True, "MAN", False, False)
    TL_GUO_loc[76] = GuoPlace(3383, 198, __("Tsitsihar"), True, "MAN", False, False)
    TL_GUO_loc[77] = GuoPlace(3796, 180, __("Kiamusze"), True, "MAN", False, False)
    TL_GUO_loc[78] = GuoPlace(3798, 335, __("Mutankiang"), True, "MAN", False, False)
    TL_GUO_loc[79] = GuoPlace(140, 500, __("Kashgar"), True, "SIK", False , False)
    TL_GUO_loc[80] = GuoPlace(902, 221, __("Karamay"), True, "SIK", False, False)
    TL_GUO_loc[81] = GuoPlace(1146, 102, __("Altay"), True, "SIK", False, False)
    TL_GUO_loc[82] = GuoPlace(1035, 363, __("Urumqi"), True, "SIK", False, True)
        ##    ##    ###    ######## ####  #######  ##    ##  ######  
        ###   ##   ## ##      ##     ##  ##     ## ###   ## ##    ## 
        ####  ##  ##   ##     ##     ##  ##     ## ####  ## ##       
        ## ## ## ##     ##    ##     ##  ##     ## ## ## ##  ######  
        ##  #### #########    ##     ##  ##     ## ##  ####       ## 
        ##   ### ##     ##    ##     ##  ##     ## ##   ### ##    ## 
        ##    ## ##     ##    ##    ####  #######  ##    ##  ###### 
    CHI_log = []
    PRC_log = []
    JAP_log = []
    MAN_log = []
    RNG_log = []
    EHA_log = []
    MEN_log = []
    PGR_log = []
    SHX_log = []
    XSM_log = []
    GXC_log = []
    YUN_log = []
    SDC_log = []
    HNC_log = []
    SHC_log = []
    SKC_log = []
    SIK_log = []
    TIB_log = []
    ETR_log = []
    BKT_log = []
    KII_log = []
    KON_log = []
    DRK_log = []
    KOR_log = []
    ENG_log = []
    POR_log = []
    FRA_log = []
    SOV_log = []
    USA_log = []

    CHI_DESC = "The Republic of China was established on Janurary 1st 1912 after the Xinhai Revolution which overthrew the Qing dynasty. It was de-facto dissolved during the warlord era until in 1921 the Kuomintang established a rival government in Canton. Chiang Chieh Shih who came into power through a military coup began a northern expedition to capture cities fro warlords and proclaim a central government to unite China under. Many foreign nations recognised the Nationalist government as the legitimate unified government of China, even the Soviet Union which supported the Chinese communists. After the Nanjing decades of the 1930s the Republic was weak and thrown into constant war of unification and resistance against foreign powers such as Japan."
    PRC_DESC = ""
    JAP_DESC = ""
    MAN_DESC = ""
    RNG_DESC = ""
    EHA_DESC = ""
    MEN_DESC = ""
    PGR_DESC = ""
    SHX_DESC = ""
    XSM_DESC = ""
    GXC_DESC = ""
    YUN_DESC = ""
    SDC_DESC = ""
    HNC_DESC = ""
    SHC_DESC = ""
    SKC_DESC = ""
    SIK_DESC = ""
    TIB_DESC = ""
    ETR_DESC = ""
    BKT_DESC = ""
    KII_DESC = ""
    KON_DESC = ""
    DRK_DESC = ""
    KOR_DESC = ""
    ENG_DESC = ""
    POR_DESC = ""
    FRA_DESC = ""
    SOV_DESC = ""
    USA_DESC = ""
##     ##    ###    #### ##    ##    ##    ##    ###    ######## ####  #######  ##    ##  ######  
###   ###   ## ##    ##  ###   ##    ###   ##   ## ##      ##     ##  ##     ## ###   ## ##    ## 
#### ####  ##   ##   ##  ####  ##    ####  ##  ##   ##     ##     ##  ##     ## ####  ## ##       
## ### ## ##     ##  ##  ## ## ##    ## ## ## ##     ##    ##     ##  ##     ## ## ## ##  ######  
##     ## #########  ##  ##  ####    ##  #### #########    ##     ##  ##     ## ##  ####       ## 
##     ## ##     ##  ##  ##   ###    ##   ### ##     ##    ##     ##  ##     ## ##   ### ##    ## 
##     ## ##     ## #### ##    ##    ##    ## ##     ##    ##    ####  #######  ##    ##  ######  
    TL_GUO[0] = Nation(
        __("Republic of China"),
        "CHI", 
        __("Chiang Chie Shih"), 
        __("Generalissimo President of the Republic"), 
        __("Conservative Junta"),
        __("Central Government of Kuomintang"), 
        __("Kuomintang"), 
        __("Second United Front"), 
        True, 
        False, 
        "country_flags/CHI.png", 
        CHI_log, 
        CHI_DESC)
    

    TL_GUO[1] = Nation(
        __("Chinese Soviet Republic"), 
        "PRC", 
        __("Mao Tse-Tung"), 
        __("Revolutionary Marxist Leader"), 
        __("Marxist Guerillas"), 
        __("International Marxism"), 
        __("Chung-kuo Kung-ch'an-tang"), 
        __("Second United Front"), 
        True, 
        False, 
        "country_flags/PRC_1937.png", 
        PRC_log, 
        PRC_DESC)

 ######   #######          ########  ########   #######  ########   ######  ######## ########  #### ######## ##    ##     ######  ########  ##     ## ######## ########  ######## 
##    ## ##     ##         ##     ## ##     ## ##     ## ##     ## ##    ## ##       ##     ##  ##     ##     ##  ##     ##    ## ##     ## ##     ## ##       ##     ## ##       
##       ##     ##         ##     ## ##     ## ##     ## ##     ## ##       ##       ##     ##  ##     ##      ####      ##       ##     ## ##     ## ##       ##     ## ##       
##       ##     ## ####### ########  ########  ##     ## ########   ######  ######   ########   ##     ##       ##        ######  ########  ######### ######   ########  ######   
##       ##     ##         ##        ##   ##   ##     ## ##              ## ##       ##   ##    ##     ##       ##             ## ##        ##     ## ##       ##   ##   ##       
##    ## ##     ##         ##        ##    ##  ##     ## ##        ##    ## ##       ##    ##   ##     ##       ##       ##    ## ##        ##     ## ##       ##    ##  ##       
 ######   #######          ##        ##     ##  #######  ##         ######  ######## ##     ## ####    ##       ##        ######  ##        ##     ## ######## ##     ## ######## 
    
    TL_GUO[2] = Nation(
        __("Empire of Japan"), 
        "JAP", 
        __("Emperor Hirohito"), 
        __("Emperor of Japan"), 
        __("Fascist Monarchy"), 
        __("Co-Prosperity Sphere"), 
        __("Tohokai"), 
        __("Co-Properity Sphere"), 
        True, 
        False, 
        "country_flags/JAP.png", 
        JAP_log, 
        JAP_DESC)

    TL_GUO[3] = Nation(
        __("Empire of Manchukuo"), 
        "MAN", 
        __("Aisin Gioro Pu-Yi"),
        __("Collaborationist Emperor of Manchukuo"), 
        __("Fascist Puppet Monarchy"), 
        __("Co-Prosperity Sphere"), 
        __("Manchōwkuó Hsiéhehuì"), 
        __("Co-Prosperity Sphere"), 
        True, 
        False, 
        "country_flags/MAN.png", 
        MAN_log, 
        MAN_DESC)
    
    TL_GUO[4] = Nation(
        __("Reorganized National Government of the Republic of China"), 
        "RNG", 
        __("Wang Ching-Wei"),
        __("Japanese Collaborationist Dictator"), 
        __("Fascist Puppet State"), 
        __("Co-Prosperity Sphere"), 
        __("Left Kuomintang"), 
        __("Co-Prosperity Sphere"), 
        False, 
        False, 
        "country_flags/RNG.png", 
        RNG_log, 
        RNG_DESC)

    TL_GUO[5] = Nation(
        __("East Hopeh autonomous\nanti-communism council"), 
        "EHA", 
        __("Yin-Ju-Keng"), 
        __("Japanese Collaborationist Dictator"), 
        __("Buffer State"), 
        __("Co-Prosperity Sphere"), 
        __("East Hopei Autonomous Government"), 
        __("Co-Prosperity Sphere"), 
        True, 
        False, 
        "country_flags/EHA.png",
        EHA_log, 
        EHA_DESC)

    TL_GUO[6] = Nation(
        __("Mongol United\nAutonomous Government"), 
        "MEN", 
        __("Prince Demchugdongrub"), 
        __("Japanese Collaborationist Dictator"), 
        __("Fascist Puppet State"), 
        __("Co-Prosperity Sphere"), 
        __("Mongol Military Government"), 
        __("Co-Prosperity Sphere"), 
        True, 
        False, 
        "country_flags/MEN.png",
        MEN_log, 
        MEN_DESC)

##      ##    ###    ########  ##        #######  ########  ########      ######  ##       ####  #######  ##     ## ########  ######  
##  ##  ##   ## ##   ##     ## ##       ##     ## ##     ## ##     ##    ##    ## ##        ##  ##     ## ##     ## ##       ##    ## 
##  ##  ##  ##   ##  ##     ## ##       ##     ## ##     ## ##     ##    ##       ##        ##  ##     ## ##     ## ##       ##       
##  ##  ## ##     ## ########  ##       ##     ## ########  ##     ##    ##       ##        ##  ##     ## ##     ## ######    ######  
##  ##  ## ######### ##   ##   ##       ##     ## ##   ##   ##     ##    ##       ##        ##  ##  ## ## ##     ## ##             ## 
##  ##  ## ##     ## ##    ##  ##       ##     ## ##    ##  ##     ##    ##    ## ##        ##  ##    ##  ##     ## ##       ##    ## 
 ###  ###  ##     ## ##     ## ########  #######  ##     ## ########      ######  ######## ####  ##### ##  #######  ########  ######  
    TL_GUO[7] = Nation(
        __("Hopeh-Chahar Political Council"), 
        "PGR", 
        __("Sung Che Yuan"), 
        __("Chairman of Hopeh-Chahar"), 
        __("Buffer State"), 
        __("Central Government of Kuomintang"), 
        __("Kuomintang"), 
        __("Second United Front"), 
        True, 
        False, 
        "country_flags/PGR.png", 
        PGR_log, 
        PGR_DESC)

    TL_GUO[8] = Nation(
        __("Shaanxi Clique"), 
        "SHX", 
        __("Yan HsiShan"), 
        __("Warlord"), 
        __("Conservative Junta"), 
        __("Central Government of Kuomintang"), 
        __("Kuomintang"), 
        __("Second United Front"), 
        True, 
        False, 
        "country_flags/SHX.png", 
        SHX_log, 
        SHX_DESC)

    TL_GUO[9] = Nation(
        __("Hsi Pei San Ma"), 
        "XSM", 
        __("Ma Bu Fang"), 
        __("Warlord"), 
        __("Conservative Junta"), 
        __("Central Government of Kuomintang"), 
        __("Kuomintang"), 
        __("Second United Front"), 
        True, 
        False, 
        "country_flags/XSM.png", 
        XSM_log, 
        XSM_DESC)

    TL_GUO[10] = Nation(
        __("KwangHsi Clique"), 
        "GXC", 
        __("Li Tsung-Jen"), 
        __("Warlord"), 
        __("Conservative Junta"), 
        __("Central Government of Kuomintang"), 
        __("Kuomintang"), 
        __("Second United Front"), 
        True, 
        False, 
        "country_flags/GXC.png", 
        GXC_log, 
        GXC_DESC)

    TL_GUO[11] = Nation(
        __("Yunnan Clique"), 
        "YUN", 
        __("Lung Yun"), 
        __("Warlord"), 
        __("Conservative Junta"), 
        __("Central Government of Kuomintang"), 
        __("Kuomintang"), 
        __("Second United Front"), 
        True, 
        False, 
        "country_flags/YUN.png", 
        YUN_log, 
        YUN_DESC)

    TL_GUO[12] = Nation(
        __("Shandong Clique"), 
        "SDC", 
        __("Han Fuju"), 
        __("Warlord"), 
        __("Conservative Junta"), 
        __("Central Government of Kuomintang"), 
        __("Kuomintang"), 
        __("Second United Front"), 
        True, 
        False, 
        "country_flags/SDC.png", 
        SDC_log, 
        SDC_DESC)

    TL_GUO[13] = Nation(
        __("Hunan Clique"),
        "HNC", 
        __("Chang Chih Chung"), 
        __("Warlord"), 
        __("Conservative Junta"), 
        __("Central Government of Kuomintang"), 
        __("Kuomintang"), 
        __("Second United Front"), 
        True, 
        False, 
        "country_flags/HNC.png", 
        HNC_log, 
        HNC_DESC)

    TL_GUO[14] = Nation(
        __("Szechewan Clique"), 
        "SHC", 
        __("Liu Hsiang"), 
        __("Warlord"), 
        __("Conservative Junta"), 
        __("Central Government of Kuomintang"), 
        __("Kuomintang"), 
        __("Second United Front"), 
        True, 
        False, 
        "country_flags/SHC.png", 
        SHC_log, 
        SHC_DESC)

    TL_GUO[15] = Nation(
        __("Sikang Clique"), 
        "SKC", 
        __("Liu Wen Hui"),
        __("Warlord"), 
        __("Conservative Junta"), 
        __("Central Government of Kuomintang"), 
        __("Kuomintang"), 
        __("Second United Front"), 
        True, 
        False, 
        "country_flags/SKC.png", 
        SKC_log, 
        SKC_DESC)

    TL_GUO[16] = Nation(
        __("Sinkiang Clique"), 
        "SIK", 
        __("ShengShih Ts'ai"), 
        __("Warlord"), 
        __("Soviet Junta"), 
        __("Internationale & Central Government of Kuomintang"), 
        __("People's Anti-Imperialist Association"), 
        __("Second United Front"), 
        True, 
        False, 
        "country_flags/SIK.png", 
        SIK_log, 
        SIK_DESC)

    TL_GUO[17] = Nation(
        __("Kingdom of Tibet"), 
        "TIB", 
        __("Jamphel Yeshe Gyaltsen"), 
        __("Fifth Reting Rinpoche"), 
        __("Monastic Monarchy"), 
        __("Non-Aligned"), 
        __("Dalai Lama"), 
        __("No Faction"), 
        True, 
        False, 
        "country_flags/TIB.png", 
        TIB_log, 
        TIB_DESC)

    TL_GUO[18] = Nation(
        __("Second East Turkestan Republic"), 
        "ETR", 
        __("Elihan Tore"), 
        __("President of East Turkestan Republic"), 
        __("Independance Uprising"), 
        __("Non-Aligned"), 
        __("East Turkestan Governemnt"),
        __("No Faction"), 
        False, 
        False, 
        "country_flags/ETR.png", 
        ETR_log, 
        ETR_DESC)

    TL_GUO[19] = Nation(
        __("Yunnan Anti-communist National Salvation Army"), 
        "BKT", 
        __("Li Mi"), 
        __("General of the Yunnan National Salvation Army"), 
        __("Nationalist Guerillas"), 
        __("Central Government of Kuomintang"), 
        __("Kuomintang"), 
        __("Nationalist Coalition"), 
        False, 
        False, 
        "country_flags/BKT.png",  
        BKT_log, 
        BKT_DESC)

    TL_GUO[20] = Nation(
        __("Kuomintang Islamic Insurgency"), 
        "KII", 
        __("Ma Bu Fang"), 
        __("General of the Islamic Insurgency"), 
        __("Nationalist Guerillas"), 
        __("Central Government of Kuomintang"), 
        __("Kuomintang"), 
        __("Nationalist Coalition"), 
        False, 
        False, 
        "country_flags/KII.png", 
        KII_log, 
        KII_DESC)

    TL_GUO[21] = Nation(
        __("Kingdom of Ngolok"), 
        "KON", 
        __("Ngolok Tribes"), 
        __("Ngolok Tibetan Insurgents"), 
        __("Independance Uprising"), 
        __("Non-Aligned"), 
        __("Ngolok Tribes"), 
        __("No Faction"), 
        True, 
        False, 
        "country_flags/KON.png", 
        KON_log, 
        KON_DESC)
    
    TL_GUO[22] = Nation(
        __("Provisional People's Committee for North Korea"), 
        "DRK", 
        __("Kim Il-Sung"), 
        __("Chairman of the Provisional Comittee"), 
        __("Provisional Military Government"), 
        __("International Marxism"), 
        __("Provisional People's Committee for North Korea"), 
        __("No Faction"), 
        False, 
        False, 
        "country_flags/DRK_1945.png", 
        DRK_log, 
        DRK_DESC)

    TL_GUO[23] = Nation(
        __("United States Army Military Government in Korea"), 
        "KOR", 
        __("Archibald Vincent Arnold"), 
        __("Military Governer of Korea"), 
        __("Provisional Military Government"), 
        __("United States"), 
        __("United State Army Military Government"), 
        __("No Faction"), 
        False, 
        False, 
        "country_flags/KOR_1945", 
        KOR_log, 
        KOR_DESC)
######## ##     ## ########   #######  ########  ########    ###    ##    ##     ######   #######  ##        #######  ##    ## #### ########  ######  
##       ##     ## ##     ## ##     ## ##     ## ##         ## ##   ###   ##    ##    ## ##     ## ##       ##     ## ###   ##  ##  ##       ##    ## 
##       ##     ## ##     ## ##     ## ##     ## ##        ##   ##  ####  ##    ##       ##     ## ##       ##     ## ####  ##  ##  ##       ##       
######   ##     ## ########  ##     ## ########  ######   ##     ## ## ## ##    ##       ##     ## ##       ##     ## ## ## ##  ##  ######    ######  
##       ##     ## ##   ##   ##     ## ##        ##       ######### ##  ####    ##       ##     ## ##       ##     ## ##  ####  ##  ##             ## 
##       ##     ## ##    ##  ##     ## ##        ##       ##     ## ##   ###    ##    ## ##     ## ##       ##     ## ##   ###  ##  ##       ##    ## 
########  #######  ##     ##  #######  ##        ######## ##     ## ##    ##     ######   #######  ########  #######  ##    ## #### ########  ######  
    TL_GUO[24] = Nation(
        __("United Kingdom"), 
        "ENG", 
        __("Neville Chamberlain"), 
        __("Prime Minister of United Kingdom"), 
        __("Imperial Federation"), 
        __("League of Nations"), 
        __("Conservative Party"), 
        __("Anglo-French Alliance"), 
        True, 
        False, 
        "country_flags/ENG.png", 
        ENG_log, 
        ENG_DESC)

    TL_GUO[25] = Nation(
        __("Portugese Republic"), 
        "POR", 
        __("Antonio de Oliveira Salazar"), 
        __("Prime Minister of Portugal"), 
        __("Authoritarian Oligarchic Republic"), 
        __("Estada Novo"), 
        __("Uniao Nacional"), 
        __("No Faction"), 
        True, 
        False, 
        "country_flags/POR.png", 
        POR_log, 
        POR_DESC)

    TL_GUO[26] = Nation(
        __("French Republic"), 
        "FRA", 
        __("Camille Chautemps"),
        __("Prime Minister of France"), 
        __("Democratic Republic"), 
        __("League of Nations"), 
        __("Parti radical"), 
        __("Anglo-French Alliance"), 
        True, 
        False, 
        "country_flags/FRA.png", 
        FRA_log, 
        FRA_DESC)

    TL_GUO[27] = Nation(
        __("Union of\nSoviet Socialist Republics"), 
        "SOV",
        __("Joseph Stalin"),
        __("General Secretary of the Communist Party of the Soviet Union"), 
        __("Marxist Dictatorship"), 
        __("International Marxism"), 
        __("Kommunisticheskaya partiya\nSovetskogo Soyuza"), 
        __("Comintern"), 
        True, 
        False, 
        "country_flags/SOV.png", 
        SOV_log, 
        SOV_DESC)

    TL_GUO[28] = Nation(
        __("United States of America"), 
        "USA", 
        __("Franklin D Roosevelt"), 
        __("President of the United States"), 
        __("Democratic Republic"), 
        __("Isolationism"), 
        __("Democratic party"), 
        __("No Faction"), 
        True, 
        False, 
        "country_flags/USA.png", 
        USA_log, 
        USA_DESC)
    

    TL_Provinces[0] = Province(2493, 1848, __("kuang tung"), "CHI", "GDG")
    TL_Provinces[1] = Province(2066, 1783, __("Kwanghsi"), "GXC", "GNZ")
    TL_Provinces[2] = Province(2439, 1515, __("Hunan"), "HNC", "HNN")
    TL_Provinces[3] = Province(2824, 1509, __("Chiang Hsi"), "CHI", "JNX")
    TL_Provinces[4] = Province(3019, 1624, __("Fukien"), "CHI", "FJN")

# '''
# This will optimise code in the long run. 
# It's easier to give country tags as reference points when needing to work with nation objects.
# '''
    CHI = TL_GUO[0]
    PRC = TL_GUO[1]
    JAP = TL_GUO[2]
    MAN = TL_GUO[3]
    RNG = TL_GUO[4]
    EHA = TL_GUO[5]
    MEN = TL_GUO[6]
    PGR = TL_GUO[7]
    SHX = TL_GUO[8]
    XSM = TL_GUO[9]
    GXC = TL_GUO[10]
    YUN = TL_GUO[11]
    SDC = TL_GUO[12]
    HNC = TL_GUO[13]
    SHC = TL_GUO[14]
    SKC = TL_GUO[15]
    SIK = TL_GUO[16]
    TIB = TL_GUO[17]
    ETR = TL_GUO[18]
    BKT = TL_GUO[19]
    KII = TL_GUO[20]
    KON = TL_GUO[21]
    DRK = TL_GUO[22]
    KOR = TL_GUO[23]
    ENG = TL_GUO[24]
    POR = TL_GUO[25]
    FRA = TL_GUO[26]
    SOV = TL_GUO[27]
    USA = TL_GUO[28]