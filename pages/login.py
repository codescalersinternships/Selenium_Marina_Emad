from selenium.webdriver.common.by import By

class LoginPage:
    # URL of the login page
    base_url = 'https://www.saucedemo.com/'

    # Locators for elements on the login page
    username_locator = (By.ID, 'user-name')
    password_locator = (By.ID, 'password')
    login_button_locator = (By.ID, 'login-button')

    # Constructor to initialize the class with a browser instance
    def __init__(self, browser):
        self.browser = browser

    # Method to load the login page
    def load(self):
        self.browser.get(self.base_url)

    # Method to enter username in the username input field
    def enter_username(self, username):
        username_input = self.browser.find_element(*self.username_locator)
        username_input.clear()  # Clear any existing text in the field
        username_input.send_keys(username)

    # Method to enter password in the password input field
    def enter_password(self, password):
        password_input = self.browser.find_element(*self.password_locator)
        password_input.clear()  # Clear any existing text in the field
        password_input.send_keys(password)

    # Method to click the login button
    def click_login_button(self):
        login_button = self.browser.find_element(*self.login_button_locator)
        login_button.click()

    # Method to perform login with provided credentials
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
