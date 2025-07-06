import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from method.method import core_sky, sign_wallet, gway

def monad_task():
    driver.get("https://monad.talentum.id/tasks?status=in_progress")

def main():
    # 如果本地chrome版本低于135，可以用默认user目录，没有就需要使用chrome的调试模式
    # # 创建ChromeOptions对象
    # chrome_options = Options()
    #
    # # 指定用户数据目录（注意要加上默认配置文件路径）
    # user_data_dir = r'C:\Users\ACER\AppData\Local\Google\Chrome\User Data'
    # chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
    #
    # # 指定配置文件（默认配置文件通常是Default）
    # chrome_options.add_argument('--profile-directory=Default')
    #
    # chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # 关闭自动控制blink特征
    # chrome_options.add_argument('--disable-infobars')
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # chrome_options.add_experimental_option('useAutomationExtension', False)
    # 设置调试地址

    debugger_address = "127.0.0.1:9223"

    # 创建选项并连接到已有浏览器
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)

    # 创建Chrome浏览器实例
    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(20)
    # 测试是否可用
    driver.get('https://baidu.com')
    time.sleep(2)
    # 登录钱包
    sign_wallet()

    # gway任务
    gway(driver)

    # coresky任务
    # core_sky(driver)

    # warden 任务
    # warden()

    # Billions 任务
    # billions()

    # zk_verify()
    # zk_verify()



# 后续操作...

# 关闭浏览器
# driver.quit()

if __name__ == '__main__':
    main()
    driver = webdriver.Chrome()
