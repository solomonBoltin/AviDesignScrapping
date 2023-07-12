import time
from typing import List

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class DriverTools:
    driver = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def getElement(self, cssSelector, timeout=5) -> WebElement:
        driver = self.driver
        timeout = timeout * 5
        for x in range(timeout):
            try:
                el = driver.find_element_by_css_selector(cssSelector)
                if el.is_displayed():
                    return el
                time.sleep(0.2)
            except:
                time.sleep(0.2)
        el = driver.find_element_by_css_selector(cssSelector)
        return el

    def getElements(self, cssSelector, timeout=5) -> List[WebElement]:
        driver = self.driver
        timeout = timeout * 5
        for x in range(timeout):
            try:
                els = driver.find_elements(By.CSS_SELECTOR, cssSelector)
                return els

            except:
                time.sleep(0.2)
        els = driver.find_elements(By.CSS_SELECTOR, cssSelector)
        return els

    def click(self, cssSelector, timeout=5):
        for sec in range(timeout * 5):
            try:
                em = self.getElement(cssSelector, timeout=1)
                em.click()
                return em
            except:
                time.sleep(1 / 5)

        em = self.getElement(cssSelector, timeout=1)
        em.click()
        return em

    def clickByIndex(self, cssSelector, index, timeout=5):
        for sec in range(timeout * 5):
            try:
                em = self.getElements(cssSelector)[index]
                em.click()
                return em
            except:
                time.sleep(1 / 5)
        em = self.getElements(cssSelector)[index]
        em.click()
        return em

    def clickByText(self, text, timeout=5):
        for sec in range(timeout * 5):
            try:
                em = self.driver.find_elements_by_xpath(f'//*[text()="{text}"]')[-1]
                em.click()
                return em
            except:
                time.sleep(1 / 5)

        em = self.driver.find_elements_by_xpath(f'//*[text()="{text}"]')[-1]
        em.click()
        return em

    def get_element_text(self, css_selector, timeout=5, skips=0.1):
        element = self.getElement(css_selector)
        time_passed = 0
        while time_passed < timeout:
            try:
                te = element.text
                if te != "":
                    return te
                else:
                    element = self.getElement(css_selector)
                    time.sleep(skips)
                    time_passed += skips
            except Exception:
                element = self.getElement(css_selector)
                time.sleep(skips)
                time_passed += skips
        raise ValueError('Element has no text \ncss selector:' + css_selector)
