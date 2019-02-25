__author__ = "Luna"
__copyright__ = "Copyright (c) 2019 Isabel Luna"
__credits__ = ["Luna, Isabel"]
__license__ = "MIT lisence"

import time

def question_name():
    print('What\'s your name?')
    name = input(' ')
    return name

def question_gender():
    print('Are you female or male?')
    gender = input('')
    return gender



def story_male(name):
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You feel a sharp pain in your back and you open your eyes to notice that the breeze has dried your eyes. You turn to your side but realize the pain in your back only seems to be getting worse. A light
groan exits your lips as you fall onto your stomach, your hands rubbing your back. Your eyes remain close but you begin to hear the whistles of the wind, the grass as your elbow runs through it.
You decide to open your eyes, blinking many times due to the wind. You notice several figures on the ground a few meters away from you.

What do you do?

1) Try and walk to the figures.
2)Remain still, hoping they don\'t see you.

Please type out 1 or 2.
        ''')
    path = input('')
    if path == '1':
        continuationFirstPath()
    else:
        continuedFirstPath()

def continuationFirstPath():
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You struggle to get up. The pain in your back seems to be diminishing, however as you manage to find your balance your legs
give up and you fall to your arms and knees. You look outward to notice three bodies, all seeming to be male. Suddenly you hear
something behind you as it moves along the grass. You quickly look behind to see a girl groaning, struggling to keep her eyes open. You let out a
sharp gasp as you crawl away from her. As you move back you notice the other people beginning to wake up. You quickly stand up in a panic. The girl stands up, her legs
mildly shaking. You stare at her as she tries to find her balance. Her eyes are a beatiful shade of green and her hair, although very messy, drapes down to her wide hips.

"Who are you? Where am I? What's going on!?" The girl asks aggresively. She had a pleasant British accent that sounded soothing to your American ears. "God my back..."

You remain silent to look behind you. The other guys slowly move away from each other. You instictively hold your hands up and they turn back to you with frownsself.
You feel a soft tap on your shouder and you turn around to see the girl.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''')
    print('"Well?" She says')
    nameStory = input('')

    print('"' + nameStory + ' huh? What an interesting name" She says.')
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"Do you have any idea where we are?" She asks, looking behind your shoulder.
The guys begin to move closer circling around you two. You step to the side so you all form a small circle.

"No idea my mind is completely blank" one of theem says. His voice was incredibly deep considering how young he looked. He had very dark skin and his hair was in these reall nice dreads.
He had a sharp jawline a chiseled beard. "My name's Tyree though, what about you guys?"

"I'm Tori, I'm from England" Tori smiledself.

"I'm Koen, I live in Canada. I can't really remember much though..." Koen, the guy standing next to you says as he rubs the back of his head.
You immediately connect with his accent for it's very similar to yours unlike Tyree's and
Tori's. You look at Koen's hair and can't help but notice how well kept it was. It was black but it shined when the sun hit it, you'd always wanted hair like that but your stubborn spikes could never seem to glow like that.
No matter how much gel you seemed to put on you always seemed to be walking around with bed hairself.

"Yeah man, my mind is completely out of it. I'm Kevin, can't really remember where I'm from yet. Luck bastards." Kevin playfully smirked, he seemed very warm and playful.
His phydique was very nice, even you had to admit that much. It pained you
to see yourself surrounded by good looking guys and a girl. You'd never been that one good looking guy or anywhere near good looking. You had a very generic face with dark brown eyes and your hair was always a mess.
You remembered why you stopped trying on your looks, it was when your ex had dumped you for some jock on the soccer team. Even at twenty years old, a sophomore in college you still haven't managed to get your looks or life together.

"Alright so no one has ANY idea where we are or how we got here?" Tori asks throwing her hands in the air. You then realized how small she was, you guess she's around five feet. Of course you'll never ask her. That'd be awkward and rude.

"No but my back is killing me, can someone give me a massage?" Kevin laughed obviously in pain.

"Here turn around let me check" Tyree walked over to him and lifted Kevin's shirt up. Kevin groaned and tried to move away but Tyree held him in place. "All I see is your nice tattoo dude."

"I've never gotten a tattoo..." Kevin mumbled.

"Check if I have one." Tyree turned around and lifted his shirt so everyone could see. On his back was a drawing of a puzzle piece with abstract paintings on it.

