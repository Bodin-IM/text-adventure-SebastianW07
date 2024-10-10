




stamina = 100

print("You are running away from a serial killer.")

print("You see a abandoed lodge in the middle of ther forest")

print("what do you choose to do?")
print("A: Run in and close the doors behind you.")
print("B: Ignore it and go deeper into the forest")


answer = input(": ").lower()

if answer == "a":
    print("You managed to close the door in the killers face")
    print("You found a weird looking dog")
    q1 = input("Do you wish to keep it? yes/no:")
    if q1 == "yes":
        print("You chose to keep the dog and you guys slept trough the night...")
        print("+ 20 Stamina")
        stamina += 20

        print("When you wake up you notice that there is food on the counter")
        q2 = input("do you wish to eat the food? yes/no:")

        if q2 == "yes":
            print("10 + Stamina")
            print("You feel energised and ready to try to escape again")
            q3 = input("Do you wish to take the dog with you? yes/no:")

            if q3 == "yes":
                print("You and the dog leave trough the backdoor")
                print("While you guys are walking you hear wierd noises coming from the bush")
                q4 = input("Do you wish to investigate? yes/no:")

                if q4 == "yes":
                    print("It was the killer :YOU DIED:")

                elif q4 == "no":
                    print("You ignored the noises and started running")
                    print("- 20 Stamina")
                    stamina -= 20
                    
                    print("Its starting to get dark")
                    print("You can see the city lights in the horizon")
                    q4 == input("Do you want to run for it? yes/no:")

                    if q4 == "yes":
                        print("You succesfully made it to the city and called the police")
                        print("The police located the killer and arrested him")
                        print("YOU WON")

                    elif q4 == "no":
                        print("You went to sleep in a bush")
                        print("You hear weird noises")
                        q5 = input("Do you wish to run to the city? yes/no:")

                        if q5 == "yes":
                            print("You succesfully made it to the city and called the police")
                            print("The police located the killer and arrested him")
                            print("YOU WON")

                        elif q5 == "no":
                            print("IT WAS THE KILLER AND YOU DIED")



            elif q3 == "no":
                print("THE DOG KILLED YOU")
        elif q2 == "no":
            print("YOU DIED OF STARVATION")

        
    elif q1 == "no":
        print("The dog took that personally...")
        print("YOU DIED")

elif answer == "b":
    print("You ignored the lodge and went deeper.")
    print("The killer FOUND YOU!")
    print("YOU DIED")
    