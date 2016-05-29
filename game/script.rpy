# You can place the script of your game in this file.

# the pizzas
image pizza newyork     = "nystyle.png"
image pizza californian = "californian.png"
image pizza deepdish    = "deepdish.png"
image pizza neopolitan  = "neopolitan.png"
image pizza sicilian    = "sicilian.png"

image bg pizzaria       = "background.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
