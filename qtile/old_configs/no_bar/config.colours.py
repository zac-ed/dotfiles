from libqtile                           import bar, widget
from libqtile.lazy                      import lazy
from libqtile.layout                    import Max, MonadTall, Floating
from libqtile.config                    import Click, Drag, Group, Key, Match, Screen


mod         = "mod4"
terminal    = "alacritty"

    #colors:
baby_pink   = 'a55890'
shock_pink  = 'b4005b'
hot_pink    = '781155'

steely_grey = '655178'
dark_grey   = '241d23'
cream_white = 'ab90a1'

lavender    = '562478'
eggplant    = '412e45'

leafy_green = '393e38'
waxy_green  = '394745'

colours = [
            'a55890',      'b4005b',    '781155',
###       0: baby pink, 1: shock pink, 2: hot pink
##
            '655178',       '241d23',
###       3: steely grey, 4: dark grey
##            
            'ab90a1',
###       5: cream white
##           
            '562478',    '412e45',
###       6: lavender, 7: eggplant
##
            '393e38',       '394745'
###       8: leafy green, 9: waxy green
         ]



keys = [
        #Change focus#
    Key([mod], "h",            lazy.layout.left(),              desc="Move focus to left"),
    Key([mod], "l",            lazy.layout.right(),             desc="Move focus to right"),
    Key([mod], "j",            lazy.layout.down(),              desc="Move focus down"),
    Key([mod], "k",            lazy.layout.up(),                desc="Move focus up"),
        #alternatively, use# 
        #  1-4 like hjkl   #
    Key([mod], "1",            lazy.layout.left(),              desc="Move focus to left"),
    Key([mod], "4",            lazy.layout.right(),             desc="Move focus to right"),
    Key([mod], "2",            lazy.layout.down(),              desc="Move focus down"),
    Key([mod], "3",            lazy.layout.up(),                desc="Move focus up"),

    
        #Move windows around#
    Key([mod, "shift"], "h",   lazy.layout.shuffle_left(),      desc="Move window to the left"),
    Key([mod, "shift"], "l",   lazy.layout.shuffle_right(),     desc="Move window to the right"),
    Key([mod, "shift"], "j",   lazy.layout.shuffle_down(),      desc="Move window down"),
    Key([mod, "shift"], "k",   lazy.layout.shuffle_up(),        desc="Move window up"),
        #Or move with 1-4#
    Key([mod, "shift"], "1",   lazy.layout.shuffle_left(),      desc="Move window to the left"),
    Key([mod, "shift"], "4",   lazy.layout.shuffle_right(),     desc="Move window to the right"),
    Key([mod, "shift"], "2",   lazy.layout.shuffle_down(),      desc="Move window down"),
    Key([mod, "shift"], "3",   lazy.layout.shuffle_up(),        desc="Move window up"),

        #Grow & shrink#
    Key([mod, "control"], "h", lazy.layout.grow_left(),         desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),         desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(),           desc="Grow window up"),
    Key([mod], "e",            lazy.layout.normalize(),         desc="Reset all window sizes"),
        #   1-4   #
    Key([mod, "control"], "1", lazy.layout.grow_left(),         desc="Grow window to the left"),
    Key([mod, "control"], "4", lazy.layout.grow_right(),        desc="Grow window to the right"),
    Key([mod, "control"], "2", lazy.layout.grow_down(),         desc="Grow window down"),
    Key([mod, "control"], "3", lazy.layout.grow_up(),           desc="Grow window up"),

        #important actions#
    
            #Terminal#
    Key([mod], "Return",       lazy.spawn(terminal),            desc="Launch terminal"),
    Key([mod], "t",            lazy.spawn(terminal),            desc="Launch Terminal"),
            #Layout#
    Key([mod], "Tab",          lazy.next_layout(),              desc="Toggle between layouts"),
            #Kill window#
    Key([mod], "w",            lazy.window.kill(),              desc="Kill focused window"),
    Key([mod], "backspace",    lazy.window.kill(),              desc="Kill focused window"),
            #X-server actions#
    Key([mod, "control"], "r", lazy.reload_config(),            desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(),                 desc="Shutdown Qtile"),
    
                #Screenshot script#
            #Key([], "Print",           lazy.spawn("~/.local/bin/screenshot.sh")),#

        #ROFI#
    Key([mod], "r",             lazy.spawn(
        'rofi drun -theme eggbox -show-icons -icon-theme "elementary-p" -show drun'
                                          ), 
                                desc="Rofi"),

    Key([mod], "space",         lazy.spawn(
        'rofi drun -theme eggbox -show-icons -icon-theme "elementary-p" -show drun'
                                          ), 
                                desc="Rofi"),
    Key([mod, "shift"], "space",         lazy.spawn(
        'rofi window,ssh -theme eggbox -show-icons -icon-theme "elementary-p" -show window'
                                          ), 
                                desc="Rofi apps in groups"),

    Key([mod], "s",         lazy.spawn(
        'rofi window,ssh -theme eggbox -show-icons -icon-theme "elementary-p" -show window'
                                          ), 
                                desc="Rofi apps in groups"),

       ]


    #Defining desktops::#
