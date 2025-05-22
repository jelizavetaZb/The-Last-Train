# game/stranger.rpy:18
translate russian coupe_open_3bccc841:

    # g "You still don't remember who you are? Get out of my way."
    g "Ты всё ещё не помнишь, кто ты? Убирайся с дороги."

# game/stranger.rpy:20
translate russian coupe_open_143508f7:

    # g "Who are you? What's going on?"
    g "Кто ты? Что происходит?"

# game/stranger.rpy:23
translate russian coupe_open_4b340443:

    # g "..."
    g "..."

# game/stranger.rpy:23
translate russian coupe_open_9545f8fb:

    # companion "I'm not the answer. And not your enemy."
    companion "Я — не ответ. И не враг твой."

# game/stranger.rpy:24
translate russian coupe_open_45ab86a0:

    # companion "Just one of those who stayed. Who chose not to step out."
    companion "Всего лишь один из тех, кто остался. Кто не сделал шаг вперёд."

# game/stranger.rpy:25
translate russian coupe_open_b50bae88:

    # g "Who are you, and what's happening here?"
    g "Кто ты? И что здесь происходит?"

# game/stranger.rpy:27
translate russian coupe_open_041e657f:

    # g "So you're here by choice?"
    g "Значит, ты здесь по собственной воле?"

# game/stranger.rpy:28
translate russian coupe_open_b025f031:

    # companion "Once — maybe. Now... it doesn't matter anymore."
    companion "Когда-то — возможно. Сейчас... это уже не важно."

# game/stranger.rpy:29
translate russian coupe_open_63096460:

    # companion "You think you're choosing. But the train moves on its own."
    companion "Ты думаешь, что выбираешь. Но поезд идёт сам по себе."

# game/stranger.rpy:30
translate russian coupe_open_7f67283f:

    # g "Why should I trust you?"
    g "Почему я должен тебе доверять?"

# game/stranger.rpy:32
translate russian coupe_open_9eedb480:

    # g "Why am I here?"
    g "Почему я здесь?"

# game/stranger.rpy:32
translate russian coupe_open_07a68550:

    # companion "Because none of us asked to board this train of passing souls."
    companion "Потому что никто из нас не просил садиться в этот поезд блуждающих душ."

# game/stranger.rpy:34
translate russian coupe_open_d953173e:

    # companion "Sometimes, to remember."
    companion "Иногда — чтобы вспомнить."

# game/stranger.rpy:35
translate russian coupe_open_5788985f:

    # companion "Sometimes, to forget."
    companion "Иногда — чтобы забыть."

# game/stranger.rpy:36
translate russian coupe_open_0375ab51:

    # companion "You feel it already — something important. Beneath your skin. Beneath the fear."
    companion "Ты уже чувствуешь — что-то важное. Под кожей. Под страхом."

# game/stranger.rpy:34
translate russian coupe_open_28c63d61:

    # g "What should I do now?"
    g "Что мне теперь делать?"

# game/stranger.rpy:39
translate russian coupe_open_5d4bf40f:

    # g "Then what should I do?"
    g "Тогда что мне делать?"

# game/stranger.rpy:41
translate russian coupe_open_cab237ca:

    # companion "Listen. Look. And walk — even if you're unsure."
    companion "Слушай. Смотри. И иди — даже если не уверен."

# game/stranger.rpy:42
translate russian coupe_open_73677470:

    # companion "When the door opens, the choice will be yours. Not for me. Not for anyone. Just for you."
    companion "Когда откроется дверь, выбор будет за тобой. Не за мной. Не за кем-то. Только за тобой."

# game/stranger.rpy:36
translate russian coupe_open_d9ee782e:

    # companion "After we part ways, the train will stop, and the door to the vestibule will open."
    companion "Когда мы расстанемся, поезд остановится, и откроется дверь в тамбур."

# game/stranger.rpy:44
translate russian strings:

    old "Stay. Hear him out a little longer."
    new "Остаться. Выслушать его чуть дольше."

    old "Step away. Leave it all behind."
    new "Отойти. Оставить всё позади."

    old "Trust the companion"
    new "Довериться страннику"

    old "Don't trust him"
    new "Не доверять ему"

# game/stranger.rpy:52
translate russian trust_companion_851824f6:

    # g "I hear the brakes... the train is slowing."
    g "Я слышу тормоза... поезд замедляется."

# game/stranger.rpy:63
translate russian trust_companion_ff74db94:

    # companion "You've made a step. Doesn't matter where — what matters is you didn't turn away."
    companion "Ты сделал шаг. Не важно, куда — важно, что ты не отвернулся."

# game/stranger.rpy:64
translate russian trust_companion_99f26312:

    # companion "You won’t find the truth here. But maybe... it’ll find you up ahead."
    companion "Ты не найдёшь истину здесь. Но, возможно... она найдёт тебя дальше."

# game/stranger.rpy:68
translate russian trust_companion_2b33a42f:

    # g "Whatever lies ahead — I need to face it."
    $ face_it = "должен это пройти" if player_gender != "female" else "должна это пройти"
    g "Что бы ни ждало впереди — я [face_it]."

# game/stranger.rpy:58
translate russian distrust_companion_6d9c7d46:

    # companion "Rest... you need to gather strength."
    companion "Отдохни... тебе нужно набраться сил."

# game/stranger.rpy:73
translate russian distrust_companion_d864d057:

    # companion "So you're not ready yet."
    companion "Значит, ты пока не готов."

# game/stranger.rpy:74
translate russian distrust_companion_6b7ee836:

    # companion "That's not a fault. Time is different for each of us."
    companion "Это не ошибка. Время у каждого своё."

# game/stranger.rpy:81
translate russian distrust_companion_4cf111d5:

    # g "He shuts the door... I'm alone again."
    $ alone = "один" if player_gender != "female" else "одна"
    g "Он закрывает дверь... и я снова [alone]."

# game/stranger.rpy:93
translate russian distrust_companion_ea90779b:

    # g "And still... what if I was wrong?"
    $ wrong = "ошибся" if player_gender != "female" else "ошиблась"
    g "И всё же... а вдруг я [wrong]?"
