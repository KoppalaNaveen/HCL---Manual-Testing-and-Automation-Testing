from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 15)

driver.get("https://www.selenium.dev/selenium/web/alerts.html")

links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    if "prompt happen" in link.text.lower():
        link.click()
        break

alert = wait.until(
    EC.alert_is_present()
)

print("TC04 - Prompt Alert:")
print(alert.text)

time.sleep(5)

alert.send_keys("Naveen")

print("TC04 - Value entered: Naveen")

alert.accept()

print("TC04 - Prompt submitted successfully")

input("Press Enter to close browser...")

driver.quit()