# Clinic Home Screen
default awardsUnlocked = [False, False, False, False, False, False]
default searchName = None
default fullNames = {
    "viola": ["Viola Phoenix", "Transfeminine patient"],
    "roc": ["Roc Garcia", "Transmasculine patient"],
    "olivia": ["Olivia Li", "Nonbinary patient"]
}

screen home(): 
    # music 
    on "show" action Play("music", "waiting_room_mario_version.mp3", loop=True, fadein=3)
    on "hide" action Stop("music", fadeout=2)

    # menu button
    textbutton "Menu": 
        style_prefix "player_select"
        xpos 125
        ypos 55
        action Hide("home"), Show("menuUI")
    
    # computer
    imagebutton:
        xpos 350
        ypos 360
        idle Image("BG_WaitingRoom_PatientProfile_Idle.png", oversample = 2)
        hover Image("BG_WaitingRoom_PatientProfile_Hover.png", oversample = 2)
        tooltip "{font=Gilbert.otf}{size=40}Computer{/size}{/font} \nReview patient records"
        action Show("computer")
    # poster
    imagebutton: 
        xpos 860
        ypos 140
        idle Image("BG_WaitingRoom_Achievement_Idle.png", oversample = 2)
        hover Image("BG_WaitingRoom_Achievement_Hover.png", oversample = 2)
        tooltip "{font=Gilbert.otf}{size=40}Roadmap{/size}{/font} \nCheck game progress"
        action Show("poster")
    # awards items
    imagebutton: 
        xpos 250
        ypos 300
        idle Image("BG_WaitingRoom_PlayerProgresss_Idle.png", oversample = 2)
        hover Image("BG_WaitingRoom_PlayerProgresss_Hover.png", oversample = 2)
        tooltip "{font=Gilbert.otf}{size=40}{color=#00B3E3}Good Listener Award{/color}{/size}{/font} \n {i}Viola Visit 2{/i}\n You were an empathetic and caring listener in this visit!"
        action Show("awards")
    
    # clickable patient sprites for waiting room 
    # viola button
    imagebutton:
        xpos 569
        ypos 460
        auto "sprite viola %s.png"
        tooltip "{font=Gilbert.otf}{size=40}{color=#7689ED}Viola{/color}{/size}{/font}"
        action SetVariable("patientName", "viola"), Show("visitSelect", visitSelectPatient="viola")
    # olivia button
    imagebutton:
        xpos 1700
        ypos 350
        auto "sprite teddy %s.png"
        tooltip "{font=Gilbert.otf}{size=40}{color=#7689ED}Olivia{/color}{/size}{/font}"
        action SetVariable("patientName", "olivia"), Show("visitSelect", visitSelectPatient="olivia")
    # roc button
    imagebutton:
        xpos 950
        ypos 550
        auto "sprite roc %s.png"
        tooltip "{font=Gilbert.otf}{size=40}{color=#7689ED}Roc{/color}{/size}{/font}"
        action SetVariable("patientName", "roc"), Show("visitSelect", visitSelectPatient="roc")
    
    # tooltips for buttons when hovered over
    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                background Frame("tooltip.png")
                padding (25, 25)
                xalign 0.5
                xmaximum 450
                text tooltip: 
                    text_align 0.5
                    size 32

screen menuUI(): 
    modal True
    frame: 
        background "bg player select.png"
        xalign 0.5
        yalign 0.5
        textbutton "Back": 
            style_prefix "player_select"
            xpos 125
            ypos 965
            action Hide("menuUI"), Show("home")
        vbox: 
            style_prefix "choice"
            xalign 0.5
            yalign 0.5
            text "Menu": 
                font "Gilbert.otf"
                size 60
                xalign 0.5
            textbutton _("Save Game") action ShowMenu('save')
            textbutton _("Load Game") action ShowMenu('load')
            textbutton _("Options") action ShowMenu('options')
            textbutton _("Exit to Title Screen") action MainMenu()


# first computer screen, buttons for each character profile
screen computer(): 
    modal True
    add "bg player select.png"
    frame: 
        xalign 0.5
        yalign 0.5
        background None

        textbutton "Back": 
            style_prefix "player_select"
            xpos 125
            ypos 965
            action Hide("computer"), Show("home")

        vbox: 
            xalign 0.5
            yalign 0.05
            text "Select a patient to view their medical records":
                font "Gilbert.otf"
                xalign 0.5
                size 45
                textalign 0.5
                color "#FFFFFF"

    # buttons for each patient to see patient records
        hbox: 
            style_prefix "player_select"
            xalign 0.5
            yalign 0.7
            spacing 50
            vbox: 
                add "player select viola.png"
                textbutton "Viola": 
                    action SetVariable("searchName", "viola"), Hide("computer"), Show("searchRecords")
            vbox: 
                add "player select roc.png"
                textbutton "Roc":
                    action SetVariable("searchName", "roc"), Hide("computer"), Show("searchRecords")
            vbox: 
                add "player select olivia.png"
                textbutton "Olivia":
                    action SetVariable("searchName", "olivia"), Hide("computer"), Show("searchRecords")

