import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from pyquery import PyQuery as pq
from config import *
from urllib.parse import quote
import time
import datetime
import string
import zipfile


profile = webdriver.FirefoxOptions()
profile.add_argument("--start-maximized")

#profile.add_extension(proxy_auth_plugin_path)
browser=webdriver.Firefox(options=profile)
#opt.add_argument('--headless')  # 浏览器不提供可视化界面。Linux下如果系统不支持可视化不加这条会启动失败
# opt.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" # 手动指定使用的浏览器位置
#browser  = webdriver.Chrome()  # 创建无界面对象
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#profile.add_argument('-headless')
#browser = webdriver.Chrome()

wait = WebDriverWait(browser, 15)


cookie_list=[
{
    "domain": ".zhipin.com",
    "expirationDate": 1911010249,
    "hostOnly": false,
    "httpOnly": false,
    "name": "__a",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "30036493.1595601173.1595601173.1595650224.9.2.2.9",
    "id": 1
},
{
    "domain": ".zhipin.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "__c",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "1595650224",
    "id": 2
},
{
    "domain": ".zhipin.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "__g",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "-",
    "id": 3
},
{
    "domain": ".zhipin.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "__l",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2FresumeAnalyze%3FparserId%3D2212ad0f74bb480b1nZ_3dm4E1E~%26ka%3Dto_resume_click_1&r=&friend_source=0&friend_source=0",
    "id": 4
},
{
    "domain": ".zhipin.com",
    "expirationDate": 1595831586,
    "hostOnly": false,
    "httpOnly": false,
    "name": "__zp_stoken__",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "c819aGmpbUnBXAX9tOhxKU1AEcVl7YDJ4AzB%2BBARcFGhMNTYfXTBeSB0VNEl4PjxlNjs9AhlWNn9XYHI3diwlFiweTyhYXR51CGBJSkk4XSh4XBVQH0lwHRAfP20Ga3g1dAJ4fRxfN1xBIXw%3D",
    "id": 5
},
{
    "domain": ".zhipin.com",
    "expirationDate": 1627137185,
    "hostOnly": false,
    "httpOnly": false,
    "name": "Hm_lvt_194df3105ad7148dcf2b98a91b5e727a",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1595601170,1595601186",
    "id": 6
},
{
    "domain": ".zhipin.com",
    "expirationDate": 1627186244.104559,
    "hostOnly": false,
    "httpOnly": false,
    "name": "lastCity",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "101020100",
    "id": 7
},
{
    "domain": ".zhipin.com",
    "expirationDate": 1596205984.254443,
    "hostOnly": false,
    "httpOnly": false,
    "name": "t",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "IGaAPPadchtU5ssh",
    "id": 8
},
{
    "domain": ".zhipin.com",
    "expirationDate": 1596205984.2546,
    "hostOnly": false,
    "httpOnly": false,
    "name": "wt",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "IGaAPPadchtU5ssh",
    "id": 9
},
{
    "domain": "www.zhipin.com",
    "hostOnly": true,
    "httpOnly": false,
    "name": "__zp__pub__",
    "path": "/shanghai",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "",
    "id": 10
},
{
    "domain": "www.zhipin.com",
    "expirationDate": 1611153196.824889,
    "hostOnly": true,
    "httpOnly": false,
    "name": "_bl_uid",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "vLk4wd560gqbnUr8k6w7zgwc9sI0",
    "id": 11
}
]
def index_page(page,x,k):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第',k, '次')
    try:
        url = 'https://www.zhipin.com/c101010100-p110105/?page='+str(k)+'&ka=page-'+str(k)
        browser.get(url)
        for cookie in cookie_list:
            browser.add_cookie(cookie)
        browser.get(url)
        # button1 = wait.until( EC.element_to_be_clickable((By.CSS_SELECTOR, '')))
        current_window = browser.current_window_handle
        for N in range(1, 30):
            time.sleep(2)
            #button1 = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, )))
            button1 = browser.find_element_by_css_selector('li:nth-of-type(' + str(N) + ') .job-name')
            time.sleep(2)

            button1.click()
            print('点击1成功')
            n = browser.window_handles
            browser.switch_to.window(n[-1])
            button2 = WebDriverWait(browser, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-startchat')))
            time.sleep(2)
            button2.click()
            print('点击2成功')
            button3 = WebDriverWait(browser, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-sure')))
            button3.click()
            time.sleep(2)
            print('成功')
            browser.close()
            browser.switch_to.window(current_window)
            print('爬取第',N,'item成功')

    except TimeoutException:
             print('失败')


def main():
    """
    遍历每一页
    """
    n=1

    for x in range(1, 10):
        for i in range(1, 30):
            index_page(i,x,n)
            n = n +1

if __name__ == '__main__':
    main()