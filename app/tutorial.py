class Tutorial:
    def __init__(self, val):
        self.val = val

    def tut_intro(self):
        # Section 1
        print("""
      Welcome to the PyCruise Tutorial! PyCruise is a handy-dandy tool that saves the user time no matter who they are!
      You will be able to create "lists", which you can populate with browsers or applications you want /n
      to open upon command. You can also edit your lists to include more or less whenever you wish. Let's get Cruisin'/n
      shall we?
      """)

        # Section 2
        print("First, we have our Main Menu. Let's explore it's options.")
        print("\n\033[1;30m[+] 1. Tutorial")
        print("\033[1;30m[+] 2. Create new collection")
        print("\033[1;30m[+] 3. View existing collections")
        print("\033[1;30m[+] 4. Switch collections")
        print("\033[1;30m[+] 5. Quit\n")

        # Section 3
        print("Looking at option option 1, which is the current tutorial you are going through.")
        print("\n\033[1;31m[+] 1. Tutorial")
        print("\033[1;30m[+] 2. View existing collections")
        print("\033[1;30m[+] 3. Create new collection")
        print("\033[1;30m[+] 4. Switch collections")
        print("\033[1;30m[+] 5. Quit\n")

        # Section 4
        print("""
        In option two, we can view a list of our current collections available. 
        """)
        print("\n\033[1;30m[+] 1. Tutorial")
        print("\033[1;31m[+] 2. View existing collections")
        print("\033[1;30m[+] 3. Create new collection")
        print("\033[1;30m[+] 4. Switch collections")
        print("\033[1;30m[+] 5. Quit\n")

        # Section 5
        print("""
        If you are using this tool for the first time, this will be blank. This option gives you a quick idea\n
        of what you currently have. 
       """)
        print("""
        Collection 1
        Collection 2
        Collection 3
        """)

        # Section 6
        print("""
        Of course, you can create more collections. Option 3 lets you create and personalize a new collection.\n
        """)
        print("\n\033[1;30m[+] 1. Tutorial")
        print("\033[1;30m[+] 2. View existing collections")
        print("\033[1;31m[+] 3. Create new collection")
        print("\033[1;30m[+] 4. Switch collections")
        print("\033[1;30m[+] 5. Quit\n")

        # Section 4
        print("""
        In option two, we can view a list of our current collections available. If you are using this tool\n
        for the first time, this will be blank. This option gives you a quick idea of what you currently have. 
        """)
        print("\n\033[1;30m[+] 1. Tutorial")
        print("\033[1;31m[+] 2. View existing collections")
        print("\033[1;30m[+] 3. Create new collection")
        print("\033[1;30m[+] 4. Switch collections")
        print("\033[1;30m[+] 5. Quit\n")


        option = input("Enter (y) to continue or (x) to exit out of the tutorial.")
        while True:
            if option.lower() == "x":
                break
            else:
                print("hi")
