import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from pyquery import PyQuery as pq
from configboos import *
from bson.objectid import ObjectId
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
    "expirationDate": 1913120108,
    "hostOnly": false,
    "httpOnly": false,
    "name": "__a",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "30036493.1595601173.1595733884.1597664382.38.4.4.38",
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
    "value": "1597664382",
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
    "value": "l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2FresumeAnalyze%3FparserId%3D2212ad0f74bb480b1nZ_3dm4E1E~%26ka%3Dto_resume_click_1&r=&g=&friend_source=0&friend_source=0",
    "id": 4
},
{
    "domain": ".zhipin.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "1597664384",
    "id": 5
},
{
    "domain": ".zhipin.com",
    "expirationDate": 1629200383,
    "hostOnly": false,
    "httpOnly": false,
    "name": "Hm_lvt_194df3105ad7148dcf2b98a91b5e727a",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1595601186,1595650251,1595733884,1597664384",
    "id": 6
},
{
    "domain": ".zhipin.com",
    "expirationDate": 1627306871.788752,
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
    "expirationDate": 1598727600.163529,
    "hostOnly": false,
    "httpOnly": true,
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
    "expirationDate": 1598727600.163759,
    "hostOnly": false,
    "httpOnly": true,
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
    "id": 10
},
{
    "domain": "www.zhipin.com",
    "hostOnly": true,
    "httpOnly": true,
    "name": "JSESSIONID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": true,
    "storeId": "0",
    "value": "\"\"",
    "id": 11
}
]
def index_page(page,x,k):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在投递',k, '次')
    try:
        url = 'https://www.zhipin.com/'
        browser.get(url)
        print(x['公司'])
        print(x['link'])
        url = 'https://www.zhipin.com/' + str(x['link'])
        for cookie in cookie_list:
            browser.add_cookie(cookie)

        browser.get(url)
        button2 = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-startchat')))
        time.sleep(1)
        button2.click()
        print('点击2成功')
        button3 = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-sure')))
        time.sleep(1)
        button3.click()
        time.sleep(1)
        print('投递成功')



    except TimeoutException:
             print('失败')



def main():
    """
    遍历每一页
    """
    i=0
    x=0
    n=1
    myclient = pymongo.MongoClient("mongodb://140.143.11.236:27017/")
    mydb = myclient["zhaop"]
    mycol = mydb["boss"]
   # myquery = {'_id': 0, 'link': 1}
    for x in mycol.find({"_id": {"$gt": ObjectId("5f3d07b2e99eea30d9c69a7f")}}):
        index_page(i,x,n)
        n = n + 1


if __name__ == '__main__':
    main()