"Do we all have it?" Tori gasped lifting the back of her shirt to reveal another puzzle piece. Koen quickly followed to also show another puzzle piece. You stubbornly lift your shirt up awkwardly
and stand next to them in the circle. You do your best to look behind you and notice all the puzzle pieces seem to fit with each other. Yours fit with Tori and Kevin's which made you feel foolish pride.

"What even is this? Oh dude my mom's gonna kill me." Koen frowned.

"What if this is an experiment?" Tori asked, putting her shirt down.

"Well this is pretty messed up. But if it is then they obviously want us to do something. Prove something." Tyree said running his fingers on his lips.

"Whatever look at where we are, we're in the middle of nowhere. All I see is grass grass grass. Wait" Koen stopped suddenly and pointed behind Kevin. There was a mountain with a forest surrounding it. Although it was extrememly far away
the forest made it seem as if it were closer.

"That's our best shot at finding anything. I can't see anything else." Tori suggested.

"Alright let's start moving then. Everyone in?" Tyreen said, looking at you.

    ''')
    responseTori = input('"Are you in, yes or no?" Tori asked.').lower()
    if responseTori == 'yes':
        headingToMount()
    elif responseTori == 'no':
        print('You are left behind as they head to the mount. Days later you die from hunger.')
    else:
        exit()

def headingToMount():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('You follow them to the mountain. Tyreen had managed to estimate the time using the sun and he said it was around 5 o\'clock meaning that it had been over two hours since they first started walking')
    print('After hours of walking the sun began to fall and night was approaching.')
    print('The five of you agree to continue since you could already see the forest up ahead. Koen had mentioned that there might be "creatures" there that they don\'t know of. You agreed with Tori to sout the area once you got there and set up camp.')
    print('After arriving at the edge of the forest you and Tyreen walk a number of meters away and come back telling everyone it\'d be safe for now.')
    print('You all help bring supplies to Koen who had begun to form a fire and contain it.')
    print('Everyone eventually begins to go to sleep.')
    print('Who do you sleep next to?')
    people = ['tori', 'koen', 'tyree', 'kevin']
    responsePeople = input('')
    if responsePeople.lower() not in people:
        print('Who do you sleep next to? ')
    else:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('The following morning you wake up next to ' + responsePeople)
    print('You all begint to walk into the forest and begin to notice many small animals. You\'ve been walking with ' + responsePeople)
    print('And somehow that\'s made you feel safer while walking.')
    print('Tyree updated everyone everytime a new hour came by. It was around the third hour of walking when you all came across two paths.')
    print('To the left the path seemed to go down a small hill where the trees covered the rest and on the right the path just stretched onto the forest.')
    print('"Which one do we take?" Tori asked. They all gave each other looks and then look back to you')
    answerRL = input('')
    if answerRL == 'left':
        print('You point left and begin to lead the group down the small incline.')
        toLake()
    elif answerRL == 'right':
        print('You begin to walk down the right path as the others follow close behind.')
        time.sleep(3)
        print('As you walk carefully through the forest you hear a large growl. Suddenly a beast rises from the bushes. A black bear stands right above you.')
        print('What do you do, Run back or Play dead?')
        answerbear = input('')
        if answerbear == 'run back':
            print('You succesfully run away down the left path, leaving the bear behind.')
            toLake()
        elif answerbear == 'play dead':
                print('You play dead and hope the bear just goes away.')
                time.sleep(3)
                print('However the bear is too smart for that and begins to eat its free meal.')
        else:
            print('What do you do, Run back or play dead?')
    else:
        print('Choose, left or right.')

def toLake():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('You all scurry down the hill and begin to smell a nice auroma that reminds you of the beach. As you all head down the path the smell gets stronger and then you begin to hear noises.')
    print('You hear water crash against rocks but very faintly.')
    print('Koen begins to run to the sound, you all follow behind except Tori')
    print('You decide to stay behind with Tori')
    print('You use this oppurtunity to try and get close.')
    print('')
    print('1. "So any sports you into?"')
    print('2. "What do you think of all this?"')
    while True:
        toriTalkAnswerM = input('')
        if toriTalkAnswerM == '1':
            print('"Well from what I can remember I did like lacrosse. But I think I\'m more of a bookworm to be honest. And given my height I can\'t do many sports." Tori giggled.')
            print('"If you don\'t mind me asking...How tall are you?" You ask politely already breaking into a cold sweat.')
            print('"Only five one. I\'m a midget!" She continued to giggle.')
            print('You give a small chuckle, "Heh, that\'s adorable though."')
            print('Her face turns red as she looks away. You immediately regret saying that.')
            break
        elif toriTalkAnswerM == '2':
            print('It\'s crazy honestly, but also very scary. I\'m terrified couldn\'t really sleep at night. I just want to get home.')
            print('You give a slight nod and say, "Yeah same, I don\'t like admitting it but I am scared. But hey I know we\'ll find a way to get home."')
            print('She looks up to you and gives you a beautiful smile. Your heart begins to race.')
            break
        else:
            print('What do you want to ask Tori? 1 or 2?')
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You both make your way down to a lake where the guys had already begun to splash around. Tori quickly follows them, pulling up her sleeves and pants. You look around and spot something to your left. It appears
to be a small boat with a long lantern on it.

"Hey you guys, there's a boat over there!" You shout. They all turn to the left and examine the boat. Tyree begins to walk toward it, stepping out of the water and putting his shoes back on.

"Be careful..." Tori mumbled. You all follow closely behind. Your heart begins to pump faster and you notice Tori has wrapped her arms around you. Your heart goes crazy with all these emotions and you can feel your face turn red.
''')
    time.sleep(10)
    print('''
Tyree screams and falls back as a pale white man jumps from inside the small boat.

"HIIIIYAHHH~!" The man screams, in a poor fighting stance. You all let out a scream and go back. "You'll never eat me you monsters!" The man began to wave the lamp around.

"HEY we're good!" Tyree got up, trying to dodge the lamp.

"That's what they all say and then the next thing I know you've eaten my grandmother." The man said aggresively.

"What the - No look we don't know where we are we just need help getting back to where we came from. Do you know if there's a city nearby to call the cops?" Tyree explained.

"Cops? are you foreigners? The only city near here is the elves' but that's in the mountain and considering the war going on right now you are not getting anywhere near there." The man chuckled still waving the lamp around.

"Can you put that down. What are you talking about? War? There's no war dude." Kevin said.

"Well yes there is. It's been going on for almost five years you foreigners." The man shook his head. "You ain't getting anymore information out of me. You won't! Never!" The man yelled.

"What a lunatic..." Tori laughed quietly. You looked down at her and she was holding in laughter.

"Can you tell us what planet this is?" Koen asked.

"Planet? What strange language do you use you foreigner?" The man asked.

"Planet. Like Earth? Are we on Earth?" Koen said.

"Well of course you're not on Earth. That's not a planet ya bimbo. It's a celestial body, but no this is Scorux." The man chuckled.

"Obviously we're not on Earth anymore then. Damn it." Koen said. "Could someone in the city help us get back to Earth?"

"Probably but you ain't getting there anytime soon. Not without me that is." The man smiled.

"Can you take us there? We don't have much but once we get back on our feet we promise to help you with whatever you want." Tori said walking toward the man.

"Ah well I would like to play a game . It's been so long. If you beat me I'll give you a ride on my boat to a large city where they could help you. If not then I'll just leave ya here." The man suggested.

"Deal. Who wants to play?" Tori asked the group. They all shrugged obviusly not wanting to play.

"I'll do it." You say, walking toward the man confidently trying to impress Tori.

"Good let's begin." He said.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

    print('"It\'ll be a simple math game. I\'ll have my friend think of two equations, each one having the answer from the previous equation." The man explained.')
    print('"For example, their first equation can be one plus one whih of course is two, their second equation can be two times four and so on and so forth. Understand?" the man asked. They all shook their head.')
    print('"Whoever gets the most correct wins, however if you get the last questions right you win the entire game no matter how many points you or the oppenent has." The man explained.')
    print('"Just get the last one correct no need to try for the first few." Tori whispered.')
    print('You nodded, your plan was exactly that.')
    print('The man pulled out a creature from his coat. It was a dwarf, at least it looked like one to you. Except it was incredily small, the size of a puppy.')
    print('"Did you hear that? Now get started with them equations!" the man said putting the dwarf creature down. The dwarf coughed and began to say the equations.')

    from random import randint
    firstnumber = randint(1, 10)

    mul = firstnumber * 12
    firstanswer = input('')
    if firstanswer == mul:
        print('"Correct"')
    else:
        print('"Incorrect"')


def continuedFirstPath():

    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You remain still, trying to focus your eyes to see what these figures are. You rub your eyes a few times before your vision begins to finally clear upself.
You notice there are three of them, all seeming to be guys. You begin to look around, trying to find out where exactly you are. As you turn your head back you
see a girl lying next to your feet. You let out a sharp gasp as you craw away from her. As you move back you notice the other people beginning to wake up. You quickly stand up in a panic. The girl stands up, her legs
mildly shaking. You stare at her as she tries to find her balance. Her eyes are a beatiful shade of green and her hair, although very messy, drapes down to her wide hipsself.

"Who are you? Where am I? What's going on!?" The girl asks aggresively. She had a pleasant British accent that sounded soothing to your American ears. "God my back..."

You remain silent to look behind you. The other guys slowly move away from each other. You instictively hold your hands up and they turn back to you with frownsself.
You feel a soft tap on your shouder and you turn around to see the girl.

        ''')
    print('"Well?" She says')
    nameStory = input('')
    print('"' + nameStory + ' huh? What an interesting name" She says.')
    print('''
"Do you have any idea where we are?" She asks, looking behind your shoulder.
The guys begin to move closer circling around you two. You step to the side so you all form a small circle.

"No idea my mind is completely blank" one of theem says. His voice was incredibly deep considering how young he looked. He had very dark skin and his hair was in these reall nice dreads.
He had a sharp jawline a chiseled beard. "My name's Tyree though, what about you guys?"

"I'm Tori, I'm from England" Tori smiledself.

"I'm Koen, I live in Canada. I can't really remember much though..." Koen, the guy standing next to you says as he rubs the back of his head.
You immediately connect with his accent for it's very similar to yours unlike Tyree's and
Tori's. You look at Koen's hair and can't help but notice how well kept it was. It was black but it shined when the sun hit it, you'd always wanted hair like that but your stubborn spikes could never seem to glow like that.
No matter how much gel you seemed to put on you always seemed to be walking around with bed hairself.

"Yeah man, my mind is completely out of it. I'm Kevin, can't really remember where I'm from yet. Luck bastards." Kevin playfully smirked, he seemed very warm and playful.
His phydique was very nice, even you had to admit that much. It pained you
to see yourself surrounded by good looking guys and a girl. You'd never been that one good looking guy or anywhere near good looking. You had a very generic face with dark brown eyes and your hair was always a mess.
You remembered why you stopped trying on your looks, it was when your ex had dumped you for some jock on the soccer team. Even at twenty years old, a sophomore in college you still haven't managed to get your looks or life together.

"Alright so no one has ANY idea where we are or how we got here?" Tori asks throwing her hands in the air. You then realized how small she was, you guess she's around five feet. Of course you'll never ask her. That'd be awkward and rude.

"No but my back is killing me, can someone give me a massage?" Kevin laughed obviously in pain.

"Here turn around let me check" Tyree walked over to him and lifted Kevin's shirt up. Kevin groaned and tried to move away but Tyree held him in place. "All I see is your nice tattoo dude."

"I've never gotten a tattoo..." Kevin mumbled.

"Check if I have one." Tyree turned around and lifted his shirt so everyone could see. On his back was a drawing of a puzzle piece with abstract paintings on it.

"Do we all have it?" Tori gasped lifting the back of her shirt to reveal another puzzle piece. Koen quickly followed to also show another puzzle piece. You stubbornly lift your shirt up awkwardly
and stand next to them in the circle. You do your best to look behind you and notice all the puzzle pieces seem to fit with each other. Yours fit with Tori and Kevin's which made you feel foolish pride.

"What even is this? Oh dude my mom's gonna kill me." Koen frowned.

"What if this is an experiment?" Tori asked, putting her shirt down.

"Well this is pretty messed up. But if it is then they obviously want us to do something. Prove something." Tyree said running his fingers on his lips.

"Whatever look at where we are, we're in the middle of nowhere. All I see is grass grass grass. Wait" Koen stopped suddenly and pointed behind Kevin. There was a mountain with a forest surrounding it. Although it was extrememly far away
the forest made it seem as if it were closer.

"That's our best shot at finding anything. I can't see anything else." Tori suggested.

"Alright let's start moving then. Everyone in?" Tyreen said, looking at you.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')
    responseTori = input('"Are you in, yes or no?" Tori asked.')
    if responseTori == 'yes':
        headingToMount()
    elif responseTori == 'no':
        print('You are left behind as they head to the mount. Days later you die from hunger.')
    else:
        exit()

def story_female(name):
    print('''
    You feel a sharp pain in your back and you open your eyes to notice that the breeze has dried your eyes. You turn to your side but realize the pain in your back only seems to be getting worse. A light
    groan exits your lips as you fall onto your stomach being careful not to lean too hard on your breasts, your hands rubbing your back. Your eyes remain close but you begin to hear the whistles of the wind, the grass as your elbow runs through it.
    You decide to open your eyes, blinking many times due to the wind. You notice several figures on the ground a few meters away from you.

    What do you do?

    1) Try and walk to the figures.
    2)Remain still, hoping they don\'t see you.

    Please type out 1 or 2.
    ''')
    path = input('')
    if path == ('1'):
        firstPathF()
    else:
        secondPathF()

def firstPathF():
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You struggle to get up. The pain in your back seems to be diminishing, however as you manage to find your balance your legs
give up and you fall to your arms and knees. You look outward to notice three bodies, all seeming to be male. Suddenly you hear
something behind you as it moves along the grass. You quickly look behind to see a girl groaning, struggling to keep her eyes open. You let out a
sharp gasp as you crawl away from her. As you move back you notice the other people beginning to wake up. You quickly stand up in a panic. The girl stands up, her legs
mildly shaking. You stare at her as she tries to find her balance. Her eyes are a beatiful shade of green and her hair, although very messy, drapes down to her wide hips.

"Who are you? Where am I? What's going on!?" The girl asks aggresively. She had a pleasant British accent that sounded soothing to your American ears. "God my back..."

You remain silent to look behind you. The other guys slowly move away from each other. You instictively hold your hands up and they turn back to you with frownsself.
You feel a soft tap on your shouder and you turn around to see the girl.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''')
    print('"Well?" She says')
    nameStory = input('')

    print('"' + nameStory + ' huh? What an interesting name" She says.')
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"Do you have any idea where we are?" She asks, looking behind your shoulder.
The guys begin to move closer circling around you two. You step to the side so you all form a small circle.

