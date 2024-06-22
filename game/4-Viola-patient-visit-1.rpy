##################################
## VIOLA
## VIST 1
##################################

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

# start patient interaction
label startViola_Visit_1: 
    hide screen home
    scene bg_waitingroom_full
    with fade
    $ searchName = patientName
    # Declare your characters! Format it as below with name, age, and sex
    $ viola = Patient(Character("Viola", color="#FFFFFF", namebox_style = "namebox_magenta"), "Viola", 24, "female", "she/her", "pink", "swimming", "vanilla")

    #GA4 Key Event
    $ analytics.event("violaVisit1", "start_violaVisit1")

# 1.A. VIOLA PRE-VISIT VIGNETTE

    "You've started Viola's case!"

    viola.char "Hi! I'm Viola!"

label violaVisit1_1A:

    "This is where a vignette of Viola's life will go once we make it."

    "The scene will show how despite Viola's bravado, she is very anxious about this appointment, because she's had negative experiences in the past."

    #GA4 Key Event
    $ analytics.event("violaVisit1", "end_violaVisit1_1A")

label violaVisit1_1B_1:
    scene bg_waitingroom_full
    with fade 
    $ nr = Person(Character("Nurse Roxy", color="#FFFFFF", namebox_style = "namebox_red"), "Nurse Roxy", 50, "female") 
    $ sd = Person(Character("Sandy", color="#FFFFFF", namebox_style = "namebox_orange"), "Sandy", 40, "female")
    $ mr = Person(Character("Marco", color="#FFFFFF", namebox_style = "namebox_purple"), "Marco", 33, "male")

# 1.B. REVIEW EHR
# INT. CLINIC STAFF ROOM - EARLY MORNING
# FOUR PEOPLE IN THIS SCENE, IN ADDITION TO PLAYER


    player.char "Morning everyone. What's the buzz?"

    mentor.char "Look at this, [player.name]..."

    mentor.char "\"Debut feature film from trans director removed from film festival...\""

    mentor.char "\"Governor blocks film release at publicly-funded art center...\""

    player.char "What? Are you all movie buffs?"

    nr.char "No this is Viola Phoenix's movie."

    mr.char "Her film was banned from all these festivals but it just made it go viral. She's a horror director."

    sd.char "And a makeup vlogger. Look, she's probably better known for this."

    player.char "Wow. That's pretty impressive. What am I missing?"

    mentor.char "[player.name], this is your first patient today!"

    nr.char "A true artist! A Vincent Van Gogh!"

    sd.char "She could feature our clinic in her videos!"

    nr.char "Or drive it into the ground!"

    mentor.char "Let's review her information, [player.name]. I'll meet you in my office. We have our work cut out for us!"

    nr.char "Careful, [player.name]!"

    #GA4 Key Event
    $ analytics.event("violaVisit1", "end_violaVisit1_1B_1")

# INT. DR G'S OFFICE

label violaVisit1_1B_2:
    scene bg_clinicroom
    show screen clipboard
    show screen pencil
    show screen lookup

    mentor.char "The patient's name is [viola.name], age is [viola.age], and pronouns are [viola.pronouns]."

    mentor.char "First, let's familiarize ourselves with her medical history."
    
    mentor.char "Let me know when you're done reviewing her file and then we'll talk."

    #GA4 Key Event
    $ analytics.event("violaVisit1", "end_violaVisit1_1B_2")

# Turning this off due to an error    call screen openPatientFile

# PLAYER reviews medical record

# 1.C COACHING FROM DR G

label violaVisit1_1C:
    scene bg_clinicroom

    mentor.char "Alright, let's talk about our approach for Viola Phoenix." 
    
    mentor.char "She's currently on 6m of oral estradiol per day and is asking for an increase in dose. We don't have her serum levels yet, so we don't know what her hormone level are, but 6mg is on the higher side."

    mentor.char "She's not on any anti-androgens, which block testosterone and oftentimes complement estrogen therapy in trans-feminine patients."

    mentor.char "It's not unusual to only take estradiol, but interestingly, she said she was on spironolactone but stopped and we don't know why."

    mentor.char "Maybe she had an adverse reaction to spiro -- let her tell you. Try to get her comfortable before you behind your comprehensive health assessment."

    mentor.char "Be curious, and make sure you ask open-ended questions to help her open up to you."

    mentor.char "We should understand her journey up to this point. What's worked? What hasn't worked? Have there been side effects? What progress has she made? And what more does she want to do?"

    mentor.char "This background will guide our clinical decisions and make us good partners for her."

    mentor.char "Next, we'll examine her current and family medical history."

    mentor.char "Her BMI is 30, she listed a family history of diabetes, and her blood pressure is elevated."

    mentor.char "It'd be good to ask her to do a self-test at a drug store and see if it's white coat hypertension or not."

    mentor.char "In any case, given all this information and her age, I think we should test her A1-C."

    mentor.char "We of course want to discuss diet and exercise with VIOLA, but let's focus on gaining her trust and gathering data first."

    mentor.char "Diabetes or pre-diabetes could complicate her hormone therapy or any other gender-affirming care needs she'll have."

    mentor.char "It certainly would increase the danger of a high estradiol dose that she is asking to increase even higher."

#DR G shows a diagram of estradiol formulations

    mentor.char "Speaking of which, she's taking oral estradiol."

    mentor.char "Since it is extensively metabolized in the liver, oral estradiol has a higher risk of causing deep vein thrombosis and I want to get her off of this as soon as we get her lab results with serum levels and liver numbers."

    mentor.char "I should also mention a higher dose is required for oral estradiol. The current approach is to try sublingual estradiol or a transdermal form."

    player.char "It looks like her prescription will run out in the next few weeks. Should we re-prescribe for a month until we can review her labs?"

    mentor.char "Exactly. Let's maintain the current regimen until we gather more data. Abrupt changes can lead to instability, and the last thing we should tell our patients is that we're letting their prescription run out."

    mentor.char "So let's just collect the lab results and touch base when they come back in. We definitely shouldn't promise an increase."

    mentor.char "We can promise safety as we work with her to get an appropriate dose and collaborate with her on her gender-affirming care goals."

    mentor.char "Remember, this kind of care is holistic."

    mentor.char "It's not just medical; it's about supporting her transition in a way that respects her needs and ensures her safety."

    label whatMedication_Viola_1:
    mentor.char "What medication is Viola currently taking that is relevant to her gender-affirming care?"

    menu: 
            "Estradiol": 
                    #GA4 Event
                    $ analytics.event("viola1_menu_whatCurrentMedication", "estradiol")
                    mentor.char "Yes, exactly!" 

                    label whatIsEstradiol_Viola_1:
                    mentor.char "What hormone is estradiol?" 

                    menu:
                            "Insulin": 
                                    #GA4 Event
                                    $ analytics.event("viola1_menu_whatIsEstradiol", "insulin")
                                    mentor.char "Not quite."
                                    jump whatIsEstradiol_Viola_1
                            "Testosterone": 
                                    #GA4 Event
                                    $ analytics.event("viola1_menu_whatIsEstradiol", "testosterone")
                                    mentor.char "Almost! Testestorone is actually the corresponding male sex hormone."
                                    jump whatIsEstradiol_Viola_1
                            "Progesterone": 
                                    #GA4 Event
                                    $ analytics.event("viola1_menu_whatIsEstradiol", "progesterone")
                                    mentor.char "Good guess, but not exactly!"
                                    jump whatIsEstradiol_Viola_1
                            "Estrogen":  
                                    #GA4 Event
                                    $ analytics.event("viola1_whatIsEstradiol", "estrogen")
                                    mentor.char "Indeed! Estradiol is the form of estrogen primarily produced by ovaries."
                
            "Cyproterone": 
                    #GA4 Event
                    $ analytics.event("viola1_menu_whatCurrentMedication", "cyproterone")
                    mentor.char "Not quite. Cyproterone is an anti-androgen, but Viola isn't currently taking one."
                    jump whatMedication_Viola_1

            "Testosterone": 
                    #GA4 Event
                    $ analytics.event("viola1_menu_whatCurrentMedication", "testosterone")
                    mentor.char "No, for gender-affirming care, testosterone is mostly used by trans men for its masculinizing effects. Viola is a transwoman."
                    jump whatMedication_Viola_1

            "Spironolactone": 
                    #GA4 Event
                    $ analytics.event("viola1_menu_whatCurrentMedication", "spironolactone")
                    mentor.char "Not exactly. While spironolactone is an anti-androgen commonly used by transwomen, Viola is not currently on it."
                    jump whatMedication_Viola_1

    mentor.char "Great job!" 
    
    mentor.char "Something that stands out to me is that Viola is currently not on an anti-androgen."

    #GA4 Key Event
    $ analytics.event("violaVisit1", "end_violaVisit1_1C")

