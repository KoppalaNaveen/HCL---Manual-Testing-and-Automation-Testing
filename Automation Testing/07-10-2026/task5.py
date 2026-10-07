from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 15)

driver.get(
    "https://www.selenium.dev/selenium/web/mouse_interaction.html"
)

element = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "hover")
    )
)

ActionChains(driver).move_to_element(
    element
).perform()

time.sleep(3)

print("TC05 - Mouse Hover performed")

input("Press Enter to close browser...")

driver.quit()