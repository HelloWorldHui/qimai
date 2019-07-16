# coding=utf
"""
author=Hui_T
"""
import time

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待相关
from selenium.webdriver.support import expected_conditions as EC  # 显示等待相关
from selenium.webdriver.common.by import By  # 显示等待相关
import json

url = 'https://www.qimai.cn/rank'
driver = webdriver.Firefox(executable_path='F:/火狐/geckodriver')
driver.implicitly_wait(10)  # 隐式等待 等待网页加载10秒
driver.get(url)

for i in range(10):
    driver.execute_script('window.scroll(0,100000)')
    time.sleep(1)


div_1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="rank-all-list"]/div[2]/div[2]/div[1]')))
div_2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="rank-all-list"]/div[2]/div[2]/div[2]')))
div_3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="rank-all-list"]/div[2]/div[2]/div[3]')))

div_list = [div_1,div_2,div_3]
# driver.find_element_by_xpath()
def parse(div):
    free = div.find_element_by_xpath('.//div/ul/li[1]/div[1]/p[1]').text
    first_time = div.find_element_by_xpath('.//div/ul/li[1]/div[1]/p[2]').text
    li_list = div.find_elements_by_xpath('.//div/ul/li')
    # print(li_list)
    print(free,first_time,'=============================')
    li_list.pop(0)

    f = open(free+'.json','w',encoding='utf8')

    for li in li_list:
        rank = li.find_element_by_xpath('.//div/div[1]/span').text
        name = li.find_element_by_xpath('.//div/div[2]/div/div/p[1]/a').text
        describe_str = li.find_element_by_xpath('.//div/div[2]/div/div/p[2]').text
        describe = describe_str.split(' ',1)[0]
        company = li.find_element_by_xpath('.//div/div[2]/div/div/p[2]/span[2]').text
        dic = {'rank':rank,"name":name,'describe':describe,"company":company}
        f.write(json.dumps(dic,ensure_ascii=False)+'\n')
        print(dic,'\n')
    f.close()

for i in range(len(div_list)):
    parse(div_list[i])
time.sleep(5)
driver.close()