groups = [Group(i, label='') for i in "zxcvbnm"]

for i in groups:
    keys.extend(
        [
                # super + group label = switch to group
            Key(
                [mod], i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
               ),
                # super + shift + group label = Move focused window to group
            Key(
                [mod, "shift"], i.name,
                lazy.window.togroup(i.name, switch_group=False),    ## previously set as True
                desc="Move focused window to group {}".format(i.name),
               ),
            Key(
                [mod, "control"], i.name,
                lazy.window.togroup(i.name, switch_group=True),    ## previously set as True
                desc="Move focused window to group {}".format(i.name),
               ),
        ]
               )


layouts = [
    
    MonadTall(
              border_focus   = shock_pink, 
              border_normal  = dark_grey, 
              border_width   = 2,
              margin         = 5 
             ),

    Max(),
]


widget_defaults = dict(
                       font        = "agave Nerd Font",
                       fontsize    = 1,
                       padding     = 6,
                       foreground  = baby_pink
                      )


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                                    padding                     = 4,
                                    fontsize                    = 4, 
                                    highlight_method            = 'text', 
                                    active                      = baby_pink, 
                                    this_current_screen_border  = cream_white, 
                                    inactive                    = steely_grey, 
                                    background                  = lavender,
                               ),
 
                 
                widget.Wallpaper(
                                    directory          = '~/wallpapers', 
                                    label              = '󱕅 ',   
                                    fontsize           = 8,
                                    padding            = 0,
                                    random_selection   = True,
                                    foreground         = cream_white,
                                    background         = hot_pink,
                                ),
                
            ],
            0, margin = 0, opacity = 1 #, border_color = cream_white, border_width = 2  # bar height, margin
        ),
    ),
]


# Drag floating layouts.
mouse = [
         Drag( [mod], "Button1",  lazy.window.set_position_floating(),    start=lazy.window.get_position()),
         Drag( [mod], "Button3",  lazy.window.set_size_floating(),        start=lazy.window.get_size()),
         Click([mod], "Button2",  lazy.window.bring_to_front()),
        ]


dgroups_key_binder  = None
dgroups_app_rules   = []    # type: list
follow_mouse_focus  = True
bring_front_click   = False
cursor_warp         = False


floating_layout = Floating(
    float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
        *Floating.default_float_rules,
        Match(wm_class  = "confirmreset"),  # gitk
        Match(wm_class  = "makebranch"),    # gitk
        Match(wm_class  = "maketag"),       # gitk
        Match(wm_class  = "ssh-askpass"),   # ssh-askpass
        Match(title     = "branchdialog"),  # gitk
        Match(title     = "pinentry"),      # GPG key password entry
    ]
)


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

