from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 15)

driver.get("https://www.saucedemo.com/")

username = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "user-name")
    )
)

password = driver.find_element(
    By.ID,
    "password"
)

login = driver.find_element(
    By.ID,
    "login-button"
)

username.send_keys("standard_user")
password.send_keys("secret_sauce")

login.click()

print("TC08 - Login completed")

product = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "inventory_item")
    )
)

print("TC08 - Product results loaded successfully")

print("Product:")
print(product.text)

time.sleep(3)

input("Press Enter to close browser...")

driver.quit()