"No idea my mind is completely blank" one of theem says. His voice was incredibly deep considering how young he looked. He had very dark skin and his hair was in these reall nice dreads.
He had a sharp jawline a chiseled beard. "My name's Tyree though, what about you guys?" He was very handsome.

"I'm Tori, I'm from England" Tori smiled.

"I'm Koen, I live in Canada. I can't really remember much though..." Koen, the guy standing next to you says as he rubs the back of his head.
You immediately connect with his accent for it's very similar to yours unlike Tyree's and
Tori's. You look at Koen's hair and can't help but notice how well kept it was. It reminded you of your ex who also had very nice hair.

"Yeah man, my mind is completely out of it. I'm Kevin, can't really remember where I'm from yet. Luck bastards." Kevin playfully smirked, he seemed very warm and playful.
His phydique was charming, even you had to admit that much. You felt excited but also overwhelmed
to see yourself surrounded by good looking guys and a girl. You've never been that one good looking girl or anywhere near good looking. You had a very generic face with dark brown eyes and your hair was always tied up in the same bun.
You remembered why you stopped trying on your looks, it was when your ex had dumped you for some girl on the honor roll. Even at twenty years old, a sophomore in college you still haven't managed to get your looks or life together.

"Alright so no one has ANY idea where we are or how we got here?" Tori asks throwing her hands in the air. You then realized how small she was because she wasn't any taller than you. You were only five one which you were both proud of and embarrassed.
You'll probably ask her later just to confirm and it'd serve as good small talk.

