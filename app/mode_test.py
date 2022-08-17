import webbrowser
import os
import fnmatch


# Inspiration for the layout of this script is from
# the ghost_eye repository on GitHub
# https://github.com/BullsEye0/ghost_eye/blob/master/ghost_eye.py

def banner():
    print("""
    WELCOME TO PYCRUISE!!
    """)


def main_menu():
    print("\n\033[1;34m[+] 1. Tutorial")
    print("\033[1;34m[+] 2. Create new collection")
    print("\033[1;34m[+] 3. View existing collections")
    print("\033[1;34m[+] 4. Switch collections")
    print("\033[1;34m[+] 5. Quit\n")

def secondary_menu():
    print("\n\033[1;34m[+] 6. Run existing list of apps")
    print("\033[1;34m[+] 7. Add to current list of apps/websites")
    print("\033[1;34m[+] 8. Delete from current list of apps/websites")
    print("\033[1;34m[+] 9. View current list of apps/websites")
    print("\033[1;34m[+] 10. Main Menu")
    print("\033[1;34m[+] 5. Quit\n")


def choice_one(choice):
    """Tutorial should probably be placed within it's own Python file but this is a placeholder"""
    if choice == "1":

      print("""
      Welcome to the PyCruise Tutorial! PyCruise is a handy-dandy tool that saves the user time no matter who they are!
      You will be able to create "lists", which you can populate with browsers or applications you want /n
      to open upon command. You can also edit your lists to include more or less whenever you wish. Let's get Cruisin'/n
      shall we?

      [Rest of tutorial will go here but this will be a placeholder for now]
      """)


def choice_three(choice):
    if choice == "3":
        # file_list = None
        # print(len([name for name in os.listdir('.') if os.path.isfile(name)]))

        # path joining version for other paths
        DIR = 'txt_files/'
        # print(*str(fnmatch.filter(os.listdir(DIR), '*txt')), sep= "\n")

        file_list = fnmatch.filter(os.listdir(DIR), '*txt')
        # print(file_list)

        for i in range(len(file_list)):
            print(file_list[i].strip('.txt'))

        # a = ["Hello", "World"]
        # print(' '.join(a))
        # print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
        # go through and populate file_list with all txt files
        # if file_list is None:
        #     print(":( Sorry, you don't have any lists yet. Would you like to make one?")
        #     main_menu()
        # else:
        #     print(file_list)
        #     main_menu()


def choice_six(choice):
    """This is for Linux. For Mac/Windows users replace system path with path to application execution files"""
    if choice == "6":

        with open("add_app.txt", "r") as f:
            text_from_file = f.readlines()

            for app in text_from_file:
                if "http" in app or "www" in app:
                    webbrowser.open(app)
                else:
                    os.system(f"/snap/bin/{app}")


def choice_seven(choice):
    if choice == "7":

        while True:
            app_choice = input("Enter an app or website to add or (f) as finished: ")
            if app_choice.lower() == "f":
                break
            else:
                with open("add_app.txt", "a") as f:
                    f.write(f"{app_choice}\n")


def choice_eight(choice):
    if choice == "8":
        while True:
            delete_choice = input("Enter an app or website to delete or (f) as finished: ")
            if delete_choice.lower() == "f":
                break
            else:
                with open("add_app.txt", "r") as fr:
                    lines = fr.readlines()
                    with open("add_app.txt", "w") as fw:
                        for line in lines:
                            if line.strip('\n') != f"{delete_choice}":
                                fw.write(line)


def choice_nine(choice):
    if choice == "9":
        with open("add_app.txt", "r") as f:
            text_from_file = f.readlines()
            for file in text_from_file:
                print(file)


def choice_ten(choice):
    if choice == "10":
        main_menu()


def run():
    choice = "9"
    banner()

    while choice != "5":
        main_menu()
        choice = input("\033[1;34m[+]\033[1;m \033[1;91mEnter your choice:\033[1;m ")
        choice_one(choice)
        choice_two(choice)
        choice_three(choice)
        choice_four(choice)



run()