# 1.D. PATIENT VISIT
label violaVisit1_1D:
    scene bg_clinicroom
    with fade

    image viola confused = "viola_confused_sprite.png"
    image viola happy = "viola_happy_sprite.png"
    image viola laughing = "viola_laughing_sprite.png"
    image viola neutral = "viola_neutral_sprite.png"
    image viola sad = "viola_sad_sprite.png"
    image viola surprised = "viola_surprised_sprite.png"
    image viola thoughtful = "viola_thoughtful_sprite.png"
    image viola uncomfortable = "viola_uncomfortable_sprite.png"
    image viola upset = "viola_upset_sprite.png"

    show viola neutral at half_size, center

    voice "vo clips/player_good/player_good_line001.ogg"
    player.char "Hi there! Welcome to our clinic!"

    voice "vo clips/viola_good/viola_good_line001.ogg"
    viola.char "Hello."

    menu introduceViola1_1D:
        "Introduce yourself"

        "Share your name":
            #GA4 Event
            $ analytics.event("viola1_menu_introduceViola1_1D", "share_your_name")

            voice "vo clips/misc/misc_026.ogg"
            player.char "My name is [player.name]."
            
            show viola neutral at half_size, center
            voice "vo clips/misc/misc_022.ogg"
            viola.char "Nice to meet you, [player.name]."

        "Share your name and pronouns":
            #GA4 Event
            $ analytics.event("viola1_menu_introduceViola1_1D", "share_your_name_pronouns")

            voice "vo clips/player_good/player_good_line002.ogg"
            player.char "My name is [player.name]. My pronouns are [player.pronouns]."

            show viola neutral at half_size, center
            voice "vo clips/misc/misc_022.ogg"
            viola.char "Nice to meet you, [player.name]."

        "Share your name, pronouns, and gender-affirming values":
            #GA4 Event
            $ analytics.event("viola1_menu_introduceViola1_1D", "share_your_name_pronouns_values")

            voice "vo clips/player_good/player_good_line002.ogg"
            player.char "My name is [player.name]. My pronouns are [player.pronouns]."

            show viola neutral at half_size, center
            voice "vo clips/misc/misc_022.ogg"
            viola.char "Nice to meet you, [player.name]."

            voice "vo clips/misc/misc_023.ogg"
            player.char "Before we begin, I want to let you know that I specialize in gender-affirming care."

            voice "vo clips/misc/misc_024.ogg"
            player.char "This means I'm here to support your health needs in a way that respects and aligns with your gender identity and expression. My goal is to create a safe and welcoming space where you can be open about your health concerns and needs."

            show viola neutral at half_size, center
            voice "vo clips/misc/misc_025.ogg"
            viola.char "Wow, good for you..."

    menu meetViolaViola1_1D:
        "Meet Viola"

        "Confirm Viola's name":
            #GA4 Event
            $ analytics.event("viola1_menu_meetViolaViola1_1D", "confirm_name")

            voice "vo clips/player_good/player_good_line003.ogg"
            player.char "And you are?"
            
            show viola neutral at half_size, center
            voice "vo clips/viola_good/viola_good_line002.ogg"
            viola.char "Viola Phoenix."

            voice "vo clips/player_good/player_good_line004.ogg"
            player.char "Phew! I'm in the right room."

        "You must be Viola":
            #GA4 Event
            $ analytics.event("viola1_menu_meetViolaViola1_1D", "you_must_be_viola")

            voice "vo clips/misc/misc_028.ogg"
            player.char "You must be Viola?"

            voice "vo clips/misc/misc_029.ogg"
            viola.char "Yes, that's me."

        "I recognize you from your vlog":
            #GA4 Event
            $ analytics.event("viola1_menu_meetViolaViola1_1D", "i_recognize_you")

            voice "vo clips/misc/misc_001.ogg"
            player.char "I know I'm in the right room because you're *the* VIOLA PHOENIX -- from Transcendence: Blood Warriors! I heard all about your film."

            voice "vo clips/misc/misc_002.ogg"
            viola.char "Oh you did? Did you go see it?"

            voice "vo clips/misc/misc_003.ogg"
            player.char "Not exactly. But I've seen your vlogs."

            voice "vo clips/misc/misc_004.ogg"
            viola.char "So you must know everything about me?"

            voice "vo clips/misc/misc_005.ogg"
            player.char "Oh, no, I didn't mean to imply that."

            voice "vo clips/misc/misc_006.ogg"
            viola.char "So what are you saying?"

            voice "vo clips/misc/misc_007.ogg"
            player.char "Let me start that over. Viola Phoenix, I presume?"

            voice "vo clips/misc/misc_008.ogg"
            viola.char "Yes, that's me."

    menu confirmViolasPronounsViola1_1D:
        "Confirm Viola's pronouns"

        "Ask for Viola's pronouns":
            #GA4 Event
            $ analytics.event("viola1_menu_confirmViolasPronounsViola1_1D", "ask_for_pronouns")

            voice "vo clips/player_good/player_good_line005.ogg"
            player.char "May I ask which pronouns you use?"

            voice "vo clips/viola_good/viola_good_line003.ogg"
            viola.char "She/her, or just Viola. Either is good."

            voice "vo clips/player_good/player_good_line006.ogg"
            player.char "Excellent. I'm looking forward to working with you as your primary care physician!"

            voice "vo clips/misc/misc_017.ogg"
            viola.char "Great, I'm looking forward to it too."

        "Read Viola's pronouns from her record":
            #GA4 Event
            $ analytics.event("viola1_menu_confirmViolasPronounsViola1_1D", "read_pronouns")

            voice "vo clips/misc/misc_018.ogg"
            player.char "You use she/her pronouns, is that correct?"

            voice "vo clips/misc/misc_019.ogg"
            viola.char "Or just Viola. Either is fine."

            voice "vo clips/misc/misc_020.ogg"
            player.char "Thank you. I'm looking forward to working with you as your primary care physician!"

            voice "vo clips/misc/misc_021.ogg"
            viola.char "I'm looking forward to it too."

        "Move on":
            #GA4 Event
            $ analytics.event("viola1_menu_confirmViolasPronounsViola1_1D", "move_on")

            voice "vo clips/player_good/player_good_line007.ogg"
            player.char "How are you doing today?"

            voice "vo clips/viola_good/viola_good_line005.ogg"
            viola.char "I'm fine, thanks. A bit anxous I guess. A new doctor, a new place..."

    menu askAboutViola:
        "Ask about Viola"

        "How are you doing today?":
            #GA4 Event
            $ analytics.event("viola1_menu_askAboutViola", "how_are_you")

            voice "vo clips/player_good/player_good_line007.ogg"
            player.char "How are you doing today?"

            show viola neutral at half_size, center
            voice "vo clips/viola_good/viola_good_line005.ogg"
            viola.char "I'm fine, thanks. A bit anxious I guess. A new doctor, a new place..."

        "I recognize you":
            #GA4 Event
            $ analytics.event("viola1_menu_askAboutViola", "i_recognize_you")

            voice "vo clips/misc/misc_009.ogg"
            player.char "I wanted to mention, I heard all about your film, Transcendence: Blood Warriors!"
            
            show viola surprised at half_size, center
            voice "vo clips/misc/misc_010.ogg"
            viola.char "Oh you did? Did you go see it?"

            voice "vo clips/misc/misc_011.ogg"
            player.char "Not exactly. But I've seen your vlogs."
            
            show viola uncomfortable at half_size, center
            voice "vo clips/misc/misc_012.ogg"
            viola.char "So you must know everything about me."

            voice "vo clips/misc/misc_013.ogg"
            player.char "Oh, no, I didn't mean to imply that."
            
            show viola upset at half_size, center
            voice "vo clips/misc/misc_014.ogg"
            viola.char "So what are you saying?"

            voice "vo clips/misc/misc_015.ogg"
            player.char "I'm just a supporter of yours, and I am looking forward to helping you with your healthcare needs."
            
            show viola uncomfortable at half_size, center
            voice "vo clips/misc/misc_016.ogg"
            viola.char "Great, that's why I am here! Do you want to talk about that?"
            #JUMP TO DISCUSSING VISIT
            jump  discussReasonsForVisit_violaVisit_1D

        "You're here about your estradiol dose?":
            #GA4 Event
            $ analytics.event("viola1_menu_askAboutViola", "here_for_estradiol")

            voice "vo clips/misc/misc_027.ogg"
            player.char "So I see in your file that you are here to refill your estradiol dose?"
            
            show viola neutral at half_size, center
            viola.char "Yes, that's right."
            #JUMP TO CLINICAL DISCUSSION
            jump  discussionPointsConfirmation_violaVisit_1D

    menu respondToViolasAnxiety:
        "Respond to Viola's Anxiety"

        "It's common to be nervous seeing a new doctor":
            #GA4 Event
            $ analytics.event("viola1_menu_respondToViolasAnxiety", "common_to_be_nervous")

            voice "vo clips/player_good/player_good_line008.ogg"
            player.char "That's completely normal. I know you've got a lot on your mind. I get nervous myself before my doctors' appointments. Did you find the office OK?"
            
            show viola happy at half_size, center
            voice "vo clips/viola_good/viola_good_line006.ogg"
            viola.char "It was pretty easy to find, but I still got lost haha. Nice spot."

            voice "vo clips/player_good/player_good_line009.ogg"
            player.char "Definitely, if you stick around the area afterward there are some great lunch spots."
            
            show viola happy at half_size, center
            voice "vo clips/viola_good/viola_good_line007.ogg"
            viola.char "I'll keep that in mind, thanks."

        "Reassure this is a gender-affirming clinic":
            #GA4 Event
            $ analytics.event("viola1_menu_respondToViolasAnxiety", "reassure_gender_affirming")

            voice "vo clips/branching/branching_line001.ogg"
            player.char "I know you've got a lot on your mind. I see you are looking to renew your estradiol dose and possibly increase it?"
            
            show viola neutral at half_size, center
            voice "vo clips/branching/branching_line002.ogg"
            viola.char "Yes. That is one of the main reasons I scheduled the appointment. I'm also hoping I can get some support with my overall health -- mental health, fitness, et cetera. You are my new primary care doctor, after all."

            voice "vo clips/branching/branching_line003.ogg"
            player.char "Of course, of course."
            
            show viola sad at half_size, center
            voice "vo clips/branching/branching_line004.ogg"
            viola.char "I didn't really feel like I got a healthy focus on that stuff with my old doctor."
            #JUMP to Overall Health Check
            jump discussionPointsConfirmation_violaVisit_1D

        "Resolve by discussing reasons for visit":
            #GA4 Event
            $ analytics.event("viola1_menu_respondToViolasAnxiety", "discuss_reasons")

            voice "vo clips/branching/branching_line005.ogg"
            player.char "I know you've got a lot on your mind. So how about we get right to it and discuss your estradiol dose."
            
            show viola neutral at half_size, center
            voice "vo clips/branching/branching_line006.ogg"
            viola.char "Okay, sure."

            voice "vo clips/branching/branching_line007.ogg"
            player.char "I see you are looking to renew your estradiol dose and possibly increase it?"
            #Jump to Discussing Reasons for Visit
            jump discussReasonsForVisit_violaVisit_1D

    menu askMoreAboutViola:
        "Ask more about Viola"

        "Ask what Viola does":
            #GA4 Event
            $ analytics.event("viola1_menu_askMoreAboutViola", "reassure_gender_affirming")

            voice "vo clips/player_good/player_good_line010.ogg"
            player.char "So, your student health plan brought you here, what are you studying?"
            
            show viola happy at half_size, center
            voice "vo clips/viola_good/viola_good_line008.ogg"
            viola.char "I'm a filmmaker. I want to become a better director."

            voice "vo clips/player_good/player_good_line011.ogg"
            player.char "Wow, that's amazing. I'm something of a movie buff myself. What kind of films do you make?"
            
            show viola happy at half_size, center
            voice "vo clips/viola_good/viola_good_line009.ogg"
            viola.char "Horror."

            voice "vo clips/player_good/player_good_line012.ogg"
            player.char "Amazing. I bet you have a lot of fun."
            
            show viola neutral at half_size, center
            voice "vo clips/viola_good/viola_good_line010.ogg"
            viola.char "Yes, it's my emotional and creative outlet for sure. But, school also gives me health care, so that's why I am here..."

            player.char "Wonderful."

        "I know who you are":
            #GA4 Event
            $ analytics.event("viola1_menu_askMoreAboutViola", "i_know_who_you_are")

            voice "vo clips/branching/branching_line009.ogg"
            player.char "I wanted to mention, I heard all about your film, Transcendence: Blood Warriors!"
            
            show viola surprised at half_size, center
            voice "vo clips/branching/branching_line010.ogg"
            viola.char "Oh you did? Did you go see it?"

            voice "vo clips/branching/branching_line011.ogg"
            player.char "Not exactly. But I've seen your vlogs."
            
            show viola neutal at half_size, center
            voice "vo clips/branching/branching_line012.ogg"
            viola.char "Oh, yes. Lots of people have. You enjoy them?"

            voice "vo clips/branching/branching_line013.ogg"
            player.char "There are some fans of yours in the clinic."
            
            show viola uncomfortable at half_size, center
            voice "vo clips/branching/branching_line014.ogg"
            viola.char "Y'all are gossiping?"

            voice "vo clips/branching/branching_line015.ogg"
            player.char "No, no! There was just a buzz. We're looking forward to helping you with your healthcare needs."
        
            show viola neutral at half_size, center
            voice "vo clips/branching/branching_line016.ogg"
            viola.char "Great, that's why I am here! Do you want to talk about that?"

        "Are you new to the area?":
            #GA4 Event
            $ analytics.event("viola1_menu_askMoreAboutViola", "are_you_new")
            voice "vo clips/branching/branching_line017.ogg"
            player.char "Did you recently move to the area?"
            
            show viola neutral at half_size, center
            voice "vo clips/branching/branching_line018.ogg"
            viola.char "Oh no, I just got into the film school, but I grew up here."

            voice "vo clips/branching/branching_line019.ogg"
            player.char "Amazing, congratulations! What  are you studying?"
            
            show viola happy at half_size, center
            voice "vo clips/viola_good/viola_good_line008.ogg"
            viola.char "I'm a filmmaker. I want to become a better director."

            voice "vo clips/player_good/player_good_line011.ogg"
            player.char "Wow, that's amazing. I'm something of a movie buff myself. What kind of films do you make?"
            
            show viola happy at half_size, center
            voice "vo clips/viola_good/viola_good_line009.ogg"
            viola.char "Horror."

            voice "vo clips/player_good/player_good_line012.ogg"
            player.char "Amazing. I bet you have a lot of fun."
            
            show viola neutral at half_size, center
            voice "vo clips/viola_good/viola_good_line010.ogg"
            viola.char "Yes, it's my emotional and creative outlet for sure. But, school also gives me health care, so that's why I am here..."

