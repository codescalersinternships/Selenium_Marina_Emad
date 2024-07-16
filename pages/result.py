class Result:
    # URL of the expected home page after login
    home = 'https://www.saucedemo.com/inventory.html'

    def __init__(self, browser):
        self.browser = browser

    def check(self) -> bool:
        # Get the current URL of the browser
        current_url = self.browser.current_url
        
        # Check if the current URL matches the expected home URL
        if current_url == self.home:
            return True  # Return True if it matches
        else:
            return False  # Return False if it does not match
