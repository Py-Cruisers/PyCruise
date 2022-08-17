import pytest
import mock
import builtins
import app.master_open

# @pytest.mark.skip("TODO")
def test_choice_two():
    """
    While testing choice_two:
    - enter "2"  when prompted to "add to current list of apps/websites"
    - enter "code" after "Enter an app or website to add or (f) as finished:"
    - enter "f" after "Enter an app or website to add or (f) as finished:"
    - enter "5" to quit

    If successful "code" will be added to the add_app.txt and test
    will pass 
    """
    app.master_open.input = lambda: '2'
    app.master_open.input = lambda: 'code'
    with open ("./add_app.txt", 'r') as f:
        content = f.readlines()
    expected = "code"
    assert content[-1].strip("\n") == expected


# @pytest.mark.skip("TODO")       
# def test_choice_three():
#     app.master_open.input = lambda: '2'