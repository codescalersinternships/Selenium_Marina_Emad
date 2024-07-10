"""
These tests cover Login page.
"""

import pytest

from pages.actual import Result
from pages.login import LoginPage

USERNAME= 'error_user'
PASSWORD= 'secret_sauce'

def test_login_page(browser):
  login_page = LoginPage(browser)
  login_page.load()
  login_page.login(USERNAME,PASSWORD)
  actual= Result(browser)
  assert actual.check()
  



