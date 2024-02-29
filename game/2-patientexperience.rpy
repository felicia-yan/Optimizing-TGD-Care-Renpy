# Clinic Home Screen + Basic Patient Experience

# use list to keep track of decisions made by user in patient interaction
default decisionscores = []
default patientfiles = {
    "viola": "This is the text of Viola's medical file",
    "teddy": "This is the text of Teddy's medical file" 
}
default patient_name = None
default patient_names = list(patientfiles.keys())

# clickable patient sprites for waiting room 
screen patientswaiting(): 
    # viola button
    imagebutton:
        xalign 0.2
        yalign 0.5 
        auto "waitingroom viola %s.png"
        action SetVariable("patient_name", "viola"), Jump("viola_case")
    # teddy button
    imagebutton:
        xalign 0.8
        yalign 0.2
        auto "waitingroom teddy %s.png"
        action SetVariable("patient_name", "teddy"), Jump("teddy_case")

# start clinic scene 
label clinic: 
    scene bg clinic

    m.c "Welcome to the clinic waiting room! This is where your patients will arrive for appointments."

    show screen patientswaiting with dissolve

    m.c "Here's your first patient now!"

    m.c "Click on the patient to begin their visit." 
    
return

# ui screens for patient interaction
# clipboard button in upper left for opening files
screen clipboard(): 
    imagebutton:
        xalign 0.05
        yalign 0.05
        auto "files clipboard %s.png"
        action Show("allmedicalfiles"), Hide("clipboard")

# show all patient folders to choose from 
screen allmedicalfiles(): 
    grid 3 2: 
        xalign 0.5
        yalign 0.5
        spacing 60
        imagebutton: 
            auto "files folder %s.png"
            action Show("openpatientfile"), Hide("allmedicalfiles")
        imagebutton: 
            auto "files folder %s.png"
            action Show("openpatientfile"), Hide("allmedicalfiles")
        imagebutton: 
            auto "files folder %s.png"
            action Show("openpatientfile"), Hide("allmedicalfiles")
        imagebutton: 
            auto "files folder %s.png"
            action Show("openpatientfile"), Hide("allmedicalfiles")
        imagebutton: 
            auto "files folder %s.png"
            action Show("openpatientfile"), Hide("allmedicalfiles")
    

# show medical info for patient selected
screen openpatientfile():
    imagebutton: 
        xalign 0.02
        yalign 0.05
        auto "ui button x %s.png"
        action Hide("openpatientfile"), Show("clipboard")
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 40
        text "[patientfiles[patient_name]]"

# start patient interaction
label viola_case: 
        scene bg clinic 
        with fade
        show screen clipboard

        $ v = Patient(Character("Viola", color="#FFFFFF"), "Viola", 24, "female", "she/her", "pink", "swimming", "vanilla")

        m.c "You've started Viola's case!"

        m.c "The patient's name is [v.name], age is [v.age], and pronouns are [v.pronouns]."

        v.c "Hi! I'm Viola!"

        m.c "To get started, you'll want to review her medical file."

        m.c "Click on the clipboard to see all the files you have on hand, and select the one for your patient, Viola."

    
label teddy_case: 
        scene bg clinic 
        with fade
        show screen clipboard

        $ t = Patient(Character("Teddy", color="#FFFFFF"), "Teddy", 19, "nonbinary", "they/them", "green", "football", "chocolate")

        t.c "Hello! I'm Teddy!"

        m.c "The patient's name is [t.name], age is [t.age], and pronouns are [t.pronouns]."

        m.c "Navigate to their file to read about the medical history."

        