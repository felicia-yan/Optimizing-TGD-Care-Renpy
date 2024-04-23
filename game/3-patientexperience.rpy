# Basic Patient Experience

# ui screens for patient interaction
# clipboard button in upper left for opening files
screen clipboard(): 
    imagebutton:
        xalign 0.98
        yalign 0.36
        auto "files clipboard %s.png"
        action Show("allMedicalFiles")

screen pencil(): 
    imagebutton: 
        xalign 0.98
        yalign 0.2
        auto "button pencil %s.png"
        action Show("notepad"), Hide("pencil"), Hide("clipboard"), Hide("lookup"),

screen lookup(): 
    imagebutton: 
        xalign 0.98
        yalign 0.06
        auto "button search %s.png"
        action Show("glossary"), Hide("pencil"), Hide("clipboard"), Hide("lookup"),

# show all patient folders to choose from 
screen allMedicalFiles(): 
    modal True
    add "bg medicalfiles.png"
    textbutton "Exit": 
        xpos 1762
        ypos 55
        action Hide("allMedicalFiles"), Show("clipboard")
    text "Electronic Medical Records":
        font "Gilbert.otf"
        xalign 0.5
        yalign 0.2
        size 50
    text "Select a folder to view a patient's record.": 
        font "SourceSans3.ttf"
        xalign 0.5
        yalign 0.25
        textalign 0.5
    grid 3 2: 
        xalign 0.5
        yalign 0.7
        spacing 60
        imagebutton: 
            auto "files folder %s.png"
            action Show("openPatientFile"), Hide("allMedicalFiles"), SetVariable("searchName", "viola")
        imagebutton: 
            auto "files folder %s.png"
            action Show("openPatientFile"), Hide("allMedicalFiles"), SetVariable("searchName", "roc")
        imagebutton: 
            auto "files folder %s.png"
            action Show("openPatientFile"), Hide("allMedicalFiles"), SetVariable("searchName", "teddy")
    

