label final_train_scene:
    play music audio.bg_truth fadein 1.5
    scene bg void_station at fullscreen_bg
    with fade
    $ set_hero_portrait_mood("neutral")
    g "The door opens into a vast space."
    g "No walls. No floor. Just endless black... dotted with mirrors."
    g "They float in the air — hundreds of them. Thousands."
    g "Each one reflects not just me, but others. People I’ve never been."
    g "Different faces. Genders. Ages. Eras."

    play sound audio.sfx_truth
    g "They all stare back. And whisper."
    g "‘[player_name]’, they say. Again and again. My name echoing across nothing."

    g "I walk. The mirrors shift, parting as if they know the way."
    g "The door I came through is gone."
    g "There is only forward."

    show guide neutral at hero_portrait_small
    with fade
    guide "You’ve returned. This cycle was brief."
    guide "But you made it to the end. You always do."

    g "Who are you? What is this place?"

    guide "This is the platform between what was... and what will be."
    guide "Some call it the station of forgetfulness. Others — the gate of return."
    guide "You boarded the train to oblivion, like so many before."

    guide "But unlike most, you kept moving. You remembered what it means to try."
    g "Those mirrors... were they me?"

    guide "All versions of you. Fractures of lives lived and left behind."
    guide "Some long ago. Some yet to come."

    g "Why? Why do I keep coming back?"

    show guide smile at hero_portrait_small
    guide "Because you're not done."
    guide "Not yet."

    g "...And now?"
    guide "Now, you begin again. With all that you've seen, all that you've learned — carried within."

    $ set_hero_portrait_mood("smile")
    g "I remember. I lived."
    g "And I’m ready."

    guide "Then go. The next life waits."
    pause 2.0
    g "...Thank you."
    pause 1.5
    hide guide smile
    scene end 3 at fullscreen_bg
    with Dissolve(2.5)
    pause 6
    return
