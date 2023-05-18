# Here's the code for the phone!

define nvl_mode = "phone"  ##Allow the NVL mode to become a phone conversation
define mc_Name = "Player" ##The name of the main character, used to place them on the screen

init -1 python:
    phone_position_x = 0.5
    phone_position_y = 0.5

    def Phone_ReceiveSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("mod_assets/Phone/audio/ReceiveText.ogg")
    def Phone_SendSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("mod_assets/Phone/audio/SendText.ogg")
    def print_bonjour():
        print("bonjour")


transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

transform phone_appear(pXalign=0.5, pYalign=0.5): #Used only when the dialogue have one element
    xcenter pXalign
    yalign pYalign

    on show:
        yoffset 1080
        easein_back 1.0 yoffset 0

    
transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0
    

transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

screen PhoneDialogue(dialogue, items=None):

    style_prefix "phoneFrame"
    frame at phone_transform(phone_position_x, phone_position_y):
        if len(dialogue) == 1:
            at phone_appear(phone_position_x, phone_position_y)
        viewport:
            #draggable True
            mousewheel True
            # cols 1
            yinitial 1.0
            # scrollbars "vertical"
            vbox:
                null height 20
                use nvl_phonetext(dialogue)
                null height 100


screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None
    for id_d, d in enumerate(dialogue):
        if d.who == None: # Narrator
            text d.what:
                    xpos -335
                    ypos 0.0
                    xsize 100
                    text_align 0.5
                    italic True
                    size 28
                    slow_cps False
                    id d.what_id
                    if d.current:
                        at message_narrator
        else:
            if d.who == mc_Name:
                $ message_frame = "mod_assets/Phone/images/phone_send_frame.png"
            else:
                $ message_frame = "mod_assets/Phone/images/phone_received_frame.png"

            hbox:
                spacing 10
                if d.who == mc_Name:
                    box_reverse True
                
                #If this is the first message of the character, show an icon
                if previous_d_who != d.who:
                    if d.who == mc_Name:
                        $ message_icon = "mod_assets/Phone/images/phone_send_icon.png"
                    elif d.who == y_name:
                        $ message_icon = "mod_assets/Phone/images/yphone_received_icon.png"
                    elif d.who == k_name:
                        $ message_icon = "mod_assets/Phone/images/kphone_received_icon.png"
                    elif d.who == m_name:
                        $ message_icon = "mod_assets/Phone/images/mphone_received_icon.png"
                    elif d.who == s_name:
                        $ message_icon = "mod_assets/Phone/images/sphone_received_icon.png"
                    elif d.who == h_name:
                        $ message_icon = "mod_assets/Phone/images/hphone_received_icon.png"
                    elif d.who == n_name:
                        $ message_icon = "mod_assets/Phone/images/nphone_received_icon.png"
                    else:
                        $ message_icon = "mod_assets/Phone/images/phone_received_icon.png"

                    add message_icon:
                        if d.current:
                            at message_appear_icon()
                        
                else:
                    null width 107

                vbox:
                    yalign 1.0
                    if d.who != mc_Name and previous_d_who != d.who:
                        text d.who

                    frame:
                        padding (25,25)
                        

                        background Frame(message_frame, 23,23,23,23)
                        xsize 250

                        if d.current:
                            if d.who == mc_Name:
                                at message_appear(1)
                            else:
                                at message_appear(-1)

                        text d.what:
                            pos (0,0)
                            xsize 250
                            slow_cps False
                            

                            if d.who == mc_Name :
                                color "#FFF"
                                text_align 0.8
                                xpos -320
                            else:
                                color "#FFF"

                                
                            id d.what_id
        $ previous_d_who = d.who
                    
style phoneFrame is default

style phoneFrame_frame:
    background Transform("mod_assets/Phone/images/phone_background.png", xcenter=0.5,yalign=0.5,zoom=0.8)
    foreground Transform("mod_assets/Phone/images/phone_foreground.png", xcenter=0.5,yalign=0.5,zoom=0.8)
    
    ysize 600
    xsize 400

style phoneFrame_viewport:
    yfill True
    xfill True

    yoffset -20

style phoneFrame_vbox:
    spacing 10
    xfill True


