import os
import platform
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)


class Selenium:
    def __init__(self):
        sysstr = platform.system()
        driver_path = os.getcwd() + '/lib/'
        if sysstr == 'Windows':
            driver_path = driver_path + 'chromedriver.exe'
        elif sysstr == 'Linux':
            driver_path = driver_path + 'chromedriver'
        else:
            driver_path = driver_path + 'chromedriver_mac64'
        service = Service(driver_path)
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(3)
        self.url = f'http://202.195.176.89/eportal/index.jsp?nasip={config["nasip"]}'

    def web_actions(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

        try:
            success = self.driver.find_element(By.ID, 'userMessage')
            if success.text == '您已成功连接校园网!':
                return True
        except:
            # username = self.driver.find_element(By.ID, 'username_tip')
            # username.click()
            username = self.driver.find_element(By.ID, 'username')
            username.clear()
            username.send_keys(config['userId'])

            password = self.driver.find_element(By.ID, 'pwd_tip')
            password.click()
            password = self.driver.find_element(By.ID, 'pwd')
            password.clear()
            password.send_keys(config['password'])

            service_selector = self.driver.find_element(By.ID, 'xiala')
            service_selector.click()

            service = self.driver.find_element(By.ID, config['service'])
            service.click()

            login_button = self.driver.find_element(By.ID, 'loginLink_div')
            login_button.click()


sel = Selenium()


def login():
    try:
        flag = sel.web_actions()
        if flag:
            print("状态：已连接", time.asctime(time.localtime(time.time())))
        else:
            print("登录操作完成", time.asctime(time.localtime(time.time())))
    except Exception as e:
        print(type(e), time.asctime(time.localtime(time.time())))
        print(e.args)


while True:
    login()
    time.sleep(1)