"No but my back is killing me, can someone give me a massage?" Kevin laughed obviously in pain.

"Here turn around let me check" Tyree walked over to him and lifted Kevin's shirt up. Kevin groaned and tried to move away but Tyree held him in place. "All I see is your nice tattoo dude."

"I've never gotten a tattoo..." Kevin mumbled.

"Check if I have one." Tyree turned around and lifted his shirt so everyone could see. On his back was a drawing of a puzzle piece with abstract paintings on it.

"Do we all have it?" Tori gasped lifting the back of her shirt to reveal another puzzle piece. Koen quickly followed to also show another puzzle piece. You stubbornly lift your shirt up awkwardly
making sure not to expose the front. You walked closer to them in the circle. You do your best to look behind you and notice all the puzzle pieces seem to fit with each other. Yours fit with Tori and Kevin's which made you feel foolish pride.

"What even is this? Oh dude my mom's gonna kill me." Koen frowned.

"What if this is an experiment?" Tori asked, putting her shirt down.

"Well this is pretty messed up. But if it is then they obviously want us to do something. Prove something." Tyree said running his fingers on his lips.

"Whatever look at where we are, we're in the middle of nowhere. All I see is grass grass grass. Wait" Koen stopped suddenly and pointed behind Kevin. There was a mountain with a forest surrounding it. Although it was extrememly far away
the forest made it seem as if it were closer.