style player_select_button is default:
    properties gui.button_properties("choice_button")
    xsize 180
    xalign 0.5
    ypos -650

style player_select_button_text: 
    xalign 0.5
    size 40
    idle_color "#FFFFFF"
    hover_color "#026F9D"


# screen for when player clicks on patient in the waiting room to preview upcoming visit
screen visitSelect(visitSelectPatient): 
    modal True
    add "bg player select.png"
    frame: 
        xalign 0.5
        yalign 0.5
        background None

        textbutton "Back": 
            style_prefix "player_select"
            xpos 125
            ypos 965
            action Hide("visitSelect"), Show("home")

        vbox: 
            xalign 0.5
            yalign 0.05
            text "Preview the next visit":
                font "Gilbert.otf"
                xalign 0.5
                size 45
                textalign 0.5
                color "#FFFFFF"

    # layout for 
        hbox: 
            style_prefix "player_select"
            xalign 0.5
            yalign 0.7
            spacing 60
            vbox: 
                add "player select [visitSelectPatient].png"
                text "[fullNames[visitSelectPatient][0]]": 
                    style_prefix "visit_select_title"
                    ypos -650
            vbox: 
                xsize 750
                spacing 20
                text "VISIT 1": 
                    style_prefix "visit_select_title"
                    xalign 0.0
                    size 50
                text "Estimated time: 10 minutes"

                frame: 
                    xfill True
                    yminimum 150
                    padding (20, 20)
                    background Frame("visit yellow text bg.png", 0, 0)
                    text "Summary"
                
                text "Learning Objectives": 
                    style_prefix "visit_select_title"
                    size 40
                    xalign 0.0
                frame: 
                    xfill True
                    yminimum 150
                    padding (20, 20)
                    background Frame("visit yellow text bg.png", 0, 0)
                    text "Objectives"
                
                hbox: 
                    xalign 0.5
                    ypos 40
                    spacing 100
                    style_prefix "visit_select"
                    textbutton _("Review files") action SetVariable("searchName", "roc"), Hide("visitSelect"), Show("searchRecords")
                    textbutton _("Begin visit") action SetVariable("patientName", "viola"), Hide("visitSelect"), Jump("startcaseViola")
                
style visit_select_title_text: 
    font "Gilbert.otf"
    xalign 0.5
    size 45
    textalign 0.5
    color "#000000"

style visit_select_button: 
    properties gui.button_properties("choice_button")
    xsize 300
    padding (20, 20)

style visit_select_button_text: 
    xalign 0.5
    size 40
    idle_color "#FFFFFF"
    hover_color "#026F9D"


default currentRecordsTab = "emr"
# options to look at medical record, conversation logs, replay past visits, etc.
screen searchRecords(): 
    on "hide" action SetVariable("currentRecordsTab", "emr")

    modal True
    add "bg searchrecords.png"
    textbutton "Back": 
            style_prefix "player_select"
            xpos 130
            ypos 970
            action Hide("searchRecords"), Show("computer")

    frame: 
        background None
        xalign 0.5
        yalign 0.5

        hbox: 
            spacing 80
            vbox: 
                xalign 0.5
                yalign 0.5
                spacing 30
                text "[fullNames[searchName][0]]\n{font=SourceSans3.ttf}{size=35}[fullNames[searchName][1]]{/size}{/font}": 
                    font "Gilbert.otf"
                    size 50
                    xalign 0.5
                    text_align 0.5
                add "records headshot [searchName].png": 
                    xalign 0.5
                textbutton _("Begin visit") action SetVariable("patientName", "viola"), Hide("searchRecords"), Jump("startcaseViola"): 
                    style_prefix "gnavigation"
                    xalign 0.5
                    xsize 350

            hbox: 
                spacing 0
                # button tabs to select which page to go to 
                vbox: 
                    xalign 0.2
                    yalign 0.4
                    imagebutton: 
                        idle "records tab emr.png"
                        action SetVariable("currentRecordsTab", "emr")
                    imagebutton: 
                        idle "records tab recaps.png"
                        action SetVariable("currentRecordsTab", "recaps")
                    imagebutton: 
                        idle "records tab convos.png"
                        action SetVariable("currentRecordsTab", "convos")
                    imagebutton: 
                        idle "records tab replay.png"
                        action SetVariable("currentRecordsTab", "replay")
                    imagebutton: 
                        idle "records tab learning.png"
                        action SetVariable("currentRecordsTab", "learning")
                
                # scrollable viewport for different tabs of record
                side "c": 
                    area (0, 175, 1100, 1000)
                    viewport id "vp": 
                        draggable True
                        arrowkeys True
                        mousewheel True
                        scrollbars "vertical"
                        xsize 1100
                        ysize 1000
                        frame: 
                            xfill True
                            yminimum 920
                            xalign 0.5
                            padding (0, 40)
                            background Frame("records bg [currentRecordsTab].png", 10, 10)
                            if (currentRecordsTab == "emr"):
                                vbox:
                                    xalign 0.5
                                    text "Electronic Medical Record":
                                        style_prefix "searchRecords_title"
                            
                            if (currentRecordsTab == "recaps"):
                                vbox:
                                    xalign 0.5
                                    text "Visit Recaps":
                                        style_prefix "searchRecords_title"
                            
                            if (currentRecordsTab == "convos"):
                                vbox:
                                    xalign 0.5
                                    text "Past Conversations":
                                        style_prefix "searchRecords_title"
                            
                            if (currentRecordsTab == "replay"):
                                vbox:
                                    xalign 0.5
                                    text "Replay Past Visits":
                                        style_prefix "searchRecords_title"
                            
                            if (currentRecordsTab == "learning"):
                                vbox:
                                    xalign 0.5
                                    text "Learning Materials":
                                        style_prefix "searchRecords_title"

            # vbox: 
            #     style_prefix "searchRecords"
            #     spacing gui.choice_spacing
                
            #     textbutton _("Medical records") action Show("openPatientFile")
            #     textbutton _("Past visit recaps")
            #     textbutton _("Past conversations")
            #     textbutton _("Replay past visits")
            #     textbutton _("Learning material")

