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
else:
    print('You succesfully ate her first! However you are now dead because you ate an entire human body.(What is wrong with you.)')
    lives = lives-1

lives_score()

# Scene one
print('''You free yourself from the bonds that bind you and leave the broken down old Hag's house (which is strangley made out of gingerbread) and realize you dont know where you are
      You soon however find out you are not alone by the sound of howling in the distance.''')
time.sleep(2)
print()

print('The howling grows nearer and you begin to wonder if they are after you.')
time.sleep(2)
print()

print('Finally the howling grows so close that it sounds right next to you!')
time.sleep(20)
print()

print('Suddenly a man, who is dressed nearly naked with a Great Wolf Lodge headband on his head and some kind of collar around his neck, jumps out of the bush in front of you and says "I challenge you to a Pokemon card battle!"')

# Selection 2

choice2 = input('Press Q to accept the challenge! Press E to say sorry sir I have no cards. Or press R to scream "bad dog go away!"')
choice2 = choice2.capitalize()
if choice2 == 'Q':
    print('The card battle erupts into a fierce eruption of each side getting close to winning but then suddenly you realize the deck he man provided was rigged and you end up losing all of your belonings. You are left to starve with nothing to your name.')
    lives = lives-1
elif choice2 == 'E'