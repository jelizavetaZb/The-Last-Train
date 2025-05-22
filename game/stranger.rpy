label coupe_open:
    hide window
    hide screen quick_menu
    play sound audio.sfx_knock
    pause 0.5
    scene bg coupe_open at fullscreen_bg
    with fade
    play sound audio.sfx_door

    if not remembered_self:
        show stranger hidden at hero_portrait_small 
        g "You still don't remember who you are? Get out of my way."
        hide stranger hidden
        jump corridor

    # Memory branch
    show stranger hidden at hero_portrait_small
    g "..."
    pause 0.5
    g "Who are you? What's going on?"
    play sound audio.sfx_click

    companion "I'm not the answer. And not your enemy."
    companion "Just one of those who stayed. Who chose not to step out."
    pause 0.5

    g "So you're here by choice?"
    companion "Once — maybe. Now... it doesn't matter anymore."
    companion "You think you're choosing. But the train moves on its own."

    pause 0.5
    g "Why am I here?"

    companion "Sometimes, to remember."
    companion "Sometimes, to forget."
    companion "You feel it already — something important. Beneath your skin. Beneath the fear."

    pause 0.5
    g "Then what should I do?"

    companion "Listen. Look. And walk — even if you're unsure."
    companion "When the door opens, the choice will be yours. Not for me. Not for anyone. Just for you."

    menu:
        "Stay. Hear him out a little longer.":
            $ trusted_stranger = True
            jump trust_companion
        "Step away. Leave it all behind.":
            $ trusted_stranger = False
            jump distrust_companion

label trust_companion:
    hide stranger hidden
    show stranger visible at hero_portrait_small
    play sound audio.sfx_click
    stop music fadeout 1.0
    play sound audio.sfx_arrive
    play music audio.bg_empty fadein 1.0 loop

    g "I hear the brakes... the train is slowing."
    pause 1.0

    companion "You've made a step. Doesn't matter where — what matters is you didn't turn away."
    companion "You won’t find the truth here. But maybe... it’ll find you up ahead."

    hide stranger visible
    pause 0.5
    g "Whatever lies ahead — I need to face it."
    jump corridor_open

label distrust_companion:
    play sound audio.sfx_fail
    companion "So you're not ready yet."
    companion "That's not a fault. Time is different for each of us."

    hide companion hidden
    stop music fadeout 0.5
    play music audio.bg_empty fadein 1.0 loop
    with fade

    g "He shuts the door... I'm alone again."
    pause 1

    hide window
    hide screen quick_menu
    scene bg corridor at fullscreen_bg
    with fade
    pause 1
    scene bg coupe_start at fullscreen_bg
    with fade
    pause 1

    g "And still... what if I was wrong?"
    jump bad_ending_sleep

label door_memory_check:
    hide screen corridor_map
    play sound audio.sfx_click
    jump coupe_open

