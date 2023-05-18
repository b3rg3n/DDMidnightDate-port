# ----------------------------------------------------------------------------------------------------------------------------------+
#                                                                                                                                   |
#                                               Expression/Pose Sequencing Tool                                                     |
#                                                                                                                                   |
# ----------------------------------------------------------------------------------------------------------------------------------+


# With this tool, you can make characters change expressions in the middle of a sentence with ease.


# To see sequencing in action, here are some examples before you dive into the tool's code.
# Just call this label to see what expression sequencing would look like.
label xps_tool_example:
    scene bg club_day
    "The examples begin now."
    
    show monika 1g at t11
    $ pause(1)
    python:
        _set_sq(
        "m",
        0,
        "monika 1g",    # <-- in this example, the expression `monika 1g` is sustained for 0.75 second before we move to the next expression
        0.75,           # <-- this is how long `monika 1g` is sustained
        "monika 2m",    # <-- the next expression is `monika 3m` sustained for 0.5 second
        0.5,            # <-- how long `monika 2m` is sustained
        "monika 2e"
        )
    show monika sq
    "Here is an example of expression sequence using vanilla expressions."
    
    "Next, we will use MPT expressions (will probably throw an error if you don't have MPT installed)."
    
    show sayori turned happ at t33
    $ pause(1)
    python:
        _set_sq(
        "s",
        0,              # <-- the first 0 in the sequence is not how long an expression is sustained, but how many times the sequence repeats
        "sayori turned happ om ce lup",
        0.25,
        "sayori turned happ om ce rup",
        0.25,
        "sayori turned happ om ce lup",
        0.25,
        "sayori turned happ om ce rup",
        0.25,
        "sayori turned happ om ce lup"
        )
    show sayori sq
    "Sayori's expression sequence is shown using MPT here."
    
    show sayori turned happ
    "The same result of sequence can be achieved by using a repeating sequence (feel free to look into the label to see how it's done)."
    python:
        _set_sq(
        "s",
        2,              # <-- notice how this sequence will be done twice (putting `None` here will make the sequence repeat infinitely. try it yourself)
        "sayori turned happ om ce lup",
        0.25,
        "sayori turned happ om ce rup",
        0.25,
        "sayori turned happ om ce lup"
        )
    show sayori sq
    "Since Sayori's movement can be expressed as a repeating pattern, we can just repeat those expressions."
    
    "That's pretty much it for the examples."
    "I hope you understand how the tool works better now."
    
    return



# ##############################################            The code            ##############################################


# The _sq Dictionary
# This dictionary's key value pair refers to the characters' sequence expression.
# The dictionary's key is the character name's initial.
# The value would be a list of the expressions you want to use in the sequence.
# You can add keys for your own characters as well, but don't forget to add their sq image definition too.
default _sq = {"m":list(), "s":list(), "y":list(), "n":list(), "k":list(), "h":list(), "a":list()}


# The _set_sq() Function
# This function is used for ease of changing the _sq dictionary so you can freely 
# change what sequence of expressions you want to use.
init python:
    def _set_sq(char, rp=0, *sq):
        """
        INPUT:
            - char  (str["s", "m", "y", "n", "k", "h", "a"])        : The initials of a character to determine which of _sq's key are we modifying.
            - rp    (int, None)                      : Means repeat. Determines how many times the sequence will repeat. Will keep repeating if None.
            - *sq   (str<image names>)               : Is an *args to input however many pose/expression combination you want to use for the character.
        """
        global _sq
        _sq[char] = [var for var in sq]
        _sq[char].insert(0, rp)
        while len(_sq[char]) < 14:
            _sq[char].append(0)


# The sq image tag definitions
# These are the images you would call after changing the sq when you want an expression sequence.
# There are currently 13 rooms for alternating expressions and how long said expression is sustained, 
# but you can always add more on your own (you might need to modify _set_sq() to handle more than 13).
image monika sq:
    _sq["m"][1]
    _sq["m"][2]
    _sq["m"][3]
    _sq["m"][4]
    _sq["m"][5]
    _sq["m"][6]
    _sq["m"][8]
    _sq["m"][7]
    _sq["m"][9]
    _sq["m"][10]
    _sq["m"][11]
    _sq["m"][12]
    _sq["m"][13]
    repeat _sq["m"][0]

image sayori sq:
    _sq["s"][1]#Used
    _sq["s"][2]
    _sq["s"][3]
    _sq["s"][4]
    _sq["s"][5]
    _sq["s"][6]
    _sq["s"][7]
    _sq["s"][8]
    _sq["s"][9]
    _sq["s"][10]
    _sq["s"][11]
    _sq["s"][12]
    _sq["s"][13]
    repeat _sq["s"][0]

image yuri sq:
    _sq["y"][1]#Used
    _sq["y"][2]#Used
    _sq["y"][3]
    _sq["y"][4]
    _sq["y"][5]
    _sq["y"][6]
    _sq["y"][7]
    _sq["y"][8]
    _sq["y"][9]
    _sq["y"][10]
    _sq["y"][11]
    _sq["y"][12]
    _sq["y"][13]
    repeat _sq["y"][0]

image natsuki sq:
    _sq["n"][1]
    _sq["n"][2]
    _sq["n"][3]
    _sq["n"][4]
    _sq["n"][5]
    _sq["n"][6]
    _sq["n"][7]
    _sq["n"][8]
    _sq["n"][9]
    _sq["n"][10]
    _sq["n"][11]
    _sq["n"][12]
    _sq["n"][13]
    repeat _sq["n"][0]

image Kotonoha sq:
    _sq["k"][1]#Used
    _sq["k"][2]#Used
    _sq["k"][3]#Used
    _sq["k"][4]
    _sq["k"][5]
    _sq["k"][6]
    _sq["k"][7]
    _sq["k"][8]
    _sq["k"][9]
    _sq["k"][10]
    _sq["k"][11]
    _sq["k"][12]
    _sq["k"][13]
    repeat _sq["k"][0]

image Himari sq:
    _sq["h"][1]
    _sq["h"][2]
    _sq["h"][3]
    _sq["h"][4]
    _sq["h"][5]
    _sq["h"][6]
    _sq["h"][7]
    _sq["h"][8]
    _sq["h"][9]
    _sq["h"][10]
    _sq["h"][11]
    _sq["h"][12]
    _sq["h"][13]
    repeat _sq["h"][0]

image Akari sq:
    _sq["a"][1]
    _sq["a"][2]
    _sq["a"][3]
    _sq["a"][4]
    _sq["a"][5]
    _sq["a"][6]
    _sq["a"][7]
    _sq["a"][8]
    _sq["a"][9]
    _sq["a"][10]
    _sq["a"][11]
    _sq["a"][12]
    _sq["a"][13]
    repeat _sq["a"][0]