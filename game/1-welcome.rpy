# Introduction

init python: 
    # player classes 
    class Person:
        def __init__(self, character, name, age, sex):
            self.c = character
            self.name = name
            self.age = age 
            self.sex = sex
    
    class Patient(Person): 
        def __init__(self, character, name, age, sex, pronouns, fav_color, fav_sport, fav_flavor):
            super().__init__(character, name, age, sex) 
            self.pronouns = pronouns
            self.fav_color = fav_color
            self.fav_sport = fav_sport
            self.fav_flavor = fav_flavor



"""
# just for checking during development process, shows variable values on screen
screen checkingvariables(): 
    vbox: 
        text "Player name: [u.name]" 
        text "Player pronouns: [u.pronouns]" 
        text "Player favorite flavor: [u.fav_flavor]" 
        text "Player name: [u.name]" 
        text "Current patient name: [patientName]"
"""

# The game starts here.

label start:

    # show screen checkingvariables
    $ m = Person(Character("Mentor", color="#FFFFFF"), "Mentor", 30, "female")
    $ u = Patient(Character("User"), "Student", 30, None, None, None, None, None)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg mentor intro

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    label introduction: 
    m.c """Ahh! So much to do to get this place up to snuff!

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
        $ u.name = renpy.input("What's your name?")
        $ u.name = u.name.strip().title()
        if u.name == "": 
            jump give_name
        m.c "Got it! I'm so forgetful sometimes."
        jump select_pronouns


    label default_name: 
        $ u.name = "Student"
        m.c "Mysterious! Not to worry, I'll respect your privacy."
        jump select_pronouns

    
    label select_pronouns: 
    m.c "And could you remind me of the pronouns you use?"

    # pronoun selection here; look into tools 
    menu:
        "He/him":
                $ u.pronouns = "he/him"
        "She/her":
                $ u.pronouns = "she/her"
        "They/them":
                $ u.pronouns = "they/them"
        "Just my name please":
                $ u.pronouns = "name"
        "No preference":
                $ u.pronouns = "any"
           
    m.c "Thank you, duly noted. We'll remember this when addressing you!"

    m.c "Oh, one last super important question!"

    m.c "What's your favorite flavor of ice cream? We have a little ice cream party every now and then!"

    menu: 
        "Vanilla":
            $ u.fav_flavor = "vanilla"
            jump icecream1

        "Chocolate":
            $ u.fav_flavor = "chocolate"
            jump icecream1

        "Strawberry":
            $ u.fav_flavor = "strawberry"
            jump icecream2

        "Pistachio":
            $ u.fav_flavor = "pistachio"
            jump icecream2
        
        "Other":
            jump give_flavor
    
    label give_flavor: 
        $ u.fav_flavor = renpy.input("What's your favorite flavor?")
        $ u.fav_flavor = u.fav_flavor.strip().lower() 
        if u.fav_flavor == "": 
            jump give_flavor
        m.c "{i}Flavor, Flavor, Flavor!{/i} If I say it three times quick I'll remember it!" 
        jump tutorial

    label icecream1: 
        m.c "A classic choice. Thanks!"
        jump tutorial
    
    label icecream2: 
        m.c "Cool! I swear, I will remember that!"
        jump tutorial
    
    label tutorial: 
        m.c "Now, let me show you around. We've got a lot of work to do!"
       
        m.c "So, you're already familiar with the choice menu. As you spend more time at the clinic, you'll be making a lot of choices, mainly about how to respond to people. We'll try not to wear you out with too many choices though!"
        
        m.c "Before we step inside the clinic, I also want to show you how to save your progress."

        m.c "See that button there? If you select that, you'll open a menu where you can save your progress. Saving means that if you close the game and come back, you can \"Load\" it on the start screen and continue your learning journey."

        m.c "We'll also encourage you to save throughout your time here, after important events, so keep that in mind!"

        m.c "By the way, in that same menu, you'll see an \"Options\" button. If you select that, you'll be able to adjust accessibility features, as well as things like music and voice over volume."

        m.c "Let\'s save here, shall we? That was a lot of information!"

        jump startHome
