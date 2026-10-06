from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://vinothqaacademy.com/demo-site/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    print("Website opened")

    print("Filling First Name...")

    first_name = wait.until(
        EC.presence_of_element_located((By.ID, "vfb-5"))
    )

    first_name.clear()
    first_name.send_keys("Naveen")

    print("Filling Last Name...")

    last_name = wait.until(
        EC.presence_of_element_located((By.ID, "vfb-7"))
    )

    last_name.clear()
    last_name.send_keys("Koppala")

    print("Selecting Gender...")

    gender = wait.until(
        EC.presence_of_all_elements_located(
            (
                By.CSS_SELECTOR,
                "#item-vfb-31 input[type='radio']"
            )
        )
    )

    gender[0].click()

    print("Selecting Selenium WebDriver...")

    course = wait.until(
        EC.presence_of_all_elements_located(
            (
                By.CSS_SELECTOR,
                "#item-vfb-20 input[type='checkbox']"
            )
        )
    )

    if not course[0].is_selected():
        course[0].click()

    print("Filling Address...")

    address = wait.until(
        EC.presence_of_all_elements_located(
            (
                By.CSS_SELECTOR,
                "#item-vfb-13 input"
            )
        )
    )

    print("Address fields found:", len(address))

    address[0].send_keys("123 Main Street")
    address[1].send_keys("Apt 101")
    address[2].send_keys("Chennai")
    address[3].send_keys("Tamil Nadu")
    address[4].send_keys("600001")

    print("Selecting Country...")

    country = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "#item-vfb-13 select"
            )
        )
    )

    Select(country).select_by_visible_text("India")

    print("Filling Email...")

    email = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "#item-vfb-14 input"
            )
        )
    )

    email.send_keys("naveen@example.com")

    print("Filling Date...")

    date = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "#item-vfb-18 input"
            )
        )
    )

    date.send_keys("10/10/26")

    print("Selecting Time...")

    time_select = wait.until(
        EC.presence_of_all_elements_located(
            (
                By.CSS_SELECTOR,
                "#item-vfb-16 select"
            )
        )
    )

    print("Time dropdowns found:", len(time_select))

    Select(time_select[0]).select_by_visible_text("10")

    time_select = wait.until(
        EC.presence_of_all_elements_located(
            (
                By.CSS_SELECTOR,
                "#item-vfb-16 select"
            )
        )
    )

    Select(time_select[1]).select_by_visible_text("30")

    print("Filling Mobile Number...")

    mobile = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "#item-vfb-19 input"
            )
        )
    )

    mobile.send_keys("9876543210")

    print("Filling Query...")

    query = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "#registration-1 textarea"
            )
        )
    )

    query.send_keys(
        "I am learning Selenium WebDriver automation testing."
    )

    print("Filling Verification...")

    verification = wait.until(
        EC.presence_of_element_located(
            (By.ID, "vfb-3")
        )
    )

    verification.clear()
    verification.send_keys("33")

    print("Clicking Submit...")

    submit = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "vfb-4")
        )
    )

    submit.click()

    print()
    print("========================================")
    print("ALL DATA FILLED SUCCESSFULLY!")
    print("Verification : 33")
    print("Submit       : Clicked")
    print("========================================")

except Exception as e:

    print()
    print("========================================")
    print("ERROR OCCURRED")
    print("========================================")
    print("Error Type:", type(e).__name__)
    print("Error:", e)
    print("========================================")


finally:

    input("Press Enter to close the browser........")

    driver.quit()