"That's our best shot at finding anything. I can't see anything else." Tori suggested.

"Alright let's start moving then. Everyone in?" Tyreen said, looking at you.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')
    responseTori = input('"Are you in, yes or no?" Tori asked.')
    if responseTori == 'yes':
        headingToMountF()
    elif responseTori == 'no':
        print('You are left behind as they head to the mount. Days later you die from hunger.')
    else:
        exit()

def headingToMountF():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('You follow them to the mountain. Tyreen had managed to estimate the time using the sun and he said it was around 5 o\'clock meaning that it had been over two hours since they first started walking')
    print('After hours of walking the sun began to fall and night was approaching.')
    print('The five of you agree to continue since you could already see the forest up ahead. Koen had mentioned that there might be "creatures" there that they don\'t know of. You agreed with Tori to sout the area once you got there and set up camp.')
    print('After arriving at the edge of the forest you and Tyreen walk a number of meters away and come back telling everyone it\'d be safe for now.')
    print('You all help bring supplies to Koen who had begun to form a fire and contain it.')
    print('Everyone eventually begins to go to sleep.')
    print('Who do you sleep next to?')
    people = ['tori', 'koen', 'tyree', 'kevin']
    responsePeople = input('')
    if responsePeople not in people:
        print('Who do sleep next to? ')
    else:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('The following morning you wake up next to ' + responsePeople)
    print('You all begint to walk into the forest and begin to notice many small animals. You\'ve been walking with ' + responsePeople)
    print('And somehow that\'s made you feel safer while walking.')
    print('Tyree updated everyone everytime a new hour came by. It was around the third hour of walking when you all came across two paths.')
    print('To the left the path seemed to go down a small hill where the trees covered the rest and on the right the path just stretched onto the forest.')
    print('"Which one do we take?" Tori asked. They all gave each other looks and then look back to you')
    answerRL = input('')
    if answerRL == 'left':
        print('You point left and begin to lead the group down the small incline.')
        toLakeF()
    elif answerRL == 'right':
        print('You begin to walk down the right path as the others follow close behind.')
        time.sleep(3)
        print('As you walk carefully through the forest you hear a large growl. Suddenly a beast rises from the bushes. A black bear stands right above you.')
        print('What do you do, Run back or Play dead?')
        bearfight = ['run back', 'play dead']
        answerbear = input('')
        if answerbear == 'run back':
            print('You succesfully run away down the left path, leaving the bear behind.')
            toLake()
        elif answerbear == 'play dead':
                print('You play dead and hope the bear just goes away.')
                time.sleep(3)
                print('However the bear is too smart for that and begins to eat its free meal.')
        else:
            print('What do you do, Run back or play dead?')
    else:
        print('Choose, left or right.')

