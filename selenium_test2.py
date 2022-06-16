from selenium_test import get_daily_news
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time


def get_realtime_news(driver):
    url = "https://mops.twse.com.tw/mops/web/t05sr01_1"
    driver.get(url)
    wait = WebDriverWait(driver, 10)  # 讓DRIVER等待的物件
    original_window = driver.current_window_handle
    for i, button in enumerate(driver.find_elements(By.XPATH, "//input[@value='詳細資料']")):
        button.click()
        wait.until(EC.presence_of_element_located((By.ID, "table01")))
        driver.switch_to.window(driver.window_handles[1])  # switch to new window
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))
        time.sleep(1)
        entire = driver.find_element(By.TAG_NAME, "body")
        # driver.save_screenshot("test.png")  # save the window view
        entire.screenshot(f"{i}.png")  # save the entire body view
        driver.close()  # close the new window
        driver.switch_to.window(original_window)
        print("======")
        # print(driver.window_handles)
        if i >= 10:
            break


if __name__ == "__main__":
    service = Service(executable_path="/Users/lzrong/PycharmProjects/20220616crawling/geckodriver")
    options = Options()
    options.headless = True
    with webdriver.Firefox(service=service, options=options) as driver:
        # get_daily_news(driver)
        get_realtime_news(driver)