label discussReasonsForVisit_violaVisit_1D:
        player.char "Let's discuss the reasons for your visit today."

        menu transitionToDiscussingReasons:
            "Discuss reasons for visit."

            "Ask what Viola would like to discuss":
                #GA4 Event
                $ analytics.event("viola1_menu_transitionToDiscussingReasons", "ask_what_to_discuss")

                voice "vo clips/player_good/player_good_line014.ogg"
                player.char "I reviewed your notes, but I'm wondering if we could start with you sharing what your goals and concerns are, so we can make a plan for our appointment today."
                
                show viola neutral at half_size, center
                voice "vo clips/viola_good/viola_good_line011.ogg"
                viola.char "So I'm sure you're aware then -- I'm a trans woman. I've been taking estradiol for about 6 years and now I need to get that re-prescribed, so that's what brought me here."

                voice "vo clips/viola_good/viola_good_line012.ogg"
                viola.char "I'm hoping I can get some support with my overall health -- mental health, fitness, et cetera. I didn't really feel like I got anywhere with my old doctor."

            "You want your estradiol dose increased?":
                #GA4 Event
                $ analytics.event("viola1_menu_transitionToDiscussingReasons", "want_increase_estradiol")
                
                voice "vo clips/branching/branching_line020.ogg"
                player.char "So I see in your file that you'd like to increase your estradiol dose."
                
                show viola neutral at half_size, center
                voice "vo clips/branching/branching_line021.ogg"
                viola.char "Yes that's right. I need to get that re-prescribed, so that's what brought me here. I'm also hoping I can get some support with my overall health -- mental health, fitness, et cetera."

                voice "vo clips/branching/branching_line022.ogg"
                viola.char "I didn't really feel like I got anywhere with my old doctor."

            "Set the agenda for the visit":
                #GA4 Event
                $ analytics.event("viola1_menu_transitionToDiscussingReasons", "set_agenda")
                
                voice "vo clips/branching/branching_line023.ogg"
                player.char "Based on my notes and your vitals, I suggest we check in about your overall health and then discuss your experience with your gender-affirming care."

                voice "vo clips/branching/branching_line024.ogg"
                player.char "This should help me understand where you are with your current prescription, and that will help me know what our next steps should be. How does that sound?"
                
                show viola uncomfortable at half_size, center
                voice "vo clips/branching/branching_line025.ogg"
                viola.char "It will be a discussion right? I want to make sure I have a voice in the conversation."

                voice "vo clips/branching/branching_line026.ogg"
                player.char "Oh, of course."
                
                show viola sad at half_size, center
                voice "vo clips/branching/branching_line027.ogg"
                viola.char "I did not get that with my old doctor. I'm sorry I was having flashbacks just now."

    #Discussion Points Confirmation
