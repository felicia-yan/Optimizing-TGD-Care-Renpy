# Clinic Home Screen


# achievement system to track completion of modules 
init python: 
    g = Gallery()
    g.button("patient1visit1")
    g.condition("persistent.finish_patient1visit1")
    g.button("patient2visit1")
    g.condition("persistent.finish_patient2visit1")
    g.button("patient3visit1")
    g.condition("persistent.finish_patient3visit1")



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


# screen computer(): 

#screen poster(): 
    # add "bg poster.png"

screen awards():
    grid 3 1:  
        add g.make_button("patient1visit1", "patient1visit1", xalign=0.5, yalign=0.5)
        add g.make_button("patient2visit1", "patient2visit1", xalign=0.5, yalign=0.5)
        add g.make_button("patient3visit1", "patient3visit1", xalign=0.5, yalign=0.5)

label startHome: 
    scene bg home screen
    show screen home

    m.c "home screen!"

    m.c "this is the home screen!"

    return 


