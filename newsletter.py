import datetime
import time
import os
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SavePNG:

    def __init__(self, site, png):
        self.chromeDriverPath = os.path.join(
            "C:\\", 'Selenium', 'chromedriver.exe')
        # self.options = Options()
        # self.options.add_argument(
        #     "user-data-dir = C:\Program Files (x86)\Google\Chrome\Application andrew.mullen@avast.com")
        self.chrome = webdriver.Chrome(
            self.chromeDriverPath)
        self.chrome.fullscreen_window()
        self.site = site
        self.png = png

    def run_chrome(self):
        self.chrome.get(self.site)
        try:
            self.chrome.find_element_by_class_name('button').click()
        except Exception as E:
            print(E)
        time.sleep(60)
        self.chrome.get_screenshot_as_file(self.png)
        self.chrome.close()

    # image is 1920 x 1036
    def crop_png(self, left, up, right, bottom, name):

        img = Image.open(self.png)
        img.crop((left, up, right, bottom)).save(name)


def get_kpi_data():
    data = SavePNG(
        "https://app.powerbi.com/groups/64a5a5a9-99f0-4dac-a226-96bb1dae39e1/reports/ee86796b-373e-4f2e-b1b9-035142f0b957/ReportSectioned4821d7dfe678de7714?ctid=f6a3192f-e85f-4626-a7db-73bd301e26b7",
        "unedited.png")
    data.run_chrome()
    save = input("Would you like to save the photos? (y/n) ")
    if save == 'y':
        data.crop_png(784, 262, 1309, 576,
                      "G:\My Drive\VPN Images\stats\daily_view_users.png")
        data.crop_png(1329, 262, 1854, 576,
                      "G:\My Drive\VPN Images\stats\daily_view_installs.png")
        data.crop_png(784, 680, 1309, 995,
                      "G:\My Drive\VPN Images\stats\monthly_view_users.png")
        data.crop_png(1329, 680, 1854, 995,
                      "G:\My Drive\VPN Images\stats\monthly_view_installs.png")


get_kpi_data()
