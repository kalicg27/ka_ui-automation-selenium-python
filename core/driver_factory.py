from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from .config_loader import Config


def get_webdriver(config: Config):
    browser = config.browser.lower()

    if browser == "chrome":
        options = ChromeOptions()
        if config.headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(
            options=options,
            executable_path=ChromeDriverManager().install()
        )
    elif browser == "firefox":
        options = FirefoxOptions()
        if config.headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(
            options=options,
            executable_path=GeckoDriverManager().install()
        )
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(config.implicit_wait)
    driver.set_page_load_timeout(config.page_load_timeout)
    return driver
