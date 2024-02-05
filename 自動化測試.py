from appium import webdriver
from selenium.webdriver.common.by import By
import time

# Appium 設定
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '7.1.1',
    'deviceName': '7f3ec4be',
    'automationName': 'uiautomator2',
    'appPackage': 'com.android.chrome',  # Chrome App 的package名稱
    'appActivity': 'com.google.android.apps.chrome.Main',
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 步驟1：進入國泰世華銀行官網並截圖
driver.get('https://www.cathaybk.com.tw/cathaybk/')
driver.save_screenshot('screenshot_step1.png')

# 步驟2：進入個人金融 > 產品介紹 > 信用卡列表並截圖
menu_button = driver.find_element(By.CLASS_NAME, 'menu-button')
menu_button.click()

time.sleep(2)  # 等待選單展開，根據實際情況調整等待時間

personal_finance = driver.find_element(By.XPATH, '//span[text()="個人金融"]')
personal_finance.click()

products = driver.find_element(By.XPATH, '//span[text()="產品介紹"]')
products.click()

credit_cards = driver.find_element(By.XPATH, '//span[text()="信用卡列表"]')
credit_cards.click()

driver.save_screenshot('screenshot_step2.png')

# 步驟3：進入個人金融 > 產品介紹 > 信用卡 > 卡片介紹 > 計算頁面，統計停發信用卡數量並截圖
back_button = driver.find_element(By.CLASS_NAME, 'back-button')
back_button.click()

credit_card_detail = driver.find_element(By.XPATH, '//span[text()="信用卡"]')
credit_card_detail.click()

card_intro = driver.find_element(By.XPATH, '//span[text()="卡片介紹"]')
card_intro.click()

calculate_page = driver.find_element(By.XPATH, '//span[text()="計算"]')
calculate_page.click()

# 在這裡加入統計停發信用卡數量的邏輯，並將結果存儲在變數中

# 截圖
driver.save_screenshot('screenshot_step3.png')

# 關閉 Appium WebDriver
driver.quit()
