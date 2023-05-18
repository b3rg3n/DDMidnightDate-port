







init -100 python:

    if renpy.windows:
        try:
            onedrive_path = os.environ["OneDrive"]
            if onedrive_path in config.basedir:
                raise Exception("DDLC mods/mod projects cannot be run from a cloud folder. Move your mod/mod project to another location and try again.")
        except: pass

    if renpy.android:
        import os
        if not os.path.exists(os.environ['ANDROID_PUBLIC'] + "/characters/"):
            try:
                os.mkdir(os.environ['ANDROID_PUBLIC'] + "/characters/")
            except:
                pass
    else:
        import os
        if not os.path.exists(config.basedir + "/characters/"):
            try:
                os.makedirs(config.basedir + "/characters/")
            except OSError:
                pass


init python:
    import re

    menu_trans_time = 1


    splash_message_default = "Это неофициальное фанатское дополнение, которое никак не связано с Team Salvato."


    splash_messages = [
        "Please support Doki Doki Literature Club.",
        "Monika is watching you code."
    ]








    def recolorize(path, blackCol="#ffbde1", whiteCol="#ffe6f4", contr=1.29):
        return im.MatrixColor(im.MatrixColor(im.MatrixColor(path, im.matrix.desaturate() * im.matrix.contrast(contr)), im.matrix.colorize("#00f", "#fff")
            * im.matrix.saturation(120)), im.matrix.desaturate() * im.matrix.colorize(blackCol, whiteCol))

    def process_check(stream_list):
        if not renpy.windows:
            for x in range(len(stream_list)):
                stream_list[x] = stream_list[x].replace(".exe", "")
        
        for x in range(len(stream_list)):
            for y in range(len(process_list)):
                if re.match(r"^" + stream_list[x] + r"\b", process_list[y]):
                    return True
        return False


image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)






image menu_logo:
    "mod_assets/logo.png"

    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_fade


image menu_bg:
    "mod_assets/menu_bg.png"



image game_menu_bg:
    "mod_assets/menu_bg.png"



image menu_fade:
    "white"
    menu_fadeout


image menu_art_y:
    subpixel True
    "mod_assets/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "mod_assets/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "mod_assets/menu_art_s.png"
    xcenter 600
    ycenter 375
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "mod_assets/menu_art_m.png"
    xcenter 1000
    ycenter 360
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)




image menu_nav:
    "mod_assets/main_menu.png"

    menu_nav_move







image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("mod_assets/menu_art_m.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout


transform particle_fadeout:
    easeout 1.5 alpha 0


transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.0
        ease_cubic 0 ypos -500


transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat


transform menu_logo_fade:
    subpixel True
    yoffset -300
    time 1.925
    easein 1.5 yoffset 0

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 0.0
    easein_bounce 1.5 yoffset 0


transform menu_nav_move:
    subpixel True
    xoffset -500
    time 0.0
    easein_quint 1 xoffset 0


transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0



transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0



image intro:
    truecenter
    "white"
    0.3
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    1.2
    "white" with Dissolve(0.5, alpha=True)
    0.5
    "mod_assets/anarchisty.png" with Dissolve(0.5, alpha=True)
    1.1
    "white" with Dissolve(0.5, alpha=True)
    0.2



image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5






image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"



label splashscreen:

    python:
        process_list = []
        currentuser = ""

        if renpy.windows:
            try: process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                try:
                    process_list = subprocess.check_output("powershell (Get-Process).ProcessName", shell=True).lower().replace("\r", "").split("\n") 
                    
                    for x in range(len(process_list)):
                        process_list[x] += ".exe"
                except: pass            
        else:
            try:
                try: process_list = subprocess.check_output("ps -A --format cmd", shell=True).split(b"\n") 
                except: process_list = subprocess.check_output("ps -A -o command", shell=True).split(b"\n") 
                
                for x in range(len(process_list)):
                    process_list[x] = process_list[x].decode().split("/")[-1]
                process_list.pop(0)
            except: pass

        try:
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                user = os.environ.get(name)
                if user:
                    currentuser = user
        except: pass

    if not persistent.Firstrun:
        python:
            restore_all_characters()
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "Это неофициальное фанатское дополнение к игре Doki Doki Literature Club, которое никак не связано с Team Salvato."
        "Перед прохождением данной модификации необходимо сначала пройти оригинальную игру."
        "Вы можете загрузить Doki Doki Literature Club по ссылке: http://ddlc.moe"
        $ persistent.Firstrun = True
        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0
        scene white



    if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
        $ quick_menu = False
        scene black

        menu:
            "Предыдущий файл сохранения был найден. Хотите ли вы удалить все данные и начать заново?"
            "Да, удалить все существующие данные." if True:
                "Удаление...{nw}"
                python:
                    delete_all_saves()
                    renpy.loadsave.location.unlink_persistent()
                    renpy.persistent.should_save_persistent = False
                    renpy.utter_restart()
            "Нет, продолжить там же." if True:
                $ restore_relevant_characters()



    default persistent.lockdown_warning = False

    if not persistent.lockdown_warning:
        if config.developer:
            call lockdown_check from _call_lockdown_check
        elif True:
            $ persistent.lockdown_warning = True


    default persistent.first_run = False

    if not persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0





        "[config.name] - это фанатское дополнение к игре Doki Doki Literature Club, которое никак не связано с Team Salvato."
        "Это подразумевает, что вы уже прошли оригинальную игру, так как оно содержит некоторые спойлеры."
        "Для прохождения этого дополнения вам будут нужны файлы оригинальной Doki Doki Literature Club, которую вы сможете загрузить по ссылке: https://ddlc.moe или в Steam."

        menu:
            "Играя в [config.name], вы соглашаетесь с тем, что уже прошли оригинальную игру, и готовы к любым спойлерам, содержащимся в нём."
            "Я согласен." if True:
                pass

        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0




        if extra_settings:
            if process_check(["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]):
                $ persistent.lets_play = True
                call screen dialog("Режим Let's Play был автоматически включён.\nЭтот режим позволяет пропускать контент, который\nсодержит чувствительные/взрослые сцены, \nили изменить настройки истории.\n\nЭта настройка зависит от того, включил ли\nавтор модификации эти галочки в его историю.\n\n Чтобы выключить режим Let's Play, зайдите в Настройки и\nуберите галочку с настройки «Режим Let's Play».", 
                    [Hide("dialog"), Return()])
        scene white

























    if not persistent.special_poems:
        python hide:

            persistent.special_poems = [0,0,0]


            a = range(1,12)



            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                
                
                a.remove(b)



    $ basedir = config.basedir.replace('\\', '/')



    if persistent.autoload:
        jump autoload


    $ config.allow_skipping = False



    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black

        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        $ config.allow_skipping = True
        return

























































    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = "mod_assets/Sound/mystery-of-a-haunted-memory-SBA-300514745.mp3"
    $ renpy.music.play(config.main_menu_music)
    $ starttime = datetime.datetime.now()
    show intro with Dissolve(0.5, alpha=True)
    $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
    $ config.allow_skipping = True
    return



label warningscreen:
    hide intro
    show warning
    pause 3.0































label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if anticheat != persistent.anticheat:
        stop music
        scene black
        "The save file could not be loaded."
        "Are you trying to cheat?"

        $ renpy.utter_restart()
    return


label autoload:
    python:
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

        try: renpy.pop_call()
        except: pass

    jump expression persistent.autoload



label before_main_menu:
    $ config.main_menu_music = "mod_assets/Sound/mystery-of-a-haunted-memory-SBA-300514745.mp3"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
