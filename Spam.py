from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome("./webdrivers/chromedriver.exe")
browser.get("https://web.whatsapp.com/")

wait = WebDriverWait(browser,600)
target  = '\''+ input("Enter Target Name: ") +'\''

string = input("Message to be sent:")

x_arg = '//span[contains(@title, ' + target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH,x_arg)))
target.click()

input_box = browser.find_element_by_class_name("_1Plpp")


No = int(input("No. of Messages to be Sent:"))

for i in range(No):
    input_box.send_keys(string + Keys.ENTER)
    os.system("cls")
    print("Messages sent:",i+1,'/',No)
