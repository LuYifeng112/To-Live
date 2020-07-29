init -20 python:
    import math
    #this function is for when you want to use with a bar
    #for example, if your bar run from 0 to 100
    #and you want the wheel to be upright at 50
    #and can turn up to 100 degree to either side
    #then use upset(2,50)
    #50 is the value when the wheel is upright
    #2 means any deviation from 50 will be 2x to get the rotation angle
    def upset(blown,equil):
        def exaggerate(goal):
            return blown*(goal-equil)
        return exaggerate
   
    #this is the default method to control the speed of the motion
    #basically, it make the wheel rotate fast at the start, slow at the end
    #just like how a sine function look like
    def funtimeover(r):
        return math.sin(r*math.pi/2)
   
    #you need one instance of this class to manage the wheel
    #when initialize the class, the following argument are optional
    #time (default None): number of seconds between the wheel start
    #     to turn and when it stop at the correct location
    #     if not a positive number, will means instant rotation
    #initial (default 0): initial value for the bar
    #     after applying correction, will also become
    #     the angle the wheel is already rotated to initially when it is shown
    #correction (default the identity function): how the value of the
    #     bar need to be corrected to get the angle in degree
    #     by default this is the identity function (no correction)
    #distort (default funtimeover): how the amount of time passed since
    #     the wheel start rotating related to the amount of distance
    #     moved to reach its final position
    #resetmode (default "hide"): when would the wheel be reset
    #     to the default angle when it is shown again after hidden
    #     if "always" or "never", always or never respective
    #     if "hide", then only when it was explicitly made hidden by a hide command
    class MerryGoRound:
        def reset(self,newbegin=None):
            if newbegin==None:
                self.goal=self.initial
            else:
                self.goal=newbegin
            goal=self.correction(self.goal)            
            self.offset=0
            self.last_st=0
            self.last_angle=goal
            self.current_angle=None
            self.current_goal=goal
            self.hidden=False
            return
        def __init__(self,time=None,initial=0,correction=upset(1,0),distort=funtimeover,resetmode="hide"):
            self.initial=initial
            self.correction=correction
            self.time=time
            if not self.time>0:
                self.time=None
            self.distort=distort
            self.reset()
            if resetmode=="hide":
                self.hidereset=True
                self.showreset=False
            elif resetmode=="always":
                self.hidereset=False
                self.showreset=True
            else:
                self.hidereset=False
                self.showreset=False
            return
       
        #this function need to be passed as the function argument in Transformation
        def weee(self,d,st,at):
            if d.hide_request:
                self.hidden=True
                return 0
            if self.offset!=0:
                self.goal+=self.offset
                self.offset=0
            goal=self.correction(self.goal)
            if self.current_angle==None:
                self.current_angle=goal
                d.rotate=self.current_angle
                return 0
            if goal!=self.current_goal:
                self.last_st=st
                self.last_angle=self.current_angle
                self.current_goal=goal
            st_offset=st-self.last_st
            if st_offset<0:
                st_offset=0
                if (self.hidden and self.hidereset) or (self.showreset):
                    self.reset()
                else:
                    self.reset(self.goal)
            if self.time==None:
                self.current_angle=goal
            else:
                if st_offset>self.time:
                    st_offset=self.time
                    self.last_angle=self.goal
                ratio=st_offset/self.time
                self.current_angle=(goal-self.last_angle)*self.distort(ratio)+self.last_angle
            d.rotate=self.current_angle
            return 0

#best to move an arrow-shaped button to its proper location
#pinpoint is coordinate of the point to rotate around
#lgth is the distance of the button from the pinpoint
#direction is the angle specifying the degree of offset from the upward direction
#the "top" of the button will point away from pinpoint
transform dead_compass(pinpoint,lgth,direction):
    anchor (0.5,0.5) around pinpoint radius lgth angle direction rotate direction

image compass surface:
    "compass.png"
    size(300, 300)
    zoom 1.1
    
#compass screen example
#put this in screens.rpy
#you need to declare the image named "compass surface" somewhere
init python:
    #initialize a MerryGoRound object for this screen
    #2.0 here is the number of second the wheel will spin before reaching its correct orientation
    #the rest of the argument are left at default value
    carousel=MerryGoRound(2.0)
#use the call screen statement to test this
#we use button to rotate the wheel rather than a bar
screen dizzy_compass:
    hbox:
        xalign 0.5
        #use SetField to set the value of carousel.offset
        #this value will be added, so the wheel will rotate by an extra amount
        #if you want to use a bar instead
        #then use FieldValue to set carousel.goal
        #note that 756 degree is more than 2 rounds
        #so the wheel will rotate that much
        #though it won't be noticeable if you set time=None at the start
        textbutton _("<") action SetField(carousel,"offset",-756) #-756 means rotate counterclockwise 756 degree
        textbutton _(">") action SetField(carousel,"offset",+756) #+756 means rotate clockwise 756 degree
    
    #use at Transform(function=carousel.weee) to let carousel object to control the wheel
    #best to use a Fixed with fit_first=True
    #since you want the compass's centre to be the same as the Fixed's centre
    #fit_first ensure that this Fixed will be of the same size as the image for the compass
    fixed fit_first True pos (0.5,0.5) anchor (0.5,0.5) at Transform(function=carousel.weee):
        add "compass surface"#declare the image that also determine the size of the Fixed
        #here we add some button and point them in the right direction
        #use textbutton because I did not draw compass hand, but imagebutton should work too
        textbutton _("^") action Return("north") at dead_compass((0.5,0.5),0.4,0) #(0.5,0.5) should be the centre of the dial
                                 #0.4 means this button will be off from that centre by a distance of 0.4 the size of the image
                                 #0 means the button is pointing straight up
        textbutton _("^") action Return("east") at dead_compass((0.5,0.5),0.4,90) #90 here means the button is pointing to the right
                                 #which is 90 away degree from the upward direction
                                 #note that the button will get rotated, so the ^ will actually point in the correct direction
        textbutton _("^") action Return("south") at dead_compass((0.5,0.5),0.4,180)
        textbutton _("^") action Return("west") at dead_compass((0.5,0.5),0.4,-90)