def toLakeF():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('You all scurry down the hill and begin to smell a nice auroma that reminds you of the beach. As you all head down the path the smell gets stronger and then you begin to hear noises.')
    print('You hear water crash against rocks but very faintly.')
    print('Koen begins to run to the sound, you all follow behind except Tori')
    print('You decide to stay behind with Tori')
    print('You use this oppurtunity to try and get close. What do you say?')
    print('')
    print('1. "So any sports you into?"')
    print('2. "Like any of \'em?"')
    toriTalkAnswer = input('')
    if toriTalkAnswer == '1':
        print('"Well from what I can remember I did like lacrosse. But I think I\'m more of a bookworm to be honest. And given my height I can\'t do many sports." Tori giggled.')
        print('"I think we might be the same height. How tall are you?" You ask politely.')
        print('"Only five one. I\'m a midget!" She continued to giggle.')
        print('"Same!" You begin to laugh with her.')
    elif toriTalkAnswer == '2':
        print('"Oh dear god no! I\'ve only known them for a day or so." Tori said. "Why who do you like? No one?"')
        print('')
        print('Type the name of the guy you have interest for from the story. If you can\'t think of someone say no one.')
        boyYouLike = input('')
        if boyYouLike == 'tyree':
            print('"Oh I can totally see why. He\'s quite the handsome man himself." Tori smiled.')
        elif boyYouLike == 'koen':
            print('"Aw, he\'s a sweetie pie honestly. I can totally see why."')
        elif boyYouLike == 'kevin':
            print('"Oh you like bad boys huh? He\'s hilarious let me give you that!"')
        else:
            print('"Ah yes, we still need to get to know them. They are all pretty nice though." Tori shrugged with a smile.')
    else:
        print('What do you want to ask Tori? 1 or 2?')
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You both make your way down to a lake where the guys had already begun to splash around. Tori quickly follows them, pulling up her sleeves and pants. You look around and spot something to your left. It appears
to be a small boat with a long lantern on it.

