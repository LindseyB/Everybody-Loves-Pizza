# the pizzas
image pizza newyork     = "nystyle.png"
image pizza californian = "californian.png"
image pizza deepdish    = "deepdish.png"
image pizza neopolitan  = "neopolitan.png"
image pizza sicilian    = "sicilian.png"

image bg pizzaria       = "background.png"

# all the pizzas to love
define ny  = Character('New York Style Pizza', color="#c8ffc8")
define ca  = Character('Californian Style Pizza', color="#33cc33")
define dd  = Character('Deep Dish Pizza', color="#ff3300")
define neo = Character('Neopolitan Pizza', color="#cc6699")
define s   = Character('Sicilian Pizza', color="#3399ff")

# track who has been spoken to and how much they like the player
init python:
    spoke_ny  = False
    spoke_ca  = False
    spoke_dd  = False
    spoke_neo = False
    spoke_s   = False
    
    aff_ny    = 0
    aff_ca    = 0
    aff_dd    = 0
    aff_neo   = 0
    aff_s     = 0

# The game starts here.
label start:
    stop music fadeout 1.0
    
    scene bg pizzaria with fade

    "The local pizzaria has a speed dating event going on and after months of a dry spell you've decided to check it out. You see various interesting beings sitting around what do you do?"
    
    menu:
        
        "Scope it out and see what's interesting.":
            "You approach closer and you notice something weird about the beings at speed dating, but you figure it's probably just the cold medicine messing with you."
        "Run away in horror.":
            "You can't leave now, there's some good stuff happening here."
    
    "All the patrons appear to be different types of pizza. You are not sure how long it's been like this, but you decide to roll with it. Which pizza do you talk to?"
    jump pizza_select
    

    return
    
    
label pizza_select:
    
    scene bg pizzaria with fade
    
    menu:
        "I like my lovin' like I like my bagels, New York Syle" if not spoke_ny:
            jump ny_style
        "Hmmm... I've heard good things about Californian lovin'" if not spoke_ca:
            jump californian
        "I want the D... Deep Dish Pizza" if not spoke_dd:
            jump deep_dish
        "Wake up Neopolitan the Matrix has you and so do I" if not spoke_neo:
            jump neopolitan
        "How about some sizzlin' sicilian" if not spoke_s:
            jump sicilian
        "Well I think I've made a decision" if (spoke_ny and spoke_ca and spoke_dd and spoke_neo and spoke_s):
            jump player_choice
    
    return
    

label player_choice:
    "Well, who do you pick?"
    
    menu:
        "New York Style":
            show pizza newyork with dissolve
            if aff_ny > 10:
                play sound "harp.mp3"
                ny "Awesome! I liked you a lot too!"
            else:
                play sound "fail.mp3"
                ny "I'm not sure this will work out."
        "Californian":
            show pizza californian with dissolve
            if aff_ca > 10:
                play sound "harp.mp3"
                ca "I could tell from the moment I sensed your energy."
            else:
                play sound "fail.mp3"
                ca "Um... yeah. I uh... my house is on fire and I have to leave."
        "Deep Dish":
            show pizza deepdish with dissolve
            if aff_dd > 10:
                play sound "harp.mp3"
                dd "Yeah! That's what I am talking about!"
            else:
                play sound "fail.mp3"
                dd "Please no."
        "Neopolitan":
            show pizza neopolitan with dissolve
            if aff_neo > 10:
                play sound "harp.mp3"
                neo "Ti amo!"
            else:
                play sound "fail.mp3"
                neo "Ti odio!"
        "Sicilian":
            show pizza sicilian with dissolve
            if aff_s > 10:
                play sound "harp.mp3"
                s "Oh, cool I guess."
            else:
                play sound "fail.mp3"
                s "Oh, sorry I have plans...?"
                
    return
            
            
