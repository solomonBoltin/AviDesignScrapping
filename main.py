import sys
from time import sleep

from pages.WallpaperPage import WallpaperPage
from pages.WallpapersPage import WallpapersPage
from utils.WallpapersDatabase import WallpapersDatabase

wallpaper_database = WallpapersDatabase()


def get_wallpapers_list_test():
    print(f"Starting to steal avi's products\n"
          f"Current mission: Wallpapers\n")
    print(f"Searching for wallpapers...")
    wallpapers_page = WallpapersPage()
    wallpapers_list = wallpapers_page.load_all_products()

    print(f"I found {len(wallpapers_list)} wallpapers")
    print(f"Downloading products...")

    success_len = 0
    error_len = 0
    driver = wallpapers_page.driver
    for product_link in wallpapers_list:
        done = False
        tries = 0

        wallpaper_page = WallpaperPage(product_link, driver=driver)

        while not done:
            try:
                report_progress(product_link, len(wallpapers_list), success_len, error_len, True if tries else False)
                wallpaper_database.add_wallpaper(wallpaper_page)
                success_len += 1
                break
            except Exception as error:
                tries += 1

                if tries >= 5:
                    raise error
                wallpaper_page = WallpaperPage(product_link, driver=driver)
                sleep(tries)


    wallpapers_page.driver.close()


def report_progress(current_product, products_len, successful_len, error_len, retrying):
    sys.stdout.write(f"\rWorking on: {current_product}, {products_len}/{successful_len}, Total errors: {error_len}, "
                     f"{'Retrying..' if retrying else ''}")


get_wallpapers_list_test()
