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
        def __init__(self, x, y, name, rname, chinesesim, IsActive, country, ID, Port, Capital):
            self.x = x
            self.y = y
            self.name = name
            self.rname = rname
            self.chinesesim = chinesesim
            self.IsActive = IsActive
            self.country = country
            self.ID = ID
            self.Port = Port
            self.Capital = Capital 
    class Guoflavour(object):
        def __init__(self, x, y, name, IsActive, strength, icon):
            self.x = x
            self.y = y
            self.name = name
            self.IsActive = IsActive
            self.strength = strength
            self.icon = icon
            
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
    TL_map_flavour = []
    t = 0
    while t < 200:
        TL_GUO_loc.append(GuoPlace(0,0,"","","",False, "","", False, False))
        TL_GUO.append(Nation("","","","","","","","",0,0, False, "",""))
        TL_map_flavour.append(Guoflavour(0,0,"", False, 0, ""))
        t += 1

         ######  #### ######## #### ########  ######  
        ##    ##  ##     ##     ##  ##       ##    ## 
        ##        ##     ##     ##  ##       ##       
        ##        ##     ##     ##  ######    ######  
        ##        ##     ##     ##  ##             ## 
        ##    ##  ##     ##     ##  ##       ##    ## 
         ######  ####    ##    #### ########  ######  
    TL_GUO_loc[0] = GuoPlace(2819, 2010, "Kwangchow", "Guangzhou", "广州", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[1] = GuoPlace(2888, 2062, "Hong Kong", "Xiang Gang", "香港", True, TL_GUO[17], "ENG", True, False)
    TL_GUO_loc[2] = GuoPlace(2826, 2069, "Macau", "Ao-Men", "澳门",  True, TL_GUO[18], "POR", True, False)
    TL_GUO_loc[3] = GuoPlace(2565, 2167, "Kwang-Chow Wan", "Guang-Zhou-An", "广州湾",  True, TL_GUO[19], "FRA", True, False)
    TL_GUO_loc[4] = GuoPlace(3436, 1392, "Shanghai", "Shanghai", "山海", True, TL_GUO[0], "CHI",True, False)
    TL_GUO_loc[5] = GuoPlace(3262, 1341, "Nanking", "Nanjing", "南京", True, TL_GUO[0], "CHI", False, True)
    TL_GUO_loc[6] = GuoPlace(2519, 2046, "Yulin", "Yulin", "玉林", True, TL_GUO[7], "GXC", False, False)
    TL_GUO_loc[7] = GuoPlace(3276, 1805, "Foochow", "Fuzhou", "福州", True, TL_GUO[0], "CHI", True, False)
    TL_GUO_loc[8] = GuoPlace(3450, 1492, "Ning-Po", "Ningbo", "宁波", True, TL_GUO[0], "CHI", True, False)
    TL_GUO_loc[9] = GuoPlace(3042, 1556, "Nan-Kang", "Nan-Kang", "", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[10] = GuoPlace(3087, 1462, "An-King", "Anqing", "安庆", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[11] = GuoPlace(3037, 840, "Tientsin", "Tianjin", "天津", True, TL_GUO[0], "CHI", True, False)
    TL_GUO_loc[12] = GuoPlace(3291, 1022, "Tsingtao", "Qingdao", "青岛", True, TL_GUO[9], "SDC", True, False)
    TL_GUO_loc[13] = GuoPlace(3399, 927, "Wei-Hai-Wei", "Wei Hai", "威海", True, TL_GUO[9], "SDC", True, False) 
    TL_GUO_loc[14] = GuoPlace(3325, 827, "Da-ren", "Dalian", "大连", True, TL_GUO[2], "JAP", True, False)
    TL_GUO_loc[15] = GuoPlace(3013, 775, "Peiping", "Beijing", "北京", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[16] = GuoPlace(3336, 1400, "Soochow", "Suzhou", "苏州", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[17] = GuoPlace(3443, 1600, "Tai Ping", "Taiping", "", True, TL_GUO[0], "CHI", True, False)
    TL_GUO_loc[18] = GuoPlace(3187, 1884, "Chang Chow", "Zhangzhou", "漳州", True, TL_GUO[0], "CHI", True, False)
    TL_GUO_loc[19] = GuoPlace(2448, 1139, "Sian", "Xi\'an", "西安", True, TL_GUO[1], "PRC", False, False)
    TL_GUO_loc[20] = GuoPlace(3415, 1972, "Kaohshiung", "Gaoxiong", "高雄", True, TL_GUO[2], "JAP", True, False)
    TL_GUO_loc[21] = GuoPlace(3493,1825, "Taipei", "Taibei", "台北", True, TL_GUO[2], "JAP", True, False)
    TL_GUO_loc[22] = GuoPlace(3440, 591, "Mukden", "Shenyang", "沈阳", True, TL_GUO[3], "MAN", False, True)
    TL_GUO_loc[23] = GuoPlace(3326, 931, "Yantai", "Yantai", "烟台", True, TL_GUO[9], "SDC", True, False)
    TL_GUO_loc[24] = GuoPlace(3185, 999, "Weifang", "Weifang", "潍坊", True, TL_GUO[9], "SDC", False, False)
    TL_GUO_loc[25] = GuoPlace(3138, 1111, "Lini", "Linyi", "临沂", True, TL_GUO[9], "SDC", False, False)
    TL_GUO_loc[26] = GuoPlace(3185, 1100, "Tsining", "Jining", "济宁", True, TL_GUO[9], "SDC", False, False)
    TL_GUO_loc[27] = GuoPlace(2910, 869, "Paoting", "Baoding", "保定", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[28] = GuoPlace(3295, 1247, "Yancheng", "Yancheng", "盐城", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[29] = GuoPlace(2845, 931, "Shihkiachwuang", "Shijiazhuang", "石家庄", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[30] = GuoPlace(3219, 1157, "Lianyun", "Lianyungang", "连云港", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[31] = GuoPlace(3443, 1577, "Taichow", "Taizhou", "台州", True, TL_GUO[0], "CHI", True, False)
    TL_GUO_loc[32] = GuoPlace(3390, 1631, "Wenchow", "Wenzhou", "温州", True, TL_GUO[0], "CHI", True, False)
    TL_GUO_loc[33] = GuoPlace(2861, 2036, "Tungkuan", "Dongguan", "东莞", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[34] = GuoPlace(2680, 2098, "Yuengkong", "Yangjiang", "阳江", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[35] = GuoPlace(2984, 2021, "Swabue", "Shanwei", "汕尾", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[36] = GuoPlace(2909, 1727, "Kian", "Ji\'an", "吉安", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[37] = GuoPlace(3300, 1556, "Kingwha", "Jinhua", "金华", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[38] = GuoPlace(2937, 1186, "Shangkiu", "Shangqiu", "商丘", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[39] = GuoPlace(2715, 1291, "Nanyang", "Nanyang", "南阳", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[40] = GuoPlace(2703, 938, "Taiyuan", "Taiyuan", "太原", True, TL_GUO[5], "SHX", False, True)
    TL_GUO_loc[41] = GuoPlace(2611, 1068, "Linfen", "Linfen", "临汾", True, TL_GUO[5], "SHX", False, False)
    TL_GUO_loc[42] = GuoPlace(2752, 773, "Tatung", "Datong", "大同", True, TL_GUO[5], "SHX", False, False)
    TL_GUO_loc[43] = GuoPlace(2683, 1375, "Siangyang", "Xiangyang", "襄阳", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[44] = GuoPlace(2814, 1452, "Siaokan", "Xiaogan", "孝感", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[45] = GuoPlace(2606, 1462, "Yicheng", "Yicheng", "宜城", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[46] = GuoPlace(2735, 1728, "Hengyang", "Hengyang", "衡阳", True, TL_GUO[10], "HNC", False, False)
    TL_GUO_loc[47] = GuoPlace(2521, 1679, "Hwaihwa", "Huaihua", "怀化", True, TL_GUO[10], "HNC", False, False)
    TL_GUO_loc[48] = GuoPlace(2354, 1914, "Hochi", "Hechi", "河池", True, TL_GUO[7], "GXC", False, False)
    TL_GUO_loc[49] = GuoPlace(2845, 2018, "kweikang", "Guigang", "贵港", True, TL_GUO[7], "GXC", True, False)
    TL_GUO_loc[50] = GuoPlace(2453, 2102, "Pakhoi", "Beihai", "北海", True, TL_GUO[7], "GXC", True, False)
    TL_GUO_loc[51] = GuoPlace(2278, 1681, "Tsunyi", "Zunyi", "遵义", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[52] = GuoPlace(2170, 1586, "Luchow", "Luzhou", "泸州", True, TL_GUO[11], "SHC",False, False)
    TL_GUO_loc[53] = GuoPlace(2237, 1376, "Bachung", "Bazhong", "巴中", True, TL_GUO[11], "SHC", False, False)
    TL_GUO_loc[54] = GuoPlace(2482, 1054, "Fusze", "Yan\'an", "延安", True, TL_GUO[1], "PRC", False, True)
    TL_GUO_loc[55] = GuoPlace(2498, 812, "Ordos", "Ordos", "鄂尔多斯", True, TL_GUO[5], "SHX", False, False)
    TL_GUO_loc[56] = GuoPlace(2337, 714, "Bayan Nur", "Bayan Nur", "巴彦淖尔", True, TL_GUO[5], "SHX", False, False)
    TL_GUO_loc[57] = GuoPlace(2266, 890, "Yuchwan", "Yinchuan", "银川", True, TL_GUO[6], "XSM", False, False)
    TL_GUO_loc[58] = GuoPlace(2227, 858, "Axla", "Axla League", "阿拉善盟", True, TL_GUO[6], "XSM", False, False)
    TL_GUO_loc[59] = GuoPlace(2215, 1165, "Tenshui", "Tianshui", "天水", True, TL_GUO[6], "XSM", False, False)
    TL_GUO_loc[60] = GuoPlace(2076, 1049, "Lanchow", "Lanzhou", "兰州", True, TL_GUO[6], "XSM", False, False)
    TL_GUO_loc[61] = GuoPlace(2008, 900, "Wuwei", "Wuwei", "武威", True, TL_GUO[6], "XSM", False, False)
    TL_GUO_loc[62] = GuoPlace(1727, 756, "Kiuquan", "Jiuquan", "酒泉", True, TL_GUO[6], "XSM", False, False)
    TL_GUO_loc[63] = GuoPlace(1676, 831, "Deqen", "Deqen", "德钦", True, TL_GUO[6], "XSM", False, False)
    TL_GUO_loc[64] = GuoPlace(1740, 2002, "Puerh", "Pu'er", "普洱", True, TL_GUO[8], "YUN", False, False)
    TL_GUO_loc[65] = GuoPlace(3246, 1858, "Chinchew", "Quanzhou", "泉州", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[66] = GuoPlace(3153, 1766, "Sanming", "Sanming", "三明", True, TL_GUO[0], "CHI", False, False)
    TL_GUO_loc[67] = GuoPlace(3193, 753, "Chinwangtao", "Qinhuangdao", "秦皇岛", True, TL_GUO[3], "MAN", False, False)
    TL_GUO_loc[68] = GuoPlace(3262, 697, "Hulutao", "Huludao", "葫芦岛", True, TL_GUO[3], "MAN", False, False)
    TL_GUO_loc[69] = GuoPlace(3381, 681, "Yingkow", "Yingkou", "营口", True, TL_GUO[3], "MAN", False, False)
    TL_GUO_loc[70] = GuoPlace(3141, 637, "Chaoyang", "Chaoyang", "朝阳", True, TL_GUO[3], "MAN", False, False)
    TL_GUO_loc[71] = GuoPlace(3115, 586, "Chifeng", "Chifeng", "赤峰", True, TL_GUO[3], "MAN", False, False)
        ##    ##    ###    ######## ####  #######  ##    ##  ######  
        ###   ##   ## ##      ##     ##  ##     ## ###   ## ##    ## 
        ####  ##  ##   ##     ##     ##  ##     ## ####  ## ##       
        ## ## ## ##     ##    ##     ##  ##     ## ## ## ##  ######  
        ##  #### #########    ##     ##  ##     ## ##  ####       ## 
        ##   ### ##     ##    ##     ##  ##     ## ##   ### ##    ## 
        ##    ## ##     ##    ##    ####  #######  ##    ##  ######  
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
    TL_GUO[14] = Nation("Kingdom of Tibet", "TIB", "Tenzin Gyatso", "Theocratic Dalai Lama Leader", "Monastic Monarchy", "Non-Aligned", "Dalai Lama", "No Faction", 40, 40, True, "country_flags/TIB.png", "")
    TL_GUO[15] = Nation("East Hopeh autonomous\nanti-communism council", "EHA", "Yin-Ju-Keng", "Japanese Collaborationist Dictator", "Buffer State", "Co-Prosperity Sphere", "East Hopei Autonomous Government", "Co-Prosperity Sphere", 50, 60, True, "country_flags/EHA.png", "")
    TL_GUO[16] = Nation("Mongol United\nAutonomous Government", "MEN", "Prince Demchugdongrub", "Japanese Collaborationist Dictator", "Fascist Puppet State", "Co-Prosperity Sphere", "Mongol Military Government", "Co-Prosperity Sphere", 50, 60, True, "country_flags/MEN.png", "")
    #European Colonies
    TL_GUO[17] = Nation("United Kingdom", "ENG", "Neville Chamberlain", "Prime Minister of United Kingdom", "Imperial Federation", "League of Nations", "Conservative Party", "Anglo-French Alliance", 70, 50, True, "country_flags/ENG.png", "")
    TL_GUO[18] = Nation("Portugese Republic", "POR", "Antonio de Oliveira Salazar", "Prime Minister of Portugal", "Authoritarian Oligarchic Republic", "Estada Novo", "Uniao Nacional", "No Faction", 70, 40, True, "country_flags/POR.png", "")
    TL_GUO[19] = Nation("French Republic", "FRA", "Camille Chautemps","Prime Minister of France", "Democratic Republic", "League of Nations", "Parti radical", "Anglo-French Alliance", 80, 70, True, "country_flags/FRA.png", "")
    TL_GUO[20] = Nation("Union of\nSoviet Socialist Republics", "SOV", "Joseph Stalin","General Secretary of the Communist Party of the Soviet Union", "Marxist Dictatorship", "International Marxism", "Kommunisticheskaya partiya\nSovetskogo Soyuza", "Comintern", 60, 70, True, "country_flags/SOV.png", "")

    