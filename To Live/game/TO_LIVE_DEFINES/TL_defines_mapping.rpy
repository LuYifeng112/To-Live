###   ###    ###     ######## ##      ##  #######  ########  ##    ## 
###   ###   ## ##   ##     ## ##  ##  ## ##     ## ##     ## ##   ##  
#### ####  ##   ##  ##     ## ##  ##  ## ##     ## ##     ## ##  ##   
## ### ## ##     ## ########  ##  ##  ## ##     ## ########  #####    
##     ## ######### ##        ##  ##  ## ##     ## ##   ##   ##  ##   
##     ## ##     ## ##        ##  ##  ## ##     ## ##    ##  ##   ##  
##     ## ##     ## ##         ###  ###   #######  ##     ## ##    ## 
default show_beijing  = True

python:
    def SetMapOn():
        GuoPlace.SetMapOn()

    def SetMapOff():
        GuoPlace.SetMapOff() 

    def GetMapState():
        GuoPlace.GetMapState()

init -10 python: 
    import renpy.store as store
    nation_tags = ["CHI", "PRC", "JAP", "MAN", "RNG", "EHA", "MEN", "PGR", "SHX", "XSM", "GXC", "YUN", "SDC", "HNC", "SHC", "SKC", "SIK", "TIB", "ETR", "BKT", "KII", "KON", "DRK", "KOR", "ENG", "POR", "FRA", "SOV", "USA"]         
    class GuoPlace(store.object):
        CitySensitive = True
        ''' 
        This is the class that creates map coordinate for the map.
        - It consists of X,Y coordinates for placement.
        - The city name that will be displayed in the text button.
        - Whether that city is visible or accessible to show the country.
        - A country specific ID that has to be the same as the Nation class.
        - Port and Capital jus set map point visuals.
        '''
        def __init__(self, x, y, name, IsActive, ID, Port, Capital, highlighted=False):
            self.cityflag = []
            self.x = x
            self.y = y
            self.name = name
            self.IsActive = IsActive
            self.ID = ID
            self.Port = Port
            self.Capital = Capital
            self.highlighted = highlighted

        def ActivateCity(self):
            self.IsActive = True
        def DeActivate(self):
            self.IsActive = False
        def Highlight(self):
            self.highlight = True
        def SetOwner(self, nation):
            if nation in nation_tags:
                self.ID = nation
            else:
                raise Exception("Owner not recongised - "+nation+".")
            devlog.info("Set owner of "+self.name+"to "+nation)
            
        def SetCityFlag(self, flag):
            self.cityflag.append(flag) 
            devlog.info("Set Flag: "+flag+"in "+self.name)
            '''
        These two defines play around with map button sensitivity.
        If we want to disable looking up the owner for a city say for a quiz then we can toggle it with these two function.
        '''
        @staticmethod
        def SetMapOn():
            GuoPlace.CitySensitive = True
        @staticmethod
        def SetMapOff():
            GuoPlace.CitySensitive = False 
        @staticmethod
        def GetMapState():
            return GuoPlace.CitySensitive




    class Nation(store.object):
        '''
        How countries are displayed. These are containers for information.
        '''
        def __init__(self, Name, ID, Leader, LeaderSub, PoliticalID, AlignmentID, RulingParty, FactionID, NationLog=[], IsActive=True, Flag=""):            
            self.Name = Name                    #The official name of the country.
            self.ID = ID                        #A shortened ID to compare to the map point ID. This is a link.
            self.Leader = Leader                
            self.LeaderSub = LeaderSub          #The position of the leader of the country.
            self.PoliticalID = PoliticalID      #Form of ideology and government.
            self.AlignmentID = AlignmentID      #Which power does it align itself to? or ideology.
            self.RulingParty = RulingParty      
            self.FactionID = FactionID
            self.NationLog = NationLog
            self.IsActive = IsActive
            self.Flag = Flag

        def Activate(self):
            self.IsActive = True

        def SetName(self, tlname):
            self.Name = tlname

        def SetLeader(self, boss):
            self.Leader = boss

        def SetFlag(self, flag):
            self.Flag = flag

        def Get_Info(self):
            year = TL_datetime.Ureturn_year()
            varstring = self.ID+"-"+year+"_desc"
            return NationDescDictionary[varstring]

        def LogEvent(self, event, *args):
            self.NationLog.append(event)
            msg.msg("New Event in "+self.Name+":"+event)
            for X in args:
                X.NationLog.append(event)

        def Get_Flag(self):
            varflagpath = "images/country_flags/"+self.ID+self.Flag+".png"
            return varflagpath
            
    TL_GUO_loc = []
    TL_GUO = []
    TL_Provinces = []
    t = 0
    while t < 200:
        TL_GUO_loc.append(GuoPlace(0,0,"",False, "", False, False))
        TL_GUO.append(Nation("", "", "", "", "", "", "", "","", False, ""))
        t += 1

         ######  #### ######## #### ########  ######  
        ##    ##  ##     ##     ##  ##       ##    ## 
        ##        ##     ##     ##  ##       ##       
        ##        ##     ##     ##  ######    ######  
        ##        ##     ##     ##  ##             ## 
        ##    ##  ##     ##     ##  ##       ##    ## 
         ######  ####    ##    #### ########  ######  
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
    TL_GUO_loc[71] = GuoPlace(3115, 586, __("Chihfeng"), True, "MAN", False, False)
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
    TL_GUO_loc[83] = GuoPlace(884, 507, __("Bayingol"), True, "SIK", False, False)
    TL_GUO_loc[84] = GuoPlace(1417, 506, __("Kumul"), True, "SIK", False, False)
    TL_GUO_loc[85] = GuoPlace(1126, 1032, __("Nagqu"), True, "TIB", False, False)
    TL_GUO_loc[86] = GuoPlace(2855, 715, __("Kalgan"), True, "CHI", False, False)
    TL_GUO_loc[87] = GuoPlace(3086, 1957, __("Chaochow"), True, "CHI", False, False)
    TL_GUO_loc[88] = GuoPlace(2045, 1504, __("Chengtu"), True, "SHC", False, False)
    TL_GUO_loc[89] = GuoPlace(2300, 1263, __("Kwuangyun"),True, "CHI", False, False)
    TL_GUO_loc[89] = GuoPlace(2934, 489, __("Hsilin Gol"), True, "MEN", False, False)
    TL_GUO_loc[90] = GuoPlace(1935, 1372, __("Aba"), True, "SHC", False, False)
    TL_GUO_loc[91] = GuoPlace(2040, 1534, __("Leshan"), True, "SHC", False, False)
    TL_GUO_loc[92] = GuoPlace(1900, 1481, __("Garze"), True, "SHC", False, False)
    TL_GUO_loc[93] = GuoPlace(2456, 1984, __("Tongren"), True, "CHI", False, False)
    TL_GUO_loc[94] = GuoPlace(2695, 1488, __("Kingchow"), True, "CHI", False, False)
    TL_GUO_loc[95] = GuoPlace(2449, 1332, __("Ankang"), True, "CHI", False, False)
    TL_GUO_loc[96] = GuoPlace(2580, 1321, __("Shiyan"), True, "CHI", False, False)
    TL_GUO_loc[97] = GuoPlace(1531, 1346, __("Qamdo"), True, "TIB", False, False)
    TL_GUO_loc[98] = GuoPlace(2820, 1889, __("Shiukwan"), True, "CHI", False, False)
    TL_GUO_loc[99] = GuoPlace(2945, 1779, __("Kanchow"), True, "CHI", False, False)
    TL_GUO_loc[100] = GuoPlace(3328, 1352, __("Wu-Hsi"), True, "CHI", False, False)
        

                                    ####################################################################################
                                    ####################################################################################
                                    ####        ##    ##    ###    ######## ####  #######  ##    ##  ######         ####
                                    ####        ###   ##   ## ##      ##     ##  ##     ## ###   ## ##    ##        ####
                                    ####        ####  ##  ##   ##     ##     ##  ##     ## ####  ## ##              ####
                                    ####        ## ## ## ##     ##    ##     ##  ##     ## ## ## ##  ######         ####
                                    ####        ##  #### #########    ##     ##  ##     ## ##  ####       ##        ####
                                    ####        ##   ### ##     ##    ##     ##  ##     ## ##   ### ##    ##        ####
                                    ####        ##    ## ##     ##    ##    ####  #######  ##    ##  ######         ####
                                    ####################################################################################
                                    ####################################################################################


