from time import sleep
from typing import List

from utils.PageObject import PageObject

PRODUCTS_LINK_SELECTOR = ".product .title > h2 > a"


class WallpapersPage(PageObject):
    page_url = "https://avi-home.co.il/product-category/wallpapers/"

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    def load_all_products(self, time_out=15, max_products=None):
        sleeping_time = 0
        products_len = 0
        while True:
            new_products_len = len(self.getElements(PRODUCTS_LINK_SELECTOR))
            if new_products_len > products_len:
                self.scroll_down()
                products_len = new_products_len
                sleeping_time = 0

            else:
                sleep(0.1)
                sleeping_time += 0.1

            if sleeping_time >= time_out:
                return self.products_list

            if max_products and new_products_len > max_products:
                return self.products_list

    @property
    def products_list(self) -> List[str]:
        links = []
        for product in self.getElements(PRODUCTS_LINK_SELECTOR):
            links.append(product.get_attribute("href"))

        return links
