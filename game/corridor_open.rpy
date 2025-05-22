label corridor_open:
    scene bg corridor_open at fullscreen_bg
    hide window
    hide screen quick_menu
    call screen corridor_open_map
    show window
    show screen quick_menu
    return

screen corridor_open_map():
    modal True
    zorder 100
    add "bg corridor_open" at fullscreen_bg

    if highlight_zones:
        frame:
            xalign 1.0 yalign 0.5 xsize 400 ysize 1400
            background Solid("#00ff37aa")
    imagebutton:
        idle "gui/transparent.png" hover "gui/transparent.png"
        xalign 1.0 yalign 0.5 xsize 400 ysize 1400
        mouse "hover"
        action Jump("corridor_open_return_choice")

    if highlight_zones:
        frame:
            xalign 0.0 yalign 0.5 xsize 600 ysize 1400
            background Solid("#ffbb00aa")
    imagebutton:
        idle "gui/transparent.png" hover "gui/transparent.png"
        xalign 0.0 yalign 0.5 xsize 600 ysize 1400
        action Jump("corridor_open_window")
        mouse "hover"

    if highlight_zones:
        frame:
            xpos 1270 ypos 400 xsize 150 ysize 400
            background Solid("#ff00ffaa")
    imagebutton:
        idle "gui/transparent.png" hover "gui/transparent.png"
        xpos 1270 ypos 400 xsize 150 ysize 400
        action Jump("corridor_open_car_gap")
        mouse "hover"

label corridor_open_window:
    hide screen corridor_open_map
    g "The train is silent now. Through the grimy window, you see the station-platform bathed in pale light."
    pause 1
    jump corridor_open

label corridor_open_return_choice:
    hide screen corridor_open_map
    stop music fadeout 0.5
    play music audio.bg_heartbeat fadein 1.0
    g "I’m so tired..."
    g "That door leads back to my compartment."
    g "Maybe I should just go back."
    g "Rest. Forget all this."
    menu:
        "Return and rest":
            jump corridor_open_bad_end
        "Keep going":
            stop music fadeout 0.5
            play music audio.bg_empty fadein 0.5
            g "No. Not now. Not when I'm this close."
            jump corridor_open

label corridor_open_car_gap:
    hide screen corridor_open_map
    g "You step through the open doorway into the gap, heart pounding. New choices await..."
    jump car_gap

label corridor_open_bad_end:
    g "The moment I turn away, the door creaks..."
    g "And shuts behind me with a final sound."
    play sound audio.sfx_fail
    scene bg corridor at fullscreen_bg
    with fade
    pause 1
    g "Locked. Of course it is."
    g "I should’ve known the way back would vanish the second I chose it."
    scene bg coupe_start at fullscreen_bg
    with fade
    pause 1
    g "The bed is cold. Too quiet."
    g "Too easy."
    jump bad_ending_sleep
