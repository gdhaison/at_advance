from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google():
    # Connect to the Selenium Grid
    chrome_options = Options()

    driver = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        options=chrome_options
    )

    # Open Google
    driver.get("https://www.google.com")

    WebDriverWait(driver, 10).until(EC.title_contains("Google"))

    # Print the title of the page
    print(driver.title)

    # Close the browser
    # driver.quit()

if __name__ == "__main__":
    test_google()