label ny_style:
    show pizza newyork at right with dissolve
    
    ny "Hey, how's it goin'?"
    
    menu:
        "Eh... people don't actually want to know the answer to that question.":
            ny "I know, right? Yet we all still bother with it anyway."
            $ aff_ny += 5
        "Okay, you?":
            $ aff_ny += 1
            ny "I'm doing pretty well."
        "Super good! The best really! Oh my gosh I have so many great things going on.":
            ny "Oh... wow... aren't you spunky..."
            $ aff_ny -= 10
    
    ny "So, what do you enjoy doing in your free time?"
    
    menu:
        "Going places, expirencing new things, going to bars, I like doing it all.":
            ny "You must be busy a lot."
            $ aff_ny += 1
        "Meh. Not much really.":
            ny "That much make life hard."
        "Traveling. Traveling and more traveling. Also boats.":
            ny "Do your parents have a trust fund or something that you can have expensive taste?"
            $ aff_ny -= 10
    
    ny "What kind of music do you like?"
    
    menu:
        "Everything but country and rap, more like CRAP amirite?":
            ny "That's kinda close-minded?"
            $ aff_ny -= 10
        "A little bit of everything, but I've been digging post-punk lately":
            ny "Oh yeah, how good is Bauhaus?"
            $ aff_ny += 10
        "Everything. All music is good. Mostly I turn on the radio and whatever is on I love.":
            ny "Oh. Well, that's good."
            $ aff_ny += 1
            
    ny "If you could live anywhere in the world where would it be?"
    
    menu:
        "New York, of course, there's everything there.":
            ny "Damn straight!"
            $ aff_ny += 10
        "I dunno, the beach probably. Or the jersey shore. Have you seen that show?":
            ny "Ugh... no."
            $ aff_ny -= 10
        "France, I love the idea of living abroad.":
            ny "Oh that could be cool."
            $ aff_ny += 1
            
    ny "What's your favorite color?"
    
    menu:
        "GLITTER!":
            ny "That's not a color."
            $ aff_ny -= 10
        "Black like my heart":
            ny "Yeah, me too."
            $ aff_ny += 10
        "Blue":
            ny "Oh yeah that's a nice color."
            $ aff_ny += 1
            
    
    if aff_ny >= 10:
        ny "It was really nice meeting you."
    elif aff_ny > 0:
        ny "See ya!"
    else:
        ny "Alright, I can't take much more of this conversation."
    
    $ spoke_ny = True
    jump pizza_select
    
label californian:
    show pizza californian at right with dissolve
    
    ca "Namaste"
    
    menu:
        "Oh are you Hindu?":
            "No, but it's not cultural appropriation because I said so."
            $ aff_ca -= 10
        "Oh I love yoga!":
            "Me too!!!"
            $ aff_ca += 10
        "What does that even mean?":
            "It's just a respectful greeting"
            $ aff_ca -= 1
            
    ca "What do you like doing for exercise?"
    
    menu:
        "Mostly yoga, but sometimes I like Tai Chi":
            ca "Oh, me too!"
            $ aff_ca += 10
        "Exer-who!?":
            ca "That thing you do to stay healthy?"
            $ aff_ca -= 10
        "I run, like the wind.":
            ca "I love that!"
            $ aff_ca += 1
            
    ca "How do you feel about avocados?"
    
    menu:
        "What kind of question is that? It's like asking how you feel about pizza. Don't answer that...":
            ca "Are you feeling okay?"
            $ aff_ca -= 10
        "I LOVE AVOCADOS!!! I only eat avocados and avocado adjacent things!":
            ca "Oh we should split an avocado pizza sometime!"
            $ aff_ca += 10
        "They're food. I like them, but I don't like-like them.":
            ca "Yeah, they're delicious."
            $ aff_ca += 1
            
    ca "Do you recycle?"
    
    menu:
        "Of course!!! I also compost! It smells amazingggggggg!":
            ca "RIGHT!?!?!"
            $ aff_ca += 10
        "Um... yeah.":
            ca "It's so important."
            $ aff_ca += 1
        "Do you have a problem? First it was avocados and now recyling questions? Is this actually happening to me?":
            ca "Your pupils are looking a bit dialated."
            $ aff_ca -= 10
            
    ca "Okay, how about an easy question;  What is brown and sticky?"
    
    menu:
        "A stick!":
            ca "Yesss!!!!"
            $ aff_ca += 10
        "Poop?":
            ca "You might want to go to a doctor."
            $ aff_ca += 1
        "How about you answer a question? What is wrong with you? Seriously, what is wrong with you!?":
            ca "Um... should I call 911?"
            $ aff_ca -= 10
            
    if aff_ca >= 10:
        ca "I think we might be soulmates."
    elif aff_ca > 0:
        ca "Have a good day."
    else:
        ca "Please, forget you ever met me."
            
    
    $ spoke_ca = True
    jump pizza_select

