import base64
import io
import time

import pyautogui
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

retry_times = 10


def find_and_click_by_base64(pic):
    start_time = time.time()
    while (time.time() - start_time) < retry_times:
        try:
            # 尝试定位图片
            image_rb = base64.b64decode(pic)
            image = Image.open(io.BytesIO(image_rb))
            location = pyautogui.locateCenterOnScreen(image)
            if location:
                print(f"已找到目标图片，用时{time.time() - start_time:.2f}秒")
                pyautogui.moveTo(location)
                pyautogui.click()
                break
        except Exception as e:
            print(f"检测过程中出错: {e}")


def find_and_click_by_path(path):
    start_time = time.time()
    success = False
    while (time.time() - start_time) < retry_times:
        try:
            # 尝试定位图片
            location = pyautogui.locateCenterOnScreen(path)
            if location:
                print(f"已找到目标图片，用时{time.time() - start_time:.2f}秒")
                pyautogui.moveTo(location)
                pyautogui.click()
                success = True
                break
        except Exception as e:
            print(f"检测过程中出错: {e}")
    return success


def is_element_exist(driver, by, value, timeout=retry_times):
    """判断元素是否存在"""
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return True
    except:
        return False


def wait_for_success(path):
    start_time = time.time()
    success = False
    while (time.time() - start_time) < retry_times:
        try:
            # 尝试定位图片
            location = pyautogui.locateCenterOnScreen(path)
            if location:
                print(f"已找到目标图片，用时{time.time() - start_time:.2f}秒")
                success = True
                break
        except Exception as e:
            print(f"检测过程中出错: {e}")
    return success