label discussionPointsConfirmation_violaVisit_1D:
        voice "vo clips/player_good/player_good_line015.ogg"
        player.char "Okay, got it, thank you."

        "More dialog will go here!"

        menu startComprehensiveHealthAssessment:
            "What would you like to do now?"

            "Ask about general health":
                #GA4 Event
                $ analytics.event("viola1_menu_startComprehensiveHealthAssessment", "ask_general_health")

                voice "vo clips/player_good/player_good_line016.ogg"
                player.char "I'd like to ask you more about your overall health. How are you feeling in general? Anything concerning you in particular at the moment?"
                
                show viola neutral at half_size, center
                voice "vo clips/viola_good/viola_good_line013.ogg"
                viola.char "Ah, well. I'm doing alright."

                voice "vo clips/player_good/player_good_line017.ogg"
                player.char "We noticed your blood pressure is a bit higher than it should be."
                
                show viola uncomfortable at half_size, center
                voice "vo clips/viola_good/viola_good_line014.ogg"
                viola.char "Oh yeah... it's always been that way when I have a doctor's appointment. I haven't had the best time seeing the doctor, so I get on edge a bit. Especially with my hormone prescription expiring soon."

            "Bring up high blood pressure":
                #GA4 Event
                $ analytics.event("viola1_menu_startComprehensiveHealthAssessment", "bring_up_high_blood_pressure")
                
                voice "vo clips/player_good/player_good_line017.ogg"
                player.char "We noticed your blood pressure is a bit higher than it should be."
                
                show viola uncomfortable at half_size, center
                voice "vo clips/viola_good/viola_good_line014.ogg"
                viola.char "Oh yeah... it's always been that way when I have a doctor's appointment. I haven't had the best time seeing the doctor, so I get on edge a bit. Especially with my hormone prescription expiring soon."

            "Ask about hormone therapy":
                #GA4 Event
                $ analytics.event("viola1_menu_startComprehensiveHealthAssessment", "ask_hormone_therapy")
                
                voice "vo clips/branching/branching_line028.ogg"
                player.char "You've been on estradiol for 6 years now, is that right? Could you tell me about your current regimen?"
                
                show viola neutral at half_size, center
                voice "vo clips/branching/branching_line029.ogg"
                viola.char "Yes, about six years. We slowly went up to 6mg/day. That's where I am now. I still feel too masculine which isn't where I want to be."
                #JUMP to Ask About Spironolactone
            
        menu discussBloodPressureReading:
            "Discuss blood pressure reading"

            "Ask about blood pressure readings outside of clinic":
                #GA4 Event
                $ analytics.event("viola1_menu_discussBloodPressureReading", "ask_about_outside_readings")
                
                voice "vo clips/player_good/player_good_line018.ogg"
                player.char "Yes, that's a very normal phenomenon, it's called white coat hypertension!"

                voice "vo clips/player_good/player_good_line019.ogg"
                player.char "Just to curious, have you ever had your blood pressure taken outside of a doctor's office?"
                
                show viola surprised at half_size, center
                voice "vo clips/viola_good/viola_good_line015.ogg"
                viola.char "Now that you mention it, nope!"

                voice "vo clips/player_good/player_good_line020.ogg"
                player.char "The reason I'm asking is that I want to make sure we want to look after the whole picture of your health."

            "If it's high next time we'll look into it":
                #GA4 Event
                $ analytics.event("viola1_menu_discussBloodPressureReading", "if_high_next_time")
                
                player.char "If it's high next time we'll look into it"
                
                show viola neutral at half_size, center
                viola.char "Okay, sounds good."
            
            "Tell her it's white coat hypertension and move on":
                #GA4 Event
                $ analytics.event("viola1_menu_discussBloodPressureReading", "tell_white_coat_hypertension")
                
                voice "vo clips/player_good/player_good_line018.ogg"
                player.char "Yes, that's a very normal phenomenon, it's called white coat hypertension!"
                
                show viola thoughtful at half_size, center
                viola.char "Okay, I didn't know that. That makes me relieved."

        menu discussFamilyHistory:
            "Discuss family history"

            "Verify family history of cardiovascular issues":
                #GA4 Event
                $ analytics.event("viola1_menu_discussFamilyHistory", "verify_family_cardiovascular_issues")

                voice "vo clips/player_good/player_good_line021.ogg"
                player.char "Reading your notes, you mentioned a family history of diabetes and some cardiovascular issues, is that correct?"
                
                show viola neutral at half_size, center
                voice "vo clips/viola_good/viola_good_line016.ogg"
                viola.char "Oh yeah. Both my parents are diabetic, couple of my grandparents had it."

                player.char "Oh yes, that's not uncommon. Are you close with your grandparents?"
                
                show viola sad at half_size, center
                voice "vo clips/viola_good/viola_good_line017.ogg"
                viola.char "Yes, even after transitioning. I'm lucky... but my grandmother recently passed away, from a stroke."

                voice "vo clips/player_good/player_good_line022.ogg"
                player.char "I'm sorry for your loss."
                
                show viola sad at half_size, center
                voice "vo clips/viola_good/viola_good_line018.ogg"
                viola.char "Thank you..."
                
                show viola sad at half_size, center
                voice "vo clips/viola_good/viola_good_line019.ogg"
                viola.char "I know I need to be taking better care of myself, too. It's just, one of a thousand things other things I have to do."
            
            "Tell Viola she has an increased risk of diabetes":
                #GA4 Event
                $ analytics.event("viola1_menu_discussFamilyHistory", "tell_diabetes_risk")

                player.char "Reading your notes, you mentioned a family history of diabetes."
                
                show viola neutral at half_size, center
                voice "vo clips/viola_good/viola_good_line016.ogg"
                viola.char "Oh yeah. Both my parents are diabetic, couple of my grandparents had it."

                player.char "Because you smoke and your BMI is higher than ideal, you also have an increased risk of developing diabetes."
                
                show viola sad at half_size, center
                viola.char "Ok."

                voice "vo clips/viola_good/viola_good_line019.ogg"
                player.char "Ok, thanks. I'll take them. I know I need to be taking better care of myself, too. It's just, one of a thousand things other things I have to do."

            "Tell Viola her diabetes could complicate her hormone therapy":
                #GA4 Event
                $ analytics.event("viola1_menu_discussFamilyHistory", "tell_diabetes_complicate_hormone")

                player.char "Reading your notes, you mentioned a family history of diabetes."
                
                show viola neutral at half_size, center
                voice "vo clips/viola_good/viola_good_line016.ogg"
                viola.char "Oh yeah. Both my parents are diabetic, couple of my grandparents had it."

                player.char "Because you smoke and your BMI is higher than ideal, you also have an increased risk of developing diabetes."
                
                show viola sad at half_size, center
                viola.char "Ok."

                player.char "We should keep an eye on your sugar levels, more frequent exercise, and a healthier diet too. If you need any tips on lifestyle changes, I can send those to you after our appointment today."

                viola.char "Ok, I'll take them. Thanks."

                player.char "Getting diabetes or pre-diabetes can be affect you in a lot of ways. It can even effect the choices we have in terms of hormone therapy and gender-affirming care options."
                
                show viola sad at half_size, center
                viola.char "I know I need to be taking better care of myself, too. It's just, one of a thousand things other things I have to do."

        menu respondToViolasFrustration:
            "Respond to Viola's frustration"

            "Relate to Viola's statement":
                #GA4 Event
                $ analytics.event("viola1_menu_respondToViolasFrustration", "relate_to_viola")

                voice "vo clips/player_good/player_good_line023.ogg"
                player.char "Yeah. You've got a lot of things to juggle."
                
                show viola neutral at half_size, center
                voice "vo clips/viola_good/viola_good_line020.ogg"
                viola.char "That's correct."

                voice "vo clips/player_good/player_good_line024.ogg"
                player.char "I'm sure that makes you a good director."
                
                show viola happy at half_size, center
                voice "vo clips/viola_good/viola_good_line021.ogg"
                viola.char "I don't know about good. Maybe 10 years down the road I can call myself good. But I'll tell you I don't make time for exercise and yes, I eat junk food. It's what I need to get through the day, it's what I can afford. I don't know what to tell you."

                voice "vo clips/player_good/player_good_line025.ogg"
                player.char "I can relate to that -- it can be difficult to take care of yourself as a doctor, too. Sometimes it comes down to having a team supporting you."
                
                show viola sad at half_size, center
                voice "vo clips/viola_good/viola_good_line022.ogg"
                viola.char "Yeah, well I haven't had that. Not with my health."
            
            "Acknowledge Viola's statement":
                #GA4 Event
                $ analytics.event("viola1_menu_respondToViolasFrustration", "acknowledge_statement")

                player.char "I hear what you're saying. Sometimes your own health and well-being fall to the bottom of the priority list."
                
                show viola neutral at half_size, center
                viola.char "Absolutely. I'm blessed and cursed to make movies. I pour all my energy into that. Oh, and being trans isn't exactly easy in this country either, so something's gotta give."
                
                show viola sad at half_size, center
                viola.char "I don't make time for exercise and yes, I eat junk food. It's what I need to get through the day, it's what I can afford. I don't know what to tell you."


            "Offer support in a dedicated visit":
                #GA4 Event
                $ analytics.event("viola1_menu_respondToViolasFrustration", "offer_support")
                
                voice "vo clips/player_good/player_good_line052.ogg"
                player.char "Thank you for sharing that. It's rare to have the time to cover everything in a typical appointment. What I'd recommend for discussions about dietary change or behavior change is reserving double appointments, which we'll work with you to do."
                
                show viola happy at half_size, center
                viola.char "Ok, we can do that."
                
                player.char "Great."
                #JUMP to Wrap Up on Hypertension
                jump wrapUpOnHypertension_violaVisit_1D

        menu askAfterViolasFrustration:
            "What would you like to do next?"

            "Ask about previous experiences":
                #GA4 Event
                $ analytics.event("viola1_menu_askAfterViolasFrustration", "ask_about_previous")
                
                voice "vo clips/player_good/player_good_line026.ogg"
                player.char "And you mentioned being unsatisfied with your previous doctor and those experiences. Could you tell me more about what wasn't working, and what your expectations are?"
                
                show viola upset at half_size, center
                voice "vo clips/viola_good/viola_good_line023.ogg"
                viola.char "Yes. They just basically told me what to do with respect to my gender-affirming care, weren't listening to me, and they didn't really know what they were doing."
                
                show viola upset at half_size, center
                voice "vo clips/viola_good/viola_good_line024.ogg"
                viola.char "So I had to basically tell the doctor what to do, you know, and meanwhile we spent all this time talking about my weight and I never felt like we could actually discuss my gender-affirming needs. So I felt like I was on my own and here was this person who was just in the way the whole time."
            
            "Offer support in a dedicated visit":
                #GA4 Event
                $ analytics.event("viola1_menu_askAfterViolasFrustration", "offer_support")
                
                voice "vo clips/player_good/player_good_line052.ogg"
                player.char "Thank you for sharing that. It's rare to have the time to cover everything in a typical appointment. What I'd recommend for discussions about dietary change or behavior change is reserving double appointments, which we'll work with you to do."
                
                show viola happy at half_size, center
                viola.char "That sounds good, let's do that."

                player.char "Great."
                #JUMP to Wrap Up on Hypertension
                jump wrapUpOnHypertension_violaVisit_1D
        
        menu respondToViolasDoctorComment:
            "What woud you like to do next?"

            "Acknowledge Viola's statement and propose solutions":
                #GA4 Event
                $ analytics.event("viola1_menu_respondToViolasDoctorComment", "acknowledge_statement_propose_solutions")
                
                player.char "Thank you for sharing that. I'm sorry to hear you haven't felt supported or heard in your previous appointments. I want to make sure there is space for us to discuss everything so I want to share a few strategies we can explore together."

                player.char "How does that sound?"
                
                show viola neutral at half_size, center
                viola.char "That sounds good, what do you have in mind?"

                player.char "It's rare to have the time to cover everything in a typical appointment. What I'd recommend for discussions about dietary change or behavior change is reserving double appointments, so that we can have dedicated time to discuss that, which we'll work with you to do."
                
                show viola happy at half_size, center
                viola.char "That sounds good. Let's plan to do that. The clock is ticking and this is a big conversation."

                player.char "And I want to share that our appointments aren't the only time we can discuss your health. You can send me messages in our app, and we can schedule telehealth video visits for times when coming here is inconvenient."

                player.char "Plus, there are health incentives through your plan, like exercise class discounts, to explore."
                
                show viola surprised at half_size, center
                viola.char "Oh, I did not know about the video visits."

                player.char "It's something new -- so let's try it out sometime."
                
                show viola happy at half_size, center
                viola.char "Sounds like a plan!"
            
            "Share ways to keep the conversation going":
                #GA4 Event
                $ analytics.event("viola1_menu_respondToViolasDoctorComment", "share_ways_conversation")
                
                player.char "Thank you for sharing that."
                
                player.char "It's rare to have the time to cover everything in a typical appointment. What I'd recommend for discussions about dietary change or behavior change is reserving double appointments, so that we can have dedicated time to discuss that, which we'll work with you to do."
                
                show viola neutral at half_size, center
                viola.char "That sounds good. Let's plan to do that. The clock is ticking and this is a big conversation."

                player.char "And I want to share that our appointments aren't the only time we can discuss your health. You can send me messages in our app, and we can schedule telehealth video visits for times when coming here is inconvenient."

                player.char "Plus, there are health incentives through your plan, like exercise class discounts, to explore."
                
                show viola surprised at half_size, center
                viola.char "Oh, I did not know about the video visits."

                player.char "It's something new -- so let's try it out sometime."
                
                show viola happy at half_size, center
                viola.char "Sounds like a plan!"

            "Propose meeting separately to discuss lifestyle changes":
                #GA4 Event
                $ analytics.event("viola1_menu_respondToViolasDoctorComment", "propose_meeting_separately")
                
                player.char "Thank you for sharing that. It's rare to have the time to cover everything in a typical appointment."

                player.char "What I'd recommend for discussions about dietary change or behavior change is reserving double appointments, which we'll work with you to do."
                
                show viola neutral at half_size, center
                viola.char "That sounds good. Let's plan to do that. The clock is ticking and this is a big conversation."

                player.char "Sounds like a plan!"

