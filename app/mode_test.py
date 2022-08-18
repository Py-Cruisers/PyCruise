import platform
import webbrowser
import os
import fnmatch
from tutorial import Tutorial
from pathlib import Path


# Inspiration for the layout of this script is from
# the ghost_eye repository on GitHub
# https://github.com/BullsEye0/ghost_eye/blob/master/ghost_eye.py

def banner():
    print(""" \033[01;33m                 
8888888b.            .d8888b.                   d8b                   
888   Y88b          d88P  Y88b                  Y8P                   
888    888          888    888                                        
888   d88P 888  888 888        888d888 888  888 888 .d8888b   .d88b.  
8888888P"  888  888 888        888P"   888  888 888 88K      d8P  Y8b 
888        888  888 888    888 888     888  888 888 "Y8888b. 88888888 
888        Y88b 888 Y88b  d88P 888     Y88b 888 888      X88 Y8b.     
888         "Y88888  "Y8888P"  888      "Y88888 888  88888P'  "Y8888  
                888                                                   
           Y8b d88P                                                   
            "Y88P"                                                       
            \033[m                                                                                          
        \033[34m PyCruise - Convenience Tool \033[0m
        \033[34m Author:\033[m \033[01;33m Liesl W.\033[m, \033[34mDennis D.\033[m,\033[01;33m  Marco S.\033[m, \033[34mDominic G.\033[0m, \033[01;33m Brentice L. \033[0m
        \033[34m Github:  https://github.com/Py-Cruisers/PyCruise \033[0m
        \033[34m Code Fellow 401 Project \033[0m
              \033[01;33m Welcome to PyCruse!\033[m """)


def main_menu():
    print("\n\033[1;34m[+] 1. Select Mode")
    print("\033[1;34m[+] 2. View Your Modes")
    print("\033[1;34m[+] 3. Create New Mode")
    print("\033[1;34m[+] 4. How to use PyCruise")
    print("\033[1;34m[\033[1;91m+\033[m\033[1;34m] \033[1;91m5. Quit\033[m\n")

def secondary_menu():
    print("\n\033[1;34m[+] 6. Launch Selected Mode")
    print("\033[1;34m[+] 7. View Apps/Websites in Selected Mode")
    print("\033[1;34m[+] 8. Add Apps/Websites to Selected Mode")
    print("\033[1;34m[+] 9. Delete Apps/Websites from Selected Mode")
    print("\033[1;34m[+] R. Return to Main Menu\n")


def choice_one(choice):
     if choice == "4":
        instance = Tutorial()
        instance.tut_run()


def choice_two(choice):
    if choice == "2":

        DIR = 'txt_files/'

        file_list = fnmatch.filter(os.listdir(DIR), '*txt')
        file_len = (len(fnmatch.filter(os.listdir(DIR), '*txt')))

        if file_len == 0:
            print(":( Sorry, you have yet to create a mode. Enter (3) to create a new mode now!")

        else:
            print("Current Existing Modes: ")
            for i in range(len(file_list)):
                print(Path(file_list[i]).stem)


def choice_three(choice):
    if choice == "3":
        new_collection = input('Name your mode > ')
        open(f"txt_files/{new_collection}.txt", "a")

def choice_four(choice):
    if choice == "1":
        DIR = 'txt_files/'
        current_collection = None

        file_list = fnmatch.filter(os.listdir(DIR), '*txt')
        file_len = (len(fnmatch.filter(os.listdir(DIR), '*txt')))

        if file_len == 0:
            print(":( Sorry, you don't have any lists yet. Would you like to make one?")

        else:
            for i in range(len(file_list)):
                print(Path(file_list[i]).stem)
            switch = input("Which mode would you like to select? > ")
            current_collection = switch
            # print(current_collection)


            def choice_six(choice):
                """This is for Linux. For Mac/Windows users replace system path with path to application execution files"""
                if choice == "6":

                    with open(f"txt_files/{current_collection}.txt", "r") as f:
                        text_from_file = f.readlines()
                        if len(text_from_file) == 0:
                            print(":( Sorry, you don't have any Apps/Websites in this mode. Enter (8) to add.")

                        for app in text_from_file:
                            if "http" in app or "www" in app:
                                webbrowser.open(app.strip())
                            else:
                                app_to_use = app.strip('\n').lower()

                                if platform.system() == 'Linux':
                                    # print("Linux detected.")
                                    os.system(f"/snap/bin/{app_to_use}")

                                if platform.system() == 'Linux' and "WSL" in platform.release():
                                # print("WSL detected. Will require Windows fn()'s")
                                    pass

                                if platform.system() == 'Windows':
                                    # print("Windows detected.")
                                    pass

                                if platform.system() == 'Darwin':
                                    # print("Now opening MacOS Application!")
                                    os.system(f"""osascript -e 'tell application "{app_to_use}" to activate'""")


            def choice_seven(choice):
                if choice == "8":

                    while True:
                        app_choice = input("Enter an app or website to add or (f) as finished: ")
                        if app_choice.lower() == "f":
                            break
                        else:
                            with open(f"txt_files/{current_collection}.txt", "a") as f:
                                f.write(f"{app_choice}\n")


            def choice_eight(choice):
                if choice == "9":
                    while True:
                        delete_choice = input("Enter an app or website to delete or (f) as finished: ")
                        if delete_choice.lower() == "f":
                            break
                        else:
                            with open(f"txt_files/{current_collection}.txt", "r") as fr:
                                lines = fr.readlines()
                                with open(f"txt_files/{current_collection}.txt", "w") as fw:
                                    for line in lines:
                                        if line.strip('\n').lower() != f"{delete_choice.lower()}":
                                            fw.write(line)


            def choice_nine(choice):
                if choice == "7":
                    with open(f"txt_files/{current_collection}.txt", "r") as f:
                        text_from_file = f.readlines()
                        if len(text_from_file) == 0:
                            print(":( Sorry, you don't have any Apps/Websites in this mode. Enter (8) to add.")
                        for file in text_from_file:
                            print(file)

            def secondary_run():
                choice = "7"



                while choice != "R" and choice != "r":
                    print(f"Current Mode Activated: {current_collection}")
                    secondary_menu()
                    choice = input("\033[1;34m[+]\033[1;m \033[01;33mEnter your choice:\033[1;m ")
                    choice_six(choice)
                    choice_seven(choice)
                    choice_eight(choice)
                    choice_nine(choice)

            secondary_run()

def choice_ten(choice):
    if choice == "10":
        return main_menu()


def run():
    choice = "7"
    banner()

    while choice != "5":
        main_menu()
        choice = input("\033[1;34m[\033[01;33m+\033[1;34m]\033[1;m \033[01;33mEnter your choice:\033[1;m ")
        choice_one(choice)
        choice_two(choice)
        choice_three(choice)
        choice_four(choice)

run()
