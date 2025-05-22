define config.name = _("The Last Train")
define gui.show_name = True
define config.version = "0.1"
define gui.about = _p("""""")
define build.name = "TheLastTrain"
define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
default preferences.text_cps = 0
default preferences.afm_time = 15
define config.save_directory = "TheLastTrain-1746643048"
define config.window_icon = "gui/window_icon.png"
define config.developer = True
default highlight_zones = False
define config.default_language = "english"
define config.translations = ["russian"]

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.documentation('*.html')
    build.documentation('*.txt')

transform fullscreen_bg:
    zoom 1.5
    xalign 0.5
    yalign 0.5

transform hero_portrait_small:
    xalign 0.5
    yalign 1.0  # bottom of screen
    xzoom 0.7   # half width
    yzoom 0.7  # half height
    
define config.mouse = {
    "default": [ ("gui/cursor_default.png", 0, 0) ],
    "hover": [("gui/cursor_hover.png", 0, 0) ]
}