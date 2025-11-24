from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.google.com")

    # Handle cookie consent popup if it appears
    try:
        consent = wait.until(EC.element_to_be_clickable((By.XPATH, "//button//div[contains(text(), 'Accept')]")))
        consent.click()
    except:
        pass

    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys("SDET jobs" + Keys.RETURN)

    # Wait for results to load
    results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div#search div")))
    
    assert len(results) > 0

    driver.quit()
