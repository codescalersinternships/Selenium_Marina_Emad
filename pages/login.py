from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    # URL of the login page
    baseURL = 'https://www.saucedemo.com/'

    # Locators for elements on the login page
    username = (By.ID, 'user-name')
    password = (By.ID, 'password')
    login_button = (By.ID, 'login-button')

    # Constructor to initialize the class with a browser instance
    def __init__(self, browser):
        self.browser = browser

    # Method to load the login page
    def load(self):
        self.browser.get(self.baseURL)

    # Method to perform login with provided credentials
    def login(self, username, password):
        # Locate the username input field and enter the provided username
        username_input = self.browser.find_element(*self.username)
        username_input.send_keys(username)

        # Locate the password input field and enter the provided password
        password_input = self.browser.find_element(*self.password)
        password_input.send_keys(password)

        # Locate the login button and click on it to submit the login form
        login_button = self.browser.find_element(*self.login_button)
        login_button.click()
