# Introduction
init python: 
    # allow player to make new line in notepad by pressing enter/return
    config.keymap['input_next_line'].append('K_RETURN')
    config.has_autosave = True
    config.autosave_on_choice = True
    config.autosave_on_input = True
    config.autosave_on_quit = True
    config.allow_skipping = False

    # player classes 
    class Person:
        def __init__(self, character, name, age, sex):
            self.char = character
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

# use list to keep track of decisions made by user in patient interaction
default notes = ""
default decisionScores = [0, 0, 0]
default violaFile = {
    # patient ID information
    "Full name": "Viola Phoenix",
    "Legal name": "Vincent Andrews",
    "Pronouns": "she/her",
    "DOB": "October 20, 1996", 
    "Gender": "Female", 
    "Sex at birth": "Male", 
    "Address": "Los Angeles, CA", 
    "Race": "Black",

    # medical history 
    "Chronic conditions": "Hypertension. High cholesterol.",
    "Previous surgeries": "Top surgery. Facial feminization.", 
    "Additional information": "Smoker. Active sex life, practices safe sex. Came out as transgender 6 years ago. Previously lived as a gay man. Has been receiving gender-affirming care for 6 years.", 

    # medication list
    "Medication list": "Estrogen (estradiol)", 

    # consultation notes
    "Consultation notes": "Wants to increase dosage of estradiol for feminizing effects."
}
default rocFile = {
    # patient ID information
    "Full name": "Roc Garcia",
    "Legal name": "Andrea Garcia",
    "Pronouns": "he/him",
    "DOB": "June 10, 1988", 
    "Gender": "Male", 
    "Sex at birth": "Female", 
    "Address": "San Diego, CA", 
    "Race": "Hispanic or Latino",

    # medical history 
    "Chronic conditions": "Asthma.",
    "Previous surgeries": "None", 
    "Additional information": "Active sex life.", 

    # medication list
    "Medication list": "None", 

    # consultation notes
    "Consultation notes": "Would like to explore taking hormones and the process to affirm his gender."
}
default teddyFile = {
    # patient ID information
    "Full name": "Teddy Williams",
    "Legal name": "Theodore Williams",
    "Pronouns": "they/them",
    "DOB": "October 20, 1996", 
    "Gender": "Nonbinary", 
    "Sex at birth": "Female", 
    "Address": "Palo Alto, CA", 
    "Race": "White",

    # medical history 
    "Chronic conditions": "None",
    "Previous surgeries": "Appendectomy.", 
    "Additional information": "Family history of heart disease — mother, aunt, brother.",

    # medication list
    "Medication list": "Testosterone", 

    # consultation notes
    "Consultation notes": "Wants to increase dosage of testosterone for masculinizing effects."
}
default display_desc = ""
default glossarySearchTerm = ""
default glossaryTerms = {
    "Adrenaline": "Stress hormone that puts the body on high alert. Changes include faster heartbeat, more rapid breathing, greater energy, and higher blood pressure. Also called epinephrine.", 
    "Androgen": "Any of a group of male sex hormones, including testosterone, that controls male characteristics such as beard growth.", 
    "Defibrillation": "The delivery of an electric shock to the heart to stop an abnormal rhythm and restore a normal heartbeat.", 
    "Defibrillator": "A device that delivers an electric shock to the heart to restore normal rhythm. Used to treat cardiac arrest and other dangerous heart rhythm problems.", 
    "Estradiol": "The primary form of the sex hormone estrogen produced by women.", 
    "Estrogen": "The main sex hormone in women.", 
    "Gender dysphoria": "Distress experienced by some people whose gender identity and sex assigned at birth don’t match.", 
    "Gestational diabetes mellitus": "A form of diabetes that appears during pregnancy.",
    "Intersex": "A group of congenital conditions in which the reproductive organs, genitals, and/or other sexual anatomy do not develop according to traditional expectations for females or males.",
    "Transition": "The process of aligning gender expression with gender identity. "

}

default patientName = None



# just for checking during development process, shows variable values on screen
screen checkingvariables(): 
    vbox: 
        text "Player name: [player.name]" 
        text "Player pronouns: [player.pronouns]" 
        text "Player favorite flavor: [player.fav_flavor]" 
        text "Player name: [player.name]" 
        text "Current patient name: [patientName]"
        text "awardsUnlocked: [awardsUnlocked]"
        text "searchName: [searchName]"
        text "Notes: [notes]"
        text "decisionScores: [decisionScores]"
        text "patientName: [patientName]"


# The game starts here.

label start:

    show screen checkingvariables
    $ mentor = Person(Character("Mentor", color="#FFFFFF"), "Mentor", 30, "female")
    $ player = Patient(Character("Player"), "Student", 30, None, None, None, None, None)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg mentor intro

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    label introduction: 
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
            jump give_name

        "You can just call me Student.":
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
                $ player.pronouns = "he/him"
        "She/her":
                $ player.pronouns = "she/her"
        "They/them":
                $ player.pronouns = "they/them"
        "Just my name please":
                $ player.pronouns = "name"
        "No preference":
                $ player.pronouns = "any"
           
    mentor.char "Thank you, duly noted. We'll remember this when addressing you!"

    mentor.char "Oh, one last super important question!"

    mentor.char "What's your favorite flavor of ice cream? We have a little ice cream party every now and then!"

    menu: 
        "Vanilla":
            $ player.fav_flavor = "vanilla"
            jump icecream1

        "Chocolate":
            $ player.fav_flavor = "chocolate"
            jump icecream1

        "Strawberry":
            $ player.fav_flavor = "strawberry"
            jump icecream2

        "Pistachio":
            $ player.fav_flavor = "pistachio"
            jump icecream2
        
        "Other":
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
       
        mentor.char "So, you're already familiar with the choice menplayer. As you spend more time at the clinic, you'll be making a lot of choices, mainly about how to respond to people. We'll try not to wear you out with too many choices though!"
        
        mentor.char "Before we step inside the clinic, I also want to show you how to save your progress."

        mentor.char "If you select the \"Save\" button below, you can save your progress. Saving means that if you close the game and come back, you can \"Load\" it on the start screen and continue your learning journey."

        mentor.char "We'll also encourage you to save throughout your time here after important events, so keep that in mind!"

        mentor.char "By the way, in that same menu, you'll see an \"Preferences\" button. If you select that, you'll be able to adjust accessibility features, as well as things like music and voice over volume."

        mentor.char "Let\'s save here, shall we? That was a lot of information!"

        jump startHome
