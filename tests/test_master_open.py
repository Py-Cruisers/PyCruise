import os
import pytest
import mock
import builtins
import app.mode_test

# @pytest.mark.skip("TODO")
def test_create_mode():
    """
    While testing option_three (create new mode) 
    - run pytest -s
    - enter: '3' to create
    - enter: '1' to select mode
    - enter: 'dev' to select dev
    - enter: 'r' to return to main menu
    - enter: '5' to quite

    test should pass
    """
    app.mode_test.input = lambda: '3'
    app.mode_test.input = lambda: 'dev'
    app.mode_test.input = lambda: '1'
    app.mode_test.input = lambda: 'dev'
    file_exists = os.path.exists('txt_files/dev.txt')
    expected = True
    assert file_exists == expected
    
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
    - enter: '5' to quite

    test should pass
    """
    app.mode_test.input = lambda: '1'
    app.mode_test.input = lambda: 'dev'
    app.mode_test.input = lambda: '8'
    app.mode_test.input = lambda: 'slack'
    with open ("txt_files/dev.txt", 'r') as f:
        content = f.readlines()
    expected = "slack"
    assert content[-1].strip("\n") == expected

# @pytest.mark.skip("TODO") 
def test_delete_app():
    """
    While testing add_app  
    - run pytest -s
    - enter: '1' to select mode
    - enter: 'dev' to select dev
    - enter: '8' to add app
    - enter: 'code' to add code
    - enter: '9' to remove app
    - enter: 'code' to remove code
    - enter: 'r' to return to main menu
    - enter: '5' to quite

    test should pass
    """
    app.mode_test.input = lambda: '1'
    app.mode_test.input = lambda: 'dev'
    app.mode_test.input = lambda: '9'
    app.mode_test.input = lambda: 'code'
    with open ("txt_files/dev.txt", 'r') as f:
        content = f.readlines()
    test = True
    for file in content:
        if file.strip("\n") == 'code':
            test = False
    expected = True
    assert test == expected