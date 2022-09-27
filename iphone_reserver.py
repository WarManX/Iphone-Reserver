import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import *

import chime
from os import system
import signal
from time import sleep
from colors import *
from selenium import webdriver as uc
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import pyttsx3

text_speech = pyttsx3.init()

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")


def signal_handler(signal, frame):
    logo()
    print(O + "[" + C + "*" + O + "] " +
          C + "Thank you" + W)
    exit()


signal.signal(signal.SIGINT, signal_handler)


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


logo()


class SelectionWindow(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("IPhone Reserver")
        self.geometry(f"{SelectionWindow.WIDTH}x{SelectionWindow.HEIGHT}")
        self.minsize(SelectionWindow.WIDTH, SelectionWindow.HEIGHT)
        self.maxsize(SelectionWindow.WIDTH, SelectionWindow.HEIGHT)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ============ create two frames ============
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        self.devices_var = tkinter.IntVar(value=0)
        self.colors_var = tkinter.IntVar(value=0)

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(4, weight=1)
        self.frame_left.grid_rowconfigure(9, weight=1)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        # ============ Devices ============

        self.devices_label = customtkinter.CTkLabel(master=self.frame_left,
                                                    text="Devices",
                                                    text_font=("Roboto Medium", -16), anchor='w')  # font name and size in px
        self.devices_label.grid(row=1, column=0, pady=10, padx=10)

        self.iphone14_pro_radio = customtkinter.CTkRadioButton(master=self.frame_left,
                                                               variable=self.devices_var,
                                                               value=0, text="Iphone 14 Pro")
        self.iphone14_pro_radio.grid(
            row=2, column=0, pady=10, padx=10, sticky="nw")

        self.iphone14_pro_max_radio = customtkinter.CTkRadioButton(master=self.frame_left,
                                                                   variable=self.devices_var,
                                                                   value=1, text="Iphone 14 Pro Max")

        self.iphone14_pro_max_radio.grid(
            row=3, column=0, pady=10, padx=10, sticky="nw")

        # ============ Colors ============

        self.colors_label = customtkinter.CTkLabel(master=self.frame_left,
                                                   text="Colors",
                                                   text_font=("Roboto Medium", -16), anchor='w')  # font name and size in px
        self.colors_label.grid(row=5, column=0, pady=10, padx=10)

        self.deep_purple_radio = customtkinter.CTkRadioButton(master=self.frame_left,
                                                              variable=self.colors_var,
                                                              value=0, text="Deep Purple")
        self.deep_purple_radio.grid(
            row=6, column=0, pady=10, padx=10, sticky="nw")

        self.space_black_radio = customtkinter.CTkRadioButton(master=self.frame_left,
                                                              variable=self.colors_var,
                                                              value=1, text="Space Black")
        self.space_black_radio.grid(
            row=7, column=0, pady=10, padx=10, sticky="nw")

        self.silver_radio = customtkinter.CTkRadioButton(master=self.frame_left,
                                                         variable=self.colors_var,
                                                         value=2, text="Silver")
        self.silver_radio.grid(
            row=8, column=0, pady=10, padx=10, sticky="nw")

        self.gold_radio = customtkinter.CTkRadioButton(master=self.frame_left,
                                                       variable=self.colors_var,
                                                       value=3, text="Gold")
        self.gold_radio.grid(
            row=9, column=0, pady=10, padx=10, sticky="nw")

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2,
                             rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Iphone Reserver allows users to\n" +
                                                        "get the specific iphone they want it\n" +
                                                        "or to reserve it, the users can get\n" +
                                                        "notification by adding Webhook URL\n" +
                                                        "and download Pushcut app from app store",
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   # <- custom tuple-color
                                                   fg_color=(
                                                       "white", "gray38"),
                                                   justify=tkinter.CENTER)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.frame_info_label = customtkinter.CTkLabel(master=self.frame_info,
                                                       text="Details",
                                                       text_font=("Roboto Medium", -16), anchor='w')  # font name and size in px
        self.frame_info_label.grid(
            row=1, column=0, pady=10, padx=5, sticky="nw",)

        self.device_frame_info_label = customtkinter.CTkLabel(master=self.frame_info,
                                                              text="Device: ",
                                                              text_font=("Roboto Medium", -16), anchor='w')  # font name and size in px
        self.device_frame_info_label.grid(
            row=2, column=0, pady=0, padx=5, sticky="nw",)

        self.color_frame_info_label = customtkinter.CTkLabel(master=self.frame_info,
                                                             text="Color: ",
                                                             text_font=("Roboto Medium", -16), anchor='w')  # font name and size in px
        self.color_frame_info_label.grid(
            row=3, column=0, pady=0, padx=5, sticky="nw",)

        self.storage_frame_info_label = customtkinter.CTkLabel(master=self.frame_info,
                                                               text="Storage: ",
                                                               text_font=("Roboto Medium", -16), anchor='w')  # font name and size in px
        self.storage_frame_info_label.grid(
            row=4, column=0, pady=0, padx=5, sticky="nw",)

        SelectionWindow.status_frame_info_label = customtkinter.CTkLabel(master=self.frame_info,
                                                                         text="Status",
                                                                         text_font=("Roboto Medium", -16), anchor='w')  # font name and size in px
        SelectionWindow.status_frame_info_label.grid(
            row=5, column=0, pady=20, padx=5, sticky="nw",)

        SelectionWindow.counting_lable = customtkinter.CTkLabel(master=self.frame_info,
                                                                text="",
                                                                text_font=("Roboto Medium", -16), anchor='w')  # font name and size in px
        SelectionWindow.counting_lable.grid(
            row=6, column=0, pady=5, padx=5, sticky="nw",)

        # ============ Storage ============

        self.storage_var = tkinter.IntVar(value=0)

        self.storage_label = customtkinter.CTkLabel(master=self.frame_right,
                                                    text="Storage",
                                                    text_font=("Roboto Medium", -16), anchor='w')  # font name and size in px
        self.storage_label.grid(row=0, column=2, pady=0, padx=0)

        self.gb128_radio = customtkinter.CTkRadioButton(master=self.frame_right,
                                                        variable=self.storage_var,
                                                        value=0, text="128GB")
        self.gb128_radio.grid(
            row=1, column=2, pady=0, padx=0, sticky="nw")

        self.gb256_radio = customtkinter.CTkRadioButton(master=self.frame_right,
                                                        variable=self.storage_var,
                                                        value=1, text="256GB")
        self.gb256_radio.grid(
            row=2, column=2, pady=0, padx=0, sticky="nw")

        self.gb512_radio = customtkinter.CTkRadioButton(master=self.frame_right,
                                                        variable=self.storage_var,
                                                        value=2, text="512GB")
        self.gb512_radio.grid(
            row=3, column=2, pady=0, padx=0, sticky="nw")

        self.tb1_radio = customtkinter.CTkRadioButton(master=self.frame_right,
                                                      variable=self.storage_var,
                                                      value=3, text="1TB")
        self.tb1_radio.grid(
            row=4, column=2, pady=0, padx=0, sticky="nw")

        # ============ End Storage ============

        SelectionWindow.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                           text="Start",
                                                           command=self.button_event)
        SelectionWindow.button_5.grid(row=8, column=2, columnspan=1,
                                      pady=20, padx=20, sticky="we")

        SelectionWindow.webhook_url = customtkinter.CTkEntry(master=self.frame_right,
                                                             width=120,
                                                             placeholder_text="Webhook URL")
        SelectionWindow.webhook_url.grid(row=8, column=0, columnspan=2,
                                         pady=20, padx=20, sticky="we")

        # set default values
        self.iphone14_pro_radio.select()
        self.deep_purple_radio.select()
        self.gb128_radio.select()
        self.switch_2.select()
        SelectionWindow.selected_device = "Iphone 14 Pro"
        SelectionWindow.selected_color = "Deep Purple"
        SelectionWindow.selected_storage = "128GB2"

    def button_event(self):

        # ============ Device ============
        if (self.devices_var.get() == 0):
            SelectionWindow.selected_device = "Iphone 14 Pro"
        elif (self.devices_var.get() == 1):
            SelectionWindow.selected_device = "Iphone 14 Pro Max"

        # ============ Colors ============
        if (self.colors_var.get() == 0):
            SelectionWindow.selected_color = "Deep Purple"
        elif (self.colors_var.get() == 1):
            SelectionWindow.selected_color = "Space Black"
        elif (self.colors_var.get() == 2):
            SelectionWindow.selected_color = "Silver"
        elif (self.colors_var.get() == 3):
            SelectionWindow.selected_color = "Gold"

        # ============ Storage ============
        if (self.storage_var.get() == 0):
            SelectionWindow.selected_storage = "128GB2"
        elif (self.storage_var.get() == 1):
            SelectionWindow.selected_storage = "256GB2"
        elif (self.storage_var.get() == 2):
            SelectionWindow.selected_storage = "512GB2"
        elif (self.storage_var.get() == 3):
            SelectionWindow.selected_storage = "1TB2"

        self.device_frame_info_label.configure(
            text="Device: " + SelectionWindow.selected_device)
        self.color_frame_info_label.configure(
            text="Color: " + SelectionWindow.selected_color)
        self.storage_frame_info_label.configure(
            text="Storage: " + SelectionWindow.selected_storage)
        self.start_search()

    def start_search(self):
        s = AppleSearch()
        s.start()

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        ProviderSelect.button_5.configure(state=NORMAL)
        self.destroy()

    def start(self):
        self.mainloop()