##     ##    ###    #### ##    ##    ##    ##    ###    ######## ####  #######  ##    ##  ######  
###   ###   ## ##    ##  ###   ##    ###   ##   ## ##      ##     ##  ##     ## ###   ## ##    ## 
#### ####  ##   ##   ##  ####  ##    ####  ##  ##   ##     ##     ##  ##     ## ####  ## ##       
## ### ## ##     ##  ##  ## ## ##    ## ## ## ##     ##    ##     ##  ##     ## ## ## ##  ######  
##     ## #########  ##  ##  ####    ##  #### #########    ##     ##  ##     ## ##  ####       ## 
##     ## ##     ##  ##  ##   ###    ##   ### ##     ##    ##     ##  ##     ## ##   ### ##    ## 
##     ## ##     ## #### ##    ##    ##    ## ##     ##    ##    ####  #######  ##    ##  ######  
    TL_GUO[0] = Nation(
        Name=__("Republic of China"),
        ID="CHI", 
        Leader=__("Chiang Chie Shih"), 
        LeaderSub=__("Generalissimo President of the Republic"), 
        PoliticalID=__("Conservative Junta"),
        AlignmentID=__("Central Government of Kuomintang"), 
        RulingParty=__("Kuomintang"), 
        FactionID=__("Second United Front"), 
        IsActive=True
        )
    

    TL_GUO[1] = Nation(
        Name=__("Chinese Soviet Republic"), 
        ID="PRC", 
        Leader=__("Mao Tse-Tung"), 
        LeaderSub=__("Revolutionary Marxist Leader"), 
        PoliticalID=__("Marxist Guerillas"), 
        AlignmentID=__("International Marxism"), 
        RulingParty=__("Chung-kuo Kung-ch'an-tang"), 
        FactionID=__("Second United Front"), 
        IsActive=True,
        Flag='_1937'
        )

 ######   #######          ########  ########   #######  ########   ######  ######## ########  #### ######## ##    ##     ######  ########  ##     ## ######## ########  ######## 
