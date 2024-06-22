screen skipToHome(): 
    textbutton "Skip to Home Screen": 
        xpos 1600
        ypos 55
        action Hide("skipToHome"), Jump("startHome")

# screen with start button to show before main menu
screen pressToStart():
    tag menu
    add "gui/main_menu.png"
    textbutton "START": 
        style_prefix "gnavigation"
        xpos 80
        ypos 875
        xsize 250
        action MainMenu(confirm=False)

# splashscreen shown before game starts
image splash = "stanford med splash.png"
label splashscreen: 
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(1)

    scene black with dissolve
    with Pause(1)
    
    call screen pressToStart with dissolve
    return

# The game starts here.
label start:
    # show screen checkingvariables
    show screen skipToHome
    image side mentor debrief = "side mentor.png"

    $ mentor = Person(Character("Mentor", color="#FFFFFF", namebox_style = "namebox_green", image="mentor"), "Mentor", 30, "female")
    $ player = Patient(Character("Player", color="#FFFFFF", namebox_style = "namebox_blue"), "Student", 30, None, None, None, None, None)

    

    # GA4 Key Event (key events are added to track learner progress)
    $ analytics.event("welcome", "start_welcome")

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg mentor intro

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    label introduction: 
    $ achievement.grant("Beginning")

    mentor.char """Ahh! So much to do to get this place up to snuff!

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
            # GA4 Key Event
            $ analytics.event("name_choice", "call_me_student")
            jump default_name


    label give_name: 
        $ player.name = renpy.input("What's your name?")
        $ player.name = player.name.strip().title()
        if player.name == "": 
            jump give_name
        mentor.char "Got it, [player.name]! I'm so forgetful sometimes."
        jump select_pronouns


    label default_name: 
        $ player.name = "Student"
        mentor.char "Mysterious! Not to worry, I'll respect your privacy."
        jump select_pronouns

    
    label select_pronouns: 
    mentor.char "And could you remind me of the pronouns you use?"

    # pronoun selection here; look into tools 
    menu:
        "He/him":
                # GA4 Event
                $ analytics.event("pronoun_choice", "he_him")
                $ player.pronouns = "he/him"
        "She/her":
                # GA4 Event
                $ analytics.event("pronoun_choice", "she_her")
                $ player.pronouns = "she/her"
        "They/them":
                # GA4 Event
                $ analytics.event("pronoun_choice", "they_them")
                $ player.pronouns = "they/them"
        "Just my name please":
                # GA4 Event
                $ analytics.event("pronoun_choice", "name")
                $ player.pronouns = "name"
        "No preference":
                # GA4 Event
                $ analytics.event("pronoun_choice", "any")
                $ player.pronouns = "any"
           
    mentor.char "Thank you, duly noted. We'll remember this when addressing you!"

    mentor.char "Oh, one last super important question!"

    mentor.char "What's your favorite flavor of ice cream? We have a little ice cream party every now and then!"

    menu: 
        "Vanilla":
            # GA4 Event
            $ analytics.event("fav_flavor", "vanilla")
            $ player.fav_flavor = "vanilla"
            jump icecream1

        "Chocolate":
            # GA4 Event
            $ analytics.event("fav_flavor", "chocolate")
            $ player.fav_flavor = "chocolate"
            jump icecream1

        "Strawberry":
            # GA4 Event
            $ analytics.event("fav_flavor", "strawberry")
            $ player.fav_flavor = "strawberry"
            jump icecream2

        "Pistachio":
            # GA4 Event
            $ analytics.event("fav_flavor", "pistachio")
            $ player.fav_flavor = "pistachio"
            jump icecream2
        
        "Other":
            # GA4 Event
            $ analytics.event("fav_flavor", "other")
            jump give_flavor
    
    label give_flavor: 
        $ player.fav_flavor = renpy.input("What's your favorite flavor?")
        $ player.fav_flavor = player.fav_flavor.strip().lower() 
        if player.fav_flavor == "": 
            jump give_flavor
        mentor.char "{i}Flavor, Flavor, Flavor!{/i} If I say it three times quick I'll remember it!" 
        jump tutorial

    label icecream1: 
        mentor.char "A classic choice. Thanks!"
        jump tutorial
    
    label icecream2: 
        mentor.char "Cool! I swear, I will remember that!"
        jump tutorial
    
    label tutorial: 
        mentor.char "Now, let me show you around. We've got a lot of work to do!"
       
        mentor.char "So, you're already familiar with the choice menu. As you spend more time at the clinic, you'll be making a lot of choices, mainly about how to respond to people. We'll try not to wear you out with too many choices though!"
        
        mentor.char "Before we step inside the clinic, I also want to show you how to save your progress."

        mentor.char "If you select the \"Save\" button below, you can save your progress. Saving means that if you close the game and come back, you can \"Load\" it on the start screen and continue your learning journey."

        mentor.char "We'll also encourage you to save throughout your time here after important events, so keep that in mind!"

        mentor.char "By the way, in that same menu, you'll see an \"Preferences\" button. If you select that, you'll be able to adjust accessibility features, as well as things like music and voice over volume."

        mentor.char "Let\'s save here, shall we? That was a lot of information!"
        # GA4 Key Event
        $ analytics.event("welcome", "end_welcome")
        jump startHome