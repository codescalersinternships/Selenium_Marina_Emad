
from pages.login import LoginPage  # Importing LoginPage page object

# Define a base URL for the application
base_url = 'https://www.saucedemo.com'
username = 'standard_user'  # Username used for login
password = 'secret_sauce'  # Password used for login
expected_url = base_url + '/inventory.html'  # Define the expected URL after successful login

# Define a test function named test_login_page that takes 'browser' fixture as an argument
def test_login_page(browser):
    # Instantiate LoginPage object with the 'browser' fixture
    login_page = LoginPage(browser)
    
    # Load the login page
    login_page.load()
    
    # Perform login with provided username and password
    login_page.login(username, password)
    
    # Instantiate LoginPage object with the 'browser' fixture
    login_page = LoginPage(browser)
    
    # Load the login page
    login_page.load()
    
    # Perform login with provided username and password
    login_page.login(username, password)
    
    # Get the current URL of the browser after login
    current_url = browser.current_url
    
    # Assert that the current URL matches the expected URL after successful login
    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"
