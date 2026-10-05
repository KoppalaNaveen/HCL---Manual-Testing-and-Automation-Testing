from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

driver.get("https://www.flipkart.com/login?ret=/")

mobile = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[type='number']")
    )
)

mobile.send_keys("9876543210")

continue_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Continue']")
    )
)

continue_btn.click()


otp = input("Enter verification code: ")


otp_box = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@type='number']")
    )
)

otp_box.send_keys(otp)


verify_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,
         "//button[contains(.,'Verify') or contains(.,'Login') or contains(.,'Continue')]")
    )
)

verify_btn.click()

input("Press Enter to close the browser...")

driver.quit()