#Wrap Up on Hypertension and Move on To Gender Affirming Care
label wrapUpOnHypertension_violaVisit_1D:
    voice "vo clips/player_good/player_good_line027.ogg"
    player.char "But for now, let's shift gears because I want to make sure we have time to review your gender-affirming care needs. How does that sound?"
    
    show viola happy at half_size, center
    voice "vo clips/viola_good/viola_good_line025.ogg"
    viola.char "Perfect."

    voice "vo clips/player_good/player_good_line028.ogg"
    player.char "But! I want to do two things."

    voice "vo clips/player_good/player_good_line029.ogg"
    player.char "I want to ask if you could take your blood pressure at a CATS drug store in the next week or so and just tell me what your results are."

    voice "vo clips/player_good/player_good_line030.ogg"
    player.char "That way, we can see what it's like outside of the doctor's office."
    
    show viola neutral at half_size, center
    voice "vo clips/viola_good/viola_good_line026.ogg"
    viola.char "...Sure, that's not a problem. Is it free, or could I get reimbursed for it?"

    voice "vo clips/player_good/player_good_line031.ogg"
    player.char "Yes, it should be totally free. If not, keep the receipt."

    voice "vo clips/player_good/player_good_line032.ogg"
    player.char "So, the second thing is, I'd like test your A1-C level. That's your blood sugar level."

    voice "vo clips/player_good/player_good_line033.ogg"
    player.char "Considering your family history of diabetes, hypertension, and your BMI, we should screen for diabetes to make sure we manage it."
    
    show viola happy at half_size, center
    voice "vo clips/viola_good/viola_good_line027.ogg"
    viola.char "Ok, I have to get my blood drawn anyway, right, so that sounds good."

    voice "vo clips/player_good/player_good_line034.ogg"
    player.char "You're an expert at this!"

    voice "vo clips/player_good/player_good_line035.ogg"
    player.char "So, yes, moving on to your gender-affirming care..."

    menu askAboutViolasGenderAffirmingCareHistory:
        "Ask about Viola's gender-affirming care history"

        "Ask Viola to tell you about her hormone therapy":
            #GA4 Event
            $ analytics.event("viola1_menu_askAboutViolasGenderAffirmingCareHistory", "ask_hormone_therapy")
            
            voice "vo clips/player_good/player_good_line036.ogg"
            player.char "You've been on estradiol for 6 years now, is that right? Could you tell me about your current regimen?"
            
            show viola neutral at half_size, center
            voice "vo clips/viola_good/viola_good_line028.ogg"
            viola.char "Yes, about six years. We slowly went up to 6mg/day. That's where I am now. I still feel too masculine which isn't where I want to be."

        "Ask Viola about her estradiol dose":
            #GA4 Event
            $ analytics.event("viola1_menu_askAboutViolasGenderAffirmingCareHistory", "ask_estradiol_dose")
            
            voice "vo clips/player_good/player_good_line036.ogg"
            player.char "You've been on estradiol for 6 years now, is that right? Could you tell me about your current regimen?"
            
            show viola neutral at half_size, center
            voice "vo clips/viola_good/viola_good_line028.ogg"
            viola.char "Yes, about six years. We slowly went up to 6mg/day. That's where I am now. I still feel too masculine which isn't where I want to be."

        "Ask about Viola's gender-affirming care journey":
            #GA4 Event
            $ analytics.event("viola1_menu_askAboutViolasGenderAffirmingCareHistory", "ask_gender_affirming_care")
                
            player.char "Can you tell me about your gender-affirming care experiences -- what's the history, some key points, and where you are now?"
            
            show viola neutral at half_size, center
            viola.char "Um, well, it's been a lot of work. I've been taking estradiol for about six years. We slowly went up to 6mg/day. That's where I am now."
            #gesturing to her body
            viola.char "I got my top surgery."
            #gesturing to her face
            viola.char "I had my facial feminization -- paid out of pocket for that."
            
            show viola happy at half_size, center
            viola.char "That definitely didn't help my mental health."
            
            viola.char "But other than that...I froze some sperm. So I gotta pay their rent AND my own!"

            viola.char "Oh, lots of therapy. I've been hit or miss with that. Been in and out of some trans communities too... I could go on if you really want my life story."
            
            show viola neutral at half_size, center
            viola.char "But anyway. The estradiol dose is on the higher side, and has been helping to a point, but I'm not where I want to be."
           
            show viola sad at half_size, center
            viola.char "I still feel like a guy sometimes."
            
            show viola upset at half_size, center
            viola.char "And I worked really hard to be where I am. I've had to advocate. And I had to survive a lot of bullshit."

