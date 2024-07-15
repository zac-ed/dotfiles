from libqtile.layout.max        import Max
from libqtile.layout.xmonad     import MonadTall
from colours                    import colours

colours = colours

layouts = [
    MonadTall(
              border_focus   = colours[1], 
              border_normal  = colours[4], 
              border_width   = 2,
              margin         = 5 
             ),
    Max(),
          ]
