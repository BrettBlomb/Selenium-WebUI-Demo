from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_flow():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/login")

    # Enter login credentials
    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("SuperSecretPassword!")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.radius"))).click()

    # Validate login success
    message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    assert "You logged into a secure area!" in message.text

    driver.quit()
