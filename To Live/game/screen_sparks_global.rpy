init:
    python:

        class ExplodeFactory: # the factory that makes the particles
            
            def __init__(self, theDisplayable, explodeTime=0, numParticles=20):
                self.displayable = theDisplayable
                self.time = explodeTime
                self.particleMax = numParticles
            def create(self, partList, timePassed):
                newParticles = None
                if partList == None or len(partList) < self.particleMax:
                    if timePassed < self.time or self.time == 0:
                        newParticles = self.createParticles()
                return newParticles
                
            
            def createParticles(self):
                timeDelay = renpy.random.random() * 0.6
                return [ExplodeParticle(self.displayable, timeDelay)]
            
            def predict(self):
                return [self.displayable]

init:
    python:        
        class ExplodeParticle:
            
            def __init__(self, theDisplayable, timeDelay):
                self.displayable = theDisplayable
                self.delay = timeDelay
                self.xSpeed = (renpy.random.random() - 0.5) * 0.02
                self.ySpeed = (renpy.random.random() - 0.5) * 0.02
                self.xPos = 0.5
                self.yPos = 0.5
            
            def update(self, theTime):
                
                if (theTime > self.delay):
                    self.xPos += self.xSpeed
                    self.yPos += self.ySpeed
                    
                    if self.xPos > 1.05 or self.xPos < -1.05 or self.yPos > 1.05 or self.yPos < -1.05:
                        return None
                
                return (self.xPos, self.yPos, theTime, self.displayable)
                    
init:
    image boom = Particles(ExplodeFactory("00_globals/spark.png", numParticles=80, explodeTime = 1.0))

