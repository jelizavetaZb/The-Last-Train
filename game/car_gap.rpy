label car_gap:
    scene bg car_gap at fullscreen_bg
    with fade
    play music audio.bg_empty fadein 1.0 loop
    $ set_hero_portrait_mood("neutral")
    g "The door to the station is open. I could step out."
    play sound audio.sfx_door

    call screen car_gap_map
    return

screen car_gap_map():
    modal True
    zorder 100
    add "bg car_gap" at fullscreen_bg

    # 1) Return to compartment
    if highlight_zones:
        frame:
            xalign 0.0 yalign 0.5 xsize 400 ysize 1400
            background Solid("#00ff37aa")
    imagebutton:
        idle "gui/transparent.png" hover "gui/transparent.png"
        xalign 0.0 yalign 0.5 xsize 400 ysize 1400
        mouse "hover"
        action Jump("car_gap_return_choice")

    # 2) Exit to platform
    if highlight_zones:
        frame:
            xpos 700 yalign 0.5 xsize 500 ysize 1400
            background Solid("#ffbb00aa")
    imagebutton:
        idle "gui/transparent.png" hover "gui/transparent.png"
        xpos 700 yalign 0.5 xsize 500 ysize 1400
        mouse "hover"
        action Jump("car_gap_exit_choice")

    # 3) Proceed forward
    if highlight_zones:
        frame:
            xalign 1.0 yalign 0.5 xsize 500 ysize 1400
            background Solid("#ff00ffaa")
    imagebutton:
        idle "gui/transparent.png" hover "gui/transparent.png"
        xpos 1300 ypos 300 xsize 200 ysize 600
        mouse "hover"
        action Jump("car_gap_forward_choice")

label car_gap_return_choice:
    stop music fadeout 0.5
    play music audio.bg_heartbeat fadein 0.5
    $ set_hero_portrait_mood("worried")
    g "That's the door back to my compartment."
    g "Some part of me wants to go back. Lie down. Rest."
    g "But each step forward feels harder than the last."
    menu:
        "Return to rest":
            jump car_gap_bad_end
        "Stay in the vestibule":
            stop music fadeout 0.5
            play music audio.bg_empty fadein 0.5
            g "No. I’ve made it this far."
            call screen car_gap_map
            return

label car_gap_bad_end:
    $ set_hero_portrait_mood("sad")
    g "I turn back. The door closes behind me with a metallic snap."
    play sound audio.sfx_fail
    scene bg car_gap at fullscreen_bg
    with fade
    g "Too late to change my mind."
    scene bg corridor_open at fullscreen_bg
    with fade
    g "The door behind me seals shut with finality."
    play sound audio.sfx_depart
    g "The train begins to move again."
    pause 1.5
    scene bg corridor at fullscreen_bg
    with fade
    g "I make my way back through the empty hallway."
    scene bg coupe_start at fullscreen_bg
    with fade
    g "The bed is here. Waiting."
    g "And I’m so tired."
    jump bad_ending_sleep

label car_gap_exit_choice:
    $ set_hero_portrait_mood("sad")
    g "Through the doorway, I see the station."
    g "Empty platforms. Cold, grey light. No people. No movement."
    play sound audio.sfx_fail
    g "The tracks stretch into forever."
    menu:
        "Step off the train":
            jump ending_leave_train
        "Stay aboard":
            g "Not yet. This isn’t where I stop."
            call screen car_gap_map
            return

label car_gap_forward_choice:
    $ set_hero_portrait_mood("worried")
    g "A heavy metal door. Probably leads to the next car."
    g "I could try it... but something tells me it won't be easy."
    play sound audio.sfx_door
    menu:
        "Open the door":
            g "My hand trembles, but I push forward."
            g "Whatever’s next, I have to face it."
            play sound audio.sfx_click
            jump empty_wagon_1  # Replace with your actual next label
        "Don’t open it":
            g "Not yet. Not this way."
            call screen car_gap_bad_end
            return
