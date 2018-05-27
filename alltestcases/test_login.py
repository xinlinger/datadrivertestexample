
import unittest
from selenium import webdriver

# def add(x,y):
#     return x+y

class UserActionTest(unittest.TestCase):
    
    # def test_add(self):
    #     expect_val = 3
    #     self.assertEqual(add(1,2),expect_val)

    def test_login(self):
        driver = webdriver.Chrome()
        driver.get('http:118.31.19.120:3000/signin')
        driver.find_element_by_id('name').send_keys('testuser3')
        driver.find_element_by_id('pass').send_keys('123456')
        driver.find_element_by_id('pass').submit()
        okurl = driver.current_url

        self.assertEqual(okurl,'ttp:118.31.19.120:3000/')

        loginName = driver.find_elements_by_css_selector('')

        self.assertEqual(loginName,'testuser3')


if __name__ =="__main__":
    unittest.main()
