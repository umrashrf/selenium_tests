import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import TimeoutException

def wait_and_click(driver, xpath):
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath))
    )
    elems = driver.find_elements(By.XPATH, xpath)
    if len(elems) > 0:
        elems[0].click()


options = Options()
options.add_argument(
    "user-data-dir=/Users/umairashraf/Library/Application Support/Google/Chrome/Default"
)
driver = webdriver.Chrome(
    executable_path="/Users/umairashraf/Develop/selenium_tests/chromedriver",
    chrome_options=options,
)

stop = False

while not stop:
    try:
        driver.get(
            "https://ceda.datatrium.com/fmi/webd/CEDA?homeurl=https://cedamtl.org/francisation-au-quebec/"
        )
        xpath1 = "//div[@role='dialog']"
        WebDriverWait(driver, 60 * 10).until(
            EC.presence_of_element_located((By.XPATH, xpath1))
        )
        elems = driver.find_elements(By.XPATH, xpath1)
        if len(elems) > 0:
            wait_and_click(driver, "//span[@class='v-button-caption']")
            wait_and_click(driver, "//div[text()='Francisation']")
            time.sleep(2)
        else:
            stop = True
    except TimeoutException as timeout_exc:
        pass
    except:
        driver.close()
        os.system('say "Uh oh"')
        raise

for i in range(50):
    os.system('say "It\'s Ready!"')
    time.sleep(2)
