

default persistent.iphone = True

init python:

    class TextMessage():
        
        def __init__(self, reciever, date, text_set):
            self.reciever = reciever
            self.date = date
            
            if type(text_set) != list:
                raise Exception("Not a list array of tuples.")
            
            for x in text_set:
                if type(x) != tuple:
                    raise Exception("Non-tuple found in list.")
            
            self.text_set = text_set


    class TextHistoryCharacter():
        
        def __init__(self, character):
            self.character = character.lower()
            self.text_history = []


    test_text_one = TextMessage("mc", "December 17th", [("s", "Can you buy me cookies?"), ("mc", "Please stop asking me"), ("s", "Pleaseeee..."),
("mc", "I said stop texting me about this"), ("s", "Meanie!")])

    test_text_two = TextMessage("mc", "December 18th", [("s", "...Can you buy me cookies?"), ("mc", "If you can stop texting me about it then yes."), ("s", "Yay!")])


    test_text_three = TextMessage("mc", "December 24th", [("m", "Um...can you see me?"), ("s", "I can!"), ("y", "I can see you just fine"), ("n", "Monika, stop being so dramatic"),
("mc", "Jeez...what a fine day I woke up to..."), ("s", "Says the neet!"), ("n", "GanyuXD")])

    test_text_four = TextMessage("mc", None, [("mc", "Shut you"), ("n", "How about I shut you myself?!"), ("y", "I-I don't like where this is going"), ("m", "Behave or you will be kicked out."),
("mc", "Fine..."), ("n", "Hmph!")])


    test_text_five = TextMessage("mc", None, [("s", "Can we get some cookies for the event?"), ("m", "No"), ("mc", "no"), ("s", "Awww... :(")])











    sayori_text_one = TextMessage("mc", "December 17th", [("s", "Hey, Kotos here with me, ready whenever!"), ("s", "Hellooooo..."), ("s", "Did you fall asleep?!"), ("s", "Answerrrrrrrr!"), ("s", "Thats it were coming over to get you")])

    sayori_text_two = TextMessage("mc", "December 17th", [("mc", "Sorry was in the bathroom, no I didnt fall asleep"), ("mc", "Also a bit late to come over isnt it?"), ("s", "You jerk!"), ("s", "Why didnt you answer earlier?!"), ("mc", "We went over this already"), ("s", "Oh yeah"), ("mc", "Someone needs sleep I think"), ("s", "Neverrrr!"), ("mc", "Im curious, how long does never last?"), ("s", "...About 10 minutes"), ("mc", "Thought so"), ("mc", "Goodnight Sayori"), ("s", "Night!")])

    sayori_text_three = TextMessage("mc", "December 17th", [("mc", "Hey Sayo, whatcha up to"), ("s", "Painting!"), ("mc", "I didnt know you liked painting"), ("s", "Thats because youre never around when im doing it"), ("mc", "Yeah but you never mention it either"), ("s", "You never ask"), ("mc", "Terrible logic"), ("mc", "But anyways back on topic"), ("s", "What topic?"), ("mc", "The topic of you coming to the mall to cheer Koto up"), ("s", "Why is she sad?!"), ("mc", "Because shes concerned about my past again"), ("s", "Oh well that makes sense"), ("s", "You should just tell her"), ("mc", "When the time is right"), ("mc", "So you coming or not?"), ("s", "Well I just need to finish up what Im doing then I can head there!"), ("mc", "Sounds good, we're eating lunch anyways still so no rush"), ("s", "Okay, see you soon!"), ("mc", "Sure thing, just text me when you get here"), ("s", "I will!")])










    def get_time(st, at):
        d = datetime.datetime.now().strftime("%I:%M")
        if renpy.get_screen("phone_call"):
            return Text(d, style="phone_text", size=12, color="#fff"), 0.20
        else:
            return Text(d, style="phone_text", size=12, color="#000"), 0.20

image time_now = DynamicDisplayable(get_time)


default current_text_num = 0


default s_hist = TextHistoryCharacter("sayori")
default n_hist = TextHistoryCharacter("natsuki")
default m_hist = TextHistoryCharacter("monika")
default y_hist = TextHistoryCharacter("yuri")
default group_hist = []
default character_hist_list = [s_hist, n_hist, m_hist, y_hist]

