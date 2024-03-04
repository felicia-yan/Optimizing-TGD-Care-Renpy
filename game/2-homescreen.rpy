# Clinic Home Screen

screen home(): 
    # menu button
    textbutton "Menu": 
        xpos 1762
        ypos 55
        action Jump("homeMenu")
    
    # computer
    imagebutton:
        xpos 1165
        ypos 395
        auto "button computer %s.png"
        action Jump("homeComputer")

    # poster
    imagebutton: 
        xpos 1600
        ypos 100
        auto "button poster %s.png"
        action Jump("homePoster")

    # awards shelf
    imagebutton: 
        xpos 500
        ypos 100
        auto "button shelf %s.png"
        action Jump("homeAwards")
    
    # clickable patient sprites for waiting room 
    # viola button
    imagebutton:
        xpos 569
        ypos 403
        auto "sprite viola %s.png"
        action SetVariable("patientName", "viola"), Jump("caseViola")
    # teddy button
    imagebutton:
        xpos 288
        ypos 470
        auto "sprite teddy %s.png"
        action SetVariable("patientName", "teddy"), Jump("caseTeddy")
    # roc button
    imagebutton:
        xpos 141
        ypos 573
        auto "sprite roc %s.png"
        action SetVariable("patientName", "roc"), Jump("caseRoc")

label homeMenu(): 
    show screen menuUI
    menu: 
        "Save Game": 
            pass
        "Load Game": 
            pass
        "Options": 
            pass 
        "Exit to Title Screen": 
            $ MainMenu(confirm=False)()

screen menuUI(): 
    frame: 
        xalign 0.5
        yalign 0.5
        add "bg home menu.png"
        textbutton "Exit": 
            xpos 1762
            ypos 55
            action Hide("menuUI"), Jump("startHome")

"""
screen computer(): 
screen poster(): 
screen awards(): 
    text "Awards" 

label homeComputer: 
    show screen computer

label homePoster: 
    show screen poster

label homeAwards: 
    show screen 
"""

label startHome: 
    scene bg home screen
    show screen home

    m.c "home screen!"

    m.c "this is the home screen!"


