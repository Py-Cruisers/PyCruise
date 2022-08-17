import webbrowser
import os

# Inspiration for the layout of this script is from
# the ghost_eye repository on GitHub
# https://github.com/BullsEye0/ghost_eye/blob/master/ghost_eye.py

def banner():

    print(""" Welcome to PyCruise! This is a program that will open your favorite apps and websites.                                                         
    """)


def main_menu():
    print("\n\033[1;34m[+] 1. Run existing list of apps")
    print("\033[1;34m[+] 2. Add to current list of apps/websites")
    print("\033[1;34m[+] 3. Delete from current list of apps/websites")
    print("\033[1;34m[+] 4. View current list of apps/websites")
    print("\033[1;34m[+] 5. Quit\n")

def choice_one(choice):
    """This is for Linux. For Mac/Windows users replace system path with path to application execution files"""
    if choice == "1":

        with open("add_app.txt", "r") as f:
            text_from_file = f.readlines()
            
            for app in text_from_file:
                if "http" in app or "www" in app:
                    webbrowser.open(app)
                else:
                    app_to_use = app.strip('\n').lower()
                    os.system(f"/snap/bin/{app_to_use}")

def choice_two(choice):
    if choice == "2":

        while True:
            app_choice = input("Enter an app or website to add or (f) as finished: ")
            if app_choice.lower() == "f":
                break
            else:
                with open("add_app.txt", "a") as f:
                    f.write(f"{app_choice}\n")

def choice_three(choice):
    if choice == "3":
        while True:
            delete_choice = input("Enter an app or website to delete or (f) as finished: ")
            if delete_choice.lower() == "f":
                break
            else:
                with open("add_app.txt", "r") as fr:
                    lines = fr.readlines()
                    with open("add_app.txt", "w") as fw:
                        for line in lines:
                            if line.strip('\n').lower() != f"{delete_choice}":
                                fw.write(line)

def choice_four(choice):
    if choice == "4":
        with open("add_app.txt", "r") as f:
            text_from_file = f.readlines()
            for file in text_from_file:
                print(file)


def run():
    choice = "4"
    banner()

    while choice != "5":
        main_menu()
        choice = input("\033[1;34m[+]\033[1;m \033[1;91mEnter your choice:\033[1;m ")
        choice_one(choice)
        choice_two(choice)
        choice_three(choice)
        choice_four(choice)


run()
