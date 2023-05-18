




label start:





    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = config.developer






    $ s_name = "Сайори"
    $ m_name = "Моника"
    $ n_name = "Нацуки"
    $ y_name = "Юри"


    $ quick_menu = True



    $ style.say_dialogue = style.normal



    $ in_sayori_kill = None


    $ allow_skipping = True
    $ config.allow_skipping = True




    if persistent.playthrough == 0:



        $ chapter = 0



        call story from _call_story







































        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
