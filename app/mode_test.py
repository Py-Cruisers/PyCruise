import webbrowser
import os
import fnmatch
from tutorial import Tutorial


# Inspiration for the layout of this script is from
# the ghost_eye repository on GitHub
# https://github.com/BullsEye0/ghost_eye/blob/master/ghost_eye.py

def banner():
    print("""
    WELCOME TO PYCRUISE!!
    """)


def main_menu():
    print("\n\033[1;34m[+] 1. Tutorial")
    print("\033[1;34m[+] 2. View existing collections")
    print("\033[1;34m[+] 3. Create new collection")
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
    if choice == "1":
        Tutorial
        main_menu()



def choice_two(choice):
    if choice == "2":

        DIR = 'txt_files/'

        file_list = fnmatch.filter(os.listdir(DIR), '*txt')
        file_len = (len(fnmatch.filter(os.listdir(DIR), '*txt')))

        if file_len == 0:
            print(":( Sorry, you don't have any lists yet. Would you like to make one?")

        else:
            for i in range(len(file_list)):
                print(file_list[i].strip('.txt'))


def choice_three(choice):
    if choice == "3":
        new_collection = input('> ')
        open(f"txt_files/{new_collection}.txt", "a")

def choice_four(choice):
    if choice == "4":
        DIR = 'txt_files/'
        current_collection = None

        file_list = fnmatch.filter(os.listdir(DIR), '*txt')
        file_len = (len(fnmatch.filter(os.listdir(DIR), '*txt')))

        if file_len == 0:
            print(":( Sorry, you don't have any lists yet. Would you like to make one?")

        else:
            for i in range(len(file_list)):
                print(file_list[i].strip('.txt'))
            switch = input("What collection would you like to choose? > ")
            current_collection = switch
            print(current_collection)


            def choice_six(choice):
                """This is for Linux. For Mac/Windows users replace system path with path to application execution files"""
                if choice == "6":

                    with open(f"txt_files/{current_collection}.txt", "r") as f:
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
                            with open(f"txt_files/{current_collection}.txt", "a") as f:
                                f.write(f"{app_choice}\n")


            def choice_eight(choice):
                if choice == "8":
                    while True:
                        delete_choice = input("Enter an app or website to delete or (f) as finished: ")
                        if delete_choice.lower() == "f":
                            break
                        else:
                            with open(f"txt_files/{current_collection}.txt", "r") as fr:
                                lines = fr.readlines()
                                with open(f"txt_files/{current_collection}.txt", "w") as fw:
                                    for line in lines:
                                        if line.strip('\n') != f"{delete_choice}":
                                            fw.write(line)


            def choice_nine(choice):
                if choice == "9":
                    with open(f"txt_files/{current_collection}.txt", "r") as f:
                        text_from_file = f.readlines()
                        for file in text_from_file:
                            print(file)

            def secondary_run():
                choice = "9"
                banner()

                while choice != "5":
                    secondary_menu()
                    choice = input("\033[1;34m[+]\033[1;m \033[1;91mEnter your choice:\033[1;m ")
                    choice_six(choice)
                    choice_seven(choice)
                    choice_eight(choice)
                    choice_nine(choice)

            secondary_run()

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
