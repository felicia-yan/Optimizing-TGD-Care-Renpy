##################################
# TEMPLATE FILE - Duplicate this file to create your own
## [PATIENT NAME]
## VIST [NUMBER (there will be up to 5 visits per patient)]
#Comments are defined with # at the beginning
##################################

# THIS DOCUMENT INCLUDES:
## FILE STRUCTURE
## FORMATTING NOTES
## TEMPLATE CODE FOR ALL SCRIPT SECTIONS

# FILE STRUCTURE #
# The script is divided into the below parts according to the design of the TGD Care game.
# Follow the instructions to name and format each section so that this code remains readable.
##################################
## SCRIPT SETUP
## - various parameters and definitions will be set up here. Do not put content here.
## A. PRE-VISIT VIGNETTE
## --- Optional location of a video cutscene showing the patient before their clinic visit.
## --- Not strictly video, but that is the plan at the moment.
## --- Label as [Patient Visit Number].A. [Patient Name] "Pre-Visit Vignette"
## --- e.g. 1.A. Viola Pre-Visit Vignette  
## B. REVIEW EHR
## --- Required review of patient's electronic health record.
## --- Includes prompt to open EHR and read it. May optionally include story moments with clinic staff.
## --- Label as [Patient Visit Number].B. [Patient Name] "Review EHR"
## --- e.g 1.B. Viola Review EHR
## C. COACHING CONVERSATION
## --- Required discussion with mentor (Dr G) after reviewing EHR and before Patient Interaction
## --- May include knowledge checks (e.g. "What is estradiol?") -- content is not fully developed.
## --- Label as [Patient Visit Number].C. [Patient Name] "Coaching Conversation"
## --- e.g 1.C. Viola Coaching Conversation
## D. PATIENT INTERACTION
## --- Main gameplay, in which learner speaks with patient and makes multiple decisions.
## --- Learner choices and performance are tracked.
## --- Trust and stress values are given to each choice.
## --- Label as [Patient Visit Number].D. [Patient Name] "Patient Interaction"
## --- e.g 1.D. Viola Patient Interaction
## E. POST-VISIT VIGNETTE
## --- Optional location of a video cutscene showing the patient after their clinic visit.
## --- Not strictly video, but that is the plan at the moment.
## --- Label as [Patient Visit Number].E. [Patient Name] "Post-Visit Vignette"
## --- e.g. 1.E. Viola Post-Visit Vignette  
## F. DEBRIEF
## --- Required review of learner's performance during Patient Interaction.
## --- Scorecard including trust, stress, and review of learner choices is shown.
## --- Content is not fully developed.
## --- Label as [Patient Visit Number].F. [Patient Name] "Debrief"
## --- e.g. 1.F. Viola Debrief  

# SCRIPT SETUP

transform half_size: 
    zoom 0.5

# FORMATTING NOTES

# LABELS
# Here's an example of a label. This is a section of dialogue and choices. 
# Labels should have a suffix on them corresponding to the patient name, visit number, and script section
# label_[Patient][Visit#][A,B,C,D,E, or F]
# This is essential because labels are global and unique.
# Using the same label twice will result in an error, or take them to another patient visit.
label first: 
    # Declare your characters! Format it as below with name, age, and sex
    $ mentor = Person(Character("Mentor", color="#FFFFFF"), "Mentor", 30, "female")
    $ alice = Person(Character("Alice", color="#FFFFFF"), "Alice", 18, "female")

    # Each line will display as a piece of dialogue that needs to be clicked through 
    mentor.char "What's up!"
    
    mentor.char "It's a lovely day today."

    alice.char "Yes, it is!"

    # Jump to another label 
    jump second


label second: 
    mentor.char "Hi! You've jumped to the label \"second\"!" # "\" is used as escaped character to include "" in the string

    mentor.char "What do you think about ice cream?"

    # Use menus to let the player make choices
    menu: 
        "I love it!":
            ##################################
            #GA4 TRACKING IMPLEMENTATION
            #Adding $analytics.event (category, action) under any decision to track the player's choice
            #The .event() has been defined in analytics.rpy
            ##################################
            $ analytics.event ("category_to_track", {"choice": "choice_name"})
            mentor.char "Me too!"

        "It's alright...": 
            mentor.char "Oh..."

        "Can you say that again?": 
            # You can call labels in any order; you can even loop back to the same label!
            jump second 



# TEMPLATE CODE FOR ALL SCRIPT SECTIONS (Not finished!)

# [#].A. [PATIENT] PRE-VISIT VIGNETTE



# [#].B. [PATIENT] REVIEW EHR


# [#].C. [PATIENT] COACHING CONVERSATION


# [#].D. [PATIENT] PATIENT INTERACTION


# [#].E. [PATIENT] POST-VISIT VIGNETTE


# [#].F. [PATIENT] DEBRIEF