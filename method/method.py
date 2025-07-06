import json
import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from method.utils import find_and_click_by_base64, is_element_exist, find_and_click_by_path


# 重试装饰器
def t(data=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(data):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Exception occurred: {e}")

            return None

        return wrapper

    return decorator


# gway 签到任务
@t(data=3)
def gway(driver):
    driver.get('https://gway.ai/')
    button = driver.find_element(By.XPATH, '//*[@id="points-twitter-modal"]/div/div/div/div/div/div[3]/button/div/div')
    # 滚动到按钮位置
    ActionChains(driver).scroll_to_element(button).perform()
    # 点击按钮
    button.click()


# warden 签到、聊天、swap任务

@t(data=3)
def warden(driver):
    driver.get('https://app.wardenprotocol.org/dashboard')
    input_box = driver.find_element(By.XPATH, '//*[@id="chat-form-desktop"]/textarea')
    input_box.send_keys('swap 0.0001 sol to usdt')
    with open("basecode.json", 'r', encoding='utf-8') as file:
        jsonData = json.load(file)  # 自动解析JSON为字典或列表
    find_and_click_by_base64(jsonData['warButton'])
    input_box = driver.find_element(By.XPATH, '//*[@id="chat-form-desktop"]/textarea')
    input_box.send_keys('confirm')
    time.sleep(1)
    find_and_click_by_base64(jsonData['warButton'])


# coresky 签到任务、投票（滑块需要自己滑动）
@t(data=3)
def core_sky(driver):
    driver.get("https://share.coresky.com/s96gwl/tasks-rewards")
    # 定位包含"collect wallet"文本的div
    if is_element_exist(driver, By.XPATH, "//div[contains(text(), 'Connect Wallet')]"):
        login_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Connect Wallet')]")
        login_button.click()
        okx_button = driver.find_element(By.XPATH, "//span[contains(text(), 'OKX')]")
        okx_button.click()
        if not is_element_exist(driver, By.CLASS_NAME, "checkin-action"):
            find_and_click_by_path("picture/Snipaste_2025-07-06_19-31-45.png")
            find_and_click_by_path("picture/Snipaste_2025-07-06_19-54-15.png")
    check_in_button = driver.find_element(By.CLASS_NAME, "checkin-action")
    check_in_button.click()
    #     TODO 设置滑块操作，要怎么实现 目前手动操作限时5s
    time.sleep(5)
    driver.get("https://www.coresky.com/meme")
    time.sleep(2)
    input_box = driver.find_element(By.XPATH, "//div[@class='input-box round']")
    input_box.click()
    input_box.click()
    pyautogui.typewrite('CZTellMEWhy')
    pyautogui.press("enter")
    time.sleep(1)
    vote = driver.find_element(By.XPATH, "//div[text()=' Vote ']")
    vote.click()
    find_and_click_by_path("picture/Snipaste_2025-07-06_20-46-51.png")
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite("20")
    find_and_click_by_path("picture/Snipaste_2025-07-06_20-49-11.png")


# billions 任务、未完成
def billions(driver):
    driver.get("https://signup.billions.network/sign-in?rc=SIGXG66O")


# zkVerify 签到任务
@t(data=3)
def zk_verify(driver):
    driver.get("https://points.zkverify.io/loyalty?referral_code=TNFJ6JBS")
    find_and_click_by_path("picture/Snipaste_2025-07-06_19-54-15.png")
    check_in_button = driver.find_element(By.XPATH, "//button[text()='Check in']")
    check_in_button.click()
    find_and_click_by_path("picture/Snipaste_2025-07-06_19-54-15.png")


# 钱包登录
def sign_wallet():
    with open("basecode.json", 'r', encoding='utf-8') as file:
        json_data = json.load(file)  # 自动解析JSON为字典或列表
    find_and_click_by_base64(json_data['wallet'])
    time.sleep(1)
    # 密码输入
    pyautogui.typewrite('as12301230')
    pyautogui.press('enter')



