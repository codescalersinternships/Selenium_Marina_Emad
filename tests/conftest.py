import pytest
from selenium import webdriver

# Define a fixture named 'browser' using pytest.fixture decorator
@pytest.fixture
def browser():
    # Configure Chrome options
    options = webdriver.ChromeOptions()

    # Set window size to maximum
    options.add_argument("--start-maximized")
    
    # Set headless mode
    options.add_argument("--headless")  # Comment this line if you want to run in non-headless mode
    
    # Initialize Chrome WebDriver with the configured options
    driver = webdriver.Chrome(options=options)
    
    # Set implicit wait time to 10 seconds
    driver.implicitly_wait(30)
    
    # Yield the WebDriver instance to the test function
    yield driver
    
    # Quit the WebDriver instance after the test completes
    driver.quit()
