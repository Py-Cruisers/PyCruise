import webbrowser
import os 

# Inspiration for the layout of this script is from
# the ghost_eye repository on GitHub
# https://github.com/BullsEye0/ghost_eye/blob/master/ghost_eye.py

def banner():
    print("""
    WELCOME TO PYCRUISE!!
    """)

def main_menu():
    print("\n\033[1;34m[+] 1. Run existing list of apps")
    print("\033[1;34m[+] 2. Add to current list of apps/websites")
    print("\033[1;34m[+] 3. Delete from current list of apps/websites")
    print("\033[1;34m[+] 4. View current list of apps/websites")
    print("\033[1;34m[+] 5. Quit\n")

def choice_one(choice):
    """This is for Linux. For Mac users replace system path with path to application execution files"""
    if choice == "1":

        with open("add_app.txt", "r") as f:
            text_from_file = f.read()
            for app in text_from_file:
                os.system(f"/snap/bin/{app}")
            print(text_from_file)
                

            # os.system("/snap/bin/code")
            # os.system("/snap/bin/slack")

            # webbrowser.open('https://canvas.instructure.com/courses/4916427')
            # webbrowser.open('https://zoom.us/j/99194599654?pwd=dUowRi9DSHpNbFBNaWtRQ3NYMDd4Zz09#success')

def choice_two(choice):
    if choice == "2":

        while True:
            app_choice = input("Enter an app or website to add or (f) as finished: ")
            if app_choice.lower() == "f":
                break
            else:
                with open("add_app.txt", "a") as f:
                    f.write(f"{app_choice}\n")

def run():
    choice = "4"
    banner()

    while choice != "5":
        main_menu()
        choice = input("\033[1;34m[+]\033[1;m \033[1;91mEnter your choice:\033[1;m ")
        choice_one(choice)
        choice_two(choice)

        


run()