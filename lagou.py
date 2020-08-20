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
    "domain": ".lagou.com",
    "expirationDate": 1658757515,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_ga",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "GA1.2.961835564.1556626406",
    "id": 1
},
{
    "domain": ".lagou.com",
    "expirationDate": 1595771915,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_gid",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "GA1.2.878930150.1595601217",
    "id": 2
},
{
    "domain": ".lagou.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "_putrc",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "3AC832488DEC8ACE123F89F2B170EADC",
    "id": 3
},
{
    "domain": ".lagou.com",
    "expirationDate": 1596290120.407759,
    "hostOnly": false,
    "httpOnly": false,
    "name": "gate_login_token",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "a06875c559f92c12434ef66ef51ecbae44a1eafafc41f03aba54e30c9332e7e5",
    "id": 4
},
{
    "domain": ".lagou.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "1595685515",
    "id": 5
},
{
    "domain": ".lagou.com",
    "expirationDate": 1627221515,
    "hostOnly": false,
    "httpOnly": false,
    "name": "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1595070028,1595601217,1595685321",
    "id": 6
},
{
    "domain": ".lagou.com",
    "expirationDate": 1598277512.359336,
    "hostOnly": false,
    "httpOnly": false,
    "name": "index_location_city",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "%E4%B8%8A%E6%B5%B7",
    "id": 7
},
{
    "domain": ".lagou.com",
    "expirationDate": 3716432278.772044,
    "hostOnly": false,
    "httpOnly": false,
    "name": "LG_HAS_LOGIN",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1",
    "id": 8
},
{
    "domain": ".lagou.com",
    "expirationDate": 3716432278.771919,
    "hostOnly": false,
    "httpOnly": false,
    "name": "LG_LOGIN_USER_ID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "7dd36a9d9e83cff6c878ddfc28e9f6295996d79323bb775d454a8a576f2d3aa5",
    "id": 9
},
{
    "domain": ".lagou.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "LGRID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "20200725215835-fe21ee63-96eb-4119-be62-de7502e6046d",
    "id": 10
},
{
    "domain": ".lagou.com",
    "expirationDate": 1595687315.210238,
    "hostOnly": false,
    "httpOnly": false,
    "name": "LGSID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "20200725215520-0e465e48-1b49-4c07-a24c-8cd23dec0add",
    "id": 11
},
{
    "domain": ".lagou.com",
    "expirationDate": 1871986405.625196,
    "hostOnly": false,
    "httpOnly": false,
    "name": "LGUID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "20190430201325-5b0d3a05-6b41-11e9-9d75-5254005c3644",
    "id": 12
},
{
    "domain": ".lagou.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "login",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "true",
    "id": 13
},
{
    "domain": ".lagou.com",
    "expirationDate": 1595687120.439011,
    "hostOnly": false,
    "httpOnly": false,
    "name": "PRE_HOST",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "",
    "id": 14
},
{
    "domain": ".lagou.com",
    "expirationDate": 1595687120.439513,
    "hostOnly": false,
    "httpOnly": false,
    "name": "PRE_LAND",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "https%3A%2F%2Fwww.lagou.com%2F",
    "id": 15
},
{
    "domain": ".lagou.com",
    "expirationDate": 1595687120.439442,
    "hostOnly": false,
    "httpOnly": false,
    "name": "PRE_SITE",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "https%3A%2F%2Fwww.lagou.com",
    "id": 16
},
{
    "domain": ".lagou.com",
    "expirationDate": 1595687120.438894,
    "hostOnly": false,
    "httpOnly": false,
    "name": "PRE_UTM",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "",
    "id": 17
},
{
    "domain": ".lagou.com",
    "expirationDate": 1596290120.407842,
    "hostOnly": false,
    "httpOnly": false,
    "name": "privacyPolicyPopup",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "false",
    "id": 18
},
{
    "domain": ".lagou.com",
    "expirationDate": 7902885515,
    "hostOnly": false,
    "httpOnly": false,
    "name": "sensorsdata2015jssdkcross",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "%7B%22distinct_id%22%3A%2214561598%22%2C%22%24device_id%22%3A%2216a6e2a04b0f1-0e1c07ae59e437-37677f03-1024000-16a6e2a04b12f5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22lagou%22%2C%22%24latest_utm_medium%22%3A%22pcbanner%22%2C%22%24latest_utm_campaign%22%3A%22Java%E5%B7%A5%E7%A8%8B%E5%B8%88%E9%AB%98%E8%96%AA%E8%AE%AD%E7%BB%83%E8%90%A5%22%2C%22%24latest_utm_content%22%3A%22java_architect%22%2C%22%24latest_utm_term%22%3A%22java_architect%22%2C%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2284.0.4147.89%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%2C%22first_id%22%3A%2216a6e2a04b0f1-0e1c07ae59e437-37677f03-1024000-16a6e2a04b12f5%22%7D",
    "id": 19
},
{
    "domain": ".lagou.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "sensorsdata2015session",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "%7B%7D",
    "id": 20
},
{
    "domain": ".lagou.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "unick",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "%E5%85%9A%E7%9A%93%E7%8E%84",
    "id": 21
},
{
    "domain": ".lagou.com",
    "expirationDate": 1626606026.787807,
    "hostOnly": false,
    "httpOnly": false,
    "name": "user_trace_token",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "20200718190026-3a788419-4a96-4288-a486-212981d8a694",
    "id": 22
},
{
    "domain": ".lagou.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "X_HTTP_TOKEN",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "43b87aabe3eb73b04155865951377d439906b67165",
    "id": 23
},
{
    "domain": ".www.lagou.com",
    "expirationDate": 1598100586,
    "hostOnly": false,
    "httpOnly": false,
    "name": "Hm_lvt_cdce8cda34e84469b1c8015204129522",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1566478265,1566478279,1566478301,1566478320",
    "id": 24
},
{
    "domain": "www.lagou.com",
    "expirationDate": 1596290278.023464,
    "hostOnly": true,
    "httpOnly": false,
    "name": "hasDeliver",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1",
    "id": 25
},
{
    "domain": "www.lagou.com",
    "hostOnly": true,
    "httpOnly": true,
    "name": "JSESSIONID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "ABAAAECABIEACCA6AD4895F41BA7005ADA6A27AC90625AA",
    "id": 26
},
{
    "domain": "www.lagou.com",
    "expirationDate": 1627221320,
    "hostOnly": true,
    "httpOnly": false,
    "name": "RECOMMEND_TIP",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "true",
    "id": 27
},
{
    "domain": "www.lagou.com",
    "expirationDate": 1595771913.359235,
    "hostOnly": true,
    "httpOnly": false,
    "name": "SEARCH_ID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "4bb05713da934a4ab3b6fcc2f70253ca",
    "id": 28
},
{
    "domain": "www.lagou.com",
    "expirationDate": 1596290120.407614,
    "hostOnly": true,
    "httpOnly": false,
    "name": "showExpriedCompanyHome",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1",
    "id": 29
},
{
    "domain": "www.lagou.com",
    "expirationDate": 1596290120.407553,
    "hostOnly": true,
    "httpOnly": false,
    "name": "showExpriedIndex",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1",
    "id": 30
},
{
    "domain": "www.lagou.com",
    "expirationDate": 1596290120.407662,
    "hostOnly": true,
    "httpOnly": false,
    "name": "showExpriedMyPublish",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1",
    "id": 31
},
{
    "domain": "www.lagou.com",
    "hostOnly": true,
    "httpOnly": false,
    "name": "TG-TRACK-CODE",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "index_search",
    "id": 32
},
{
    "domain": "www.lagou.com",
    "hostOnly": true,
    "httpOnly": false,
    "name": "WEBTJ-ID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "20200725215520-1738641b58e376-01678566566e7e-15366650-1024000-1738641b58f365",
    "id": 33
}
]
def index_page(page,x,k):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第',k, '次')
    try:
        url = 'https://www.lagou.com/beijing-zhaopin/shangyeshjufenxi/'+str(k)+'/?filterOption=2&sid=db07e143097e4b16b6d578e3b7356d00'
        browser.get(url)
        for cookie in cookie_list:
            browser.add_cookie(cookie)
        browser.get(url)
        button = wait.until( EC.element_to_be_clickable((By.CSS_SELECTOR, '.body-btn')))
        button.click()
        current_window = browser.current_window_handle
        for N in range(1, 15):
            time.sleep(3)
            #button1 = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, )))
            button1 = browser.find_element_by_css_selector('li:nth-of-type(' + str(N) + ') .position_link')
            ActionChains(browser).move_to_element(button1).click(button1).perform()
            print('点击1成功')
            n = browser.window_handles
            browser.switch_to.window(n[-1])
            button2 = WebDriverWait(browser, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.send-CV-btn.s-send-btn.fr')))
            time.sleep(2)
            button2.click()
            print('点击2成功')
            button3 = WebDriverWait(browser, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#delayConfirmDeliver')))
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