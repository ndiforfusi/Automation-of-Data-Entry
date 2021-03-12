# import the web driver and other packages 
from selenium import webdriver
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# tell the web driver to get an instance of Chrome
browser = webdriver.Chrome()

# grab the xpath of the elements  
url_name = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
url_email = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
url_comments = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea'
url_button = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span'

# upload the data 
data = pd.read_csv("info_data.csv")

# enter and submit data using a loop 
for i in range(len(data)):

    # let's get and open a url 
    browser.get("https://forms.gle/Expe7ApjJA6JRFEr7")

    # locate each element of interest, grab its data and enter the data
    name_input = browser.find_element_by_xpath(url_name)
    names = data["names"][i]
    name_input.send_keys(names)

    email_input = browser.find_element_by_xpath(url_email)
    email = data["email"][i]
    email_input.send_keys(email)

    comments_textarea = browser.find_element_by_xpath(url_comments)
    comments = data["comments"][i]
    comments_textarea.send_keys(comments)

    button_element = browser.find_element_by_xpath(url_button)
    time.sleep(3)
    
    # submit the form
    button_element.click()
    time.sleep(3)