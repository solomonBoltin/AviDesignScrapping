from time import sleep

from selenium.webdriver.common.by import By

from utils.PageObject import PageObject
from utils.table_builder import build_table


class WallpaperPage(PageObject):

    def __init__(self, wallpaper_link, driver=None):
        self.page_url = wallpaper_link
        super().__init__(driver=driver)

    @property
    def title(self):
        return self.get_element_text(".product_title")

    @property
    def price(self):
        return self.get_element_text(".price")

    @property
    def images(self):
        thumbs = self.getElements(".flex-control-nav.flex-control-thumbs img")
        if len(thumbs) > 1:
            for thumb in thumbs:
                thumb.click()
            sleep(1)
        images_text = ""
        for img in self.getElements(".zoomImg"):
            images_text += f"{img.get_attribute('src')},"
        return images_text

    @property
    def details(self):
        details_name = self.getElements(".woocommerce-product-attributes-item th")
        details_value = self.getElements(".woocommerce-product-attributes-item td")

        details = []
        for name, value in zip(details_name, details_value):
            details.append((name.text, value.text))
        return build_table(details)

    @property
    def product_id(self):
        try:
            return self.get_element_text(".sku_wrapper :last-child")
        except:
            return int(self.get_element_text(".product_title")[:6])

    @property
    def categories(self):
        return self.get_element_text(".posted_in :last-child")

    @property
    def hashtags(self):
        return self.get_element_text(".tagged_as :last-child")
