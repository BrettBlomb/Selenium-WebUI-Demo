from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_google_search():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Required for CI
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("SDET jobs")
    search_box.submit()

    results = driver.find_elements(By.CSS_SELECTOR, "div.g")
    assert len(results) > 0

    driver.quit()
