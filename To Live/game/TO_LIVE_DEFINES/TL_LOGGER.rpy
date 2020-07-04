
init -100 python:
    import os
    import sys
    import logging

    config.log = config.gamedir+"devtools.txt"
    # absolute path to the game directory, which is formatted according
    # to the conventions of the local OS
    gamedir = os.path.normpath(config.gamedir)

    # required to make the above work with with RenPy:
    config.reject_backslash = False

    # setting the window on center
    # useful if game is launched in the window mode
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    sys.setdefaultencoding('utf-8')

    # Game may bug out on saving, in such case, comment should be removed
    # config.use_cpickle = False
    
    
    # enable logging via the 'logging' module
    # if (logging.hasHandlers()): Next Ren'py update will have V3 support
    #     logging.handlers.clear()
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(name)-15s %(message)s')
    devlog = logging.getLogger(" ".join([config.name, config.version]))
    devlogfile = logging.FileHandler(os.path.join(gamedir, "devlog.txt"), mode='w')
    devlogfile.setLevel(logging.DEBUG)
    devlog.addHandler(devlogfile)
    devlog.critical("\n--- launch game ---")
    devlog.critical("Credits to Lu-Yi-Feng")
    devlog.critical("Logging system established 9-6-2020 :)")
    devlog.critical("")
    fm = logging.Formatter('%(asctime)-s %(levelname)-s %(name)-s %(message)s')
    devlogfile.setFormatter(fm)
    del fm

    devlog.info("Game directory: %s" % gamedir)
    devtool = logging.getLogger(" ".join([config.name, config.version]))
    devtoolfile = logging.FileHandler(os.path.join(gamedir, "devtools.txt"), mode='w')
    devtoolfile.setLevel(logging.DEBUG)
    devtool.addHandler(devtoolfile)
    devtool.critical("\n--- launch game ---")
    devtooler = logging.Formatter('%(lineno)d %(message)s')
    devtoolfile.setFormatter(devtooler)
    del devtooler
python early:
    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "To Live"
    config.version = "0.0.79"

define devlog = logging.getLogger(" ".join([config.name, config.version]))
define devtool = logging.getLogger("".join([config.name, config.version]))


