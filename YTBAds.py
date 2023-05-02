from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

# Use ChromeDriverManager to automatically download and install the latest ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
web_url = "https://youtube.com/"
driver.get(web_url)

wait = ui.WebDriverWait(driver, 300)

while True:
    try:
        if EC.presence_of_all_elements_located((By.XPATH, ".//div/div/div/div/div/span/button/div[contains(text(),'skip Ad')]")):
            button = driver.find_element(By.XPATH, ".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")
            driver.execute_script("arguments[0].click();", button)
            print("Ad Skipped")
            time.sleep(2)
        else:
            continue
    except NoSuchElementException:
        print("waiting...")
        time.sleep(3)
