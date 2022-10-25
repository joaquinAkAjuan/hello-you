import time 

#antwoorden
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Objecten
glock19 = 0
beercan = 0

required = ("\nUse only A, B, or C\n") 


def intro():
  print ("""Welcome in this story you wil follow Ramon and help him in this confusing time.
  
        Ramon is walking around at night. 
        He goes to his usual gasstation to buy a drink and some snacks.
        when Ramon gets inside MR.Omar isn't behind the counter,
        infact nobody is in the shop.
        Ramon thinks nothing of it and just wants his drink he walks to the back
        searching for an employee.
        He goes to the first door then a second door and a third.
        it looks like its never ending.
        Ramon decides to go back but when he opend the doors he came trough
        it's not changing 
        it looks like he is stuck here.
        Ramon heard some noice he turns around and something is running at him
        what do you do: """)

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
  print ("\nYou were hesitant, since the backroom was dark and "
  "ominous. Before you fully enter, you notice a shiny glock on "
  "the ground. Do you pick up a glock. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    glock19 = 1 
  else:
    glock19 = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
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
    print ("\nYou laid in wait. The beer attracted "
    "the entity, which thought you were no match. As he walked "
    "closer and closer, your heart beat rapidly. As the entity "
    "reached out to grab the glock, you pierced the bullet into "
    "its chest. \n\nYou survived!")
   else: #als hij niet de glock19 oppakt
     print ("\nYou should have picked up that glock19. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As the entity enters the emplopyee only door, you sliently "
    "sneak out. You're several feet away, but the entity turns "
    "around and sees you running.")
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
  print ("\nWhile frantically running, you notice a rusted "
  "glock lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated building, waiting for the entity to come "
  "charging around the corner. You notice a beer can "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    beercan = 1 #voegt een biertje toe
  else:
    beercan = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending entity.")
  time.sleep(1)
  if beercan > 0:
    print ("\nYou quickly hold out the beer can, somehow "
    "hoping it will stop the entity. It does! The entity was looking "
    "for love. "
    "\n\nThis got weird, but you survived!")
  else: #als hij weer niet de glock19 op heeft gepakt
     print ("\nMaybe you should have picked up the beer can. "
     "\n\nYou died!")

intro()