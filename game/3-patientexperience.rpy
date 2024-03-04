# Basic Patient Experience

# use list to keep track of decisions made by user in patient interaction
default decisionScores = [0, 0, 0, 0, 0, 0]
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

    timer 4 action Hide('patientStatus')

style statusUI_text: 
    size 45

    
transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0



# start patient interaction
label caseViola: 
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
                call screen patientStatus("positive", "trust")

            "Ok response": 
                $ decisionScores[0] = 5
                call screen patientStatus("positive", "trust")

            "Bad response":
                $ decisionScores[0] = 1
                call screen patientStatus("negative", "trust")