screen phone(number, sender, text_class, hist=None, groupChat=False):

    style_prefix "phone"
    zorder 190


    python:
        vp_xsize = 290
        if persistent.iphone:
            vp_ysize = 385
        else:
            vp_ysize = 445

        text_class_size = len(text_class.text_set) - 1


    frame:
        xpos 0.34
        ypos 0.03
        xsize vp_xsize
        ysize vp_ysize


        hbox:
            if persistent.iphone:
                xoffset 205
                yoffset 85
            else:
                xoffset 70
                yoffset 58
            add "time_now"


        viewport:
            if persistent.iphone:
                xoffset 175
                yoffset 105
            else:
                xoffset 125
                yoffset 77
            vbox:

                text sender substitute False size 12
                text number substitute False size 12


        viewport:
            xoffset 80
            if persistent.iphone:
                yoffset 160
            else:
                yoffset 130
            xsize vp_xsize
            ysize vp_ysize
            mousewheel True
            vbox:
                spacing 10



                if not groupChat:
                    python:
                        if hist is None:
                            for x in character_hist_list:
                                if sender.lower() == x.character:
                                    hist = x.text_history

                        if hist is None:
                            raise Exception("Cannot find history list for character " + sender)
                else:
                    python:
                        if hist is None:
                            hist = group_hist


                if len(hist) > 0:
                    for past in hist:
                        text past.date substitute False size 10 xalign 0.9
                        for prev in range(0, len(past.text_set)):
                            if past.text_set[prev][0] == text_class.reciever:
                                frame:
                                    style "player_text_frame"
                                    text past.text_set[prev][1] substitute False
                            else:
                                if groupChat:
                                    if past.text_set[prev][0] != "mc":
                                        text eval(past.text_set[prev][0] + "_name") size 10
                                    else:
                                        text "[player]" size 10
                                frame:
                                    style "text_frame"
                                    text past.text_set[prev][1] substitute False



                if text_class.date is not None:
                    text text_class.date substitute False size 10 xalign 0.9



                if current_text_num >= 1:
                    for prev in range(0, current_text_num):
                        if text_class.text_set[prev][0] == text_class.reciever:
                            frame:
                                style "player_text_frame"
                                text text_class.text_set[prev][1] substitute False
                        else:
                            if groupChat:
                                if text_class.text_set[prev][0] != "mc":
                                    text eval(text_class.text_set[prev][0] + "_name") size 10
                                else:
                                    text "[player]" size 10
                            frame:
                                style "text_frame"
                                text text_class.text_set[prev][1] substitute False


                if groupChat:

                    if text_class.text_set[current_text_num][0] != "mc":
                        if text_class.text_set[current_text_num][0] != text_class.reciever:
                            text eval(text_class.text_set[current_text_num][0] + "_name") size 10
                    else:
                        if text_class.text_set[current_text_num][0] != text_class.reciever:
                            text "[player]" size 10



                if text_class.text_set[current_text_num][0] == text_class.reciever:
                    if persistent.iphone:
                        frame at iphone_text_trans(240, 95):
                            style "player_text_frame"
                            text text_class.text_set[current_text_num][1] substitute False
                    else:
                        frame at samsung_text_trans:
                            style "player_text_frame"
                            text text_class.text_set[current_text_num][1] substitute False
                else:
                    if persistent.iphone:
                        frame at iphone_text_trans(-80, 95):
                            style "text_frame"
                            text text_class.text_set[current_text_num][1] substitute False
                    else:
                        frame at samsung_text_trans:
                            style "text_frame"
                            text text_class.text_set[current_text_num][1] substitute False

    key "mousedown_1" action If(current_text_num < text_class_size, SetVariable("current_text_num", current_text_num+1), Return(0))

style phone_frame is empty:
    background If(persistent.iphone, true="mod_assets/iosphoneon.png", false="mod_assets/samsungphoneon.png")

style phone_text:
    color "#000"
    outlines []
    size 16

style samsung_back_text is phone_text:
    size 26

style iphone_back_text is phone_text:
    size 20

style text_frame:
    xsize 190
    background Frame("mod_assets/temptextbubble.png", tile=False)

style player_text_frame:
    xoffset 100
    background Frame(If(persistent.iphone, "mod_assets/iphonereplybubble.png", "mod_assets/samsungreplybubble.png"), tile=False)

transform samsung_text_trans:
    alpha 0.0
    linear 0.2 alpha 1.0

transform iphone_text_trans(x1, x2):
    xcenter x1
    linear 0.2 xcenter x2

screen phone_call(caller, region, voicefile, inCall=False):

    style_prefix "phone_call"
    zorder 190

    python:
        vp_xsize = 290
        if persistent.iphone:
            vp_ysize = 385
        else:
            vp_ysize = 445

    frame:
        if inCall:
            style "phone_call_incall_frame"
        else:
            style "phone_call_frame"
        xpos 0.34
        ypos 0.03

        hbox:
            if persistent.iphone:
                xoffset 205
                yoffset 80
            else:
                xoffset 70
                yoffset 55
            add "time_now"


        hbox:
            xoffset 135
            if persistent.iphone:
                yoffset 150
            else:
                yoffset 135
            vbox:
                text caller
                text region size 14


        hbox:
            if persistent.iphone:
                xoffset 185
                yoffset 470
            else:
                xoffset 185
                yoffset 500


            if inCall:
                button:
                    action [Stop("voice"), Return(0)]

                    add "mod_assets/samsunghangupicon.png"
            else:
                button:
                    action [Play("voice", voicefile), Show("phone_call", caller=caller, region=region, voicefile=voicefile, inCall=True), With(Dissolve(0.2))]

                    add "mod_assets/samsungcallicon.png"

style phone_call_frame:
    background If(persistent.iphone, "mod_assets/iosphonecall.png", "mod_assets/samsungphonecall.png")

style phone_call_incall_frame:
    background If(persistent.iphone, "mod_assets/iosphonecall.png", "mod_assets/samsungphoneincall.png")

style phone_call_text is phone_text:
    color "#ebebeb"
    size 24
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
