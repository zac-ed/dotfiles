from libqtile.config    import Key
from libqtile.lazy      import lazy

mod      = "mod4"
terminal = "alacritty"

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
        'rofi drun -theme eggbox -show-icons -icon-theme "elementary-p" -show drun'                                   ), 
        desc="Rofi"
       ),
    Key(    ### This spawns the app launcher ###
        [mod], "space",
        lazy.spawn(
        'rofi drun -theme eggbox -show-icons -icon-theme "elementary-p" -show drun'
                  ), 
                                
        desc="Rofi"
       ),
    Key(    ### This shows you which windows are in which workspace! ###
        [mod], "s",
        lazy.spawn(
        'rofi window,ssh -theme eggbox -show-icons -icon-theme "elementary-p" -show window'
                  ), 
        desc="Rofi apps in groups"
       ),

            ]    