# show medical info for patient selected
screen openPatientFile():
    modal True
    add "bg medicalfiles.png"
    # exit button
    textbutton "Exit": 
        xpos 1762
        ypos 55
        action Hide("openPatientFile")

    # scrollable viewport for medical information
    side "c": 
        area (300, 200, 1550, 860)

        viewport id "vp": 
            draggable True
            arrowkeys True
            mousewheel True
            scrollbars "vertical"
            xsize 1350
            ysize 700

            if searchName == "viola": 
                vbox: 
                    text "Patient name: {color=#00B3E3}[violaFile['Full name']]{/color}":
                        font "Gilbert.otf"
                        size 45
                    text "Patient Identification Information":
                        font "Gilbert.otf"
                        size 40
                    frame: 
                        background "#EEEEEE"
                        padding (50, 50)
                        xfill True
                        vbox: 
                            text "{b}Legal Name:{/b} [violaFile['Legal name']]"
                            text "{b}Pronouns:{/b} [violaFile['Pronouns']]"
                            text "{b}DOB:{/b} [violaFile['DOB']]"
                            text "{b}Gender:{/b} [violaFile['Gender']]"
                            text "{b}Sex at Birth:{/b} [violaFile['Sex at birth']]"
                            text "{b}Address:{/b} [violaFile['Address']]"
                            text "{b}Race:{/b} [violaFile['Race']]"


                    text "Medical History":
                        font "Gilbert.otf"
                        size 40
                    frame: 
                        background "#EEEEEE"
                        padding (50, 50)
                        xfill True
                        vbox: 
                            text "{b}Chronic conditions:{/b} [violaFile['Chronic conditions']]"
                            text "{b}Previous surgeries:{/b} [violaFile['Previous surgeries']]"
                            text "{b}Additional information:{/b} [violaFile['Additional information']]"

                    text "Medication list:":
                        font "Gilbert.otf"
                        size 40
                    frame:
                        background "#EEEEEE"
                        padding (50, 50)
                        xfill True
                        vbox: 
                            text "[violaFile['Medication list']]"

                    text "Consultation notes:":
                        font "Gilbert.otf"
                        size 40
                    frame: 
                        background "#EEEEEE"
                        padding (50, 50)
                        xfill True
                        vbox: 
                            text "[violaFile['Consultation notes']]"
            
            if searchName == "roc": 
                vbox: 
                    text "Patient name: {color=#00B3E3}[rocFile['Full name']]{/color}":
                        font "Gilbert.otf"
                        size 45
                    text "Patient Identification Information":
                        font "Gilbert.otf"
                        size 40
                    frame: 
                        background "#EEEEEE"
                        padding (50, 50)
                        xfill True
                        vbox: 
                            text "{b}Legal Name:{/b} [rocFile['Legal name']]"
                            text "{b}Pronouns:{/b} [rocFile['Pronouns']]"
                            text "{b}DOB:{/b} [rocFile['DOB']]"
                            text "{b}Gender:{/b} [rocFile['Gender']]"
                            text "{b}Sex at Birth:{/b} [rocFile['Sex at birth']]"
                            text "{b}Address:{/b} [rocFile['Address']]"
                            text "{b}Race:{/b} [rocFile['Race']]"


                    text "Medical History":
                        font "Gilbert.otf"
                        size 40
                    frame: 
                        background "#EEEEEE"
                        padding (50, 50)
                        xfill True
                        vbox: 
                            text "{b}Chronic conditions:{/b} [rocFile['Chronic conditions']]"
                            text "{b}Previous surgeries:{/b} [rocFile['Previous surgeries']]"
                            text "{b}Additional information:{/b} [rocFile['Additional information']]"

                    text "Medication list:":
                        font "Gilbert.otf"
                        size 40
                    frame:
                        background "#EEEEEE"
                        padding (50, 50)
                        xfill True
                        vbox: 
                            text "[rocFile['Medication list']]"

                    text "Consultation notes:":
                        font "Gilbert.otf"
                        size 40
                    frame: 
                        background "#EEEEEE"
                        padding (50, 50)
                        xfill True
                        vbox: 
                            text "[rocFile['Consultation notes']]"
            if searchName == "teddy": 
                vbox: 
                    text "Patient name: {color=#00B3E3}[teddyFile['Full name']]{/color}":
                        font "Gilbert.otf"
                        size 45
                    text "Patient Identification Information":
                        font "Gilbert.otf"
                        size 40
                    frame: 
                        background "#EEEEEE"
                        padding (50, 50)
                        xfill True
                        vbox: 
                            text "{b}Legal Name:{/b} [teddyFile['Legal name']]"
                            text "{b}Pronouns:{/b} [teddyFile['Pronouns']]"
                            text "{b}DOB:{/b} [teddyFile['DOB']]"
                            text "{b}Gender:{/b} [teddyFile['Gender']]"
                            text "{b}Sex at Birth:{/b} [teddyFile['Sex at birth']]"
                            text "{b}Address:{/b} [teddyFile['Address']]"
                            text "{b}Race:{/b} [teddyFile['Race']]"


                    text "Medical History":
                        font "Gilbert.otf"
                        size 40
                    frame: 
                        background "#EEEEEE"
                        padding (50, 50)
                        xfill True
                        vbox: 
                            text "{b}Chronic conditions:{/b} [teddyFile['Chronic conditions']]"
                            text "{b}Previous surgeries:{/b} [teddyFile['Previous surgeries']]"
                            text "{b}Additional information:{/b} [teddyFile['Additional information']]"

                    text "Medication list:":
                        font "Gilbert.otf"
                        size 40
                    frame:
                        background "#EEEEEE"
                        padding (50, 50)
                        xfill True
                        vbox: 
                            text "[teddyFile['Medication list']]"

                    text "Consultation notes:":
                        font "Gilbert.otf"
                        size 40
                    frame: 
                        background "#EEEEEE"
                        padding (50, 50)
                        xfill True
                        vbox: 
                            text "[teddyFile['Consultation notes']]"



