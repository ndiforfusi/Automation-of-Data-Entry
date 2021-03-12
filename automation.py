# import the web driver 
from selenium import webdriver
# tell the web driver to get an instance of chrome 
browser = webdriver.Chrome()

# let's get and open a url 
browser.get("https://nebanfonsang.com/contact-form/")

# get the name, email and message element from the form
name_input = browser.find_element_by_css_selector('input[id="nf-field-9"]')
email_input = browser.find_element_by_css_selector('input[id="nf-field-10"]')
message_input = browser.find_element_by_css_selector('textarea[id="nf-field-11"]')
button_element = browser.find_element_by_css_selector('input[id="nf-field-12"]')

# enter the input values 
name_input.send_keys("John Williams")
email_input.send_keys("john.williaams@company.com")
message_input.send_keys("Hello, this is John, I want to learn coding")
# submit the form 
button_element = browser.find_element_by_css_selector('input[id="nf-field-12"]')
button_element.click() 
