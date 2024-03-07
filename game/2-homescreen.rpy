# Clinic Home Screen

screen home(): 
    # menu button
    textbutton "Menu": 
        xpos 1780
        ypos 55
        action Show("menuUI"), Hide("home")
    # computer
    imagebutton:
        xpos 1165
        ypos 395
        auto "button computer %s.png"
        action Show("computer")
    # poster
    imagebutton: 
        xpos 1600
        ypos 100
        auto "button poster %s.png"
        action Show("poster")
    # awards shelf
    imagebutton: 
        xpos 500
        ypos 100
        auto "button shelf %s.png"
        action Show("awards")
    # clickable patient sprites for waiting room 
    # viola button
    imagebutton:
        xpos 569
        ypos 403
        auto "sprite viola %s.png"
        action SetVariable("patientName", "viola"), Jump("startcaseViola")
    # teddy button
    imagebutton:
        xpos 288
        ypos 470
        auto "sprite teddy %s.png"
        action SetVariable("patientName", "teddy"), Jump("startcaseTeddy")
    # roc button
    imagebutton:
        xpos 141
        ypos 573
        auto "sprite roc %s.png"
        action SetVariable("patientName", "roc"), Jump("startcaseRoc")


screen menuUI(): 
    modal True
    frame: 
        background "bg lighten overlay.png"
        xalign 0.5
        yalign 0.5
        add "bg home menu.png"
        textbutton "Exit": 
            xpos 1780
            ypos 55
            action Hide("menuUI"), Jump("startHome")
        vbox: 
            style_prefix "choice"
            yalign 0.7
            textbutton _("Save Game") action ShowMenu('save')
            textbutton _("Load Game") action ShowMenu('load')
            textbutton _("Preferences") action ShowMenu('preferences')
            textbutton _("Exit to Title Screen") action MainMenu()



screen computer(): 
    modal True
    add "bg medicalfiles.png"
    textbutton "Exit": 
            xpos 1780
            ypos 55
            action Hide("computer")
    frame: 
        xalign 0.5
        yalign 0.5
        background None
        text "{b}Patient Records{/b}\n Select the patient whose record you would like to view.":
            size 45
            xalign 0.5
            yalign 0.25
            textalign 0.5
    # buttons for each patient to see patient records
        hbox: 
            style_prefix "profiles"
            xalign 0.5
            yalign 0.7
            spacing 100
            vbox: 
                imagebutton: 
                    auto "profiles viola %s.png"
                    action Hide("computer")
                text "Viola Phoenix"
            vbox: 
                imagebutton: 
                    auto "profiles roc %s.png"
                    action Hide("computer")
                text "Roc Garcia"
            vbox: 
                imagebutton: 
                    auto "profiles teddy %s.png"
                    action Hide("computer")
                text "Teddy Williams"

style profiles_text: 
    xalign 0.5
    font "Gilbert.otf"

screen poster(): 
    modal True
    add "bg poster.png"
    textbutton "Exit": 
            xpos 1780
            ypos 55
            action Hide("poster")
    frame: 
        text "Progress Roadmap": 
            xpos 250
            ypos 210
            font "Gilbert.otf"
            size 50
        background None
        # buttons for each module 
        imagebutton: 
            xpos 270
            ypos 320
            auto "bg unlocked module %s.png"
            action Hide("poster")
        imagebutton: 
            xpos 470
            ypos 310
            auto "bg unlocked module %s.png"
            action Hide("poster")
        imagebutton: 
            xpos 670
            ypos 310
            auto "bg current module %s.png"
            action Hide("poster")
        imagebutton: 
            xpos 870
            ypos 260
            auto "bg locked module %s.png"


screen awards():
    modal True
    add "bg awards.png"
    textbutton "Exit": 
            xpos 1780
            ypos 55
            action Hide("awards")

label startHome: 
    scene bg home screen
    show screen home

    m.c "This is the home screen!"

    m.c "This is where you will find your patients, begin patient visits, and review your progress." 


