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
    if "test confirm" in link.text.lower():
        link.click()
        break

alert = wait.until(
    EC.alert_is_present()
)

print("TC03 - Confirmation Alert:")
print(alert.text)

time.sleep(5)

alert.dismiss()

print("TC03 - Cancel selected successfully")

input("Press Enter to close browser...")

driver.quit()