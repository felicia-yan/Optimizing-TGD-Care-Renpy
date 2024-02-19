# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mentor", who_color="#FFFFFF")
define p = Character("Player", who_color="#FFFFFF")


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

    label introduction: 
    m """Ahh! So much to do to get this place up to snuff!

    ...Oh! How funny, I was just talking to myself! You must be our new recruit!

    Forgive me, we're on a mission to optimize this clinic for patients receiving gender-affirming care.

    So go figure, I'm a bit distracted. There's a lot to be done!

    ...And I was supposed to give you an orientation today! That's what I forgot to do!

    I'm Dr G., I'll be your mentor here. I use they/them pronouns.

    But, I'm getting ahead of myself... We haven't even been introduced!

    I should know this already but, what is your name?

    I'm going to give you a choice of typing in your name or a generic name. Just tap which option you'd like to continue with.

    Oh, and I should mention, none of this information will be shared -- it's strictly confidential!
    """

    menu: 
        "Let me give you my name!": 
            jump give_name

        "You can just call me Student.":
            jump default_name


    label give_name: 
        $ player_name = renpy.input("What's your name?")
        $ player_name = player_name.strip() 
        $ player_name = player_name.title()
        if player_name == "": 
            jump give_name
        m "Got it! I'm so forgetful sometimes."
        jump select_pronouns


    label default_name: 
        $ player_name = "Student"
        m "Mysterious! Not to worry, I'll respect your privacy."
        jump select_pronouns

    
    label select_pronouns: 
    m "And could you remind me of the pronouns you use?"

    # pronoun selection here; look into tools 
        
    m "Thank you, duly noted. We'll remember this when addressing you!"

    m "Oh, one last super important question!"

    m "What's your favorite flavor of ice cream? We have a little ice cream party every now and then!"

    menu: 
        "Vanilla":
            $ fav_flavor = "vanilla"
            jump icecream1

        "Chocolate":
            $ fav_flavor = "chocolate"
            jump icecream1

        "Strawberry":
            $ fav_flavor = "strawberry"
            jump icecream2

        "Pistachio":
            $ fav_flavor = "pistachio"
            jump icecream2
        
        "Other":
            jump give_flavor
    
    label give_flavor: 
        $ fav_flavor = renpy.input("What's your favorite flavor?")
        $ fav_flavor = player_name.strip()
        $ fav_flavor = player_name.lower() 
        if fav_flavor == "": 
            jump give_flavor
        m "{i}Flavor, Flavor, Flavor!{/i} If I say it three times quick I'll remember it!" 
        jump tutorial

    label icecream1: 
        m "A classic choice. Thanks!"
        jump tutorial
    
    label icecream2: 
        m "Cool! I swear, I will remember that!"
        jump tutorial
    
    label tutorial: 
        m "Now, let me show you around. We've got a lot of work to do!"

    return
