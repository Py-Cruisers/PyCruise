# want to end up putting this in a class that we can import into master file and run tutorial from there. However, this
# was too complicated at first so going to try getting it working as a separate file itself then go from there.

# #################################### STRINGS #####################################

class Tutorial:

    # def __init__(self, value):
    #     self.value = value

    # ##### Main Menu Tutorial ######

    choice_a_intro = """
    \nFirst, we have our Main Menu. Each of it's options is assigned a number which makes for easy selection.\n
     Let's explore it's options.\n
        \033[1;30m[+] 1. Tutorial
        \033[1;30m[+] 2. Create new collection
        \033[1;30m[+] 3. View existing collections
        \033[1;30m[+] 4. Switch collections
        \033[1;30m[+] 5. Quit\n
    """

    menu_explore_tutorial = """
    We are in option 1, which is the tutorial you are going through.\n
       \n\033[1;31m[+] 1. Tutorial
       \033[1;30m[+] 2. View existing collections
       \033[1;30m[+] 3. Create new collection
       \033[1;30m[+] 4. Switch collections
       \033[1;30m[+] 5. Quit\n
    """

    menu_explore_view_collections = """
    In option two, we can view a list of our current collections available. Note that this won't do much if you are using\n
    this tool for the first time.\n
        \033[1;30m[+] 1. Tutorial
        \033[1;31m[+] 2. View existing collections
        \033[1;30m[+] 3. Create new collection
        \033[1;30m[+] 4. Switch collections
        \033[1;30m[+] 5. Quit\n
    """

    menu_explore_create = """
    Option 3 allows you to create a new collection, which will be what you will enter your browsers and/or applications into.\n 
        \033[1;30m[+] 1. Tutorial
        \033[1;30m[+] 2. View existing collections
        \033[1;31m[+] 3. Create new collection
        \033[1;30m[+] 4. Switch collections
        \033[1;30m[+] 5. Quit\n
    """

    menu_explore_switch = """
    To go into your collection(s), use option 4.\n 
        \033[1;30m[+] 1. Tutorial
        \033[1;30m[+] 2. View existing collections
        \033[1;30m[+] 3. Create new collection
        \033[1;31m[+] 4. Switch collections
        \033[1;30m[+] 5. Quit\n
    """

    menu_explore_quit = """
    Finally, we have option 5. Selecting option 5 from the Main Menu will exit you out of PyCruise entirely.\n
        \033[1;30m[+] 1. Tutorial
        \033[1;30m[+] 2. View existing collections
        \033[1;30m[+] 3. Create new collection
        \033[1;30m[+] 4. Switch collections
        \033[1;31m[+] 5. Quit\n
    """

    menu_conclusion = """
    That's it for the basic Main Menu of your PyCruise tool. If you want to learn more about the specific features, feel 
    free to explore more of the tutorial!
    """

    # ##### Collections Tutorial #####

    choice_b_intro = """
    Let's dive a little deeper into what collections are, shall we?\n
    Here in the Main Menu, we have three options pertaining to collections. 
        \033[1;30m[+] 2. View existing collections
        \033[1;30m[+] 3. Create new collection
        \033[1;30m[+] 4. Switch collections
    """

    collect_definition = """
    Now you might be asking yourself, "what is a collection?"\n
    Well, a collection is a personalized list of urls and application names that the user can utilize to open this list with\n
    a single command. Essentially, you can put in as many browser urls or application names as you want and one command will\n
    open all of them at once! Real time saver, huh?
    """

    collect_creation = """
    You can create as many collections as you want! And if we take a look back at those options, we can see this can be done\n
    via option 3, "Create new collection". Let's see what happens when we enter the number 3. 
        \033[1;30m[+] 2. View existing collections
        \033[1;31m[+] 3. Create new collection
        \033[1;30m[+] 4. Switch collections
    """

    collect_creation_name = """
    This will bring you to a new prompt, which will ask you to name your new collection.\n
    What do you want to name your new collection?
    >  
    """

    collect_creation_name_note = """
    Enter whatever title you want to name your new collection.\n
    What do you want to name your new collection?
    > school-work
    
    \n**NOTE** Do not include SPACES within your title.
    """

    collect_creation_name_examples = """
    Here are some acceptable titles for your collections:\n
    school-work
    HOMEWORK
    I-like-SURFING
    \n...And here are some that won't work:
    S C H O O L - R U L E Z
    Surfing Stinks 
     homework 
    """

    collect_explore_view = """
    Now that we've created a new collection, let's see what we can do with it.\n
    Back in the Main Menu, there's two more choices. 
        \033[1;30m[+] 2. View existing collections
        \033[1;30m[+] 3. Create new collection
        \033[1;30m[+] 4. Switch collections
    """

    collect_select_view = """
    If we select option 2, "View existing collections", it will display a list of your existing collections and also take you\n
    back to the Main Menu. Note that if you are using PyCruise for the first time or you haven't created any collections yet,\n
    it won't display anything.\n 
    \033[1;30m[+] Collection-1")
    \033[1;30m[+] Collection-2")
    \033[1;30m[+] Collection-3\n")
        
        \033[1;30m[+] 1. Tutorial
        \033[1;30m[+] 2. Create new collection
        \033[1;30m[+] 3. View existing collections
        \033[1;30m[+] 4. Switch collections
        \033[1;30m[+] 5. Quit\n
    """

    collect_explore_switch = """
    Finally, we have one last option in our Main Menu when talking about collections. And that is our "Switch Collections".\n  
        \033[1;30m[+] 2. View existing collections
        \033[1;30m[+] 3. Create new collection
        \033[1;31m[+] 4. Switch collections
    """

    collect_select_switch = """
    Selecting option 4 will let you go into one of your collections and work on it from within.\n 
    \033[1;30m[+] Collection-1")
    \033[1;30m[+] Collection-2")
    \033[1;30m[+] Collection-3\n")
    
    What collection would you like to choose? > Collection-1
    """

    collect_switch_second_menu = """
    Once you go into your new collection, a new secondary menu will pop up with more options! To learn more, check out more\n
    of the tutorial. 
    
    You are now in Collection-1
        \n\033[1;34m[+] 6. Run existing list of apps
        \033[1;34m[+] 7. Add to current list of apps/websites
        \033[1;34m[+] 8. Delete from current list of apps/websites
        \033[1;34m[+] 9. View current list of apps/websites
        \033[1;34m[+] 5. Main Menu\n
    
    """

    # ##### Secondary Menu Tutorial #####

    choice_c_intro = """
    When you switch into one of your collections, you will see what is called the "Secondary Menu". Here is an extended\n
    list of options you can do in terms of your collection. This tutorial will go through each of those. 
    
    
    \n\033[1;30m[+] 6. Run existing list of apps
    \033[1;30m[+] 7. Add to current list of apps/websites
    \033[1;30m[+] 8. Delete from current list of apps/websites
    \033[1;30m[+] 9. View current list of apps/websites
    \033[1;30m[+] 10. Main Menu")
    \033[1;30m[+] 5. Quit\n
    
    
    """




    def tut_banner(self):
        print("""\033[1;30m
          Welcome to the PyCruise Tutorial! PyCruise is a handy-dandy tool that saves the user time no matter who they are!\n
          You will be able to create "collections", which you can populate with browsers or applications you want\n
          to open upon command. You can also edit your collections to include more or less whenever you wish. 
          
          Below is a list of the various features this tool offers you and the tutorials along with them:\n
          Enter the letter of the one you would like to cruise around. 
          """)

    def tut_main_menu(self):
        print("\n\033[1;34m[+] A. Main Menu")
        print("\033[1;34m[+] B. Collections")
        print("\033[1;34m[+] C. Secondary Menu")
        print("\033[1;34m[+] D. Adding Applications and Browsers")
        print("\033[1;34m[+] E. Deleting Applications and Browsers")
        print("\033[1;34m[+] F. Running Applications and Browsers\n")
        # print("\033[1;34m[+] G. Quit\n")

        print("\033[1;30m Let's get Cruisin' shall we?\n")

        print("\033[1;34m[+] 5. Go back to Main Menu\n")




    def choice_a(self, choice):
        if choice.upper() == "A":
            print(self.choice_a_intro)
            # while statement here?
            continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
            if continue_or_ext.upper() == "X":
                self.tut_banner()
                self.tut_main_menu()
            elif continue_or_ext.upper() == "C":
                print(self.menu_explore_tutorial)
                continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
                if continue_or_ext.upper() == "X":
                    self.tut_banner()
                    self.tut_main_menu()
                elif continue_or_ext.upper() == "C":
                    print(self.menu_explore_view_collections)
                    continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
                    if continue_or_ext.upper() == "X":
                        self.tut_banner()
                        self.tut_main_menu()
                    elif continue_or_ext.upper() == "C":
                        print(self.menu_explore_create)
                        continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
                        if continue_or_ext.upper() == "X":
                            self.tut_banner()
                            self.tut_main_menu()
                        elif continue_or_ext.upper() == "C":
                            print(self.menu_explore_switch)
                            continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
                            if continue_or_ext.upper() == "X":
                                self.tut_banner()
                                self.tut_main_menu()
                            elif continue_or_ext.upper() == "C":
                                print(self.menu_explore_quit)
                                continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
                                if continue_or_ext.upper() == "X":
                                    self.tut_banner()
                                    self.tut_main_menu()
                                elif continue_or_ext.upper() == "C":
                                    print(self.menu_conclusion)
                                    ext_tutorial = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (X) to exit:\033[1;m ")
                                    if continue_or_ext.upper() == "X":
                                        self.tut_banner()
                                        self.tut_main_menu()
                                    else:
                                        self.tut_banner()
                                        self.tut_main_menu()
            else:
                print("Please enter valid input")
                self.choice_a(choice)

    def choice_b(self, choice):
        if choice.upper() == "B":
            print(self.choice_b_intro)
            # while statement here?
            continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
            if continue_or_ext.upper() == "X":
                self.tut_banner()
                self.tut_main_menu()
            elif continue_or_ext.upper() == "C":
                print(self.collect_definition)
                continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
                if continue_or_ext.upper() == "X":
                    self.tut_banner()
                    self.tut_main_menu()
                elif continue_or_ext.upper() == "C":
                    print(self.collect_creation)
                    continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
                    if continue_or_ext.upper() == "X":
                        self.tut_banner()
                        self.tut_main_menu()
                    elif continue_or_ext.upper() == "C":
                        print(self.collect_creation_name)
                        continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
                        if continue_or_ext.upper() == "X":
                            self.tut_banner()
                            self.tut_main_menu()
                        elif continue_or_ext.upper() == "C":
                            print(self.collect_creation_name_note)
                            continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
                            if continue_or_ext.upper() == "X":
                                self.tut_banner()
                                self.tut_main_menu()
                            elif continue_or_ext.upper() == "C":
                                print(self.collect_creation_name_examples)
                                continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
                                if continue_or_ext.upper() == "X":
                                    self.tut_banner()
                                    self.tut_main_menu()
                                elif continue_or_ext.upper() == "C":
                                    print(self.collect_explore_view)
                                    continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
                                    if continue_or_ext.upper() == "X":
                                        self.tut_banner()
                                        self.tut_main_menu()
                                    elif continue_or_ext.upper() == "C":
                                        print(self.collect_select_view)
                                        continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
                                        if continue_or_ext.upper() == "X":
                                            self.tut_banner()
                                            self.tut_main_menu()
                                        elif continue_or_ext.upper() == "C":
                                            print(self.collect_explore_switch)
                                            continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
                                            if continue_or_ext.upper() == "X":
                                                self.tut_banner()
                                                self.tut_main_menu()
                                            elif continue_or_ext.upper() == "C":
                                                print(self.collect_select_switch)
                                                continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
                                                if continue_or_ext.upper() == "X":
                                                    self.tut_banner()
                                                    self.tut_main_menu()
                                                elif continue_or_ext.upper() == "C":
                                                    print(self.collect_switch_second_menu)
                                                    ext_tutorial = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (X) to exit:\033[1;m ")
                                                    if continue_or_ext.upper() == "X":
                                                        self.tut_banner()
                                                        self.tut_main_menu()
                                                    else:
                                                        self.tut_banner()
                                                        self.tut_main_menu()
            else:
                print("Please enter valid input")
                self.choice_a(choice)
    # def choice_b(self, choice):
    #     if choice.upper() == "B":
    #         print(self.choice_b_intro)
    #         continue_or_ext = input("\033[1;34m[+]\033[1;m \033[1;91mEnter (C) to continue or (X) to exit:\033[1;m ")
    #         if continue_or_ext.upper() == "X":
    #             self.tut_main_menu()
    #         elif continue_or_ext.upper() == "C":
    #             def explore_tutorial():
    #                 print(self.collect_definition)
    #         else:
    #             print("hi")

    #
    # def choice_c(self, choice):
    #     if choice.upper() == "C":
    #
    #
    # def choice_d(self, choice):
    #     if choice.upper() == "D":
    #
    # def choice_e(self, choice):
    #     if choice.upper() == "E":
    #
    # def choice_f(self, choice):
    #     if choice.upper() == "F":
    #
    # def choice_g(self, choice):
    #     if choice.upper() == "G":

    def tut_run(self):
        choice = "4"
        self.tut_banner()
        self.tut_main_menu()

        while choice != "5":
            self.tut_banner()
            self.tut_main_menu()
            choice = input("\033[1;34m[+]\033[1;m \033[1;91mEnter your choice:\033[1;m ")
            self.choice_a(choice)
            self.choice_b(choice)
            # choice_c(choice)
            # choice_d(choice)
            # choice_e(choice)
            # choice_f(choice)


# instance = Tutorial()
# instance.tut_run()
