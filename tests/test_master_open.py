import os
import pytest
# import mock
import builtins
import app.mode_test


# @pytest.mark.skip("TODO")
def test_create_mode():
    try:
        os.remove("txt_files/dev.txt")
    except FileNotFoundError:
        pass
    responses = ["3", "dev", "5", "5"]

    def mock_input(*args, **kwargs):
        response = responses.pop(0)
        print(f"> {response}\n")
        return response

    real_input = builtins.input
    builtins.input = mock_input

    app.mode_test.run

    response = input("Enter your choice: ")
    app.mode_test.choice_three(response)

    file_exists = os.path.exists('txt_files/dev.txt')
    expected = True
    assert file_exists == expected

# @pytest.mark.skip("TODO") 
def test_select_modes():
    """
    
    """
    responses = ["1", "dev", "r", "5"]
    output = ""

    def mock_input(*args, **kwargs):
        response = responses.pop(0)
        print(f"{response}\n")
        return response

    def mock_print(*args, **kwargs):
        nonlocal output
        output += args[0] + "\n"
        return

    real_print = builtins.print
    builtins.print = mock_print

    real_input = builtins.input
    builtins.input = mock_input

    app.mode_test.run
    response = input("Enter your choice: ")
    app.mode_test.choice_four(response)
    input("Which mode would you like to select? > ")
    

    
    real_print(output)

    assert output == """1

dev
dev

Current Mode Activated: dev

\033[1;34m[+] 6. Launch Selected Mode
\033[1;34m[+] 7. View Apps/Websites in Selected Mode
\033[1;34m[+] 8. Add Apps/Websites to Selected Mode
\033[1;34m[+] 9. Delete Apps/Websites from Selected Mode
\033[1;34m[+] R. Return to Main Menu

r

5

"""

# @pytest.mark.skip("TODO") 
def test_add_app():
    """
    While testing add_app  
    - run pytest -s
    - enter: '1' to select mode
    - enter: 'dev' to select dev
    - enter: '8' to add app
    - enter: 'slack' to add slack
    - enter: 'r' to return to main menu
    - enter: '5' to quit

    test should pass
    """
    responses = ["1", "dev", "8", "slack", "f", "r", "5"]

    def mock_input(*args, **kwargs):
        response = responses.pop(0)
        print(f"> {response}\n")
        return response

    real_input = builtins.input
    builtins.input = mock_input

    app.mode_test.run

    response_one = input("select mode ")
    app.mode_test.choice_four(response_one)
   
    with open ("txt_files/dev.txt", 'r') as f:
        content = f.readlines()
    expected = "slack"
    assert content[-1].strip("\n") == expected

# @pytest.mark.skip("TODO") 
def test_delete_app():
    """
    While testing delete_app  
    
    - enter: '1' to select mode
    - enter: 'dev' to select dev
    - enter: '8' to add app
    - enter: 'code' to add code
    - enter: 'f' to finish
    - enter: '9' to remove app
    - enter: 'code' to remove code
    - enter: 'f' to finish
    - enter: 'r' to return to main menu
    - enter: '5' to quite

    test should pass
    """
    responses = ["1", "dev", "8", "code", "f", "9", "code", "f", "r", "5"]

    def mock_input(*args, **kwargs):
        response = responses.pop(0)
        print(f"> {response}\n")
        return response

    real_input = builtins.input
    builtins.input = mock_input

    app.mode_test.run

    response_one = input("select mode ")
    # app.mode_test.choice_four(response_one)

    with open ("txt_files/dev.txt", 'r') as f:
        content = f.readlines()
    test = True
    for file in content:
        if file.strip("\n") == 'code':
            test = False
    expected = True
    assert test == expected

# @pytest.mark.skip("TODO") 
def test_view_apps():
    """
    
    """
    responses = ["1", "dev", "7", "r", "5"]
    output = ""

    def mock_input(*args, **kwargs):
        response = responses.pop(0)
        print(f"> {response}\n")
        return response

    def mock_print(*args, **kwargs):
        nonlocal output
        output += args[0] + "\n"
        return

    real_print = builtins.print
    builtins.print = mock_print

    real_input = builtins.input
    builtins.input = mock_input

    app.mode_test.run
    response = input("Enter your choice: ")
    app.mode_test.choice_four(response)


    
    real_print(output)

    assert output == """> 1

dev
> dev

Current Mode Activated: dev

\033[1;34m[+] 6. Launch Selected Mode
\033[1;34m[+] 7. View Apps/Websites in Selected Mode
\033[1;34m[+] 8. Add Apps/Websites to Selected Mode
\033[1;34m[+] 9. Delete Apps/Websites from Selected Mode
\033[1;34m[+] R. Return to Main Menu

> 7

slack

Current Mode Activated: dev

\033[1;34m[+] 6. Launch Selected Mode
\033[1;34m[+] 7. View Apps/Websites in Selected Mode
\033[1;34m[+] 8. Add Apps/Websites to Selected Mode
\033[1;34m[+] 9. Delete Apps/Websites from Selected Mode
\033[1;34m[+] R. Return to Main Menu

> r

"""

# @pytest.mark.skip("TODO") 
def test_view_modes():
    """
    
    """
    responses = ["2", "5"]
    output = ""

    def mock_input(*args, **kwargs):
        response = responses.pop(0)
        print(f"> {response}\n")
        return response

    def mock_print(*args, **kwargs):
        nonlocal output
        output += args[0] + "\n"
        return

    real_print = builtins.print
    builtins.print = mock_print

    real_input = builtins.input
    builtins.input = mock_input

    app.mode_test.run
    response = input("Enter your choice: ")
    app.mode_test.choice_two(response)


    
    real_print(output)

    assert output == """> 2

Current Existing Modes: 
dev
"""