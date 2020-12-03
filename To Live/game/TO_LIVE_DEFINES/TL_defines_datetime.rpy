'''
Credit to Socradeath
'''
init python:
    weekdays = ("mon","tue","wed","thu","fri","sat","sun")
    dayperiods = [ "Early Morning", "Late Morning", "Early Afternoon", "Dusk", "Early Night", "Late Night", "Midnight"]
    class Date(object):
        def __init__(self, year, month, day, weekday, daytime):
            self.year = year
            self.month = month
            self.day = day
            self.weekday = weekday
            self.daytime = daytime

        def timepass(self):
            if self.daytime == dayperiods[6]:
                end_day()
            else:
                self.daytime = dayperiods[dayperiods.index(self.daytime)+1]

        def end_day(self):
            self.day += 1
            self.weekday = weekdays[weekdays.index(self.weekday)-6]
            self.daytime = dayperiods[dayperiods.index(self.daytime)-6]
            if self.month in (1,3,5,7,8,10,12):
                if self.day > 31:
                    self.day = 1
                    self.month += 1
            elif self.month in (4,6,9,11):
                if self.day > 30:
                    self.day = 1
                    self.month += 1
           
        #february in leap year
            else :
                # devide by 4
                if (self.year // 4) == 0 :
                    # devide by 100
                    if (self.year // 100) == 0 :
                        # devide by 400
                        if (self.year // 400) == 0 :
                            #leap year
                            __d = 29
                        else:
                            #normal year
                            __d = 28
                    else:
                        #devide by 4 - leap year
                        __d = 29
                else:
                    #normal year
                    __d = 28

                if self.day > __d:
                    self.day = 1
                    self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1



        # get weekdays
        def get_weekdays(self):
            if self.month < 3 :
                __m = self.month + 12
                __y = self.year - 1
            else :
                __m = self.month
                __y = self.year
            __weekday = ((__y+__y/4-__y/100+__y/400+(13*__m+8)/5+self.day) % 7) - 1
            self.weekday = weekdays[__weekday]
            return weekdays[__weekday]
        
        def return_date(self):
            return unicode(self.year)+". "+unicode(self.month)+". "+unicode(self.day)

        def return_day(self):
            return int(self.day)

        def return_month(self):
            return int(self.month)

        def return_year(self):
            return int(self.year)

        def Ureturn_year(self):
            return str(self.year)

        def return_daytime(self):
            return unicode(self.daytime)

default TL_datetime = Date(
        year = 1937,
        month = 9,
        day = 5,
        weekday = weekdays[1],
        daytime = dayperiods[1]
        )

style TL_datetime is text:
    antialias True
    font "fonts/eng_phat_grunge/PhatGrunge.ttf"

translate chinesesim style TL_datetime:
    antialias True
    font "fonts/chi_cities/MaShanZheng-Regular.ttf"

translate chinese style TL_datetime:
    antialias True
    font "fonts/chi_wangfonts/wt064.ttf"

translate korean style TL_datetime:
    antialias True
    font "fonts/kor_songmyung/SongMyung-Regular.ttf"
    language "korean-with-spaces"

translate japanese style TL_datetime:
    antialias True
    font "fonts/jap_mincho/SawarabiMincho-Regular.ttf"
    language "japanese-normal"

translate russian style TL_datetime:
    antialias True
    font "fonts/rus_roboto/RobotoSlab-Regular.ttf"
