layeredimage kiyomi turned:
    at AutofocusDisplayable(name="kiyomi turned")
    #####
    # If you're using Autofocus, uncomment the lines below and comment/remove the 'at Flatten' above
    #####
    
    
    group autofocus_coloring:
        attribute day default null
        attribute dawn null
        attribute afternoon null
        attribute evening null
        attribute night null

    always "mod_assets/MPT/kiyomi/facebase.png"

    group head:
        attribute headclip default:
            "mod_assets/MPT/kiyomi/headclip.png"   # self-explainatory
        attribute no_headclip null

    group outfit:
        attribute uniform default null
        attribute casual null
        attribute beach null

    group mood:

        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null #cry
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute sad null #sad
        attribute surp null #surprised
        attribute vang null #very angry
        attribute worr null #worried
        attribute yand null #yandere
    
    group left:
        subpixel True
        xoffset 0.5

        attribute ldown default if_any "uniform":
            "mod_assets/MPT/kiyomi/outfits/uniform_ldown.png"
        attribute ldown default if_any "casual":
            "mod_assets/MPT/kiyomi/outfits/casual_ldown.png"
        attribute ldown default if_any "beach":
            "mod_assets/MPT/kiyomi/outfits/beach_ldown.png"
        
        attribute lhip if_any "uniform":
            "mod_assets/MPT/kiyomi/outfits/uniform_lhip.png"
        attribute lhip if_any "casual":
            "mod_assets/MPT/kiyomi/outfits/casual_lhip.png"
        attribute lhip if_any "beach":
            "mod_assets/MPT/kiyomi/outfits/beach_lhip.png"
        
        attribute lup if_any "uniform":
            "mod_assets/MPT/kiyomi/outfits/uniform_lup.png"
        attribute lup if_any "casual":
            "mod_assets/MPT/kiyomi/outfits/casual_lup.png"
        attribute lup if_any "beach":
            "mod_assets/MPT/kiyomi/outfits/beach_lup.png"
        
        attribute peace if_any "uniform":
            "mod_assets/MPT/kiyomi/outfits/uniform_lup.png"
        attribute peace if_any "casual":
            "mod_assets/MPT/kiyomi/outfits/casual_lup.png"
        attribute peace if_any "beach":
            "mod_assets/MPT/kiyomi/outfits/beach_lup.png"
        
    group right:
        subpixel True
        xoffset -0.2

        attribute rdown default if_any "uniform":
            "mod_assets/MPT/kiyomi/outfits/uniform_rdown.png"
        attribute rdown default if_any "casual":
            "mod_assets/MPT/kiyomi/outfits/casual_rdown.png"
        attribute rdown default if_any "beach":
            "mod_assets/MPT/kiyomi/outfits/beach_rdown.png"

        attribute rup if_any "uniform":
            "mod_assets/MPT/kiyomi/outfits/uniform_rhip.png"
        attribute rup if_any "casual":
            "mod_assets/MPT/kiyomi/outfits/casual_rhip.png"
        attribute rup if_any "beach":
            "mod_assets/MPT/kiyomi/outfits/beach_rhip.png"
        
        attribute rhip if_any "uniform":
            "mod_assets/MPT/kiyomi/outfits/uniform_rhip.png"
        attribute rhip if_any "casual":
            "mod_assets/MPT/kiyomi/outfits/casual_rhip.png"
        attribute rhip if_any "beach":
            "mod_assets/MPT/kiyomi/outfits/beach_rhip.png"

    
    group nose:
        attribute nose default if_any(["pani", "worr"]):
            "mod_assets/MPT/kiyomi/nose_b.png"
        attribute nose default if_any(["yand"]):
            "mod_assets/MPT/kiyomi/nose_c.png"
        attribute nose default if_any(["nerv"]):
            "mod_assets/MPT/kiyomi/nose_d.png"

        attribute na null                  # no blush
        attribute nb:
            "mod_assets/MPT/kiyomi/nose_b.png"     # sweat drop
        attribute nc:
            "mod_assets/MPT/kiyomi/nose_c.png"     # blush
        attribute nd:
            "mod_assets/MPT/kiyomi/nose_d.png"     # blush + sweat drop


    group eyes:
        attribute oe default if_any(["anno", "curi", "happ", "laug", "neut", "sad", "worr"]):
            "mod_assets/MPT/kiyomi/eyes_a.png"
        attribute oe default if_any(["dist", "doub", "flus", "nerv"]):
            "mod_assets/MPT/kiyomi/eyes_b.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/kiyomi/eyes_c.png"
        attribute oe default if_any(["angr", "surp", "vang"]):
            "mod_assets/MPT/kiyomi/eyes_d.png"
        attribute oe default if_any(["hold"]):
            "mod_assets/MPT/kiyomi/eyes_e.png"
        attribute oe default if_any(["pani", "yand"]):
            "mod_assets/MPT/kiyomi/eyes_i.png"

        attribute ce if_any(["happ", "laug", "yand"]):
            "mod_assets/MPT/kiyomi/eyes_f.png"
        attribute ce if_any(["angr", "anno", "curi", "dist", "doub", "flus", "nerv", "neut", "pani", "sad", "surp", "vang", "worr"]):
            "mod_assets/MPT/kiyomi/eyes_g.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/kiyomi/eyes_h.png"

        attribute ea:
            "mod_assets/MPT/kiyomi/eyes_a.png"     # neutral
        attribute eb:
            "mod_assets/MPT/kiyomi/eyes_b.png"     # looking left
        attribute ec:
            "mod_assets/MPT/kiyomi/eyes_c.png"     # crying
        attribute ed:
            "mod_assets/MPT/kiyomi/eyes_d.png"     # surprised
        attribute ee:
            "mod_assets/MPT/kiyomi/eyes_e.png"     # surprised + crying
        attribute ef:
            "mod_assets/MPT/kiyomi/eyes_f.png"     # closed + happy
        attribute eg:
            "mod_assets/MPT/kiyomi/eyes_g.png"     # closed
        attribute eh:
            "mod_assets/MPT/kiyomi/eyes_h.png"     # closed + crying
        attribute ei:
            "mod_assets/MPT/kiyomi/eyes_i.png"     # crazy
        attribute ej:
            "mod_assets/MPT/kiyomi/eyes_j.png"     # happy wink
        attribute ek:
            "mod_assets/MPT/kiyomi/eyes_k.png"     # wink
        
    group eyebrows:
        attribute brow default if_any(["dist", "happ", "laug", "neut", "pani", "surp", "yand"]):
            "mod_assets/MPT/kiyomi/eyebrows_a.png"
        attribute brow default if_any(["cry", "flus", "sad", "nerv", "worr"]):
            "mod_assets/MPT/kiyomi/eyebrows_b.png"
        attribute brow default if_any(["angr", "anno", "vang"]):
            "mod_assets/MPT/kiyomi/eyebrows_c.png"
        attribute brow default if_any(["curi", "doub"]):
            "mod_assets/MPT/kiyomi/eyebrows_d.png"

        attribute ba:
            "mod_assets/MPT/kiyomi/eyebrows_a.png" # neutral
        attribute bb:
            "mod_assets/MPT/kiyomi/eyebrows_b.png" # sad / worried
        attribute bc:
            "mod_assets/MPT/kiyomi/eyebrows_c.png" # mad
        attribute bd:
            "mod_assets/MPT/kiyomi/eyebrows_d.png" # curi
        
    group mouths:
        attribute cm default if_any(["happ", "nerv"]):
            "mod_assets/MPT/kiyomi/mouth_a.png"
        attribute cm default if_any(["laug", "yand"]):
            "mod_assets/MPT/kiyomi/mouth_c.png"
        attribute cm default if_any(["angr", "anno", "cry", "dist", "flus", "neut", "sad"]):
            "mod_assets/MPT/kiyomi/mouth_d.png"
        attribute cm default if_any(["curi", "doub", "pani", "surp", "worr"]):
            "mod_assets/MPT/kiyomi/mouth_e.png"
        attribute cm default if_any(["vang"]):
            "mod_assets/MPT/kiyomi/mouth_h.png"

        attribute om if_any(["happ", "nerv"]):
            "mod_assets/MPT/kiyomi/mouth_b.png"
        attribute om if_any(["angr", "cry"]):
            "mod_assets/MPT/kiyomi/mouth_f.png"
        attribute om if_any(["anno", "curi", "dist", "doub", "flus", "neut", "sad", "surp", "worr"]):
            "mod_assets/MPT/kiyomi/mouth_g.png"
        attribute om if_any(["pani", "vang"]):
            "mod_assets/MPT/kiyomi/mouth_i.png"
        attribute om if_any(["laug", "yand"]):
            "mod_assets/MPT/kiyomi/mouth_j.png"


        attribute ma:
            "mod_assets/MPT/kiyomi/mouth_a.png"    # happy
        attribute mb:
            "mod_assets/MPT/kiyomi/mouth_b.png"    # talking + happy
        attribute mc:
            "mod_assets/MPT/kiyomi/mouth_c.png"    # troll face smile
        attribute md:
            "mod_assets/MPT/kiyomi/mouth_d.png"    # closed / neutral
        attribute me:
            "mod_assets/MPT/kiyomi/mouth_e.png"    # slightly opened
        attribute mf:
            "mod_assets/MPT/kiyomi/mouth_f.png"    # talking + neutral
        attribute mg:
            "mod_assets/MPT/kiyomi/mouth_g.png"    # wide open (surprised?)
        attribute mh:
            "mod_assets/MPT/kiyomi/mouth_h.png"    # showing teeth (mad?)
        attribute mi:
            "mod_assets/MPT/kiyomi/mouth_i.png"    # crazy
        attribute mj:
            "mod_assets/MPT/kiyomi/mouth_j.png"    # laugh
        

init python:
    #Layered image refreshes
    def kiyoref(target="master"):
        if not "kiyomi" in renpy.get_showing_tags(layer=target, sort=True):
            #If not currently showing this sprite, stop function.
            return
        pose = str(renpy.get_attributes("kiyomi",layer=target)[0])
        if pose == "":
            #Nope out if there's no actual pose here.
            return
        renpy.show("kiyomi " + pose + " refreshattribute",layer=target)
        renpy.show("kiyomi",layer=target)  
