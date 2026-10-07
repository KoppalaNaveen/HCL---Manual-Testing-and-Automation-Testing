from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 15)

delay = 3

driver.get("https://www.saucedemo.com/")

print("\nTC01 - Shopping website opened")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

login.click()

print("TC01 - Login successful")

time.sleep(3)

driver.get("https://www.selenium.dev/selenium/web/alerts.html")

# Find test confirm link
links = driver.find_elements(
    By.TAG_NAME,
    "a"
)

for link in links:
    if "test confirm" in link.text.lower():
        link.click()
        break

alert = wait.until(
    EC.alert_is_present()
)

print("\nTC02 - Confirmation Alert:")
print(alert.text)

time.sleep(5)

alert.accept()

print("TC02 - Alert accepted successfully")

driver.get("https://www.selenium.dev/selenium/web/alerts.html")

links = driver.find_elements(
    By.TAG_NAME,
    "a"
)

for link in links:
    if "test confirm" in link.text.lower():
        link.click()
        break

alert = wait.until(
    EC.alert_is_present()
)

print("\nTC03 - Confirmation Alert:")
print(alert.text)

time.sleep(5)

alert.dismiss()

print("TC03 - Cancel selected successfully")

driver.get("https://www.selenium.dev/selenium/web/alerts.html")

links = driver.find_elements(
    By.TAG_NAME,
    "a"
)

for link in links:
    if "prompt happen" in link.text.lower():
        link.click()
        break

alert = wait.until(
    EC.alert_is_present()
)

print("\nTC04 - Prompt Alert:")
print(alert.text)

time.sleep(5)

alert.send_keys("Naveen")

print("TC04 - Value entered: Naveen")

alert.accept()

print("TC04 - Prompt submitted successfully")

driver.get(
    "https://www.selenium.dev/selenium/web/mouse_interaction.html"
)

time.sleep(2)

element = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "hover")
    )
)

ActionChains(driver).move_to_element(
    element
).perform()

time.sleep(3)

print("\nTC05 - Mouse Hover performed")

driver.get(
    "https://www.selenium.dev/selenium/web/mouse_interaction.html"
)

time.sleep(2)

element = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "clickable")
    )
)

ActionChains(driver).double_click(
    element
).perform()

time.sleep(3)

print("\nTC06 - Double Click performed")

driver.get(
    "https://www.selenium.dev/selenium/web/mouse_interaction.html"
)

time.sleep(2)

source = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "draggable")
    )
)

target = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "droppable")
    )
)

ActionChains(driver).drag_and_drop(
    source,
    target
).perform()

time.sleep(3)

print("\nTC07 - Drag and Drop performed")

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

print("\nTC08 - Login completed")

product = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "inventory_item")
    )
)

print("TC08 - Product results loaded successfully")

print("Product:")
print(product.text)

time.sleep(3)

add = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack")
    )
)

add.click()

print("\nTC09 - Product added to cart")

time.sleep(delay)
cart = wait.until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "shopping_cart_link")
    )
)

cart.click()

print("TC09 - Cart opened")

time.sleep(delay)
checkout = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "checkout")
    )
)

checkout.click()

print("TC09 - Checkout page opened")

time.sleep(2)

first_name = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "first-name")
    )
)

first_name.send_keys("Naveen")

driver.find_element(
    By.ID,
    "last-name"
).send_keys("Koppala")

driver.find_element(
    By.ID,
    "postal-code"
).send_keys("600001")

time.sleep(2)

driver.find_element(
    By.ID,
    "continue"
).click()

time.sleep(3)

place_order = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "finish")
    )
)

print("TC09 - Place Order button is clickable")

time.sleep(3)

place_order.click()

print("TC09 - Order submitted successfully")

time.sleep(3)

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

print("\nTC10 - Login completed")

time.sleep(3)

add = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack")
    )
)

add.click()

print("TC10 - Product added to cart")

time.sleep(delay)

cart = wait.until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "shopping_cart_link")
    )
)

cart.click()

print("TC10 - Cart opened")

time.sleep(delay)

checkout = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "checkout")
    )
)

checkout.click()

time.sleep(2)

first_name = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "first-name")
    )
)

first_name.send_keys("Naveen")

driver.find_element(
    By.ID,
    "last-name"
).send_keys("Koppala")

driver.find_element(
    By.ID,
    "postal-code"
).send_keys("600001")

time.sleep(2)

driver.find_element(
    By.ID,
    "continue"
).click()

time.sleep(3)

finish = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "finish")
    )
)

finish.click()

print("TC10 - Order completed")

time.sleep(3)

confirmation = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "complete-header")
    )
)

print("TC10 - Order confirmation page displayed")
print("Message:", confirmation.text)

time.sleep(3)

driver.execute_script("""
    setTimeout(function() {
        alert('Order confirmed successfully!');
    }, 500);
""")

alert = wait.until(
    EC.alert_is_present()
)

print("TC10 - Confirmation Alert:")
print(alert.text)

time.sleep(5)

alert.accept()

print("TC10 - Confirmation alert handled successfully")

print("\n====================================")
print("ALL 10 TEST CASES COMPLETED")
print("====================================")

input("\nPress Enter to close browser...")

driver.quit()