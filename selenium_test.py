from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


dayUrl = "https://mops.twse.com.tw/mops/web/t05st02"

service = Service(executable_path="/Users/lzrong/PycharmProjects/20220616crawling/chromedriver")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)  # 讓DRIVER等待的物件
driver.get(dayUrl)
year = driver.find_element(By.ID, "year")
year.clear()
year.send_keys("111")
driver.find_element(By.ID, "month").send_keys("6")
driver.find_element(By.ID, "day").send_keys("15")
driver.find_element(By.XPATH, "//input[@value=' 查詢 ']").click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tblHead")))
driver.find_element(By.XPATH, "//input[@value='詳細資料'] ").click()
time.sleep(5)
driver.close()
