label corridor:
    scene bg corridor at fullscreen_bg
    hide window
    hide screen quick_menu
    call screen corridor_map
    show window
    show screen quick_menu
    return

screen corridor_map():
    modal True
    zorder 100
    add "bg corridor" at fullscreen_bg

    # 1) Locked door
    if highlight_zones:
        frame:
            xpos 1330 ypos 350
            xsize 100 ysize 250
            background Solid("#ff00ffaa")
    imagebutton:
        idle "gui/transparent.png"
        hover "gui/transparent.png"
        xpos 1330 ypos 350
        xsize 100 ysize 250
        mouse "hover"
        action Jump("door_locked")

    # 2) Return to compartment
    if highlight_zones:
        frame:
            xalign 1.0 yalign 0.5 xsize 150 ysize 1400
            background Solid("#00ff37aa")
    imagebutton:
        idle "gui/transparent.png"
        hover "gui/transparent.png"
        xalign 1.0 yalign 0.5 xsize 150 ysize 1400
        mouse "hover"
        action Jump("coupe_return")

    # 3) Empty door (one-time)
    if not explored_empty_door:
        if highlight_zones:
            frame:
                xpos 1550 yalign 0.5 xsize 100 ysize 1500
                background Solid("#eeff00a1")
        imagebutton:
            idle "gui/transparent.png"
            hover "gui/transparent.png"
            xpos 1550 yalign 0.5 xsize 100 ysize 1500
            mouse "hover"
            action Jump("corridor_empty")

    # 4) Window (one-time)
    if not explored_window:
        if highlight_zones:
            frame:
                xalign 1 yalign 0.5 xsize 800 ysize 1000
                background Solid("#ffbb00aa")
        imagebutton:
            idle "gui/transparent.png"
            hover "gui/transparent.png"
            xalign 1 yalign 0.5 xsize 800 ysize 1000
            action Jump("corridor_window")
            mouse "hover"

    # 5) Compartment door (always accessible)
    if highlight_zones:
        frame:
            xpos 1475 yalign 0.5 xsize 50 ysize 1400
            background Solid("#0026ffaa")
    imagebutton:
        idle "gui/transparent.png"
        hover "gui/transparent.png"
        xpos 1475 yalign 0.5 xsize 50 ysize 1400
        action Jump("door_memory_check")
        mouse "hover"

# Responses for doors/windows
label door_locked:
    hide screen corridor_map
    play sound audio.sfx_fail
    g "The door is locked... I can't get through."
    g "Why is it even here, if I can't open it?"
    g "Am I not supposed to go this way yet?"
    g "…Or ever?"
    jump corridor


label coupe_return:
    hide screen corridor_map
    play sound audio.sfx_click
    scene bg coupe_start at fullscreen_bg
    with fade
    g "I should head back to my compartment."
    hide window
    hide screen quick_menu
    call screen cabin
    show window
    show screen quick_menu
    return

label corridor_empty:
    hide screen corridor_map
    play sound audio.sfx_knock
    $ explored_empty_door = True
    g "This door has no label."
    g "I knock... but nothing happens."
    g "No sounds. No movement. Not even silence that feels alive."
    g "Just... absence."
    g "Whatever was here, maybe it’s long gone."
    jump corridor

label corridor_window:
    hide screen corridor_map
    play sound audio.sfx_fail
    $ explored_window = True
    g "I peer out the window."
    g "It's pitch black outside."
    g "Only the blur of trees, lights, and endless dark."
    g "The train speeds forward, but to where?"
    g "I don’t even know what I’m hoping to see."
    g "It feels like the outside world is slipping further away."
    jump corridor