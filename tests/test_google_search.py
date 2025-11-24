from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_duckduckgo_search():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://duckduckgo.com/")

    search_box = wait.until(EC.presence_of_element_located((By.ID, "search_form_input_homepage")))
    search_box.send_keys("SDET jobs" + Keys.RETURN)

    results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#links .result")))
    assert len(results) > 0, "No search results found!"

    driver.quit()