"Hey you guys, there's a boat over there!" You shout. They all turn to the left and examine the boat. Tyree begins to walk toward it, stepping out of the water and putting his shoes back on.

"Be careful..." Tori mumbled. You all follow closely behind. Your heart begins to pump faster and you notice Tori and you had your arms wrapped together in complete fear.
    ''')
    time.sleep(10)
    print('''
Tyree screams and falls back as a pale white man jumps from inside the small boat.

"HIIIIYAHHH~!" The man screams, in a poor fighting stance. You all let out a scream and go back. "You'll never eat me you monsters!" The man began to wave the lamp around.

"HEY we're good!" Tyree got up, trying to dodge the lamp.

"That's what they all say and then the next thing I know you've eaten my grandmother." The man said aggresively.

"What the - No look we don't know where we are we just need help getting back to where we came from. Do you know if there's a city nearby to call the cops?" Tyree explained.

"Cops? are you foreigners? The only city near here is the elves' but that's in the mountain and considering the war going on right now you are not getting anywhere near there." The man chuckled still waving the lamp around.

"Can you put that down. What are you talking about? War? There's no war dude." Kevin said.

"Well yes there is. It's been going on for almost five years you foreigners." The man shook his head. "You ain't getting anymore information out of me. You won't! Never!" The man yelled.

"What a lunatic..." Tori laughed quietly. You looked down at her and she was holding in laughter.

"Can you tell us what planet this is?" Koen asked.

"Planet? What strange language do you use you foreigner?" The man asked.

"Planet. Like Earth? Are we on Earth?" Koen said.

"Well of course you're not on Earth. That's not a planet ya bimbo. It's a celestial body, but no this is Scorux." The man chuckled.

"Obviously we're not on Earth anymore then. Damn it." Koen said. "Could someone in the city help us get back to Earth?"

"Probably but you ain't getting there anytime soon. Not without me that is." The man smiled.

"Can you take us there? We don't have much but once we get back on our feet we promise to help you with whatever you want." Tori said walking toward the man.

"Ah well I would like to play a game . It's been so long. If you beat me I'll give you a ride on my boat to a large city where they could help you. If not then I'll just leave ya here." The man suggested.

"Deal. Who wants to play?" Tori asked the group. They all shrugged obviusly not wanting to play.

"I'll do it." You say, walking toward the man confidently.

"Good let's begin." He said.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')



def secondPathF():

    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You remain still, trying to focus your eyes to see what these figures are. You rub your eyes a few times before your vision begins to finally clear upself.
You notice there are three of them, all seeming to be guys. You begin to look around, trying to find out where exactly you are. As you turn your head back you
see a girl lying next to your feet. You let out a sharp gasp as you craw away from her. As you move back you notice the other people beginning to wake up. You quickly stand up in a panic. The girl stands up, her legs
mildly shaking. You stare at her as she tries to find her balance. Her eyes are a beatiful shade of green and her hair, although very messy, drapes down to her wide hipsself.

