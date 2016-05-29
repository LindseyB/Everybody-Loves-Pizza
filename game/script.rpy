# the pizzas
image pizza newyork     = "nystyle.png"
image pizza californian = "californian.png"
image pizza deepdish    = "deepdish.png"
image pizza neopolitan  = "neopolitan.png"
image pizza sicilian    = "sicilian.png"

image bg pizzaria       = "background.png"

# all the pizzas to love
define ny  = Character('New York Style Pizza', color="#c8ffc8")
define ca  = Character('Californian Style Pizza', color="#33cc33")
define dd  = Character('Deep Dish Pizza', color="#ff3300")
define neo = Character('Neopolitan Pizza', color="#cc6699")
define s   = Character('Sicilian Pizza', color="#3399ff")
define nar = Character('Narrator', color="#eeeeee")

# The game starts here.
label start:
    
    scene bg pizzaria
    
    show pizza newyork

    nar "What do you think?"

    return
