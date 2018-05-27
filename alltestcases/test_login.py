
# import unittest
# from selenium import webdriver


# from common.create_driver import getDriver

# def add(x,y):
#     return x+y

# class UserActionTest(unittest.TestCase):
#     # driver = getDriver()

        
#     # def test_add(self):
#     #     expect_val = 3
#     #     self.assertEqual(add(1,2),expect_val)

#     def test_login(self):
#         driver = webdriver.Chrome()
#         # driver = getDriver()
#         driver.get('http://118.31.19.120:3000/signin')
#         driver.find_element_by_id('name').send_keys('testuser3')
#         driver.find_element_by_id('pass').send_keys('123456')
#         driver.find_element_by_id('pass').submit()
#         okurl = driver.current_url

#         self.assertEqual(okurl,'http://118.31.19.120:3000/')

#         loginName = driver.find_element_by_css_selector('#sidebar > div:nth-child(1) > div.inner > div > div > span.user_name > a').text

#         self.assertEqual(loginName,'testuser3')
    
#     def test_register(self):
#         driver = webdriver.Chrome()
#         driver.get('http://118.31.19.120:3000/signup')
#         driver.find_element_by_id('loginname').send_keys('testuser3')
#         driver.find_element_by_id('pass').send_keys('123456')
#         driver.find_element_by_id('re_pass').send_keys("123456")
#         driver.find_element_by_id('email').send_keys('123456@123.com')
#         driver.find_element_by_id('pass').submit()


# if __name__ =="__main__":
#     unittest.main()



# 截屏优化

# import unittest

# from common.create_driver import getDriver

# from common.manage_dir import getPngfileName

# import time

# class UserActionTest(unittest.TestCase):
#     driver =  getDriver()
    
#     #每次用例执行前
#     def setUp(self):
#         self.driver.maximize_window()
#         self.driver.get('http://118.31.19.120:3000/')

#     #每次用例执行后
#     def tearDown(self):
#         current_time = time.time()
#         # self.driver.save_screenshot('./screenshots/'+str(current_time)+'.png')
#         self.driver.save_screenshot(getPngfileName())
#         self.driver.delete_all_cookies()

#     @classmethod
#     def setUpClass(cls):
#         pass   

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()

#     def test_login(self):

#         self.driver.find_element_by_link_text('登录').click()
#         self.driver.find_element_by_id('name').send_keys('testuser3')
#         self.driver.find_element_by_id('pass').send_keys('123456')
#         self.driver.find_element_by_id('pass').submit()
#         okurl = self.driver.current_url

#         self.assertEqual(okurl,'http://118.31.19.120:3000/')

#         loginName = self.driver.find_element_by_css_selector('#sidebar > div:nth-child(1) > div.inner > div > div > span.user_name > a').text

#         self.assertEqual(loginName,'testuser3')

#     def test_register(self):
#         self.driver.find_element_by_link_text('注册').click()
#         self.driver.get('http://118.31.19.120:3000/signup')
#         self.driver.find_element_by_id('loginname').send_keys('testuser3')
#         self.driver.find_element_by_id('pass').send_keys('123456')
#         self.driver.find_element_by_id('re_pass').send_keys("123456")
#         self.driver.find_element_by_id('email').send_keys('123456@123.com')
#         self.driver.find_element_by_id('pass').submit()


# if __name__ == "__main__":
#     unittest.main()



#使用ddt

# import unittest

# from ddt import ddt,data,unpack,file_data
# from common.create_driver import getDriver
# from common.manage_dir import getPngfileName
# import os
# import time


# @ddt
# class UserActionTest(unittest.TestCase):
#     driver =  getDriver()

#     def setUp(self):
#         self.driver.maximize_window()
#         self.driver.get('http://118.31.19.120:3000/')

#     def tearDown(self):
#         print(getPngfileName())
#         self.driver.save_screenshot(getPngfileName())
#         self.driver.delete_all_cookies()

#     @classmethod
#     def setUpClass(cls):
#         pass   

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()


#     @data(["testuser3","123456"],["testuser4",""])
#     def test_login(self,userinfo):
#         self.driver.find_element_by_link_text('登录').click()
#         self.driver.find_element_by_id('name').send_keys(userinfo[0])
#         self.driver.find_element_by_id('pass').send_keys(userinfo[1])
#         self.driver.find_element_by_id('pass').submit()
#         okurl = self.driver.current_url

#         self.assertEqual(okurl,'http://118.31.19.120:3000/')

#         loginName = self.driver.find_element_by_css_selector('#sidebar > div:nth-child(1) > div.inner > div > div > span.user_name > a').text

#         self.assertEqual(loginName,'testuser3')


# if __name__ == "__main__":
#     unittest.main()



#引入CSV数据文件

import unittest

from ddt import ddt,data,unpack,file_data
from common.create_driver import getDriver
from common.manage_dir import getPngfileName
import os
import time
import csv

def get_data_csv(filename):
    users = []
    with open(filename,'r') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            users.append(row)
    return users


@ddt
class UserActionTest(unittest.TestCase):
    driver =  getDriver()

    def setUp(self):
        self.driver.maximize_window()
        self.driver.get('http://118.31.19.120:3000/')

    def tearDown(self):
        print(getPngfileName())
        self.driver.save_screenshot(getPngfileName())
        self.driver.delete_all_cookies()

    @classmethod
    def setUpClass(cls):
        pass   

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    @data(*get_data_csv('./testdata/userlogin.csv'))
    @unpack
    def test_login(self,username,password,excpetStatus,checkpoint):

        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_id('name').send_keys(username)
        self.driver.find_element_by_id('pass').send_keys(password)
        self.driver.find_element_by_id('pass').submit()
        okurl = self.driver.current_url

        self.assertEqual(okurl,'http://118.31.19.120:3000/')

        loginName = self.driver.find_element_by_css_selector('#sidebar > div:nth-child(1) > div.inner > div > div > span.user_name > a').text
        self.assertEqual(loginName,'testuser3')

    # def test_register(self):
    #     self.driver.find_element_by_link_text('注册').click()
    #     self.driver.get('http://118.31.19.120:3000/signup')
    #     self.driver.find_element_by_id('loginname').send_keys('testuser3')
    #     self.driver.find_element_by_id('pass').send_keys('123456')
    #     self.driver.find_element_by_id('re_pass').send_keys("123456")
    #     self.driver.find_element_by_id('email').send_keys('123456@123.com')
    #     self.driver.find_element_by_id('pass').submit()
        

if __name__ == "__main__":
    unittest.main()