# alerts for status of relationship with patient
screen patientStatus(status, statusMessage): 
    style_prefix "statusUI"
    hbox: 
        xalign 0.5
        yalign 0.1
        spacing 20
        frame: 
            background Frame("gui/bg status.png")
            padding (80, 30)

            hbox: 
                box_wrap True 
                xalign 0.5 
                yalign 0.5 
                spacing 30
                text "[patientName.upper()]":
                    yalign 0.5
                    font "Gilbert.otf"
                    color "#000000"
                    size 45

                if status == "positive": 
                    text "{b}▲ [statusMessage!tq]{/b}": 
                        color "#00B3E3"
                        size 45
                if status == "neutral": 
                    text "{b}➖ [statusMessage!tq]{/b}": 
                        color "#575757"
                        size 45    
                if status == "negative":
                    text "{b}▼ [statusMessage!tq]{/b}": 
                        color "#DE4A4A"
                        size 45
        
    timer 3.75 action Hide('patientStatus')

style statusUI_text: 
    size 35

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

# notepad screen for player to take notes
screen notepad(): 
    modal True
    add "bg notepad.png"
    text "Notepad": 
        font "Gilbert.otf"
        xalign 0.5
        yalign 0.11
        size 45
        textalign 0.5
    textbutton "Close":
        xpos 1762
        ypos 55
        action Hide("notepad"), Show("pencil"), Show("clipboard"), Show("lookup")
    frame: 
        background None
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 750
        has vbox
        input: 
            default ""
            value VariableInputValue('notes') 
            color "#000000"
            copypaste True
            multiline True

# look up screen for glossary of clinial reference material
screen glossary(): 
    modal True
    textbutton "Exit": 
        xpos 1762
        ypos 55
        action Hide("glossary"), Show("pencil"), Show("clipboard"), Show("lookup")
    frame: 
        background "bg glossary.png"
        xalign 0.5
        yalign 0.2
        padding (40, 40)
        vbox: 
            spacing 20
            text "Glossary" size 50 xalign 0.5 ypos 20 font "Gilbert.otf"
            hbox: 
                xalign 0.5
                spacing 30
                add "mini search icon.png"
                frame: 
                    background "bg searchbox.png"
                    xsize 800
                    xalign 0.5
                    input: 
                        default ""
                        value VariableInputValue('glossarySearchTerm') 
                        color "#000000"
                        copypaste True
                        pixel_width 735
                        first_indent 30

            hbox spacing 50:
                viewport:
                    xsize 300 ysize 700
                    child_size (None, 4000)
                    scrollbars "vertical"
                    spacing 5
                    draggable True
                    mousewheel True
                    arrowkeys True
                    vbox spacing 20:
                        for word in glossaryTerms: 
                            if (glossarySearchTerm == "") or (glossarySearchTerm.lower() in word.lower()): 
                                textbutton word:
                                    action SetVariable("display_desc", word)
                vbox xsize 800 ysize 700 box_wrap True:
                    text glossaryTerms.get(display_desc, ""): 
                        color "#000000"


# scorecard screen for end of visit
screen scorecard(): 
    add "bg scorecard.png"
    side "c": 
            area (1125, 150, 1600, 810)

            viewport id "scores": 
                draggable True
                arrowkeys True
                mousewheel True
                scrollbars "vertical"
                xsize 620
                ysize 840

                vbox: 
                    spacing 20
                    text "Scorecard": 
                        font "Gilbert.otf"
                        size 50
                        xalign 0.5
                        line_leading 50
                    frame:  
                        background "#E2F9FF"
                        padding (50, 50)
                        xfill True
                        hbox:   
                                spacing 10
                                add "scorecard filled checkbox.png"
                                text "Used correct pronouns for patient": 
                                    yalign 0.5
                    frame:  
                        background "#FFFFFF"
                        padding (50, 50)
                        xfill True
                        hbox:   
                                spacing 10
                                add "scorecard blank checkbox.png"
                                text "Asked about sexual history appropriately": 
                                    yalign 0.5
                    frame:  
                        background "#FFFFFF"
                        padding (50, 50)
                        xfill True
                        hbox:   
                                spacing 10
                                add "scorecard blank checkbox.png"
                                text "Was thorough in clinical history": 
                                    yalign 0.5
                    frame:  
                        background "#E2F9FF"
                        padding (50, 50)
                        xfill True
                        hbox:   
                                spacing 30
                                add "scorecard filled checkbox.png"
                                text "Made patient feel comfortable": 
                                    yalign 0.5
                    text "Summary": 
                        font "Gilbert.otf"
                        size 50
                        xalign 0.5
                    text "You made 2/4 choices to optimize their patient's gender-affirming care!": 
                        xalign 0.5
        
