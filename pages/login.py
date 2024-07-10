"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:

  # URL

  URL = 'https://www.saucedemo.com/'

  # Locators

  USERNAME_INPUT = (By.ID, 'user-name')
  PASSWORD_INPUT = (By.ID, 'password')
  LOGIN_BUTTON = (By.ID, 'login-button')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def login(self, phrase):
    username_input = self.browser.find_element(*self.USERNAME_INPUT)
    username_input.send_keys(phrase + Keys.RETURN)

    password_input = self.browser.find_element(*self.PASSWORD_INPUT)
    password_input.send_keys(phrase + Keys.RETURN)

    login_button = self.browser.find_element(*self.LOGIN_BUTTON)
    login_button.click()