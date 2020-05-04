from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://google.com")

element = driver.find_element_by_name("q")
element.send_keys("reinforcement learning")
element.submit()
time.sleep(3)

print(driver.title)

driver.quit()