# getting award screen for end of visit 
screen getAward(awardIndex): 
    modal True
    add "bg getaward.png"
    frame: 
        background None
        xalign 0.5
        vbox: 
            xalign 0.5
            yalign 0.05
            text "Unlocked!": 
                font "Gilbert.otf"
                size 100
                xalign 0.5
                color "#00B3E3"
            text "You've unlocked an award for your clinic!": 
                xalign 0.5
        vbox: 
            xalign 0.5
            yalign 0.55
            xmaximum 500
            spacing 20
            text "Good Listener!": 
                font "Gilbert.otf"
                size 60
                xalign 0.5
                color "#000000"
            text "Achieved the best ending for Viola's first visit": 
                size 35
                textalign 0.5
            add "awards trophy idle.png": 
                xalign 0.5
            textbutton _("Accept") action SetDict(awardsUnlocked, awardIndex, True), Hide("getAward"), Hide("clipboard"), Hide("pencil"), Hide("lookup"), Jump("startHome"): 
                            style_prefix "gnavigation"
                            xalign 0.5

                                


# start patient interaction
label startcaseViola: 
        hide screen home
        scene bg patient room
        with fade
        show screen clipboard
        show screen pencil
        show screen lookup
        $ searchName = patientName

        $ viola = Patient(Character("Viola", color="#FFFFFF"), "Viola", 24, "female", "she/her", "pink", "swimming", "vanilla")

        mentor.char "You've started Viola's case!"

        mentor.char "The patient's name is [viola.name], age is [viola.age], and pronouns are [viola.pronouns]."

        viola.char "Hi! I'm Viola!"

        mentor.char "To get started, you'll want to review her medical file."

        mentor.char "Click on the clipboard to see all the files you have on hand, and select the one for your patient, Viola."

        menu: 
            "Great response": 
                $ decisionScores[0] = 10
                show screen patientStatus("positive", "trusting")
                viola.char "Thanks! I feel supported and I trust you more."

            "Ok response": 
                $ decisionScores[0] = 5
                show screen patientStatus("positive", "trusting")
                viola.char "I guess that's ok."

            "Bad response":
                $ decisionScores[0] = 1
                show screen patientStatus("negative", "distrusting")
                viola.char "That was not a good choice. I don't feel good about what you said to me."


        label caseViolacontinue1: 
            mentor.char "You'll be presented with 2 more decisions to make for this patient interaction."

        menu: 
            "Great response": 
                $ decisionScores[1] = 10
                show screen patientStatus("positive", "comfort")
                viola.char "I feel more comfortable with you as my physician."

            "Ok response": 
                $ decisionScores[1] = 5
                show screen patientStatus("neutral", "uncomfortable")
                viola.char "I feel a bit uncomfortable."

            "Bad response":
                $ decisionScores[1] = 1
                show screen patientStatus("negative", "embarrassed")
                viola.char "I feel embarrassed and very uncomfortable."
            

        label caseViolacontinue2: 
        mentor.char "This is the last choice in this section."
    
        menu: 
            "Great response": 
                $ decisionScores[2] = 10
                show screen patientStatus("positive", "happy")
                viola.char "I feel very good about the outcome of this visit."

            "Ok response": 
                $ decisionScores[2] = 5
                show screen patientStatus("neutral", "content")
                viola.char "This wasn't the best visit, but it was alright."

            "Bad response":
                $ decisionScores[2] = 1
                show screen patientStatus("negative", "angry")
                viola.char "This was a horrible visit. I won't be back."


        label learner_debrief: 
            mentor.char "The patient visit is over." 
            show screen scorecard
            if decisionScores[0] == 10: 
                mentor.char "You used the correct pronouns for Viola, gaining her trust."

                mentor.char "You were a caring and empathetic listener."

            
            if decisionScores[0] == 5: 
                mentor.char "You addressed Viola as she asked to be addressed, though you seemed hesitant."
            if decisionScores[0] == 1: 
                mentor.char "You started the interaction by misgendering Viola, losing her trust."
            
            if decisionScores.count(10) == 3:
                mentor.char "Great job! You made choices that optimized Viola's gender-affirming care."
            if decisionScores.count(10) == 2:
                mentor.char "Overall, the patient interaction was mostly good, with some inappropriate choices."
            if decisionScores.count(10) == 1:
                mentor.char "Unfortunately, the quality of care for Viola was not adequate. She was uncomfortable and felt unsupported."
            
            hide screen scorecard
            call screen getAward(0)
            return

            