##    ## ##     ##         ##     ## ##     ## ##     ## ##     ## ##    ## ##       ##     ##  ##     ##     ##  ##     ##    ## ##     ## ##     ## ##       ##     ## ##       
##       ##     ##         ##     ## ##     ## ##     ## ##     ## ##       ##       ##     ##  ##     ##      ####      ##       ##     ## ##     ## ##       ##     ## ##       
##       ##     ## ####### ########  ########  ##     ## ########   ######  ######   ########   ##     ##       ##        ######  ########  ######### ######   ########  ######   
##       ##     ##         ##        ##   ##   ##     ## ##              ## ##       ##   ##    ##     ##       ##             ## ##        ##     ## ##       ##   ##   ##       
##    ## ##     ##         ##        ##    ##  ##     ## ##        ##    ## ##       ##    ##   ##     ##       ##       ##    ## ##        ##     ## ##       ##    ##  ##       
 ######   #######          ##        ##     ##  #######  ##         ######  ######## ##     ## ####    ##       ##        ######  ##        ##     ## ######## ##     ## ######## 
    
    TL_GUO[2] = Nation(
        Name=__("Empire of Japan"), 
        ID="JAP", 
        Leader=__("Emperor Hirohito"), 
        LeaderSub=__("Emperor of Japan"), 
        PoliticalID=__("Fascist Monarchy"), 
        AlignmentID=__("Co-Prosperity Sphere"), 
        RulingParty=__("Tohokai"), 
        FactionID=__("Co-Properity Sphere"), 
        IsActive=True
        )

    TL_GUO[3] = Nation(
        Name=__("Empire of Manchukuo"), 
        ID="MAN", 
        Leader=__("Aisin Gioro Pu-Yi"),
        LeaderSub=__("Collaborationist Emperor of Manchukuo"), 
        PoliticalID=__("Fascist Puppet Monarchy"), 
        AlignmentID=__("Co-Prosperity Sphere"), 
        RulingParty=__("Manchōwkuó Hsiéhehuì"), 
        FactionID=__("Co-Prosperity Sphere"), 
        IsActive=True
        )
    
    TL_GUO[4] = Nation(
        Name=__("Reorganized National Government of the Republic of China"), 
        ID="RNG", 
        Leader=__("Wang Ching-Wei"),
        LeaderSub=__("Japanese Collaborationist Dictator"), 
        PoliticalID=__("Fascist Puppet State"), 
        AlignmentID=__("Co-Prosperity Sphere"), 
        RulingParty=__("Left Kuomintang"), 
        FactionID=__("Co-Prosperity Sphere"), 
        IsActive=False
        )

    TL_GUO[5] = Nation(
        Name=__("East Hopeh autonomous\nanti-communism council"), 
        ID="EHA", 
        Leader=__("Yin-Ju-Keng"), 
        LeaderSub=__("Japanese Collaborationist Dictator"), 
        PoliticalID=__("Buffer State"), 
        AlignmentID=__("Co-Prosperity Sphere"), 
        RulingParty=__("East Hopei Autonomous Government"), 
        FactionID=__("Co-Prosperity Sphere"), 
        IsActive=True
        )

    TL_GUO[6] = Nation(
        Name=__("Mongol United\nAutonomous Government"), 
        ID="MEN", 
        Leader=__("Prince Demchugdongrub"), 
        LeaderSub=__("Japanese Collaborationist Dictator"), 
        PoliticalID=__("Fascist Puppet State"), 
        AlignmentID=__("Co-Prosperity Sphere"), 
        RulingParty=__("Mongol Military Government"), 
        FactionID=__("Co-Prosperity Sphere"), 
        IsActive=True
        )