label deep_dish:
    show pizza deepdish at right with dissolve
    
    dd "Yo, how's it hanging?"
    
    menu:
        "Down and slightly to the right":
            dd "Nice!"
            $ aff_dd += 10
        "Good":
            dd "Yeah, me too."
            $ aff_dd += 1
        "Have you noticed that everyone is pizza? See I took some cold medicine before this and now everyone is pizza.":
            dd "What are you...? I don't want to know."
            $ aff_dd -= 10
    
    dd "What's your favorite basketball team?"
    
    menu:
        "I don't really watch much basketball.":
            dd "You're missing out. It's pretty awesome."
            $ aff_dd += 1
        "I like the Knicks.":
            dd "Be careful how loud you say that."
            $ aff_dd -= 10
        "Chicago Bulls, I just loved the Jordan-era basketball.":
            dd "Hell yeah!"
            $ aff_dd += 10
    
    dd "What do you like on your hotdog?"
    
    menu:
        "Not a thing. I can eat it quicker that way. If you know what I mean?":
            dd "I don't but I could get behind it. If you know what I mean?"
            $ aff_dd += 5
        "Chi-town style fo sho!":
            dd "Aww yeah, son! You got it!"
            $ aff_dd += 10
        "Ew. I'm more into pizza. Are you sure you don't see pizza everywhere?":
            dd "I don't and you don't know what you are missing."
            $ aff_dd -= 10
    
    dd "If you could be any animal what would you be?"
    
    menu:
        "Um... pizza is an animal right? I would be pizza. Pizza pizza! That's the sound a pizza makes.":
            dd "Pizza is definitely not an animal"
            $ aff_dd -= 10
        "BEAR! ROAR!!!":
            dd "Me too!!!"
            $ aff_dd += 10
        "Probably a cute bunny.":
            dd "Aww, that's sweet."
            $ aff_dd += 1
            
    dd "Okay, final question and it's a doozy. Desert island movie. Go!"
    
    menu:
        "Gotta be Blues Brothers":
            dd "We're on a mission from God!!!"
            $ aff_dd += 10
        "Star Wars":
            dd "That's okay, I guess... for nerds."
            $ aff_dd -= 1
        "Teenage Mutant Ninja Turtules. You know with all the pizza. I kinda love pizza. I mean I'm in {b}love{/b} with pizza.":
            dd "Um... that's um... great for you."
            $ aff_dd -= 10
            
    if aff_dd >= 10:
        dd "You gotta make sure I get those digits."
    elif aff_dd > 0:
        dd "Well, bye."
    else:
        dd "Um... why don't you talk to someone else."
    
    $ spoke_dd = True
    jump pizza_select
    
