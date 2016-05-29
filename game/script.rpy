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

# The game starts here.
label start:
    
    scene bg pizzaria

    "The local pizzaria has a speed dating event going on and after months of a dry spell you've decided to check it out. You see various interesting beings sitting around what do you do?"
    
    menu:
        
        "Scope it out and see what's interesting.":
            "You approach closer and you notice something weird about the beings at speed dating, but you figure it's probably just the cold medicine messing with you."
        "Run away in horror.":
            "You can't leave now, there's some good stuff happening here."

    return