#Ask About Spironolactone
label askViolaAboutSpironolactone_violaVisit1_1D:
    menu askAboutSpironolactone:
        "Ask about spironolactone"

        "Ask about anti-androgens":
            #GA4 Event
            $ analytics.event("viola1_menu_askAboutSpironolactone", "ask_anti_androgens")
                
            player.char "You also took an anti-androgen?"

            viola.char "A what?"

            player.char "Spironolactone, to suppress testosterone, but it looks like your prescription was not renewed?"

            voice "vo clips/viola_good/viola_good_line029.ogg"
            viola.char "Yes, a while back. I had bad side effects. Dizzy, fainting. I had to shut it down."

        "You used to be on spironolactone, but not anymore?":
            #GA4 Event
            $ analytics.event("viola1_menu_askAboutSpironolactone", "you_used_to_spironolactone")
            
            voice "vo clips/player_good/player_good_line037.ogg"
            player.char "And you were also on spironolactone to block testosterone, but it looks like your prescription wasn't renewed?"
            
            show viola thoughtful at half_size, center
            viola.char "Yes, a while back. I had bad side effects. Dizzy, fainting. I had to shut it down."

        "Ask if there was anything else":
            #GA4 Event
            $ analytics.event("viola1_menu_askAboutSpironolactone", "ask_anything_else")
                
            player.char "Thank you. And regarding hormone therapy, was there anything else?"
            show viola thoughtful at half_size, center
            viola.char "Oh, yes! We tried spironolactone to block testosterone. But it made me dizzy. I had bad side effects. I shut it down."

    menu followUpAboutSpironolactone:
        "Follow up about spironolactone"

        "Ask if they tried adjusting the dose":
            #GA4 Event
            $ analytics.event("viola1_menu_followUpAboutSpironolactone", "ask_tried_adjusting_dose")

            voice "vo clips/player_good/player_good_line038.ogg"
            player.char "Could you tell me more about that? I know it was a few years ago. Did you try adjusting your dose or changing to another anti-androgen?"
            
            show viola thoughtful at half_size, center
            voice "vo clips/viola_good/viola_good_line030.ogg"
            viola.char "Um, well... I was started on 100mg/day I think. It made me feel horrible. I couldn't handle it and just stopped taking it."

            viola.char "And like I said, I didn't feel like the communication was open with my doctor. So I did my own research and just felt like this wasn't right for me. When I told my doctor, the only alternative was almost $2000 a shot."
        
        "Ask if any tests validated her symptoms":
            #GA4 Event
            $ analytics.event("viola1_menu_followUpAboutSpironolactone", "ask_tests_validated_symptoms")
                
            player.char "Were there any tests or checkups done when you started having side effects?"
            
            show viola confused at half_size, center
            viola.char "What kind of tests?"

            voice "vo clips/player_good/player_good_line039.ogg"
            player.char "Were you able to check your electrolyte levels or anything like that? If you remember?"
            
            show viola thoughtful at half_size, center
            voice "vo clips/viola_good/viola_good_line031.ogg"
            viola.char "Nope, if I recall right I just said, \"Look, I can't take this. Can we do this with just estrogen?\""

            voice "vo clips/player_good/player_good_line040.ogg"
            player.char "Right, and it's true, for a lot of transfeminine people, taking a dose of estradiol is enough for them."
            
            show viola neutral at half_size, center
            voice "vo clips/viola_good/viola_good_line032.ogg"
            viola.char "Right? Exactly. I didn't feel like I should have to take spiro if it made me feel bad when I could just take estradiol. So we bumped that up over the years."

            player.char "And do you remember the dose?"
            
            show viola thoughtful at half_size, center
            voice "vo clips/viola_good/viola_good_line030.ogg"
            viola.char "Um, well... I was started on 100mg/day I think. It made me feel horrible. I couldn't handle it and just stopped taking it."

        "Move on":
            #GA4 Event
            $ analytics.event("viola1_menu_followUpAboutSpironolactone", "move_on")
                
            player.char "Thanks for sharing that."
    
    menu moveOnFromSpironolactone:
        "What would you like to do next?"

        #THIS OPTION SHOULD only be accessible if the PLAYER did not select "Ask about Viola's gender-affirming care journey" three questions ago
        "Ask if there's anything else you should know":
            #GA4 Event
            $ analytics.event("viola1_menu_moveOnFromSpironolactone", "ask_anything_else")

            player.char "Is there anything else I should know?"
            
            show viola thoughtful at half_size, center
            voice "vo clips/viola_good/viola_good_line033.ogg"
            viola.char "Um, well..."
            #gesturing to her body
            voice "vo clips/viola_good/viola_good_line034.ogg"
            viola.char "I got my top surgery."
            #gesturing to her face
            voice "vo clips/viola_good/viola_good_line035.ogg"
            viola.char "I had my facial feminization -- paid out of pocket for that."
            
            show viola happy at half_size, center
            voice "vo clips/viola_good/viola_good_line036.ogg"
            viola.char "That definitely didn't help my mental health."
            
            voice "vo clips/viola_good/viola_good_line037.ogg"
            viola.char "But other than that...I froze some sperm. So I gotta pay their rent AND my own!"

            voice "vo clips/viola_good/viola_good_line038.ogg"
            viola.char "Oh, lots of therapy. I've been hit or miss with that. Been in and out of some trans communities too... I could go on if you really want my life story."
            
            show viola neutral at half_size, center
            voice "vo clips/viola_good/viola_good_line039.ogg"
            viola.char "But anyway. The estradiol dose is on the higher side, and has been helping to a point, but I'm not where I want to be."
            
            show viola sad at half_size, center
            voice "vo clips/viola_good/viola_good_line040.ogg"
            viola.char "I still feel like a guy sometimes."
            
            show viola upset at half_size, center
            voice "vo clips/viola_good/viola_good_line041.ogg"
            viola.char "And I worked really hard to be where I am. I've had to advocate. And I had to survive a lot of bullshit."

            player.char "Yes, I understand. To be where you are now, it's a huge accomplishment. And I want to tell you right now that you won't have to fight. We're your partners in your health, and your well-being is my priority."
            
            show viola happy at half_size, center
            voice "vo clips/viola_good/viola_good_line042.ogg"
            viola.char "Thank you for saying that. That's nice to hear."
            
            voice "vo clips/player_good/player_good_line043.ogg"
            player.char "It's the truth! As for your estradiol, I do need to ensure your treatment is safe and effective, and in order to do that, like you mentioned, we'll order some lab tests to get a look at your current hormone levels and schedule a follow up appointment."
            
            show viola uncomfortable at half_size, center
            voice "vo clips/viola_good/viola_good_line043.ogg"
            viola.char "Yes... but... I am going to run out of my prescription in the next week or so, what should I do?"

        #THIS OPTION SHOULD only be accessible if the PLAYER did not select "Ask about Viola's gender-affirming care journey" three questions ago

        "Ask about the rest of her gender-affirming care journey":
            #GA4 Event
            $ analytics.event("viola1_menu_moveOnFromSpironolactone", "ask_rest_gender_affirming_care")

            voice "vo clips/player_good/player_good_line041.ogg"
            player.char "And so how's the rest of that journey been, from increasing the estradiol dose until now?"
        
            show viola thoughtful at half_size, center
            viola.char "Um, well... it's been a lot of hard work."
            #gesturing to her body
            voice "vo clips/viola_good/viola_good_line034.ogg"
            viola.char "I got my top surgery."
            #gesturing to her face
            voice "vo clips/viola_good/viola_good_line035.ogg"
            viola.char "I had my facial feminization -- paid out of pocket for that."
            
            show viola happy at half_size, center
            voice "vo clips/viola_good/viola_good_line036.ogg"
            viola.char "That definitely didn't help my mental health."
            
            voice "vo clips/viola_good/viola_good_line037.ogg"
            viola.char "But other than that...I froze some sperm. So I gotta pay their rent AND my own!"

            voice "vo clips/viola_good/viola_good_line038.ogg"
            viola.char "Oh, lots of therapy. I've been hit or miss with that. Been in and out of some trans communities too... I could go on if you really want my life story."
            
            show viola neutral at half_size, center
            voice "vo clips/viola_good/viola_good_line039.ogg"
            viola.char "But anyway. The estradiol dose is on the higher side, and has been helping to a point, but I'm not where I want to be."
            
            show viola sad at half_size, center
            voice "vo clips/viola_good/viola_good_line040.ogg"
            viola.char "I still feel like a guy sometimes."
            
            show viola upset at half_size, center
            voice "vo clips/viola_good/viola_good_line041.ogg"
            viola.char "And I worked really hard to be where I am. I've had to advocate. And I had to survive a lot of bullshit."

            voice "vo clips/player_good/player_good_line042.ogg"
            player.char "Yes, I understand. To be where you are now, it's a huge accomplishment. And I want to tell you right now that you won't have to fight. We're your partners in your health, and your well-being is my priority."
            
            show viola happy at half_size, center
            voice "vo clips/viola_good/viola_good_line042.ogg"
            viola.char "Thank you for saying that. That's nice to hear."
            
            voice "vo clips/player_good/player_good_line043.ogg"
            player.char "It's the truth! As for your estradiol, I do need to ensure your treatment is safe and effective, and in order to do that, like you mentioned, we'll order some lab tests to get a look at your current hormone levels and schedule a follow up appointment."
            
            show viola uncomfortable at half_size, center
            voice "vo clips/viola_good/viola_good_line043.ogg"
            viola.char "Yes... but... I am going to run out of my prescription in the next week or so, what should I do?"

        "Discuss next steps":
            #GA4 Event
            $ analytics.event("viola1_menu_moveOnFromSpironolactone", "discuss_next_steps")

            player.char "So let's discuss where we go from here."
            
            show viola neutral at half_size, center
            viola.char "Ok. So what's going to happen with my dose? Can I get an increase in prescription?"
    
    menu respondAboutEstradiolDose:
        "Resond about estradiol dose"

        "Recommend delaying the renewal until after the lab results":
            #GA4 Event
            $ analytics.event("viola1_menu_respondAboutEstradiolDose", "recommend_delay_renewal")

            player.char "Your lab tests should be completed within 10 days, after which we can meet. We should be able to get you in before you run out."
            
            show viola confused at half_size, center
            viola.char "You should be able to?"

            player.char "Yes! I'm not worried about it. I want to be careful not to prescribe a dose if it's unsafe, even just for 30 days."
            
            show viola uncomfortable at half_size, center
            viola.char "But what if I get sick, or if there aren't any appointments that work for me?"

            player.char "Hmm. I guess what we can do is re-prescribe for 14 days just to be sure."
            
            show viola happy at half_size, center
            viola.char "Okay. That makes me feel better. So it seems like an increase would not be a good idea in your opinion?"

        "Renew Viola's prescription for a short period":
            #GA4 Event
            $ analytics.event("viola1_menu_respondAboutEstradiolDose", "renew_for_short_period")

            voice "vo clips/player_good/player_good_line044.ogg"
            player.char "Nothing will change for now, I'll renew your current prescription for 30 days to ensure there's no interruption in your therapy."
            
            show viola happy at half_size, center
            voice "vo clips/viola_good/viola_good_line044.ogg"
            viola.char "Ok, that's good to know. And we can talk about the increase when my blood tests come back?"

            player.char "Absolutely. But..."
    
    menu respondAboutEstradiolDoseIncrease:
        "Respond about estradiol dose increase"
            
        "Labs will determine next steps":
            #GA4 Event
            $ analytics.event("viola1_menu_respondAboutEstradiolDoseIncrease", "labs_will_determine_steps")

            player.char "We need to have your lab results to see if it's safe and effective to increase your dose, first. Once I get those I can give you my recommendation."
            
            show viola uncomfortable at half_size, center
            viola.char "Alright. I'll be on pins and needles until then."

            player.char "Don't forget, we're in this together but I need you to trust us to make the right decision."
            
            show viola sad at half_size, center
            viola.char "You leave me with no choice."

            voice "vo clips/player_good/player_good_line046.ogg"
            player.char "When you check out you can work with our front desk staff to get another appointment booked."

            voice "vo clips/player_good/player_good_line047.ogg"
            player.char "We'll also have a release form for your previous medical records for you to sign. We'll need a chance to review those so we can better understand your needs."
            
            show viola neutral at half_size, center
            viola.char "OK, I'll do that. I don't want to delay anything."

            player.char "I just want to make sure I have the full picture of tests and exams you did with your previous PCP. I'll send you a follow-up message about all of this, and the results of the A1-C test."
           
            show viola neutral at half_size, center
            viola.char "Thank you, and I can do my labs here too?"

            player.char "Yes, our front staff can help you find the lab. Is that all for now Viola?"
            
            show viola neutral at half_size, center
            viola.char "Yes, thank you."

            player.char "Bye for now!"

            show viola neutral at half_size, center
            voice "vo clips/viola_good/viola_good_line047.ogg"
            viola.char "Bye!"

        "Commit to a collaborative followup based on data":
            #GA4 Event
            $ analytics.event("viola1_menu_respondAboutEstradiolDoseIncrease", "commit_collaborative_followup")
           
            voice "vo clips/player_good/player_good_line045.ogg"
            player.char "I want to be upfront with you, that we need to make sure your estrogen levels are in the appropriate range. The labs I'm ordering for you will tell us if we can adjust your dose safely."
            
            show viola confused at half_size, center
            viola.char "So you're not sure?"

            player.char "Correct. And when we get the lab results I want to go over them with you together so that we can both come up with an informed decision."
            
            show viola happy at half_size, center
            viola.char "Ok, sure. I like talking about this stuff anyway."

            voice "vo clips/player_good/player_good_line046.ogg"
            player.char "When you check out you can work with our front desk staff to get another appointment booked."

            voice "vo clips/player_good/player_good_line047.ogg"
            player.char "We'll also have a release form for your previous medical records for you to sign. We'll need a chance to review those so we can better understand your needs."
            
            show viola neutral at half_size, center
            voice "vo clips/viola_good/viola_good_line045.ogg"
            viola.char "OK, I'll do that. No worries. You guys don't write nasty things about us in those notes do you?"

            voice "vo clips/player_good/player_good_line048.ogg"
            player.char "No, no! I just want to make sure I have the full picture of tests and exams you did with your previous PCP."

            voice "vo clips/player_good/player_good_line049.ogg"
            player.char "I'll send you a follow-up message about all of this, and the results of the A1-C test, and then we'll meet back here to discuss next steps alright Viola?"

            voice "vo clips/player_good/player_good_line050.ogg"
            player.char "We'll tackle this together!"
            
            show viola happy at half_size, center
            voice "vo clips/viola_good/viola_good_line046.ogg"
            viola.char "Thank you, looking forward to it, Doctor. Thanks for today."

            voice "vo clips/player_good/player_good_line051.ogg"
            player.char "Thank you, it's been great to meet you, and happy filming! Bye for now!"
            
            show viola happy at half_size, center
            voice "vo clips/viola_good/viola_good_line047.ogg"
            viola.char "Bye!"
    
label violaVisit1_1F: 
    show screen debrief("violaVisit1")
    $ topicsReviewed = [0, 0, 0, 0, 0, 0, 0]

    mentor.char debrief "Welcome to the debrief section!"

    mentor.char debrief "This is where we will look over the decisions you made during this visit."

    label violaVisit1_1F_Continue: 

    mentor.char debrief "Select a decision or metric to review! When you've reviewed at least 3 topics, press continue."

    label violaVisit1_1F_End:
    "This concludes Viola's first patient visit. This is the end of the script!"

    $ achievement.grant("First Look")

    #GA4 Key Event
    $ analytics.event("violaVisit1", "end_violaVisit1_1D")

    return