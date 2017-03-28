# -*- coding:utf-8 -*-
import re
import threading
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing
import time
from selenium import webdriver
import urllib.parse
import os
from mysql import connector

def get_data(c_name):

    name = os.getpid()
    driver = webdriver.PhantomJS()
    driver.set_page_load_timeout(10)
    flag = True
    print("进程: %s" %name)
    print(c_name)
    ss = urllib.parse.quote("%s"%c_name[:-1])
    print('id%s Searching for the company web page %s'%(name, c_name[:-1]))
    t1 = time.clock()
    main_p = 'http://www.tianyancha.com/search?key=%s'%ss
    print(main_p)

    try:
        driver.get(main_p)
    except:
        print('overtime')
        driver.quit()

    for b in range(5):
        search_p = driver.page_source
        link = re.findall('"http://www.tianyancha.com/company/(.*?)"',search_p)
        if link == []:
            print('zz')
            time.sleep(0.5)
            if b == 4:
                flag = False
    if not flag:
        print('error1')

        driver.quit()

    t2 = time.clock()

    print('%s obtains the company web page: %s'%(name,(t2 - t1)))
    html = 'http://www.tianyancha.com/company/%s'%link[0]
    try:
        driver.get(html)
    except:
        print('overtime1')

        driver.quit()

    data = driver.page_source
    for a in range(5):
        try:
            business_scope = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[4]/table[2]/tbody/tr[6]/td/div/span')
            break
        except:
            if a == 4:
                flag = False
            print('zzz')
            time.sleep(1)
    if not flag:
        print('process: %s %s failed '% (name, c_name[:-1]))
        driver.quit()
    try:
        legalPersonName = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[4]/table[1]/tbody/tr[2]/td[1]/p')
        regis_address = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[4]/table[2]/tbody/tr[5]/td/div/span')
        credit_code = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[4]/table[2]/tbody/tr[4]/td[2]/div/span')
        approved_date = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[4]/table[2]/tbody/tr[4]/td[1]/div/span')
        Regis_authority = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[4]/table[2]/tbody/tr[3]/td[2]/div/span')
        Operating_period= driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[4]/table[2]/tbody/tr[3]/td[1]/div/span')
        Organization_code = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[4]/table[2]/tbody/tr[2]/td[2]/div/span')
        enterprise_type = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[4]/table[2]/tbody/tr[2]/td[1]/div/span')
        industry_regis_num = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[4]/table[2]/tbody/tr[1]/td[2]/div/span')
        industry = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[4]/table[2]/tbody/tr[1]/td[1]/div/span')
        regis_time = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[4]/table[1]/tbody/tr[4]/td[2]/p')
        regis_money = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[4]/table[1]/tbody/tr[2]/td[2]/p')
        state = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[4]/table[1]/tbody/tr[4]/td[1]/p')
        tel = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/span[1]')
        emai = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/span[2]')
        website = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/span[3]')
        company_address = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/span[4]')
        company_name = driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/p')
        lock.acquire()
        sql_update = "UPDATE `gaoxinjishu`.`gaoxinjishu` SET phone = '%s', web = '%s', hangye = '%s',addres= '%s',email = '%s',comp_type = '%s',scope = '%s',reg_time = '%s', reg_money = '%s', reg_address = '%s',reg_auth = '%s', approved_t = '%s', faren = '%s', indus_reg_num = '%s', credit_cod = '%s', organ_code = '%s', zhuangtai = '%s',oper_period = '%s', tianyancha = '%s'" \
                     "where `gaoxinjishu`.name='%s' "%(tel.text,website.text, industry.text, company_address.text, emai.text, enterprise_type.text, business_scope.text,regis_time.text,regis_money.text, regis_address.text, Regis_authority.text, approved_date.text, legalPersonName.text, industry_regis_num.text, credit_code.text, Organization_code.text, state.text, Operating_period.text,html, c_name[:-1])
        print(tel.text,c_name[:-1])

        try:
            cursor = conn.cursor()
            cursor.execute(sql_update)
            cursor.close()
            conn.commit()
            print('data updated')
            print(sql_update)
            finished.write(c_name)
            print('%s has been finished'%c_name)
        except Exception as e:
            print(e)
            conn.rollback()
            driver.quit()

    except:
        print('crawl failed')

        driver.quit()
    t3 = time.clock()
    print('%s successfully get the information and ready to quit:%s'%(name,(t3 - t2)))
    global count
    count = count + 1
    print(count)
    lock.release()
    driver.quit()



if __name__ == '__main__':
    # service_args = [
    #     '--proxy=125.69.95.242:8998',
    #     '--proxy-type=HTTP',
    # ]
    global count
    count = 0
    start = time.clock()
    txt = "C:\\Users\\songjie\\Desktop\\4.txt"
    txt2 = "C:\\Users\\songjie\\Desktop\\3.txt"
    file = open(txt)
    file2 = open(txt2)
    finished = open('C:\\Users\\songjie\\Desktop\\finished.txt','a')
    webs = file.readlines()
    webs2 = file2.readlines()
    # multiprocessing.freeze_support()
    web = [webs, webs2]
    conn = connector.Connect(host="localhost", user="root", password="", db='')
    threads = []
    lock = threading.Lock()

    t1 = threading.Thread(target=get_data, args=(webs,))
    threads.append(t1)
    t1.start()
    t2 = threading.Thread(target=get_data, args=(webs2,))
    t2.start()
    threads.append(t2)
    t1.join()
    t2.join()
    # pool.map_async(get_data, webs)
    # pool.close()
    # pool.join()
    file.close()
    file2.close()
    conn.close()
    finished.close()
    end = time.clock()
    print('all: %s'%(end - start))
