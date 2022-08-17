class Tutorial:
    def __init__(self):
        self.choice = " "

    def tut_main_menu(self):
        print("""
          Welcome to the PyCruise Tutorial! PyCruise is a handy-dandy tool that saves the user time no matter who they are!\n
          You will be able to create "collections", which you can populate with browsers or applications you want\n
          to open upon command. You can also edit your collections to include more or less whenever you wish. 
          
          Below is a list of the various features this tool offers you and the tutorials along with them:\n
          Enter the letter of the one you would like to cruise around. 
          """)
        print("\n\033[1;34m[+] A. Main Menu")
        print("\033[1;34m[+] B. Collections")
        print("\033[1;34m[+] C. Secondary Menu")
        print("\033[1;34m[+] D. Adding Applications and Browsers")
        print("\033[1;34m[+] E. Deleting Applications and Browsers")
        print("\033[1;34m[+] F. Running Applications and Browsers")
        # print("\033[1;34m[+] G. Quit\n")

        print("Let's get Cruisin' shall we?")

        print("\033[1;34m[+] 5. Go back to Main Menu\n")

    def choice_main_menu_intro(self, choice):
        if choice.upper() == "A":
            print("First, we have our Main Menu. Let's explore it's options.")
            print("\n\033[1;30m[+] 1. Tutorial")
            print("\033[1;30m[+] 2. Create new collection")
            print("\033[1;30m[+] 3. View existing collections")
            print("\033[1;30m[+] 4. Switch collections")
            print("\033[1;30m[+] 5. Quit\n")

            while True:
                continue_or_ext = input("Enter (C) to continue and (X) to exit.\n > ")
                if continue_or_ext == "X":
                    tut_main_menu()
                else:
                    print("hi")


tut = Tutorial()
print(tut.tut_main_menu())

# print(tut.choice_main_menu_intro(choice))


    # def choice_b(self, choice):
    #     if choice.upper() == "B":
    #
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





    #
    #     # Section 3
    #     print("Looking at option option 1, which is the current tutorial you are going through.")
    #     print("\n\033[1;31m[+] 1. Tutorial")
    #     print("\033[1;30m[+] 2. View existing collections")
    #     print("\033[1;30m[+] 3. Create new collection")
    #     print("\033[1;30m[+] 4. Switch collections")
    #     print("\033[1;30m[+] 5. Quit\n")
    #
    #     # Section 4
    #     print("""
    #     In option two, we can view a list of our current collections available.
    #     """)
    #     print("\n\033[1;30m[+] 1. Tutorial")
    #     print("\033[1;31m[+] 2. View existing collections")
    #     print("\033[1;30m[+] 3. Create new collection")
    #     print("\033[1;30m[+] 4. Switch collections")
    #     print("\033[1;30m[+] 5. Quit\n")
    #
    #     # Section 5
    #     print("""
    #     If you are using this tool for the first time, this will be blank. This option gives you a quick idea\n
    #     of what you currently have.
    #    """)
    #     print("\n\033[1;30m[+] Collection-1")
    #     print("\033[1;30m[+] Collection-2")
    #     print("\033[1;30m[+] Collection-3")
    #
    #     # Section 6
    #     print("""
    #     Of course, you can create more collections. Option 3 lets you create and personalize a new collection.\n
    #     """)
    #     print("\n\033[1;30m[+] 1. Tutorial")
    #     print("\033[1;30m[+] 2. View existing collections")
    #     print("\033[1;31m[+] 3. Create new collection")
    #     print("\033[1;30m[+] 4. Switch collections")
    #     print("\033[1;30m[+] 5. Quit\n")
    #
    #     # Section 7
    #     print("""
    #     Entering into option three, you will see a prompt asking you to name your new collection.
    #     """)
    #     print("""\n\033[1;30m[+]
    #     Enter the name for your new collection:
    #     >
    #     """)
    #
    #     # Section 8
    #     print("""
    #     **NOTE** Do not includes any SPACES into your collection name
    #     """)
    #     print("\033[1;30m[+] 3. Create new collection")
    #     print("\033[1;30m[+] 4. Switch collections")
    #     print("\033[1;30m[+] 5. Quit\n")
    #
    #
    #     option = input("Enter (y) to continue or (x) to exit out of the tutorial.")
    #     while True:
    #         if option.lower() == "x":
    #             break
    #         else:
    #             print("hi")

