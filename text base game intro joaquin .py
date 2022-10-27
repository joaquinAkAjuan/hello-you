import time 

#antwoorden
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
drink = ["Drink", "drink", "D", "d"]

#Objecten
glock19 = 0
beercan = 0

required = ("\nUse only A, B, or C\n") 

def P_again():
  print("Do you want to play again? Y/N")
  choice = input(">>> ")
  if choice in yes:
    intro()


def intro():
  print ("""Welcome in this story you wil follow Ramon and help him in this confusing time.
  
        Ramon is walking around at night. 
        He goes to his usual gas station to buy a drink and some snacks.
        when Ramon gets inside MR.Omar isn't behind the counter,
        infact nobody is in the shop.
        Ramon thinks nothing of it and just wants his drink he walks to the back
        searching for an employee.
        He goes to the first door then a second door and a third.
        it looks like its never ending.
        Ramon decides to go back but when he opend the doors he came trough
        it's not changing 
        it looks like he is stuck here.
        Ramon heard some noice he turns around and sees a pendant and picks it up.
        He keeps on walkking trough doors till he notices something in the distance.
        Something is running at him
        what do you do:
         """)

         

  time.sleep(1)
  print ("""  A. Grab a nearby beer can and throw it at the entity
  B. Lie down and wait to be beaten
  C. Run""")
  choice = input(">>> ") #eerste keuze.
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nWelp, that was quick. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()



def option_rock(): 
  print ("\nThe entity is stunned, but regains control. He begins "
  "running towards you again. Will you:")
  time.sleep(1)
  print ("""  A. Run
  B. Throw another beer can
  C. Run towards a nearby door with employee only""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou decided to throw another beer can, as if the first " 
    "beer can thrown did much damage. The beer can flew well over the "
    "entities head. You missed. \n\nYou died!")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ("""\nYou were hesitant, since the backroom was dark and 
  ominous. Before you fully enter, you notice a gloomy and old glock on 
  the ground.You look in the magazine but it only has one bullet.
  You need to make it count if it comes to it
  Do you pick up a glock. Y/N?""")
  choice = input(">>> ")
  if choice in yes:
    glock19 = 1 
  else:
    glock19 = 0
  print ("\nWhat do you do next?")
  time.sleep(2)
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nReally? You're going to hide in the dark? I think "
    "The entity can see very well in the dark, right? Not sure, but "
    "I'm going with YES, so...\n\nYou died!")
  elif choice in answer_B:
   if glock19 > 0:
    print ("""\nYou laid in wait.
    the entity, which thought you were no match. As he walked 
    closer and closer, your heart beat rapidly. As the entity 
    reached out to grab the you, you pierced the bullet into 
    its chest. \n\nYou survived! 
    You go back all the doors and leave the store with your drink and go home.""")
   else: #als hij niet de glock19 oppakt
     print ("\nYou should have picked up that glock19. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("""As the entity enters the emplopyee only door, you sliently 
    sneak out. You're several feet away, but the entity turns 
    around and sees you running.""")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the entity's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind a fridge
  B. Trapped, so you fight
  C. Run towards an the next door""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for an entity. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  print ("""\nWhile frantically running, you notice a town and start running towards it.
  rock lying in the mud. You quickly reach down and grab it, 
  but miss. You try to calm your heavy breathing as you hide 
  behind a delapitated building, waiting for the entity to come 
  charging around the corner. You notice a beer can 
  near your foot. Do you pick it up? Y/N""")
  time.sleep(2)
  print("Or you can pick it up and drink it all? D")
  choice = input(">>> ")
  if choice in yes:
    beercan = 1 #voegt een biertje toe
  else:
    beercan = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending entity.")
  time.sleep(1)
  if beercan > 0:
    print ("""\nYou quickly hold out the beer can, somehow 
    hoping it will stop the entity. It does! The entity was looking 
    for a drinking homie. You stay in town till you grow old 
    \n\nThis got weird, but you survived!""")
  if choice in drink:
    option_reverse()
  else: #als hij weer niet de beercan op heeft gepakt
     print ("\nMaybe you should have picked up the beer can. "
     "\n\nYou died!")
    

def option_reverse():
  print("""You feel a bit weird, was it the shady drink or am i just tired.
  You push thru and keep in running, you feel cold and scared.
  When you hear the entity getting closer you move into a locker.
  The entity is close i can feel it.
  you hold your breath and stay frozen.
  Suddenly its quiet.""")
  time.sleep(1)
  print("\n")
  print("""When you look in the little holes of the locker its dark, nothing is there?
  It feels like the back wall in the locker is gone and fall.
  Looks like you're back in the beginning of the town again.
  You hear the entity comming and make a run for it.
  it looks like almost everything is closed off.""")
  print("\n")
  print("""Not liking it you keep running and you recognized a open field, its from before the town.
  You keep running and everything keeps on feeling to familiar.
  its getting dark but you run towards a light from a buildings exit door.""")
  print("\n")
  print("""The gas station?
  You come into the store and you faint.
  MR.Omar asks if you're ok
  Looks like it was all a dream and you go home.
  When you get home you see the lights burning but no one is home.
  you hide your weapon and everything from this night under your bed.
  Later go to sleep thinking its all just a big dream.""")
  print("\n")
  print("YOU SURVIVED!")
  print("\n")
  time.sleep(3)
  print(".")
  time.sleep(2)
  print("..")
  time.sleep(2)
  print("...")

  print("""You wake up in a hospital surounded by doctors.
  They say you were in a coma for 2 years
  After some time you are discharged and can finally go home.
  everyone seems relieved that you are back
  you are tired after a long day at the hospital and go to bed.
  When you wake up you step onto something hard and sit on the bed.
  You reach down to see what is is""")
  print("\n")
  print("its your pendant you hid.")
  print("\n")
  print("\n")
  print("\n")




intro()