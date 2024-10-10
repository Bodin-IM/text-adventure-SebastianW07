import random
from random import randint

Lsus = randint(1, 10)
MSus = randint(11, 25)
HSus = randint(50, 100)

susc = 50
bitc = 100

susmin = 10
susmax = 60

nostaminamin = 10
nostaminamax = 30

nohealthmin = 10
nohealthmax = 60

yesstaminamin = 20
yesstaminamax = 90

yeshealthmin = 20
yeshealtmax = 90


health = 100
suspision = 0
Stamina = 100

nightvg = 0
keycard = 0

roomvisited = False




def LandingSite():

    global suspision,health,Stamina
    
    print("you are a highly skilled spy on your way to find out crucial information on how pespsi is really made.")
    print("The options for a vehicle are slim, but good.")
    print("A: You have a chopper thats capable of leaving the hostile zone within 2 minutes")
    print("B: You also have a 500 horsepower motorcycle in your garage")

    answer = input(": ").lower()
    if answer == "a":
        print("You chose the Chopper...")


        addedSuspision = randint(0, 30)
        suspision += addedSuspision
        print(f"You gained {addedSuspision} suspision.")
        print(f"You now have {suspision} suspision")

        print("you are landing at the land site 2 miles from the target destination")
        print("when you land you notice that there is a bike laying on the ground")

        q1 = input("Do you wish to cycle to the head-quarters? yes/no").lower()

        if q1 == "yes":

            if randint(0, 100) < susc:
                suspision += randint(susmin, susmax)
                print("The bicycle made too much noise")
                
                print(f"You now have {suspision} suspision")
                BreakIn()
            else:
                print("You biked to the hq")
                BreakIn()

            
            

        elif q1 == "no":
            print("You ignored the bike and went by foot.")

            BreakIn()



    elif answer == "b":
        print("You went to the garage and began driving")
        print ("you parked 1 mile away from the target destination.")
        print("when you park you notice that there is a bike laying on the ground")

        q1 = input("Do you wish to cycle to the head-quarters? yes/no").lower()

        if q1 == "yes":

            if randint(0, 100) < susc:
                suspision += randint(susmin, susmax)
                print("The bicycle made too much noise")
                
                print(f"You now have {suspision} suspision")
                BreakIn()
            else:
                print("You biked to the hq")
                BreakIn()




def BreakIn():

    global suspision,health,Stamina

    print("You arrive outside the head-quarters")
    print ("wich  approach do you wish to take?")
    print("A: stealth.")
    print("B: rapid")

    answer = input(": ").lower()

    if answer == "a":
        print("You chose the stealth approach.")
        print("You located an air-went and started climbing towards it.")
        print("once you climb in the vent you notice that there is a spider there with you.")

        q1 = input("Do you wish to ignore it?")

        if q1 == "yes":
            print("you ignored the spider")
            
            if randint(0, 100) < bitc:

                print("The spider bit you.")
                health -= randint(nohealthmin, nohealthmax)
                print(f"You now have {health} health")
            
            else:
                print("The spider ignored you too")
                
                BreakIn2()

        
        elif q1 == "no":
            print("You killed the spider, but made some noise")

            if randint(0, 100) < susc:
                suspision += randint(susmin, susmax)
                print("someone heard you")
                print(f"You now have {suspision}: suspision")

                BreakIn2()
        
        


    elif answer == "b":
        print("idiot")

        print("YOU DIED")

      



        

def BreakIn2():
    print("you crawl some more and come across a split")
    print("Wich way do you choose")
    print("A: Right")
    q1 = input("B: Left").lower

    if q1 == "a":
        print("You chose to go right")
    elif q1 == "b":
        

            
            








LandingSite()
