from libqtile.lazy      import lazy
from libqtile.config    import Key, Group
from keys               import keys

mod = "mod4"
keys = keys

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
