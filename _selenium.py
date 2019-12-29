from selenium import webdriver
import time
driver_path = "/home/turkalp/Belgeler/python_calismalari/chromedriver"
driver = webdriver.Chrome(executable_path= driver_path)
usl = "http://github.com"
driver.get(usl)
time.sleep(2)
driver.maximize_window()
driver.save_screenshot("deneme.png")
print(driver.title)
time.sleep(2)
driver.close()