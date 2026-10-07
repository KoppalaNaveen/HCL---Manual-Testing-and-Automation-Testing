from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

driver.get("https://www.amazon.in")

driver.maximize_window()

print("Amazon opened")

signin = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "nav-link-accountList")
    )
)

signin.click()

email = "koppalanaveen20@gmail.com"

email_box = wait.until(
    EC.presence_of_element_located(
        (By.ID, "ap_email_login")
    )
)

email_box.send_keys(email)

email_box.send_keys(Keys.ENTER)

print("Email entered")

print("Complete password / OTP manually in browser")

input("After login is completed, press Enter...")

driver.switch_to.new_window("tab")

driver.get("https://www.amazon.in")

print("Search tab opened")

search = wait.until(
    EC.presence_of_element_located(
        (By.ID, "twotabsearchtextbox")
    )
)

product = "ASUS TUF Gaming laptop"

search.send_keys(product)

search.send_keys(Keys.ENTER)

print("ASUS TUF Gaming laptop searched")

time.sleep(7)

print("Finding first search result...")

first_product = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "(//h2[@aria-label])[1]"
        )
    )
)

product_name = first_product.get_attribute(
    "aria-label"
)

print("First product found:")
print(product_name)

print("Finding Add to Cart button...")

add_cart = driver.execute_script("""
    
    var title = arguments[0];

    var parent = title;

    for (var i = 0; i < 12; i++) {

        if (!parent) {
            break;
        }

        var elements = parent.querySelectorAll(
            "button, input, a"
        );

        for (var j = 0; j < elements.length; j++) {

            var el = elements[j];

            var text = (
                el.innerText ||
                el.value ||
                el.getAttribute("aria-label") ||
                ""
            ).toLowerCase();

            if (text.includes("add to cart")) {

                return el;
            }
        }

        parent = parent.parentElement;
    }

    return null;

""", first_product)

if add_cart:

    print("Add to Cart button found")

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        add_cart
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        add_cart
    )

    print("SEARCHED PRODUCT ADDED TO CART")

else:

    print("Add to Cart button not found")

    input("Press Enter to close browser...")

    driver.quit()

    exit()

time.sleep(5)

print("Cart updated")

driver.switch_to.new_window("tab")

driver.get(
    "https://www.amazon.in/gp/cart/view.html"
)

print("Cart tab opened")

time.sleep(5)

print("Cart opened successfully")

input("Press Enter to close browser...")

driver.quit()