from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_daily_news(driver, years="111", month="6", day="15"):
    dayUrl = "https://mops.twse.com.tw/mops/web/t05st02"
    wait = WebDriverWait(driver, 10)  # 讓DRIVER等待的物件
    driver.get(dayUrl)
    year = driver.find_element(By.ID, "year")
    year.clear()
    year.send_keys(years)
    driver.find_element(By.ID, "month").send_keys(month)
    driver.find_element(By.ID, "day").send_keys(day)
    driver.find_element(By.XPATH, "//input[@value=' 查詢 ']").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='詳細資料'] ")))
    driver.find_element(By.XPATH, "//input[@value='詳細資料'] ").click()
    time.sleep(5)
    print("=====")


if __name__ == "__main__":
    service = Service(executable_path="/Users/lzrong/PycharmProjects/20220616crawling/chromedriver")
    with webdriver.Chrome(service=service) as driver:
        get_daily_news(driver)
