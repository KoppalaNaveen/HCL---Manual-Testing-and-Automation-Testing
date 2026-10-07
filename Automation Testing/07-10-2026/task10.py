from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 15)

driver.get("https://www.saucedemo.com/")

username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

password = driver.find_element(By.ID,"password")

login = driver.find_element(By.ID,"login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

login.click()

print("TC10 - Login completed")

time.sleep(3)

add = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))

add.click()

print("TC10 - Product added to cart")

time.sleep(3)

cart = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
cart.click()
print("TC10 - Cart opened")
time.sleep(3)


checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
checkout.click()
time.sleep(2)

first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
first_name.send_keys("Naveen")
driver.find_element(By.ID,"last-name").send_keys("Koppala")
driver.find_element(By.ID,"postal-code").send_keys("600001")
time.sleep(2)

driver.find_element(By.ID,"continue").click()

time.sleep(3)

finish = wait.until(EC.element_to_be_clickable((By.ID, "finish")))

finish.click()

print("TC10 - Order completed")

time.sleep(3)

confirmation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))

print("TC10 - Order confirmation page displayed")
print("Message:", confirmation.text)

time.sleep(3)

driver.execute_script("""setTimeout(function() {alert('Order confirmed successfully!');}, 500);""")

alert = wait.until(EC.alert_is_present())

print("TC10 - Confirmation Alert:")
print(alert.text)
time.sleep(5)
alert.accept()
print("TC10 - Confirmation alert handled successfully")
input("Press Enter to close browser...")
driver.quit()