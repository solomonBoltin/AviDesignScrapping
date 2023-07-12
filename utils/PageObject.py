from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.DriverTool import DriverTools


class PageObject(DriverTools):
    page_url = None

    def __init__(self, driver=None):
        if not driver:
            chrome_options = Options()
            chrome_options.add_argument("--headless")

            driver = webdriver.Chrome("C:\\Users\\bolts\\Downloads\\chrome\\chromedriver.exe",
                                      options=chrome_options)
        super().__init__(driver)
        if self.page_url:
            driver.get(self.page_url)



