# Clinic Home Screen
default awardsUnlocked = [False, False, False, False, False, False]
default searchName = None
default fullNames = {
    "viola": ["Viola Phoenix", "Transfeminine patient"],
    "roc": ["Roc Garcia", "Transmasculine patient"],
    "teddy": ["Teddy Williams", "Nonbinary patient"]
}

screen home(): 
    modal True
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
        textbutton "Back": 
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
        xpos 1762
        ypos 55
        action Hide("computer")
    frame: 
        xalign 0.5
        yalign 0.5
        background None
        vbox: 
            xalign 0.5
            yalign 0.3
            text "Patient Overview":
                font "Gilbert.otf"
                xalign 0.5
                size 50
                textalign 0.5
            text "Select the patient you would like to view.": 
                font "SourceSans3.ttf"
                xalign 0.5
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
                    action SetVariable("searchName", "viola"), Hide("computer"), Show("searchRecords")
                text "Viola Phoenix"
            vbox: 
                imagebutton: 
                    auto "profiles roc %s.png"
                    action SetVariable("searchName", "roc"), Hide("computer"), Show("searchRecords")
                text "Roc Garcia"
            vbox: 
                imagebutton: 
                    auto "profiles teddy %s.png"
                    action SetVariable("searchName", "teddy"), Hide("computer"), Show("searchRecords")
                text "Teddy Williams"

# options to look at medical record, conversation logs, replay past visits, etc.
screen searchRecords(): 
    modal True
    add "bg medicalfiles.png"
    textbutton "Back": 
            xpos 1550
            ypos 200
            action Hide("searchRecords"), Show("computer")
    frame: 
        background None
        xalign 0.5
        yalign 0.55
        hbox: 
            spacing 60
            vbox: 
                xalign 0.5
                yalign 0.5
                spacing 30
                text "[fullNames[searchName][0]]\n{font=SourceSans3.ttf}{size=35}[fullNames[searchName][1]]{/size}{/font}": 
                    font "Gilbert.otf"
                    size 50
                    xalign 0.5
                    text_align 0.5
                add "profiles [searchName] idle.png": 
                    xalign 0.5
                textbutton _("Start next visit!") action SetVariable("patientName", "viola"), Hide("searchRecords"), Jump("startcaseViola"): 
                    style_prefix "gnavigation"
                    xalign 0.5
            vbox: 
                style_prefix "searchRecords"
                spacing gui.choice_spacing
                textbutton _("Medical records") action Show("openPatientFile")
                textbutton _("Past visit recaps")
                textbutton _("Past conversations")
                textbutton _("Replay past visits")
                textbutton _("Learning material")

style searchRecords_button is default:
    properties gui.button_properties("choice_button")
    xsize 450
style searchRecords_button_text is default:
    properties gui.text_properties("choice_button")
    size 30

style profiles_text: 
    xalign 0.5
    font "Gilbert.otf"
    

screen poster(): 
    modal True
    add "bg poster.png"
    textbutton "Back": 
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
        imagebutton: 
            xpos 1095
            ypos 310
            auto "bg locked module %s.png"
        imagebutton: 
            xpos 1320
            ypos 330
            auto "bg locked module %s.png"
        imagebutton: 
            xpos 270
            ypos 560
            auto "bg current module %s.png"
            action Hide("poster")
        imagebutton: 
            xpos 470
            ypos 500
            auto "bg locked module %s.png"
        imagebutton: 
            xpos 670
            ypos 575
            auto "bg locked module %s.png"
        imagebutton: 
            xpos 865
            ypos 575
            auto "bg locked module %s.png"
        imagebutton: 
            xpos 1065
            ypos 575
            auto "bg locked module %s.png"
        imagebutton: 
            xpos 1265
            ypos 575
            auto "bg locked module %s.png"
        imagebutton: 
            xpos 1560
            ypos 560
            auto "bg locked module %s.png"
        imagebutton: 
            xpos 270
            ypos 820
            auto "bg current module %s.png"
            action Hide("poster")
        imagebutton: 
            xpos 470
            ypos 820
            auto "bg locked module %s.png"
        imagebutton: 
            xpos 690
            ypos 760
            auto "bg locked module %s.png"
        imagebutton: 
            xpos 910
            ypos 820
            auto "bg locked module %s.png"
        imagebutton: 
            xpos 1120
            ypos 830
            auto "bg locked module %s.png"
        imagebutton: 
            xpos 1340
            ypos 810
            auto "bg locked module %s.png"

screen awards():
    modal True
    add "bg awards.png"
    text "Awards and Badges":
        font "Gilbert.otf"
        xalign 0.9
        yalign 0.2
        size 60

    textbutton "Back": 
            xpos 1780
            ypos 55
            action Hide("awards")
    frame: 
        background None
        xpos 200
        ypos 200
        # shelf for trophy awards
        grid 3 2: 
            spacing 100
            imagebutton: 
                yalign 1.0
                auto "awards trophy %s.png"
                action NullAction()
                sensitive awardsUnlocked[0]
            imagebutton: 
                yalign 1.0
                auto "awards star %s.png"
                action NullAction()
                sensitive awardsUnlocked[1]
            imagebutton: 
                yalign 1.0
                auto "awards plaque %s.png"
                action NullAction()
                sensitive awardsUnlocked[2]
            
            imagebutton: 
                yalign 1.0
                auto "awards plaque %s.png"
                action NullAction()
                sensitive awardsUnlocked[3]
            imagebutton: 
                yalign 1.0
                auto "awards globe %s.png"
                action NullAction()
                sensitive awardsUnlocked[4]
            imagebutton: 
                yalign 1.0
                auto "awards trophy %s.png"
                action NullAction()
                sensitive awardsUnlocked[5]
        use badges
        
screen badges(): 
    modal True
# badges for nametag swag
    frame: 
        background "badge blank.png"
        xpos 965
        ypos 125
        vbox: 
            xalign 0.03
            yalign 0.25
            xmaximum 350
            text "[player.name]": 
                font "Gilbert.otf"
                line_spacing -20
                size 50
            text "{b}Pronouns:{/b} [player.pronouns]": 
                font "SourceSans3.ttf"
                size 36
        draggroup: 
            drag: 
                drag_name "Ear"
                drag_raise True
                draggable True
                mouse_drop True
                child "badge unlocked ear.png"
            drag: 
                drag_name "Ribbon"
                drag_raise True
                draggable True
                mouse_drop True
                child "badge unlocked ribbon.png"
            drag:
                drag_name "Heart"
                drag_raise True
                draggable True
                mouse_drop True
                child "badge unlocked heart.png"
    



label startHome: 
    scene bg home screen
    show screen home

    mentor.char "This is the home screen!"

    mentor.char "This is where you will find your patients, begin patient visits, and review your progress." 
    return
