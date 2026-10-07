from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

url = "https://www.selenium.dev/selenium/web/alerts.html#"


# ==================================================
# FUNCTION TO FIND LINK
# ==================================================

def click_link(text):

    link = driver.execute_script("""
        var links = document.getElementsByTagName('a');

        for (var i = 0; i < links.length; i++) {

            var t = links[i].textContent.trim();

            if (t.includes(arguments[0])) {
                return links[i];
            }
        }

        return null;
    """, text)

    if link is None:
        raise Exception("Link not found: " + text)

    driver.execute_script(
        "arguments[0].click();",
        link
    )


# ==================================================
# 1. SIMPLE ALERT - FIRST
# ==================================================

driver.get(url)

click_link("click me")

alert = wait.until(
    EC.alert_is_present()
)

print("1. Simple Alert:")
print(alert.text)

time.sleep(5)

alert.accept()


# ==================================================
# 2. SIMPLE ALERT - SECOND
# ==================================================

driver.get(url)

links = driver.find_elements(
    By.XPATH,
    "//a[contains(., 'click me')]"
)

driver.execute_script(
    "arguments[0].click();",
    links[1]
)

alert = wait.until(
    EC.alert_is_present()
)

print("\n2. Second Simple Alert:")
print(alert.text)

time.sleep(5)

alert.accept()


# ==================================================
# 3. PROMPT
# ==================================================

driver.get(url)

click_link("prompt happen")

alert = wait.until(
    EC.alert_is_present()
)

print("\n3. Prompt Alert:")
print(alert.text)

time.sleep(5)

alert.send_keys("Python")

alert.accept()


# ==================================================
# 4. PROMPT WITH DEFAULT
# ==================================================

driver.get(url)

click_link("prompt with default happen")

alert = wait.until(
    EC.alert_is_present()
)

print("\n4. Prompt With Default:")
print(alert.text)

time.sleep(5)

alert.send_keys("Selenium")

alert.accept()


# ==================================================
# 5. TWO PROMPTS
# ==================================================

driver.get(url)

click_link("prompts happen")


# First prompt
alert = wait.until(
    EC.alert_is_present()
)

print("\n5. First Prompt:")
print(alert.text)

time.sleep(5)

alert.send_keys("First")

alert.accept()


# Second prompt
alert = wait.until(
    EC.alert_is_present()
)

print("5. Second Prompt:")
print(alert.text)

time.sleep(5)

alert.send_keys("Second")

alert.accept()


# ==================================================
# 6. SLOW ALERT
# ==================================================

driver.get(url)

click_link("SLOW")

alert = wait.until(
    EC.alert_is_present()
)

print("\n6. Slow Alert:")
print(alert.text)

time.sleep(5)

alert.accept()


# ==================================================
# 7. CONFIRMATION - ACCEPT
# ==================================================

driver.get(url)

click_link("test confirm")

alert = wait.until(
    EC.alert_is_present()
)

print("\n7. Confirmation Alert:")
print(alert.text)

time.sleep(5)

alert.accept()


# ==================================================
# 8. CONFIRMATION - DISMISS
# ==================================================

driver.get(url)

click_link("test confirm")

alert = wait.until(
    EC.alert_is_present()
)

print("\n8. Confirmation Alert:")
print(alert.text)

time.sleep(5)

alert.dismiss()


# ==================================================
# FINISHED
# ==================================================

print("\n====================================")
print("ALL DIRECT ALERTS TESTED")
print("====================================")


input("\nPress Enter to close browser...")

driver.quit()