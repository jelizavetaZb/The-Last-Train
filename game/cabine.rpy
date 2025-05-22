screen cabin():
    modal True
    zorder 100

    add "bg coupe_start" at fullscreen_bg

    # mirror
    if mirror_active:
        if highlight_zones:
            frame:
                ypos 600 xpos 1240
                xsize 150 ysize 260
                background Solid("#f00a") 
        imagebutton:
            idle "gui/transparent.png"
            hover "gui/transparent.png"
            ypos 600 xpos 1240
            xsize 150 ysize 260
            action [Play("sound", audio.sfx_mirror), Jump("mirror_choice")]
            mouse "hover"

    # window
    if highlight_zones:
        frame:
            ypos 300 xpos 800
            xsize 400 ysize 400
            background  Solid("#1100ffaa")  
    imagebutton:
        idle  "gui/transparent.png"
        hover "gui/transparent.png"
        ypos 300 xpos 800
        xsize 400 ysize 400
        action Jump("window_view")
        mouse "hover"

    # bed
    if highlight_zones:
        frame:
            ypos 700 xpos 0
            xsize 900 ysize 500
            background Solid("#0f0a") 
    imagebutton:
        idle  "gui/transparent.png"
        hover "gui/transparent.png"
        ypos  700 xpos 0
        xsize 900  ysize 500
        action Jump("bed_choice")
        mouse "hover"

label mirror_choice:
    hide screen cabin
    $ _window_show()
    menu:
        "Look into the mirror":
            $ mirror_active = False
            $ remembered_self = True
            $ tmp_name = renpy.input(your_name).strip()
            if tmp_name == "":
                $ tmp_name = "Passenger"
            $ player_name = tmp_name

            g "You stare into the mirror..."
            g "The glass doesn't just reflect. It looks back."
            g "This is more than a reflection. It's... recognition."
            menu:
                "Male":
                    $ player_gender = "male"
                    $ hero_portrait = "hero m neutral"
                "Female":
                    $ player_gender = "female"
                    $ hero_portrait = "hero f neutral"  
            $ g = Character(player_name, what_prefix="“", what_suffix="”", window_left_padding=160)                
            g "I... remember. My name is [player_name]."
            g "It doesn't make sense yet, but it’s mine."

        "Step away from it":
            g "I decide not to look. Some things are better left unknown."
            g "What if I hate what I see?"
            g "What if I don't see anything at all?"
    hide window
    hide screen quick_menu
    call screen cabin
    return

label window_view:
    hide screen cabin
    $ _window_show()
    g "The train roars on, rattling and shaking..."
    g "But outside it's too dark to see a thing."
    g "Like we’re slicing through a void, not a landscape."
    g "Wherever we're going — it’s not a place on any map."
    hide window
    hide screen quick_menu
    call screen cabin
    return

label bed_choice:
    hide screen cabin
    $ _window_show()
    menu:
        "Explore the train":
            g "I decide to get up and explore the rest of the train."
            g "Anything’s better than lying here, waiting for nothing."
            jump corridor

        "Go to sleep":
            g "I give in to exhaustion and lie down..."
            g "Maybe when I wake up, everything will make sense."
            g "Or maybe I won’t wake up at all."
            jump bad_ending_sleep

        "Continue exploring the cabin":
            g "I’m not ready to leave yet."
            g "There has to be more — something I missed."
            hide window
            hide screen quick_menu
            call screen cabin
    return
