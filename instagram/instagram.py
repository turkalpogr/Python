from instagramInfo import email,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Instagram:
    def __init__(self, email, password):
        driver_path = "/home/turkalp/Belgeler/python_calismalari/chromedriver"
        self.browser = webdriver.Chrome(executable_path= driver_path)
        self.email = email
        self.password = password
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        emailelement = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
        passelement = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")

        emailelement.send_keys(self.email)
        passelement.send_keys(self.password)
        passelement.send_keys(Keys.ENTER)
        time.sleep(2)

ins = Instagram(email,password)
ins.signIn()