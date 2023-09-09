import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Specify the language for tests (e.g., "en", "es")')
    parser.addoption('--browser', action='store', default='chrome',
                     help='Specify the browser for tests (e.g., "chrome", "firefox")')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    browser_name = request.config.getoption('browser')
    print("\nstart browser for test..")
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        options.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser should be chrome or firefox')

    yield browser
    print("\nquit browser..")
    browser.quit()