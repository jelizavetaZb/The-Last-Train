define g = Character(None, what_prefix="“", what_suffix="”", window_left_padding=160)
define guide = Character(None, what_prefix="“", what_suffix="”", window_left_padding=160)
define companion = Character(None, what_prefix="“", what_suffix="”", window_left_padding=160)
label start:
    scene black with fade
    $ hero_portrait = "hero shadow"
    $ g = Character(player_name, what_prefix="“", what_suffix="”", window_left_padding=160)
    $ guide = Character(guide_name, what_prefix="“", what_suffix="”", window_left_padding=160)
    $ companion = Character(companion_name, what_prefix="“", what_suffix="”", window_left_padding=160)

    g "..."
    g "Where... am I?"
    g "What is this place?"
    g "Why can't I remember how I got here?"
    play music audio.bg_train fadein 1.5
    g "A sound... something's moving..."
    scene bg coupe_start at fullscreen_bg
    with fade
    g "A compartment. I'm... on a train?"
    g "I should look around. Maybe something here will help."

    $ mirror_active = True
    hide window
    hide screen quick_menu
    call screen cabin
    show window
    show screen quick_menu
    return
