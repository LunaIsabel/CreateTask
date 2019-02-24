__author__ = "Luna"
__copyright__ = "Copyright (c) 2019 Isabel Luna"
__credits__ = ["Luna, Isabel"]
__license__ = "MIT lisence"

def endings():
    ending1 = 'You died'

    ending2 = 'You become hero'
    ending3 = 'Live ordinary life'
    ending_list = [ending1, ending2, ending3]
    chosen_ending = random.choice(ending_list)
    print(chosen_ending)

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
    if path == ('1'):
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
mildly shaking. You stare at her as she tries to find her balance. Her eyes are a beatiful shade of green and her hair, although very messy, drapes down to her wide hipsself.

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')

def story_female(name):
    print('Story if person is female will go here')

if __name__ == '__main__':
    name = question_name()
    gender = question_gender();
    if gender == 'male':
        story_male(name)
    else:
        story_female(name)

    ending2 = 'You became the leader'
    ending3 = 'You saved people continued to live oridinary life'