style searchRecords_title_text: 
    font "Gilbert.otf"
    size 45
    xalign 0.5

style profiles_text: 
    xalign 0.5
    font "Gilbert.otf"
    

screen poster(): 
    modal True
    add "bg blank.png"
    text "Progress Roadmap":
        font "Gilbert.otf"
        xpos 60
        ypos 80
        size 50
    textbutton "Back": 
        xpos 1780
        ypos 55
        action Hide("poster")

    # scrollable viewport for roadmap
    side "c": 
        area (0, 80, 4050, 1080)

        viewport id "vp":
            draggable True
            arrowkeys True
            mousewheel True
            scrollbars "horizontal"
            xsize 1900
            ysize 1000

            frame: 
                background "bg roadmap.png" 
                yalign 0.6
                xalign 0.5
                margin (100, 100)
                hbox: 
                    spacing 100
                    style_prefix "roadmap"
                    hbox: 
                        spacing 120
                        yalign 0.5
                        textbutton "Introduction" action Hide("poster"), Hide("home"), Jump("start")
                        textbutton "Orientation" action Hide("poster"), Hide("home"), Jump("tutorial")
                        textbutton "Home Screen" action Hide("poster"), Hide("home"), Jump("startHome")
                    vbox: 
                        spacing 120
                        hbox:
                            spacing 100 
                            textbutton "Roc: Visit 1"
                            textbutton "Roc: Visit 2"
                            textbutton "Roc: Visit 3"
                            textbutton "Mini-Case: Family Building"
                            textbutton "Roc: Visit 4"
                            textbutton "Mini-Case: Insurance"
                            textbutton "Roc: Visit 5"
                        hbox:
                            spacing 100 
                            textbutton "Viola: Visit 1" action Hide("poster"), Hide("home"), Jump("startViola_Visit_1")
                            textbutton "Viola: Visit 2"
                            textbutton "Mini-Case: E.D. Service Recovery"
                            textbutton "Viola: Visit 3"
                            textbutton "Viola: Visit 4"
                            textbutton "Viola: Visit 5"
                        hbox:
                            spacing 100 
                            textbutton "Olivia: Visit 1"
                            textbutton "Mini-Case: Teaching Strategies"
                            textbutton "Olivia: Visit 2"
                            textbutton "Mini-Case: Upstander/Bystander"
                            textbutton "Viola: Visit 3"



style roadmap_button:
    background "#f0f0f0"
    padding (10, 10)
    xsize 230
    ysize 140
    xalign 0.5

style roadmap_button_text:
    xalign 0.5
    textalign 0.5
    color "#2a2a2a"
    hover_color "#5330dd"
    font "Gilbert.otf"



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

    # Add Key Event that signifies end or introduction/progress GA4
    $ analytics.event("homescreen", "start_homescreen")

    image bg_waitingroom = Image("BG_WaitingRoom.png", oversample = 2)
    scene bg_waitingroom
    show screen home

    mentor.char "This is the home screen!"

    $ achievement.grant("Getting Oriented")

    mentor.char "This is where you will find your patients, begin patient visits, and review your progress." 
    call screen home
    
    return