"Who are you? Where am I? What's going on!?" The girl asks aggresively. She had a pleasant British accent that sounded soothing to your American ears. "God my back..."

You remain silent to look behind you. The other guys slowly move away from each other. You instictively hold your hands up and they turn back to you with frownsself.
You feel a soft tap on your shouder and you turn around to see the girl.

        ''')
    print('"Well?" She says')
    nameStory = input('')
    print('"' + nameStory + ' huh? What an interesting name" She says.')
    print('''
"Do you have any idea where we are?" She asks, looking behind your shoulder.
The guys begin to move closer circling around you two. You step to the side so you all form a small circle.

"No idea my mind is completely blank" one of theem says. His voice was incredibly deep considering how young he looked. He had very dark skin and his hair was in these reall nice dreads.
He had a sharp jawline a chiseled beard. "My name's Tyree though, what about you guys?" He was very handsome.

"I'm Tori, I'm from England" Tori smiled.

"I'm Koen, I live in Canada. I can't really remember much though..." Koen, the guy standing next to you says as he rubs the back of his head.
You immediately connect with his accent for it's very similar to yours unlike Tyree's and
Tori's. You look at Koen's hair and can't help but notice how well kept it was. It reminded you of your ex who also had very nice hair.

"Yeah man, my mind is completely out of it. I'm Kevin, can't really remember where I'm from yet. Luck bastards." Kevin playfully smirked, he seemed very warm and playful.
His phydique was charming, even you had to admit that much. You felt excited but also overwhelmed
to see yourself surrounded by good looking guys and a girl. You've never been that one good looking girl or anywhere near good looking. You had a very generic face with dark brown eyes and your hair was always tied up in the same bun.
You remembered why you stopped trying on your looks, it was when your ex had dumped you for some girl on the honor roll. Even at twenty years old, a sophomore in college you still haven't managed to get your looks or life together.

"Alright so no one has ANY idea where we are or how we got here?" Tori asks throwing her hands in the air. You then realized how small she was because she wasn't any taller than you. You were only five one which you were both proud of and embarrassed.
You'll probably ask her later just to confirm and it'd serve as good small talk.

"No but my back is killing me, can someone give me a massage?" Kevin laughed obviously in pain.

"Here turn around let me check" Tyree walked over to him and lifted Kevin's shirt up. Kevin groaned and tried to move away but Tyree held him in place. "All I see is your nice tattoo dude."

"I've never gotten a tattoo..." Kevin mumbled.

"Check if I have one." Tyree turned around and lifted his shirt so everyone could see. On his back was a drawing of a puzzle piece with abstract paintings on it.

"Do we all have it?" Tori gasped lifting the back of her shirt to reveal another puzzle piece. Koen quickly followed to also show another puzzle piece. You stubbornly lift your shirt up awkwardly
making sure not to expose the front. You walked closer to them in the circle. You do your best to look behind you and notice all the puzzle pieces seem to fit with each other. Yours fit with Tori and Kevin's which made you feel foolish pride.

"What even is this? Oh dude my mom's gonna kill me." Koen frowned.

"What if this is an experiment?" Tori asked, putting her shirt down.

"Well this is pretty messed up. But if it is then they obviously want us to do something. Prove something." Tyree said running his fingers on his lips.

"Whatever look at where we are, we're in the middle of nowhere. All I see is grass grass grass. Wait" Koen stopped suddenly and pointed behind Kevin. There was a mountain with a forest surrounding it. Although it was extrememly far away
the forest made it seem as if it were closer.

"That's our best shot at finding anything. I can't see anything else." Tori suggested.

"Alright let's start moving then. Everyone in?" Tyreen said, looking at you.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')
    responseTori = input('"Are you in, yes or no?" Tori asked.')
    if responseTori == 'yes':
        headingToMountF()
    elif responseTori == 'no':
        print('You are left behind as they head to the mount. Days later you die from hunger.')
    else:
        exit()

if __name__ == '__main__':
    name = question_name()
    gender = question_gender();
    if gender == 'male':
        story_male(name)
    elif gender == 'female':
        story_female(name)
