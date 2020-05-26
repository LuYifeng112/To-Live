########  ####  ######   ######   #######  ########  ########     ########  ##       ##     ##  ######   #### ##    ## 
##     ##  ##  ##    ## ##    ## ##     ## ##     ## ##     ##    ##     ## ##       ##     ## ##    ##   ##  ###   ## 
##     ##  ##  ##       ##       ##     ## ##     ## ##     ##    ##     ## ##       ##     ## ##         ##  ####  ## 
##     ##  ##   ######  ##       ##     ## ########  ##     ##    ########  ##       ##     ## ##   ####  ##  ## ## ## 
##     ##  ##        ## ##       ##     ## ##   ##   ##     ##    ##        ##       ##     ## ##    ##   ##  ##  #### 
##     ##  ##  ##    ## ##    ## ##     ## ##    ##  ##     ##    ##        ##       ##     ## ##    ##   ##  ##   ### 
########  ####  ######   ######   #######  ##     ## ########     ##        ########  #######   ######   #### ##    ## 
init -20 python:
    import discord_rpc
    import time

    def readyCallback(current_user):
        print('Our user: {}'.format(current_user))

    def disconnectedCallback(codeno, codemsg):
        print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
            codeno, codemsg
        ))

    def errorCallback(errno, errmsg):
        print('An error occurred! Error {}: {}'.format(
            errno, errmsg
        ))



label before_main_menu:
    python:
        # Note: 'event_name': callback
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('704183975987511348', callbacks=callbacks, log=False)
        start = time.time()
        print(start)
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Main Menu',
                'start_timestamp': start,
                'large_image_key': 'tolive'
            }
        )
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
    return

label Pre_Menu:
    show screen press_to_start


