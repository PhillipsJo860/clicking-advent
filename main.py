# Joshua Phillips
# 11/25/24
# Adventure game

# Variables settup
import time
lives = 3
score = 0

man_purse = ['key', 'duck', 'brush']

def lives_score():
    print()
    print('**********************************')
    print(f'You have, {lives} lives left.')
    print(f'Your score is: {score}.')
    print('**********************************')
    print()
#  Welcome

name = input('Enter your name: ')

print(f'Welcome {name} to the GRAND ADVENTURE OF GREAT TOIL!')
print()
print()
lives_score()
print()
time.sleep(2)
# Scene 1

print('''You awake to the sound of an Old Hag coooking up a stew in an old brewing pot.''') 
time.sleep(1)
print('She is caroling an old song about big toe stew. ')
time.sleep(1)
print('She looks HUNGRY!')
 

# Selection 1

choice1 = input('Press Q to sit down and accept you new fate. Or press E to Eat her first!(You are also hungry): ')
choice1 = choice1.capitalize()
if choice1 == 'Q':
    print('A strange flying creature flies in and eats the Old Hag!')
    score = score+5
    print('+5 points')
else:
    print('You succesfully ate her first! However you are now dead because you ate an entire human body.(What is wrong with you.)')
    lives = lives-1
    print('-1 life')

time.sleep(7)

lives_score()

# Scene one

print(''' You free yourself from the bonds that bind you and leave the broken down old Hag's house (which is strangley made out of gingerbread) and realize you dont know where you are
You soon however find out you are not alone by the sound of howling in the distance.''')
time.sleep(3)
print()

print('The howling grows nearer and you begin to wonder if they are after you.')
time.sleep(3)
print()

print('Finally the howling grows so close that it sounds right next to you!')
time.sleep(4)
print()

print('Suddenly a man, who is dressed nearly naked with a Great Wolf Lodge headband on his head and some kind of collar around his neck, jumps out of the bush in front of you and says "I challenge you to a Pokemon card battle!"')

# Selection 2

choice2 = input('Press Q to accept the challenge! Press E to say sorry sir I have no cards. Or press R to scream "bad dog go away!"')
choice2 = choice2.capitalize()
if choice2 == 'Q':
    print('The card battle erupts into a fierce eruption of each side getting close to winning but then suddenly you realize the deck he man provided was rigged and you end up losing all of your belonings. You are left to starve with nothing to your name.')
    lives = lives-1
    print('-1 life')
elif choice2 == 'E':
    print('The man tells you "Oh dont worry I have a deck for you to use come on LETZ BATTLE!!" The battle erupts into a ferocity never before seen, unfortunatley, the deck was rigged from the start. After the ferocity died down he won every time and your gambling addiction that you developed backfired, leaving you cold and alone with nothing to your name. (You die of hypothermia.)Just before you die though you savor the one time you beat the strange man.')
    lives = lives-1
    score = score+1
    print('-1 life, +1 point')
else:
    print('The man shrieked in some strange horrific way and ran off onto the fored=st saying "SCREW YOU!!" and the bush he came from reveals an extremely vintage set of Pokemon Cards! congrats!')
    score = score+10
    print('+10 points')

time.sleep(10)
lives_score()

# Scene two

print('After you collect you prize you are about to move on but then you notice...')
print()
time.sleep(3)
print('Theres a small pink purse with a lable saying"My Man Purse".')
print()
time.sleep(3)
print(f'You pick up the manly bag and look inside revealing: {man_purse}.')
print()
time.sleep(5)
print('You sit there thinking that the purpose of these items were for that strangel man but the thought quickly vanishes as you hear a ear splitting screach from behind you!')
print()
time.sleep(4)
print('You notice a bunker door on the floor in front of you...')
print()
time.sleep(3)
print('As you look back at the noise you see the man from before is running directly at you! He looks MAD, and is holding a sharpend stick!')
print()
time.sleep(3)
print('Maybe one of the items in the Manly Purse can save you?')

# Selection 3

choice3 = input('Press Q to take out the key and try the bunker door. Press E to throw the duck at the man. Press R to brush your hair and stand your ground with dominance.')
choice3 = choice3.capitalize()
if choice3 == 'Q':
    print('You rush to fit the key in the hole and fumble the key twice! By the time you finally get the key in the hole the man is already on top of you and stabs you to death morbidly until his stick breaks.')
    lives = lives-1
    print('-1 life')
    man_purse.remove('key')
elif choice3 == 'E':
    print('You take the duck out of the bag(it quacks maniacally) and absolutely nail the man with the duck... it did nothing? Nevermind the duck exploded! The man died.')
    score = score+5
    print('+5 points')
    man_purse.remove('duck')
else:
    print('As you stand there brushing your hair the man starts to slow down looking confused. he looks at you then wanders off... I suppose you have won.')
    score = score+5
    print('+5 points')
    man_purse.remove('brush')

time.sleep(10)
lives_score()

# Scenario Four

print('After the last confrontation with the man you feel weary and begin to look for a place to rest.')
print()
time.sleep(3)
print('You happen to see a small shed in the distance and start you strek towards it.')
print()
time.sleep(3)
print('As you arrive at the shed you realize there is a small food shelf with two cans of food on it.')
print()
time.sleep(3)
print('You get inside and notice a note on the shelf that reads:"One of the cans are spoiled and not edible whereas the other perfectly fine. To whever reads this note, good luck to you."')

# Selection 4

choice4 = input('Press Q to eat the can of the left and take the other with you. Press E to eat the can on the right and take the other. Or press R to leave both.')
choice4 = choice4.capitalize()
if choice4 == 'Q':
    print('You eat the food from the can on the left and have a nice rest afterwards.')
    score = score+5
    man_purse.append('can of food')
    print('+5 points, can of food added to Manly Purse.')
elif choice4 == 'E':
    print('You eat the food from the can on the right and have a rough stomach ache. You are not able to sleep.')
    man_purse.append('can on food')
    print('No points or lives changed, can of food added to Manly Purse.')
else:
    print('Dummy now you starved to death')
    lives = lives-1
    print('-1 life')

lives_score()