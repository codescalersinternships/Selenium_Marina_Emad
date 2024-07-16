from pages.result import Result  # Importing Result page object
from pages.login import LoginPage  # Importing LoginPage page object

USERNAME = 'error_user'  # Username used for login
PASSWORD = 'secret_sauce'  # Password used for login

# Define a test function named test_login_page that takes 'browser' fixture as an argument
def test_login_page(browser):
    # Instantiate LoginPage object with the 'browser' fixture
    login_page = LoginPage(browser)
    
    # Load the login page
    login_page.load()
    
    # Perform login with provided username and password
    login_page.login(USERNAME, PASSWORD)
    
    # Instantiate Result page object with the 'browser' fixture
    result = Result(browser)
    
    # Assert that the login was successful by checking some condition on the Result page
    assert result.check()
