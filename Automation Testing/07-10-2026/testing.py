from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Alerts.html#google_vignette")
driver.maximize_window()
wait = WebDriverWait(driver, 15)


driver.execute_script('alert("Welcome to the Sauce Demo Website!");')
time.sleep(3)

alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()
print("Alert accepted successfully.")
time.sleep(3)

name = driver.find_element(By.ID, "user-name")
name.send_keys("standard_user")
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
login = driver.find_element(By.ID, "login-button")
login.click()

item = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
item.click()
driver.execute_script('alert("Item added to cart!");')
time.sleep(3)

alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()
print("Alert accepted successfully.")
time.sleep(3)

# Add item to cart
shopping_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
shopping_cart.click()
driver.execute_script('alert("You are now in the shopping cart!");')
time.sleep(3)
alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()
print("Alert accepted successfully.")
time.sleep(3)

# Remove button
remove = wait.until(EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack")))
driver.execute_script("confirm('Do you want to remove this item?');")
alert = wait.until(EC.alert_is_present())
print("Alert Text:", alert.text)
time.sleep(3)
alert.accept()
print("Alert accepted successfully.")
time.sleep(3)
remove.click()
print("Item removed from cart.")
time.sleep(3)


input("Press Enter to continue...")
driver.quit()