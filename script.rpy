# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define f = Character("Felicia")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    f "Test dialogue!"

    # use $ for python statements
    $ player_name = renpy.input("What's your name")
    $ player_name = player_name.strip() 
    # need to make title case somehow

    if player_name == "": 
        $ player_name == "Default Name"

    e "Hi %(player_name)s!"

    menu: 

        "choice a : true":
            jump choice_a
        
        "choice b: false":
            jump choice_b

    label choice_a:
        e "you've picked true"
        jump last_line

    label choice_b:
        e "you've picked false"
        jump last_line

    label last_line: 
        f "last line to say"
	f "this is a test for updating the repo"

    # This ends the game.

    return
