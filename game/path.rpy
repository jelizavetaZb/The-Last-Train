label empty_wagon_1:
    $ wagon_stage = 1
    scene bg empty1 at fullscreen_bg
    with fade
    $ set_hero_portrait_mood("worried")
    g "I pass through the metal door and step into another car."
    g "Seats. Windows. Nothing out of place, yet..."
    g "A strange tension crawls under my skin."
    g "Something's off, but I can’t explain it."
    jump unified_gap

label empty_wagon_2:
    $ wagon_stage = 2
    scene bg empty2 at fullscreen_bg
    with fade
    $ set_hero_portrait_mood("worried")
    play sound audio.sfx_fail
    g "It's the same layout, but darker."
    g "No lights. Just shadows. And cold."
    g "My breath fogs in the air. Goosebumps rise across my arms."
    g "Why do I feel like something’s watching me?"
    jump unified_gap

label empty_wagon_3:
    $ wagon_stage = 3
    scene bg empty3 at fullscreen_bg
    with fade
    $ set_hero_portrait_mood("worried")
    g "It’s foggy in here. Everything is distorted."
    g "One of the seats is overturned. I stumble into it."
    play sound audio.sfx_knock
    g "This doesn’t feel real anymore."
    g "I’ve lost the thread of reality."
    g "Up ahead... a narrow door. That must be the engine."
    menu:
        "Reach the front":
            g "No more turning back. No more doubts."
            jump final_train_scene  # Replace with your true ending
        "Give up":
            g "I can’t. I just... can’t."
            jump empty_car_gap_bad_end

label unified_gap:
    scene bg car_gap at fullscreen_bg
    with fade
    $ set_hero_portrait_mood("neutral")
    g "Another car gap. Same three doors."
    call screen unified_gap_map
    return

screen unified_gap_map():
    modal True
    zorder 100
    add "bg car_gap" at fullscreen_bg

    if highlight_zones:
        frame:
            xalign 0.0 yalign 0.5 xsize 400 ysize 1400
            background Solid("#00ff37aa")
    imagebutton:
        idle "gui/transparent.png" hover "gui/transparent.png"
        xalign 0.0 yalign 0.5 xsize 400 ysize 1400
        mouse "hover"
        action Jump("gap_return_choice")

    if highlight_zones and wagon_stage < 3:
        frame:
            xpos 700 yalign 0.5 xsize 500 ysize 1400
            background Solid("#ffbb00aa")
        imagebutton:
            idle "gui/transparent.png" hover "gui/transparent.png"
            xpos 700 yalign 0.5 xsize 500 ysize 1400
            mouse "hover"
            action Jump("car_gap_exit_choice")

    if highlight_zones:
        frame:
            xalign 1.0 yalign 0.5 xsize 500 ysize 1400
            background Solid("#ff00ffaa")
    imagebutton:
        idle "gui/transparent.png" hover "gui/transparent.png"
        xalign 1.0 yalign 0.5 xsize 500 ysize 1400
        mouse "hover"
        action Jump("empty_wagon_" + str(wagon_stage + 1))

label gap_return_choice:
    $ set_hero_portrait_mood("sad")
    if wagon_stage == 3:
        g "There's nothing behind me anymore. Just shadows."
    elif wagon_stage == 2:
        g "I’d have to pass that cold, dead car again."
    elif wagon_stage == 1:
        g "If I go back, I’ll have to cross that strange car again."
    else:
        g "And behind that... just rest."
    menu:
        "Return and rest":
            if wagon_stage == 3:
                scene bg empty3 at fullscreen_bg
            elif wagon_stage == 2:
                scene bg empty2 at fullscreen_bg
            elif wagon_stage == 1:
                scene bg empty1 at fullscreen_bg
            else:
                scene bg car_gap at fullscreen_bg
            with fade
            g "I retrace my steps."
            jump empty_car_gap_bad_end
        "Stay in the vestibule":
            g "No. Not yet."
            call screen unified_gap_map
            return

label empty_car_gap_bad_end:
    $ set_hero_portrait_mood("sad")

    if wagon_stage >= 3:
        scene bg empty3 at fullscreen_bg
        with fade
        g "I turn around, dragging my feet through the fog."
        g "It clings to me like memory — cold, shapeless, unwanted."

    if wagon_stage >= 2:
        scene bg empty2 at fullscreen_bg
        with fade
        g "The lights are still dead."
        g "The cold still breathes on my neck."
        play sound audio.sfx_fail
        g "Every step echoes like a mistake I can’t take back."

    if wagon_stage >= 1:
        scene bg empty1 at fullscreen_bg
        with fade
        g "The silence here is louder than before."
        g "As if even the shadows are tired of me now."

    scene bg corridor_open at fullscreen_bg
    with fade
    g "There it is... the corridor."
    g "The door behind me seals shut with finality."
    play sound audio.sfx_fail
    pause 0.3
    play sound audio.sfx_depart
    g "And just like that — the train begins to move again."
    pause 1.5

    scene bg corridor at fullscreen_bg
    with fade
    g "No whispers. No wind. Just me and my regret."
    g "I walk the same path as before, but now it feels like the end."

    scene bg coupe_start at fullscreen_bg
    with fade
    g "The bed is here. Still untouched. Still waiting."
    g "Like it always knew I’d come back."
    g "And I’m... so tired."

    jump bad_ending_sleep