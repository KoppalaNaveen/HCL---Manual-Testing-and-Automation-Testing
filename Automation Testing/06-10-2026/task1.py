from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com/")

driver.maximize_window()

driver.get("https://www.selenium.dev/")

driver.refresh()
driver.back()
driver.forward()
driver.quit()