# utils.rpy
init python:
    def set_hero_portrait_mood(mood="neutral"):
        if not remembered_self:
            renpy.store.hero_portrait = "hero shadow"
        else:
            prefix = "hero m" if player_gender == "male" else "hero f"
            renpy.store.hero_portrait = f"{prefix} {mood}"
