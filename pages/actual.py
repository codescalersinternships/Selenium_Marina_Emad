"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Result:
  
  home= 'https://www.saucedemo.com/inventory.html'

  def __init__(self, browser):
    self.browser = browser


  def check(self)->bool:
    currentUrl= self.browser.current_url
    if currentUrl== self.home:
      return True
    else:
      return False