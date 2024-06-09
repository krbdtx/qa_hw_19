import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os
from utils import attach
from dotenv import load_dotenv
from appium import webdriver

load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": os.getenv('USER_NAME'),
            "accessKey": os.getenv('ACCESS_KEY')
        }
    })

    browser.config.driver = webdriver.Remote(
        'http://hub.browserstack.com/wd/hub',
        options=options
    )

    browser.config.timeout = 10.0

    yield

    attach.add_screenshot(browser)
    attach.add_video(browser)

    browser.quit()