label neopolitan:
    show pizza neopolitan at right with dissolve
    
    neo "Ciao bella"
    
    menu:
        "Cioa":
            neo "Close enough."
            $ aff_neo += 1
        "Ciao":
            neo "parli italiano?"
            $ aff_neo += 10
        "Hola":
            neo "What language is that?"
            $ aff_neo -= 10
            
    neo "Who's your favorite painter?"
    
    menu:
        "Michelangelo":
            neo "I love him"
            $ aff_neo += 10
        "Monet":
            neo "He's okay I guess."
            $ aff_neo += 1
        "C. M. Coolidge. You know the painting of dogs playing poker? He did the that. He's a genius.":
            neo "I don't really like the idea of things doing things they don't normally do. Dogs never play poker so why do we want to see what it would look like. It's just silly."
            $ aff_neo -= 10
            
    
    neo "Why are your eyes so dialated?"
    
    menu:
        "The better to see you with my dear.":
            neo "Nice."
            $ aff_neo += 10
        "YOUR EYES ARE DIALATED! YEAH! TAKE THAT!":
            neo "I didn't mean it like an insult."
            $ aff_neo -= 10
        "Oh. I took some cold medicine and now everything is pizza.":
            neo "Well, who hasn't done that before."
            $ aff_neo += 1
            
    neo "Okay, here's a tricky one. Favorite opera?"
    
    menu:
        "Cats... that's an opera right? I think it's an Opera.":
            neo "It's not, but I'll allow it."
            $ aff_neo += 1
        "Tosca. Everyone loves Puccini.":
            neo "Yes! So good!"
            $ aff_neo += 10
        "Um... pizza...? I dunno why I said pizza just now, but yeah I'm gonna stick with pizza.":
            neo "Well, I'm not sure that really counts."
            $ aff_neo -= 10
            
    neo "Last question. Ready!? If you could have a super power what would it be?"
    
    menu:
        "Everything pizza.":
            neo "What???"
            $ aff_neo -= 10
        "Invisibility":
            neo "Pretty handy."
            $ aff_neo += 1
        "Flight!":
            neo "The best!!!"
            $ aff_neo += 10
            
    if aff_neo >= 10:
        neo "Arrivederci bella."
    elif aff_neo > 0:
        neo "Nice meeting you."
    else:
        neo "Yeah. Bye."
            
    
    $ spoke_neo = True
    jump pizza_select
    
label sicilian:
    show pizza sicilian at right with dissolve
    
    s "Um... hi"
    
    menu:
        "Hi.":
            s "Hi..."
            $ aff_s += 10
        "Bye.":
            s "Bye..."
            $ aff_s -= 10

    s "I dunno what to say."
    
    menu:
        "That's okay try asking a question.":
            s "Okay I'll try it."
            $ aff_s += 10
        "Me neither.":
            s "Talking to people is hard."
            $ aff_s += 25
        "Step up your game, you- you- you {b}pizza{/b}!":
            s "Wait... did you call me pizza?"
            $ aff_s -= 10
    
    s "Okay, a question. I got this. What do you like?"
    
    menu:
        "What a garbage question! I like pizza, I also like other things, but really that would take too long to list.":
            s "Mean!"
            $ aff_s -= 20
        "Err... maybe try again with something less vague?":
            s "Okay I can do this!"
            $ aff_s += 10
        "PIZZA!!!":
            s "Me too!"
            $ aff_s += 20
            
    
    s "Okay, what's your favorite co-op video game to play with your mom at home at night while it's raining outside?"
    
    menu:
        "That might be too specific of a question... dial it in you'll get it.":
            s "Okay, thanks for bearing with me."
            $ aff_s += 5
        "Um... Castle Crashers? I think. I don't get to play video games with my mom very often.":
            s "Oh, me and my mom like playing Minecraft."
            $ aff_s += 20
        "...um.... pizza... um.... {i}::drools on self::{/i}":
            s "You don't look so good."
            $ aff_s -= 1
            
    s "Okay."
    
    menu:
        "Um okay.":
            s "Okay."
            $ aff_s += 1
        "Good.":
            s "Good."
            $ aff_s += 1
        "{i}::Pokes the pizza::{/i} I expected you to be stickier.":
            s "What?"
            $ aff_s -= 10
            
    if aff_s >= 10:
        s "I... {i}::blushes::{/i}"
    elif aff_s > 0:
        s "Maybe... {i}::stammer::{/i}"
    else:
        s "{i}::Walks away::{/i}"
            
    
    $ spoke_s = True
    jump pizza_select
