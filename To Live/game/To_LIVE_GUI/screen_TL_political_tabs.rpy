




screen guo_map():
    key "K_SPACE" action ShowMenu(main_menu)
    viewport:
        xysize (config.screen_width, config.screen_height)
        child_size (4040, 2230)
        xinitial 2300
        yinitial 500
        draggable True
        edgescroll (700, 700)
        add "maps/GUO_map.png"
        for q in TL_GUO_loc:
            if q.IsActive:
                button:
                    xpos q.x
                    ypos q.y
                    text q.name color "#000000" 
                    action NullAction()