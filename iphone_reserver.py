from selenium import webdriver as uc
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from colors import *

from time import sleep
import signal
from os import system

import chime
from pync import Notifier


def signal_handler(signal, frame):
    logo()
    print(O + "[" + C + "*" + O + "] " +
          C + "Thank you" + W)
    exit()


signal.signal(signal.SIGINT, signal_handler)


class Search_Iphone():
    def __init__(self):
        logo()
        self.driver = uc.Chrome(service=Service(
            ChromeDriverManager().install()))
        self.url = 'https://reserve-prime.apple.com/AE/en_AE/reserve/A/availability?iUP=N'
        self.driver.get(self.url)

        logo()

        print("")
        print(O + "[ " + C + "*" + O + " ] " + C +
              "Better to Login First then start the tool")

        user_output = input(O + "[ " + C + "*" + O + " ] " + C +
                                "Would you like to login first (Y/n): " + W)
        if user_output.lower() == "y":
            self.login()
        else:
            input(O + "[ " + C + "*" + O + " ] " + C +
                  "Press " + G + "[ENTER]" + C + " To Continue" + W)

        chime.info()
        self.send_notification(False)
        print(O + "[ " + C + "*" + O + " ] " + C + "Starting")
        print(O + "[ " + C + "*" + O + " ] " + C +
              "Searching for " + O + "Iphone 14" + C + " in Apple")

        count = 0

        self.checkAvailability(count)

    def checkAvailability(self, count):
        count = count + 1
        try:
            for count in range(100000):
                try:
                    notAvailableText = self.driver.find_element(
                        by=By.XPATH, value='/html/body/main/div/section/div/div/div/h1').text
                except:
                    notAvailableText = "Available"

                if (notAvailableText == "We’re not taking reservations to buy iPhone in the store right now."):
                    print(O + "[" + C, count, O + "] " +
                          R + "Not Available", end="\r")
                    self.driver.refresh()
                    sleep(1.5)
                elif (notAvailableText == "Available"):
                    chime.success()
                    self.send_notification(True)
                    print(O + "[ " + C + "*" + O + " ] " +
                          C + "Done" + G, count, C + "Search for the product")
                    print(O + "[ " + C + "*" + O + " ] " +
                          G + "Available" + W)
                    self.alarm()
                    self.device_details()
                    self.device_colors()
                    self.device_storage()

                    user_input = input(O + "[ " + C + "*" + O + " ] " + C +
                                       "Would you like to search again (Y/n) " + W)
                    if user_input.lower() == "y" or user_input == "":
                        self.checkAvailability(count - 1)
                    else:
                        logo()
                        break

        except:
            logo()
            print(O + "[ " + C + "*" + O + " ] " +
                      R + "Error                        ")
            system(
                "curl --request POST [App Link Here] &>/dev/null")

    def device_details(self):
        iphones = self.driver.find_element(
            by=By.XPATH, value='//*[@id="product-selector"]/fieldset[1]/ul')
        iphonesList = iphones.find_elements(
            by=By.TAG_NAME, value="li")
        for iphone in iphonesList:
            isAvailable = iphone.find_element(
                by=By.NAME, value='subfamily').is_enabled()
            if (isAvailable):
                iphone.click()
                text = iphone.text
                iphone_title = text.split("\n")[0]
                iphone_display_size = text.split("\n")[1]
                iphone_starting_price = text.split("\n")[2]
                print(G)
                print(O + "[ " + C + "*" + O + " ] " + C +
                      "Devices: ")
                print(O + "[ " + C + "*" + O + " ] " + C +
                      "Device: " + G + iphone_title + C + " Available")
                print(O + "[ " + C + "*" + O + " ] " + C +
                      "Display: " + G + iphone_display_size)
                print(O + "[ " + C + "*" + O + " ] " + C +
                      "Price: " + G + iphone_starting_price)
                print()
        return

    def device_colors(self):
        print(O + "[ " + C + "*" + O + " ] " + C +
              "Colors: ")
        colors = self.driver.find_element(
            by=By.XPATH, value='//*[@id="product-selector"]/fieldset[2]/ul')
        colorsList = colors.find_elements(
            by=By.TAG_NAME, value="li")
        for color in colorsList:
            isAvailable = color.find_element(
                by=By.NAME, value='color').is_enabled()
            if (isAvailable):
                color.click()
                text = color.text
                color_name = text.split("\n")[0]
                print(O + "[ " + C + "*" + O + " ] " + C +
                      "Color: " + G + color_name + C + " Available")
                print()
        return

    def device_storage(self):
        print(O + "[ " + C + "*" + O + " ] " + C +
              "Capacity: ")
        storage = self.driver.find_element(
            by=By.XPATH, value='//*[@id="product-selector"]/fieldset[3]/ul')
        storageList = storage.find_elements(
            by=By.TAG_NAME, value="li")
        for capacity in storageList:
            isAvailable = capacity.find_element(
                by=By.NAME, value='capacity').is_enabled()
            if (isAvailable):
                capacity.click()
                text = capacity.text
                capacity_name = text.split("\n")[0]
                capacity_price = text.split("\n")[1]
                print(O + "[ " + C + "*" + O + " ] " + C +
                      "Capacity: " + G + capacity_name + C + " Available")
                print(O + "[ " + C + "*" + O + " ] " + C +
                      "Capacity: " + G + capacity_price)
                print()
        return

    def login(self):
        print(O + "[ " + C + "*" + O + " ] " + C +
                                       "Navigating to login page" + W)
        href = self.driver.find_element(
            by=By.XPATH, value='//*[@id="ac-gn-bag"]/div/a').get_attribute("href")
        self.driver.get(href)
        sleep(2.5)
        href = self.driver.find_element(
            by=By.XPATH, value='//*[@id="bag-content"]/div/div[2]/div/div[1]/a').get_attribute("href")
        self.driver.get(href)
        input(O + "[ " + C + "*" + O + " ] " + C +
              "Press " + G + "[ENTER]" + C + " To Continue" + W)
        self.driver.get(self.url)
        return

    def alarm(self):
        chime.success()
        sleep(0.5)
        chime.success()
        sleep(0.5)
        chime.success()
        sleep(0.5)
        chime.success()
        sleep(0.5)
        return

    def send_notification(self, isAvailable):
        if (isAvailable):
            system(
                "curl --request POST [App Link Here] &>/dev/null")
        else:
            Notifier.notify('Start Searching', title='Iphone Reserver')
            system("curl --request POST [App Link Here] &>/dev/null")
        return


def logo():
    system("clear")
    print(R)
    print("""
            █████  ██████  ██████  ██      ███████                          
            ██   ██ ██   ██ ██   ██ ██      ██                               
            ███████ ██████  ██████  ██      █████                            
            ██   ██ ██      ██      ██      ██                               
            ██   ██ ██      ██      ███████ ███████                          
                                                                                               
██████  ███████ ███████ ███████ ██████  ██    ██ ███████ ██████  
██   ██ ██      ██      ██      ██   ██ ██    ██ ██      ██   ██ 
██████  █████   ███████ █████   ██████  ██    ██ █████   ██████  
██   ██ ██           ██ ██      ██   ██  ██  ██  ██      ██   ██ 
██   ██ ███████ ███████ ███████ ██   ██   ████   ███████ ██   ██ 
    """)
    print("")
    print("              Done By: " + C + "WarManX" + W)
    print("           https://github.com/WarManX")
    print("")


if __name__ == '__main__':
    Search_Iphone()
