import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FireFoxOptions

# ---------------------------------------------------------------
# @pytest.fixture(scope="module")
# def firefox_browser_instance(request):
#     """
#     Provide  a selenium Webdriver instance for FireFox I still dont know why this
#     is not working
#     """
#     options = FireFoxOptions()
#     options.add_argument("--headless") #  Make The Tests Run in the Background
#     browser = webdriver.Firefox(options = options)
#     yield browser
#     browser.close()


# ---------------------------------------------------------------
@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    Provide a selenium webdriver instance for Chrome
    """
    options = Options()
    options.headless = False
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.close()
