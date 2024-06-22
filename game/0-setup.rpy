### ACHIEVEMENT SYSTEM ###
python early:
    simple_achievement_list = (
        # ("Achievement Name", "Description when not unlocked", "Description when unlocked"),
        ("Beginning", "???", "Started a new game"),
        ("Getting Oriented", "???", "Completed the clinic orientation"),
        ("First Look", "???", "Finished your first visit with Viola"),
    )

init python:

    for a, lockdesc, unlockdesc in simple_achievement_list:
        achievement.register(a)

screen achievements():
    tag menu
    use game_menu(_("Achievements"), scroll="viewport"):
        style_prefix "about" 
        vbox: 
            spacing 20
            for aname, lockdesc, unlockdesc in simple_achievement_list:

                if achievement.has(aname):

                    text "[aname]: {color=#777} [unlockdesc] {/color}"

                else:

                    text "[aname]: {color=#ccc} [lockdesc] {/color}"

# Introduction
init python: 
    # allow player to make new line in notepad by pressing enter/return
    config.keymap['input_next_line'].append('K_RETURN')
    config.has_autosave = True
    config.autosave_on_choice = True
    config.autosave_on_input = True
    config.autosave_on_quit = True
    config.allow_skipping = False

    config.end_splash_transition = dissolve
    config.minimum_presplash_time = 5

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
            self.current_visit = 1


# use list to keep track of decisions made by user in patient interaction
default notes = "Write notes for yourself throughout the patient visit. Notes will be erased after the visit."
default decisionScores = [0, 0, 0, 0, 0]
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

# image transforms for rendering sprites
transform half_size: 
    zoom 0.5

transform third_size: 
    zoom 0.33

# tracking the completion of modules (0 is incomplete, 1 is in progress, 2 is complete)
default introductionModules = [0, 0, 0]
default rocModules = [0, 0, 0, 0, 0]
default violaModules = [0, 0, 0, 0, 0]
default oliviaModules = [0, 0, 0]
default minicaseModules = [0, 0, 0, 0, 0]


# just for checking during development process, shows variable values on screen
"""
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
"""