class ProviderSelect(customtkinter.CTk):

    WIDTH = 200
    HEIGHT = 250

    def __init__(self):
        super().__init__()

        self.title("IPhone Reserver")
        self.geometry(f"{ProviderSelect.WIDTH}x{ProviderSelect.HEIGHT}")
        self.minsize(ProviderSelect.WIDTH, ProviderSelect.HEIGHT)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        ProviderSelect.devices_var = tkinter.IntVar(value=0)

        self.devices_label = customtkinter.CTkLabel(master=self,
                                                    text="Select Website",
                                                    text_font=("Roboto Medium", -16), anchor='w')  # font name and size in px
        self.devices_label.grid(row=1, column=0, pady=10, padx=10)

        self.apple = customtkinter.CTkRadioButton(master=self,
                                                  variable=ProviderSelect.devices_var,
                                                  value=0, text="Apple")
        self.apple.grid(
            row=2, column=0, pady=10, padx=10, sticky="nw")

        self.etisalat = customtkinter.CTkRadioButton(master=self,
                                                     variable=ProviderSelect.devices_var,
                                                     value=1, text="Etisalat")

        self.etisalat.grid(
            row=3, column=0, pady=10, padx=10, sticky="nw")

        self.du = customtkinter.CTkRadioButton(master=self,
                                               variable=ProviderSelect.devices_var,
                                               value=2, text="Du")

        self.du.grid(
            row=4, column=0, pady=10, padx=10, sticky="nw")

        ProviderSelect.button_5 = customtkinter.CTkButton(master=self,
                                                          text="Continue",
                                                          command=self.button_event)
        ProviderSelect.button_5.grid(row=6, column=0, columnspan=1,
                                     pady=20, padx=20)

        self.du.configure(state=DISABLED)
        self.etisalat.configure(state=DISABLED)

    def button_event(self):
        ProviderSelect.button_5.configure(state=DISABLED)
        SelectionWindow()

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