##      ##    ###    ########  ##        #######  ########  ########      ######  ##       ####  #######  ##     ## ########  ######  
##  ##  ##   ## ##   ##     ## ##       ##     ## ##     ## ##     ##    ##    ## ##        ##  ##     ## ##     ## ##       ##    ## 
##  ##  ##  ##   ##  ##     ## ##       ##     ## ##     ## ##     ##    ##       ##        ##  ##     ## ##     ## ##       ##       
##  ##  ## ##     ## ########  ##       ##     ## ########  ##     ##    ##       ##        ##  ##     ## ##     ## ######    ######  
##  ##  ## ######### ##   ##   ##       ##     ## ##   ##   ##     ##    ##       ##        ##  ##  ## ## ##     ## ##             ## 
##  ##  ## ##     ## ##    ##  ##       ##     ## ##    ##  ##     ##    ##    ## ##        ##  ##    ##  ##     ## ##       ##    ## 
 ###  ###  ##     ## ##     ## ########  #######  ##     ## ########      ######  ######## ####  ##### ##  #######  ########  ######  
    TL_GUO[7] = Nation(
        Name=__("Hopeh-Chahar Political Council"), 
        ID="PGR", 
        Leader=__("Sung Che-Yuan"), 
        LeaderSub=__("Chairman of Hopeh-Chahar"), 
        PoliticalID=__("Buffer State"), 
        AlignmentID=__("Central Government of Kuomintang"), 
        RulingParty=__("Kuomintang"), 
        FactionID=__("Second United Front"), 
        IsActive=True
        )

    TL_GUO[8] = Nation(
        Name=__("Shaanxi Clique"), 
        ID="SHX", 
        Leader=__("Yan HsiShan"), 
        LeaderSub=__("Warlord"), 
        PoliticalID=__("Conservative Junta"), 
        AlignmentID=__("Central Government of Kuomintang"), 
        RulingParty=__("Kuomintang"), 
        FactionID=__("Second United Front"), 
        IsActive=True
        )

    TL_GUO[9] = Nation(
        Name=__("Hsi Pei San Ma"), 
        ID="XSM", 
        Leader=__("Ma Bu Fang"), 
        LeaderSub=__("Warlord"), 
        PoliticalID=__("Conservative Junta"), 
        AlignmentID=__("Central Government of Kuomintang"), 
        RulingParty=__("Kuomintang"), 
        FactionID=__("Second United Front"), 
        IsActive=True
        )

    TL_GUO[10] = Nation(
        Name=__("KwangHsi Clique"), 
        ID="GXC", 
        Leader=__("Li Tsung-Jen"), 
        LeaderSub=__("Warlord"), 
        PoliticalID=__("Conservative Junta"), 
        AlignmentID=__("Central Government of Kuomintang"), 
        RulingParty=__("Kuomintang"), 
        FactionID=__("Second United Front"), 
        IsActive=True
        )

    TL_GUO[11] = Nation(
        Name=__("Yunnan Clique"), 
        ID="YUN", 
        Leader=__("Lung Yun"), 
        LeaderSub=__("Warlord"), 
        PoliticalID=__("Conservative Junta"), 
        AlignmentID=__("Central Government of Kuomintang"), 
        RulingParty=__("Kuomintang"), 
        FactionID=__("Second United Front"), 
        IsActive=True
        )

    TL_GUO[12] = Nation(
        Name=__("Shandong Clique"), 
        ID="SDC", 
        Leader=__("Han Fuchu"), 
        LeaderSub=__("Warlord"), 
        PoliticalID=__("Conservative Junta"), 
        AlignmentID=__("Central Government of Kuomintang"), 
        RulingParty=__("Kuomintang"), 
        FactionID=__("Second United Front"), 
        IsActive=True
        )

    TL_GUO[13] = Nation(
        Name=__("Hunan Clique"),
        ID="HNC", 
        Leader=__("Chang Chih Chung"), 
        LeaderSub=__("Warlord"), 
        PoliticalID=__("Conservative Junta"), 
        AlignmentID=__("Central Government of Kuomintang"), 
        RulingParty=__("Kuomintang"), 
        FactionID=__("Second United Front"), 
        IsActive=True
        )

    TL_GUO[14] = Nation(
        Name=__("Szechewan Clique"), 
        ID="SHC", 
        Leader=__("Liu Hsiang"), 
        LeaderSub=__("Warlord"), 
        PoliticalID=__("Conservative Junta"), 
        AlignmentID=__("Central Government of Kuomintang"), 
        RulingParty=__("Kuomintang"), 
        FactionID=__("Second United Front"), 
        IsActive=True
        )

    TL_GUO[15] = Nation(
        Name=__("Sikang Clique"), 
        ID="SKC", 
        Leader=__("Liu Wen Hui"),
        LeaderSub=__("Warlord"), 
        PoliticalID=__("Conservative Junta"), 
        AlignmentID=__("Central Government of Kuomintang"), 
        RulingParty=__("Kuomintang"), 
        FactionID=__("Second United Front"), 
        IsActive=True
        )

    TL_GUO[16] = Nation(
        Name=__("Sinkiang Clique"), 
        ID="SIK", 
        Leader=__("ShengShih Ts'ai"), 
        LeaderSub=__("Warlord"), 
        PoliticalID=__("Soviet Junta"), 
        AlignmentID=__("Internationale & Central Government of Kuomintang"), 
        RulingParty=__("People's Anti-Imperialist Association"), 
        FactionID=__("Second United Front"), 
        IsActive=True
        )

    TL_GUO[17] = Nation(
        Name=__("Kingdom of Tibet"), 
        ID="TIB", 
        Leader=__("Jamphel Yeshe Gyaltsen"), 
        LeaderSub=__("Fifth Reting Rinpoche"), 
        PoliticalID=__("Monastic Monarchy"), 
        AlignmentID=__("Non-Aligned"), 
        RulingParty=__("Dalai Lama"), 
        FactionID=__("No Faction"), 
        IsActive=True
        )

    TL_GUO[18] = Nation(
        Name=__("Second East Turkestan Republic"), 
        ID="ETR", 
        Leader=__("Elihan Tore"), 
        LeaderSub=__("President of East Turkestan Republic"), 
        PoliticalID=__("Independance Uprising"), 
        AlignmentID=__("Non-Aligned"), 
        RulingParty=__("East Turkestan Governemnt"),
        FactionID=__("No Faction"), 
        IsActive=False
        )

    TL_GUO[19] = Nation(
        Name=__("Yunnan Anti-communist National Salvation Army"), 
        ID="BKT", 
        Leader=__("Li Mi"), 
        LeaderSub=__("General of the Yunnan National Salvation Army"), 
        PoliticalID=__("Nationalist Guerillas"), 
        AlignmentID=__("Central Government of Kuomintang"), 
        RulingParty=__("Kuomintang"), 
        FactionID=__("Nationalist Coalition"), 
        IsActive=False
        )

    TL_GUO[20] = Nation(
        Name=__("Kuomintang Islamic Insurgency"), 
        ID="KII", 
        Leader=__("Ma Bu Fang"), 
        LeaderSub=__("General of the Islamic Insurgency"), 
        PoliticalID=__("Nationalist Guerillas"), 
        AlignmentID=__("Central Government of Kuomintang"), 
        RulingParty=__("Kuomintang"), 
        FactionID=__("Nationalist Coalition"), 
        IsActive=False
        )

    TL_GUO[21] = Nation(
        Name=__("Kingdom of Ngolok"), 
        ID="KON", 
        Leader=__("Ngolok Tribes"), 
        LeaderSub=__("Ngolok Tibetan Insurgents"), 
        PoliticalID=__("Independance Uprising"), 
        AlignmentID=__("Non-Aligned"), 
        RulingParty=__("Ngolok Tribes"), 
        FactionID=__("No Faction"), 
        IsActive=True
        )
    
    TL_GUO[22] = Nation(
        Name=__("Provisional People's Committee for North Korea"), 
        ID="DRK", 
        Leader=__("Kim Il-Sung"), 
        LeaderSub=__("Chairman of the Provisional Comittee"), 
        PoliticalID=__("Provisional Military Government"), 
        AlignmentID=__("International Marxism"), 
        RulingParty=__("Provisional People's Committee for North Korea"), 
        FactionID=__("No Faction"), 
        IsActive=False,
        Flag='_1945'
        )

    TL_GUO[23] = Nation(
        Name=__("United States Army Military Government in Korea"), 
        ID="KOR", 
        Leader=__("Archibald Vincent Arnold"), 
        LeaderSub=__("Military Governer of Korea"), 
        PoliticalID=__("Provisional Military Government"), 
        AlignmentID=__("United States"), 
        RulingParty=__("United State Army Military Government"), 
        FactionID=__("No Faction"), 
        IsActive=False,
        Flag='_1945'
        )
