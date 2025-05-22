# TODO: Translation updated at 2025-05-18 16:33

# game/car_gap.rpy:6
translate russian car_gap_f9168f6d:
    g "Дверь на платформу открыта. Я могу выйти."

# game/car_gap.rpy:54
translate russian car_gap_return_choice_b2457a64:
    g "Это дверь обратно в моё купе."

# game/car_gap.rpy:55
translate russian car_gap_return_choice_7561ec10:
    g "Часть меня хочет вернуться. Лечь. Отдохнуть."

# game/car_gap.rpy:56
translate russian car_gap_return_choice_b65020a0:
    g "Но с каждым шагом вперёд становится всё тяжелее."

# game/car_gap.rpy:63
translate russian car_gap_return_choice_293e12b7:
    g "Нет. Я уже зашёл слишком далеко."

# game/car_gap.rpy:69
translate russian car_gap_bad_end_504d8609:
    g "Я поворачиваюсь назад. Дверь захлопывается за мной с металлическим щелчком."

# game/car_gap.rpy:73
translate russian car_gap_bad_end_62a81af0:
    g "Слишком поздно передумать."

# game/car_gap.rpy:76
translate russian car_gap_bad_end_61187360:
    g "Дверь позади меня окончательно закрывается."

# game/car_gap.rpy:78
translate russian car_gap_bad_end_4db03613:
    g "Поезд снова начинает движение."

# game/car_gap.rpy:82
translate russian car_gap_bad_end_2474b417:
    g "Я иду обратно через пустой коридор."

# game/car_gap.rpy:85
translate russian car_gap_bad_end_62bb4540:
    g "Кровать здесь. Она ждала."

# game/car_gap.rpy:86
translate russian car_gap_bad_end_a207c2c4:
    $ tired = "устал" if player_gender != "female" else "устала"
    g "И я так [tired]."


# game/car_gap.rpy:91
translate russian car_gap_exit_choice_df3341de:
    g "В проёме двери я вижу станцию."

# game/car_gap.rpy:92
translate russian car_gap_exit_choice_ddbd3e9a:
    g "Пустые платформы. Холодный, серый свет. Ни людей, ни движения."

# game/car_gap.rpy:94
translate russian car_gap_exit_choice_338060ba:
    g "Рельсы тянутся в бесконечность."

# game/car_gap.rpy:99
translate russian car_gap_exit_choice_72d12346:
    g "Пока нет. Это ещё не конец."

# game/car_gap.rpy:105
translate russian car_gap_forward_choice_ffa0ef00:
    g "Тяжёлая металлическая дверь. Наверное, ведёт в следующий вагон."

# game/car_gap.rpy:106
translate russian car_gap_forward_choice_ebebb373:
    g "Я могу попробовать… но чувствую, что будет непросто."

# game/car_gap.rpy:110
translate russian car_gap_forward_choice_b8074fc5:
    g "Моя рука дрожит, но я иду вперёд."

# game/car_gap.rpy:111
translate russian car_gap_forward_choice_1e349cef:
    $ must_face = "должен" if player_gender != "female" else "должна"
    g "Что бы ни ждало впереди — я [must_face] это пройти."


# game/car_gap.rpy:115
translate russian car_gap_forward_choice_f84af02f:
    g "Пока нет. Не этим путём."

translate russian strings:

    # game/car_gap.rpy:57
    old "Return to rest"
    new "Вернуться и отдохнуть"

    # game/car_gap.rpy:57
    old "Stay in the vestibule"
    new "Остаться в тамбуре"

    # game/car_gap.rpy:95
    old "Step off the train"
    new "Сойти с поезда"

    # game/car_gap.rpy:95
    old "Stay aboard"
    new "Остаться"

    # game/car_gap.rpy:108
    old "Open the door"
    new "Открыть дверь"

    # game/car_gap.rpy:108
    old "Don’t open it"
    new "Не открывать"
