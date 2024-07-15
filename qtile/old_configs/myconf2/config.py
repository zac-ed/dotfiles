from keys       import keys
from groups     import groups
from floaty     import floating_layout, mouse 

keys    = keys
groups  = groups
layouts = floating_layout
screens = []
mouse   = mouse

dgroups_key_binder          = None
dgroups_app_rules           = []  
follow_mouse_focus          = True
bring_front_click           = False
cursor_warp                 = False

auto_fullscreen             = True
focus_on_window_activation  = "smart"

reconfigure_screens         = True
    # If things like steam games want to auto-minimize themselves when losing
    # focus, should we respect this or not?
auto_minimize               = True
    # When using the Wayland backend, this can be used to configure input devices.
wl_input_rules              = None
    #makes java apps more likely to behave, so don't touch this setting!#
wmname                      = "LG3D"
