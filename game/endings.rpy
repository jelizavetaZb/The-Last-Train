label bad_ending_sleep:
    scene bg с at fullscreen_bg
    with fade
    play music audio.bg_ghost fadein 1.0
    $ set_hero_portrait_mood("sad")

    g "I close my eyes just for a moment…"
    g "But the moment stretches."
    g "Stretches into silence."
    g "Into something that has no end."

    g "No dreams come."
    g "No memories follow."

    g "Only the soft hum of something vast and empty."
    g "Like the world forgot I was ever here."

    g "Sleep claims me..."

    pause 1
    g "And I never wake again."
    scene end 1 at fullscreen_bg
    with Dissolve(2.5)
    pause 6
    return

label ending_leave_train:
    scene bg exit_door at fullscreen_bg
    with fade
    $ set_hero_portrait_mood("worried")
    g "I take a few steps out."
    g "The door slams shut behind me."
    play sound audio.sfx_fail
    g "The train begins to move. Without me."
    play sound audio.sfx_depart
    pause 2
    scene bg white_platform at fullscreen_bg
    with fade
    $ set_hero_portrait_mood("sad")
    g "I wander along the tracks. The world is quiet."
    g "I try to count the days. But time here doesn’t move."
    g "There are no clocks. No people. Just cold and silence."
    g "Like I’ve stepped out of life, but not into death."
    g "A ghost stuck between stations."
    g "The next train never comes."
    g "Still, I wait. I walk. I ache."
    g "And I curse myself for stepping away."
    scene end 2 at fullscreen_bg
    with Dissolve(2.5)
    pause 6
    return