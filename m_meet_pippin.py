while True:
    print("\nDo you want to meet my little kitten, Píppin?")
    print("1. Yes")
    print("2. No")
    print("0. (exit the program)")
    
    entry = input("Choose an option: ")

    try:
        entry = int(entry)

        if entry == 0:
            print("I didn't even want to. Bye! 😾")
            break 

        elif entry == 1:
            print("Now I am sleeping on the laptop keyboard, don't ever come back!")
            print(' ^   ^     ᶻ')
            print('( - - )  ᶻ')
            print(' (   ) /  ᶻ')
            print("\nOur meeting is over...\n")
        
        elif entry == 2:
            print("Well, you will meet me anyway!")
            print(' ^   ^ ')
            print('( 0 0 ) ')
            print(' (   ) / ')
            print('')

            while True:
                print("What do you want to do?")
                print("1. Give me a snack")
                print("2. Play")
                print("3. Ignore me")

                action = input("Choose an option: ")

                try:
                    action = int(action)

                    if action == 1:
                        while True:
                            print("1. Tuna")
                            print("2. Salmon")
                            print("3. Cardboard pieces")
                            flavor = input("Choose an option: ")

                            try:
                                flavor = int(flavor)
                                if flavor == 1 or flavor == 2:
                                    print("I hate that flavor, I'm going to eat a bag instead!")
                                elif flavor == 3:
                                    print("My favorite!! 😻 You should call my vet..")

                                print("\nOur meeting is over...\n")
                                break
                            
                            except ValueError:
                                print("That's not a valid flavor! 😾")
                        
                    elif action == 2:
                        while True:
                            print("1. Mouse")
                            print("2. Ball")
                            print("3. Sewing box threads - forbidden")
                            toy = input("Choose an option: ")

                            try:
                                toy = int(toy)

                                if toy == 1:
                                    print(' ^   ^ ')
                                    print('( 0 0 ) ')
                                    print(' (   ) / 🐁')
                                    print("\nI threw the mouse behind the sofa, deal with it.")
                                elif toy == 2:
                                    print(' ^   ^ ')
                                    print('( 0 0 ) ')
                                    print(' (   ) / ⚾')
                                    print("\nI never liked this one; you bought it because you wanted to.")
                                elif toy == 3:
                                    print(' ^   ^ ')
                                    print('( 0 0 ) ')
                                    print(' (   ) /  🧶')
                                    print("\nMY threads!!")
                                    print("You can pet me later.. 😻🧶💕")

                                print("\nOur meeting is over...\n")
                                break  
                            
                            except ValueError:
                                print("That doesn't even look like a real toy! 😾")
                    
                    elif action == 3:
                        print("How dare you ignore me?! 😾 MIAAAAAAU MIAÚ MIAAAU")
                        print("\nOur meeting is over...\n")
                        break 

                    else:
                        print("That's not a valid option! 😾")

                except:
                    print("I must have stepped on your keyboard, that's not valid! 😾")
        
        else:
            print("I must have stepped on your keyboard, that option is not valid. 😾")

    except:
        print("I must have stepped on your keyboard, that option is not valid. 😾")
