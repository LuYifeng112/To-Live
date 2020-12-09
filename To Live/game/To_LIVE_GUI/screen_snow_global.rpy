init python:




    import random


    random.seed()




    def Snow(image, max_particles=50, speed=150, wind=100, xborder=(0,100), yborder=(50,400), **kwargs):
        """
        This creates the snow effect. You should use this function instead of instancing
        the SnowFactory directly (we'll, doesn't matter actually, but it saves typing if you're
        using the default values =D)

        @parm {image} image:
            The image used as the snowflakes. This should always be a image file or an im object,
            since we'll apply im transformations in it.

        @parm {int} max_particles:
            The maximum number of particles at once in the screen.

        @parm {float} speed:
            The base vertical speed of the particles. The higher the value, the faster particles will fall.
            Values below 1 will be changed to 1

        @parm {float} wind:
            The max wind force that'll be applyed to the particles.

        @parm {Tuple ({int} min, {int} max)} xborder:
            The horizontal border range. A random value between those two will be applyed when creating particles.

        @parm {Tuple ({int} min, {int} max)} yborder:
            The vertical border range. A random value between those two will be applyed when creating particles.
            The higher the values, the fartest from the screen they will be created.
        """
        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))


    class SnowFactory(object):
        """
        The factory that creates the particles we use in the snow effect.
        """
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            """
            Initialize the factory. Parameters are the same as the Snow function.
            """
            
            self.max_particles = max_particles
            
            
            self.speed = speed
            
            
            self.wind = wind
            
            
            self.xborder = xborder
            self.yborder = yborder
            
            
            
            
            self.depth = kwargs.get("depth", 10)
            
            
            self.image = self.image_init(image)
        
        
        def create(self, particles, st):
            """
            This is internally called every frame by the Particles object to create new particles.
            We'll just create new particles if the number of particles on the screen is
            lower than the max number of particles we can have.
            """
            
            if particles is None or len(particles) < self.max_particles:
                
                
                depth = random.randint(1, self.depth)
                
                
                
                
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],      
                                      random.uniform(-self.wind, self.wind)*depth_speed,  
                                      self.speed*depth_speed,  
                                      random.randint(self.xborder[0], self.xborder[1]), 
                                      random.randint(self.yborder[0], self.yborder[1]), 
                                      ) ]
        
        
        def image_init(self, image):
            """
            This is called internally to initialize the images.
            will create a list of images with different sizes, so we
            can predict them all and use the cached versions to make it more memory efficient.
            """
            rv = [ ]
            
            
            for depth in range(self.depth):
                
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( im.FactorScale( im.Alpha(image, p), p ) )
            
            return rv
        
        
        def predict(self):
            """
            This is called internally by the Particles object to predict the images the particles
            are using. It's expected to return a list of images to predict.
            """
            return self.image


    class SnowParticle(object):
        """
        Represents every particle in the screen.
        """
        def __init__(self, image, wind, speed, xborder, yborder):
            """
            Initializes the snow particle. This is called automatically when the object is created.
            """
            
            
            self.image = image
            
            
            
            
            if speed <= 0:
                speed = 1
            
            
            self.wind = wind
            
            
            self.speed = speed
            
            
            
            self.oldst = None
            
            
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
        
        
        def update(self, st):
            """
            Called internally in every frame to update the particle.
            """
            
            
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            
            
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
            
            
            if self.ypos > renpy.config.screen_height or\
            (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                    
                    return None
            
            
            
            
            return int(self.xpos), int(self.ypos), st, self.image

init:
    image snow = Snow("00_globals/snow.png")
    image heavy_snow = Snow("00_globals/snow.png", max_particles=500)
    image abyss_snow = Snow("00_globals/abyss.png")
    image ashes = Snow("00_globals/abyss.png", wind=100)
    image ashes_ember = Snow("00_globals/ember.png", wind=100, max_particles=200)


    $ flash = Fade(0.3, 0, 0.5, color="#fff")
    $ flash2 = Fade(2, 2, 2, color="#fff")
    $ flash_red = Fade(1, 0, 1, color="#e11")
    $ fade3 = Fade(1.5, 0, 1.5)
    $ fade2 = Fade(1, 0, 1)
    $ hell_dissolve = Dissolve(50)
    $ dissolve2 = Dissolve(2)
    $ dissolve_fast = Dissolve(0.5)
    $ dissolve_long = Dissolve(100)
    $ dspr = Dissolve(.2)

   