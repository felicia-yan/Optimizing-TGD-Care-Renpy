# Basic Patient Experience

# use list to keep track of decisions made by user in patient interaction
default decisionScores = [0, 0, 0]
default patientFiles = {
    "viola": "This is the text of Viola's medical file",
}
default patientName = None
default patientNames = list(patientFiles.keys())

# ui screens for patient interaction
# clipboard button in upper left for opening files
screen clipboard(): 
    imagebutton:
        xalign 0.05
        yalign 0.05
        auto "files clipboard %s.png"
        action Call("allMedicalFiles"), Hide("clipboard")

# show all patient folders to choose from 
screen allMedicalFiles(): 
    grid 3 2: 
        xalign 0.5
        yalign 0.5
        spacing 60
        imagebutton: 
            auto "files folder %s.png"
            action Call("openPatientFile"), Hide("allMedicalFiles")
        imagebutton: 
            auto "files folder %s.png"
            action Call("openPatientFile"), Hide("allMedicalFiles")
        imagebutton: 
            auto "files folder %s.png"
            action Call("openPatientFile"), Hide("allMedicalFiles")
        imagebutton: 
            auto "files folder %s.png"
            action Call("openPatientFile"), Hide("allMedicalFiles")
        imagebutton: 
            auto "files folder %s.png"
            action Call("openPatientFile"), Hide("allMedicalFiles")
    

# show medical info for patient selected
screen openPatientFile():
    imagebutton: 
        xalign 0.02
        yalign 0.05
        auto "ui button x %s.png"
        action Hide("openPatientFile"), Show("clipboard")
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 40
        text "[patientFiles[patientName]]"

# alerts for status of relationship with patient
screen patientStatus(status, statusMessage): 
    style_prefix "statusUI"
    zorder 100
    frame:
        xpos 45
        ypos 45
        padding (40, 40)
        background "bg status positive.png"
        hbox: 
            xalign 0.5
            yalign 0.5
            spacing 20
            frame: 
                xalign 0.5
                yalign 0.5
                background "bg status name text.png"
                text "[patientName.upper()]":
                    font "Gilbert.otf"
                    color "#FFFFFF"
            text "[statusMessage!tq]": 
                color "#00B3E3"
                text_align 1.0

    timer 4 action Hide('patientStatus')

style statusUI_text: 
    size 35

    
transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0



# start patient interaction
label startcaseViola: 
        hide screen home
        scene bg patient room
        with fade
        show screen clipboard

        $ v = Patient(Character("Viola", color="#FFFFFF"), "Viola", 24, "female", "she/her", "pink", "swimming", "vanilla")

        m.c "You've started Viola's case!"

        m.c "The patient's name is [v.name], age is [v.age], and pronouns are [v.pronouns]."

        v.c "Hi! I'm Viola!"

        m.c "To get started, you'll want to review her medical file."

        m.c "Click on the clipboard to see all the files you have on hand, and select the one for your patient, Viola."

        menu: 
            "Great response": 
                $ decisionScores[0] = 10
                show screen patientStatus("positive", "trusting")
                v.c "Thanks! I feel supported and I trust you more."

            "Ok response": 
                $ decisionScores[0] = 5
                show screen patientStatus("positive", "trusting")
                v.c "I guess that's ok."

            "Bad response":
                $ decisionScores[0] = 1
                show screen patientStatus("negative", "distrusting")
                v.c "That was not a good choice. I don't feel good about what you said to me."


        label caseViolacontinue1: 
            m.c "You'll be presented with 2 more decisions to make for this patient interaction."

        menu: 
            "Great response": 
                $ decisionScores[1] = 10
                show screen patientStatus("positive", "comfort")
                v.c "I feel more comfortable with you as my physician."

            "Ok response": 
                $ decisionScores[1] = 5
                show screen patientStatus("positive", "uncomfortable")
                v.c "I feel a bit uncomfortable."

            "Bad response":
                $ decisionScores[1] = 1
                show screen patientStatus("negative", "embarrassed")
                v.c "I feel embarrassed and very uncomfortable."
            

        label caseViolacontinue2: 
        m.c "This is the last choice in this section."
    
        menu: 
            "Great response": 
                $ decisionScores[2] = 10
                show screen patientStatus("positive", "happy")
                v.c "I feel very good about the outcome of this visit."

            "Ok response": 
                $ decisionScores[2] = 5
                show screen patientStatus("positive", "content")
                v.c "This wasn't the best visit, but it was alright."

            "Bad response":
                $ decisionScores[2] = 1
                show screen patientStatus("negative", "angry")
                v.c "This was a horrible visit. I won't be back."


        label learner_debrief: 
            m.c "The patient visit is over." 

            if decisionScores[0] == 10: 
                m.c "You used the correct pronouns for Viola, gaining her trust."
            if decisionScores[0] == 5: 
                m.c "You addressed Viola as she asked to be addressed, though you seemed hesitant."
            if decisionScores[0] == 1: 
                m.c "You started the interaction by misgendering Viola, losing her trust."
            
            if decisionScores.count(10) == 3:
                m.c "Great job! You made choices that optimized Viola's gender-affirming care."
            if decisionScores.count(10) == 2:
                m.c "Overall, the patient interaction was mostly good, with some inappropriate choices."
            if decisionScores.count(10) == 1:
                m.c "Unfortunately, the quality of care for Viola was not adequate. She was uncomfortable and felt unsupported."
            
            return



    



    