######## ##     ## ########   #######  ########  ########    ###    ##    ##     ######   #######  ##        #######  ##    ## #### ########  ######  
##       ##     ## ##     ## ##     ## ##     ## ##         ## ##   ###   ##    ##    ## ##     ## ##       ##     ## ###   ##  ##  ##       ##    ## 
##       ##     ## ##     ## ##     ## ##     ## ##        ##   ##  ####  ##    ##       ##     ## ##       ##     ## ####  ##  ##  ##       ##       
######   ##     ## ########  ##     ## ########  ######   ##     ## ## ## ##    ##       ##     ## ##       ##     ## ## ## ##  ##  ######    ######  
##       ##     ## ##   ##   ##     ## ##        ##       ######### ##  ####    ##       ##     ## ##       ##     ## ##  ####  ##  ##             ## 
##       ##     ## ##    ##  ##     ## ##        ##       ##     ## ##   ###    ##    ## ##     ## ##       ##     ## ##   ###  ##  ##       ##    ## 
########  #######  ##     ##  #######  ##        ######## ##     ## ##    ##     ######   #######  ########  #######  ##    ## #### ########  ######  
    TL_GUO[24] = Nation(
        Name=__("United Kingdom"), 
        ID="ENG", 
        Leader=__("Neville Chamberlain"), 
        LeaderSub=__("Prime Minister of United Kingdom"), 
        PoliticalID=__("Imperial Federation"), 
        AlignmentID=__("League of Nations"), 
        RulingParty=__("Conservative Party"), 
        FactionID=__("Anglo-French Alliance"), 
        IsActive=True
        )

    TL_GUO[25] = Nation(
        Name=__("Portugese Republic"), 
        ID="POR", 
        Leader=__("Antonio de Oliveira Salazar"), 
        LeaderSub=__("Prime Minister of Portugal"), 
        PoliticalID=__("Authoritarian Oligarchic Republic"), 
        AlignmentID=__("Estada Novo"), 
        RulingParty=__("Uniao Nacional"), 
        FactionID=__("No Faction"), 
        IsActive=True
        )

    TL_GUO[26] = Nation(
        Name=__("French Republic"), 
        ID="FRA", 
        Leader=__("Camille Chautemps"),
        LeaderSub=__("Prime Minister of France"), 
        PoliticalID=__("Democratic Republic"), 
        AlignmentID=__("League of Nations"), 
        RulingParty=__("Parti radical"), 
        FactionID=__("Anglo-French Alliance"), 
        IsActive=True
        )

    TL_GUO[27] = Nation(
        Name=__("Union of\nSoviet Socialist Republics"), 
        ID="SOV",
        Leader=__("Joseph Stalin"),
        LeaderSub=__("General Secretary of the Communist Party of the Soviet Union"), 
        PoliticalID=__("Marxist Dictatorship"), 
        AlignmentID=__("International Marxism"), 
        RulingParty=__("Kommunisticheskaya partiya\nSovetskogo Soyuza"), 
        FactionID=__("Comintern"), 
        IsActive=True
        )

    TL_GUO[28] = Nation(
        Name=__("United States of America"), 
        ID="USA", 
        Leader=__("Franklin D Roosevelt"), 
        LeaderSub=__("President of the United States"), 
        PoliticalID=__("Democratic Republic"), 
        AlignmentID=__("Isolationism"), 
        RulingParty=__("Democratic party"), 
        FactionID=__("No Faction"), 
        IsActive=True
        )
# '''
# This will optimise code in the long run. 
# It's easier to give country tags as reference points when needing to work with nation objects.
# '''
define CHI = TL_GUO[0]
define PRC = TL_GUO[1]
define JAP = TL_GUO[2]
define MAN = TL_GUO[3]
define RNG = TL_GUO[4]
define EHA = TL_GUO[5]
define MEN = TL_GUO[6]
define PGR = TL_GUO[7]
define SHX = TL_GUO[8]
define XSM = TL_GUO[9]
define GXC = TL_GUO[10]
define YUN = TL_GUO[11]
define SDC = TL_GUO[12]
define HNC = TL_GUO[13]
define SHC = TL_GUO[14]
define SKC = TL_GUO[15]
define SIK = TL_GUO[16]
define TIB = TL_GUO[17]
define ETR = TL_GUO[18]
define BKT = TL_GUO[19]
define KII = TL_GUO[20]
define KON = TL_GUO[21]
define DRK = TL_GUO[22]
define KOR = TL_GUO[23]
define ENG = TL_GUO[24]
define POR = TL_GUO[25]
define FRA = TL_GUO[26]
define SOV = TL_GUO[27]
define USA = TL_GUO[28]