class AppleSearch():
    def start(self):
        self.driver = uc.Chrome(service=Service(
            ChromeDriverManager().install()))
        self.url = 'https://reserve-prime.apple.com/AE/en_AE/reserve/A/availability?iUP=N'
        self.driver.get(self.url)
        self.driver.maximize_window()

        chime.info()

        AppleSearch.count = 0

        self.checkAvailability()

    def checkAvailability(self):
        AppleSearch.count = AppleSearch.count + 1
        try:
            for AppleSearch.count in range(100000):
                try:
                    notAvailableText = self.driver.find_element(
                        by=By.XPATH, value='/html/body/main/div/section/div/div/div/h1').text
                except:
                    notAvailableText = "Available"

                if (notAvailableText == "We’re not taking reservations to buy iPhone in the store right now."):
                    print(O + "[" + C, AppleSearch.count, O + "] " +
                          R + "Not Available", end="\r")
                    self.driver.refresh()
                    sleep(1.5)
                elif (notAvailableText == "Available"):
                    chime.success()
                    self.send_notification()
                    self.alarm()
                    self.device_details()
                    self.scrolldown()
                    self.device_colors()
                    self.device_storage()
                    SelectionWindow.button_5.configure(text="Continue")
                    SelectionWindow.status_frame_info_label.configure(
                        foreground='green', text="Found!")
                    text = "Done", AppleSearch.count, "Search"
                    SelectionWindow.counting_lable.configure(
                        text=text)
                    break

        except:

            print(O + "[ " + C + "*" + O + " ] " +
                      R + "Browser Closed                        ")

    def device_details(self):
        iphones = self.driver.find_element(
            by=By.XPATH, value='//*[@id="product-selector"]/fieldset[1]/ul')
        iphonesList = iphones.find_elements(
            by=By.TAG_NAME, value="li")
        for iphone in iphonesList:
            isAvailable = iphone.find_element(
                by=By.NAME, value='subfamily').is_enabled()
            if (isAvailable):
                text = iphone.text
                iphone_title = text.split("\n")[0]
                try:
                    if iphone_title == SelectionWindow.selected_device:
                        chime.success()
                        text_speech.say(SelectionWindow.selected_device)
                        text_speech.runAndWait()
                        iphone.click()
                except:
                    return
                print()
        return

    def device_colors(self):
        colors = self.driver.find_element(
            by=By.XPATH, value='//*[@id="product-selector"]/fieldset[2]/ul')
        colorsList = colors.find_elements(
            by=By.TAG_NAME, value="li")
        for color in colorsList:
            isAvailable = color.find_element(
                by=By.NAME, value='color').is_enabled()
            if (isAvailable):
                text = color.text
                color_name = text.split("\n")[0]
                try:
                    if color_name == SelectionWindow.selected_color:
                        chime.success()
                        color.click()
                except:
                    return
                print()
        return

    def device_storage(self):
        storage = self.driver.find_element(
            by=By.XPATH, value='//*[@id="product-selector"]/fieldset[3]/ul')
        storageList = storage.find_elements(
            by=By.TAG_NAME, value="li")
        for capacity in storageList:
            isAvailable = capacity.find_element(
                by=By.NAME, value='capacity').is_enabled()
            if (isAvailable):
                text = capacity.text
                capacity_name = text.split("\n")[0]
                try:
                    if capacity_name == SelectionWindow.selected_storage:
                        chime.success()
                        capacity.click()
                except:
                    return
                print()
        return

    def alarm(self):
        chime.success()
        return

    def send_notification(self):
        if (SelectionWindow.webhook_url.get() != ""):
            system(
                "curl --request POST " + SelectionWindow.webhook_url.get() + " &>/dev/null")
        return

    def scrolldown(self):
        self.driver.execute_script("window.scrollBy(0,500)", "")
        return


if __name__ == "__main__":
    app = ProviderSelect()
    app.start()
