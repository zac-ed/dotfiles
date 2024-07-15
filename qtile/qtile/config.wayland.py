from libqtile.lazy              import lazy
from libqtile.layout.max        import Max
from libqtile.layout.xmonad     import MonadTall 
from libqtile.layout.floating   import Floating
from libqtile.config            import Screen, Click, Drag, Group, Key, Match
import os
import random

mod         = "mod4"
terminal    = "foot"

#import subprocess
#
#subprocess.call(["swaybg", "-i", "/path/to/your/wallpaper.jpg"])

def random_wallpaper():
    wallp_dir = os.path.expanduser("~/wallpapers")
    dir_contents = []
    home = os.path.expanduser("~")
    for _, _, files in os.walk(wallp_dir, topdown=True):
        dir_contents.extend(files)

    if dir_contents:
        randy = random.randint(0, len(dir_contents) - 1)
        target_image = dir_contents[randy]
        wallpaper = os.path.join(wallp_dir, target_image)
        wallpaper = wallpaper.replace(home, "~")
        return wallpaper

    else:
        return 0 

colours = [
            'a55890',       'b4005b',      '781155',
###       0: baby pink,   1: shock pink,  2: hot pink

            '655178',       '241d23',
###       3: steely grey, 4: dark grey
           
            'ab90a1',
###       5: cream white
          
            '562478',       '412e45',
###       6: lavender,    7: eggplant

            '393e38',       '394745'
###       8: leafy green, 9: waxy green
         ]


keys = [
            #Change focus#
    Key(
        [mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"
       ),
    Key(
        [mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"
       ),
    Key(
        [mod], "j",
        lazy.layout.down(),
        desc="Move focus down"
       ),
    Key(
        [mod], "k",
        lazy.layout.up(),
        desc="Move focus up"
       ),
    
        #Move windows around#
    Key(
        [mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
       ),
    Key(
            [mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
       ),
    Key(
            [mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"
       ),
    Key(
        [mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"
       ),

        #Grow & shrink#
    Key(
        [mod, "control"], "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"
       ),
    Key(
        [mod, "control"], "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"
        ),
    Key(
        [mod, "control"], "j",
        lazy.layout.grow_down(),
        desc="Grow window down"
       ),
    Key(
        [mod, "control"], "k",
        lazy.layout.grow_up(),
        desc="Grow window up"
       ),
    Key(
        [mod], "e",
        lazy.layout.normalize(),
        desc="Reset all window sizes"
       ),

        #important actions#
    
            #Terminal#
    Key(
        [mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"
       ),
    Key(
        [mod], "t",
        lazy.spawn(terminal),
        desc="Launch Terminal"
       ),
            #Layout#
    Key(
        [mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
       ),
            #Kill window#
    Key(
        [mod], "w",
        lazy.window.kill(),
        desc="Kill focused window"
       ),
    Key([mod], "backspace",
        lazy.window.kill(),
        desc="Kill focused window"
       ),
            #X-server actions#
    Key(
        [mod, "control"], "r", 
        lazy.reload_config(),
        desc="Reload the config"
       ),
    Key(
        [mod, "control"],
        "q", lazy.shutdown(),
        desc="Shutdown Qtile"
       ),
    
        #ROFI#
    Key(    ### This spawns the app launcher ###
        [mod], "r",
        lazy.spawn(
        'rofi drun -theme eggbox -show-icons -show drun'                                   ), 
        desc="Rofi"
       ),
    Key(    ### This spawns the app launcher ###
        [mod], "space",
        lazy.spawn(
        'rofi drun -theme eggbox -show-icons -show drun'
                  ), 
                                
        desc="Rofi"
       ),
    Key(    ### This shows you which windows are in which workspace! ###
        [mod], "s",
        lazy.spawn(
        'rofi window,ssh -theme eggbox -show-icons -show window'
                  ), 
        desc="Rofi apps in groups"
       ),

            ]    


    #Defining desktops::#
groups = [Group(i) for i in "zxcvbnmdfgae"]

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
              border_focus   = colours[1], 
              border_normal  = colours[4], 
              border_width   = 2,
              margin         = 5 
             ),

    Max(),
]


screens = [Screen(
            wallpaper=random_wallpaper(),
            wallpaper_mode="fill"
                 )
          ]

# Drag floating layouts.
mouse = [
         Drag( [mod], "Button1",  lazy.window.set_position_floating(),    start=lazy.window.get_position()),
         Drag( [mod], "Button3",  lazy.window.set_size_floating(),        start=lazy.window.get_size()),
         Click([mod], "Button2",  lazy.window.bring_to_front()),
        ]


dgroups_key_binder  = None
dgroups_app_rules   = []
follow_mouse_focus  = True
bring_front_click   = False
cursor_warp         = False


floating_layout = Floating(
    float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client. #
            #          I've never used these but I don't want to delete them!         #
        *Floating.default_float_rules,
        Match(wm_class  = "confirmreset"),  # gitk
        Match(wm_class  = "makebranch"),    # gitk
        Match(wm_class  = "maketag"),       # gitk
        Match(wm_class  = "ssh-askpass"),   # ssh-askpass
        Match(title     = "branchdialog"),  # gitk
        Match(title     = "pinentry"),      # GPG key password entry
                ],
        border_focus   = colours[1], 
        border_normal  = colours[4],
                          )


auto_fullscreen             = True
focus_on_window_activation  = "smart"
reconfigure_screens         = True

    # If things like steam games want to auto-minimize themselves when losing
    # focus, should we respect this or not?
auto_minimize  = False     # Previously True

    # When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

    #makes java apps more likely to behave, so don't touch this setting!#
wmname         = "LG3D"
