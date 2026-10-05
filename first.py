from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://accounts.saveetha.in/login/?next=/authorize/%3Fresponse_type%3Dcode%26client_id%3Ds8kDBbZEETxhItUhIVMlWFsfK3RsM4qlroZ7eeOl%26redirect_uri%3Dhttps%253A//learner.saveetha.in/sso/callback/%26scope%3Dopenid%2520profile%2520email%2520offline_access%2520groups%26state%3D6cfJZkA-boxd65qAThCgGw%26nonce%3Dlxv-DazNHO4LNtE-kYpY3w%26code_challenge%3DV5zQ0yd_EAAvVB5mNLXQ628hzhJ9x49Xcb_u5xiAPE4%26code_challenge_method%3DS256")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.NAME, "password")
login = driver.find_element(By.ID, "login-button")

username.send_keys("23009240")
password.send_keys("s")

print(username.get_attribute("placeholder"))
print(login.is_enabled())
print(username.is_displayed())

login.click()
driver.quit()