label violaPreVisit1: 
    $ s1 = Person(Character("Staff 1", color="#FFFFFF"), "Staff 1", 30, "female") 
    $ s2 = Person(Character("Staff 2", color="#FFFFFF"), "Staff 2", 30, "female") 

    
    player.char "What's going on? Did something happen?"

    s1.char "You won't believe this. THE Viola Phoenix is coming in today."

    player.char "Viola Phoenix?"

    s1.char "You don't know her? She's all over the news. Look at this: 'Viola Phoenix—a trans filmmaker whose controversial film was banned from film festivals.'"

    s2.char "Yep, I follow her on Instagram. She's been blowing up on social media lately."

    s1.char "Have you seen her vlogs? They're some of the best on Youtube. No wonder she's making it big."

    s2.char "Yeah, I can't believe she's coming here."

    s1.char "This could totally 'make or break' our reputation. What if we show up in one of her vlogs?"

    s2.char "That would be so cool."



    mentor.char "Let's look over Viola's case before her visit." 
    
    mentor.char "Click on the clipboard to see all the files you have on hand, and select the one for your patient, Viola."

    mentor.char "When you're ready, let's review some of the important information. You can and should always refer back to her file if you don't remember."

    label whatMedication:
    mentor.char "What medication is Viola currently taking that is relevant to her gender-affirming care?"
 
    menu: 
        "Estradiol": 
            mentor.char "Yes, exactly!" 

            label whatIsEstradiol:
            mentor.char "What hormone is estradiol?" 

            menu:
                "Insulin": 
                    mentor.char "Not quite."
                    jump whatIsEstradiol
                "Testosterone": 
                    mentor.char "Almost! Testestorone is actually the corresponding male sex hormone."
                    jump whatIsEstradiol
                "Progesterone": 
                    mentor.char "Good guess, but not exactly!"
                    jump whatIsEstradiol
                "Estrogen":  
                    mentor.char "Indeed! Estradiol is the form of estrogen primarily produced by ovaries."
            
        "Cyproterone": 
            mentor.char "Not quite. Cyproterone is an anti-androgen, but Viola isn't currently taking one."
            jump whatMedication

        "Testosterone": 
            mentor.char "No, for gender-affirming care, testosterone is mostly used by transmen for its masculinizing effects. Viola is a transwoman."
            jump whatMedication

        "Spironolactone": 
            mentor.char "Not exactly. While spironolactone is an anti-androgen commonly used by transwomen, Viola is not currently on it."
            jump whatMedication

    mentor.char "Great job!" 
    
    mentor.char "Something that stands out to me is that Viola is currently not on an anti-androgen."

    return 
