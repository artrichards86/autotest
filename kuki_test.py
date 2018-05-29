# -*- coding: utf-8 -*-
from selenium import webdriver

def addInBasketAndGoBackMain():
    driver.find_element_by_class_name("button").click()
    driver.find_element_by_class_name("fi-play-video").click()

driver = webdriver.Chrome()
driver.implicitly_wait(50)
driver.maximize_window()
base_url = "http://kuki.webtest2.htc-cs.com/"
driver.get(base_url)
driver.find_element_by_link_text(u"Войти").click()
driver.find_element_by_id("user_email").send_keys("art_richards@mail.com")
driver.find_element_by_id("user_password").send_keys("123654789")
driver.find_element_by_name("commit").click()
driver.find_element_by_xpath("//img[@alt='Mv5bmjeymjcyndi4mf5bml5banbnxkftztcwmda5mzg3oa@@. v1 sx214 al ']").click()
addInBasketAndGoBackMain()
driver.find_element_by_xpath("//img[@alt='Mv5bnzg5mzk5nzc0nf5bml5banbnxkftztcwnjg3mdqzmq@@. v1 sy317 cr5,0,214,317 al ']").click()
addInBasketAndGoBackMain()
driver.find_element_by_class_name("cart-count").click()
driver.find_element_by_xpath("//div[@id='mycart']/div[3]/div[3]/a/i").click()
driver.find_element_by_xpath("//div[@id='mycart']/div[2]/div[3]/a/i").click()
driver.find_element_by_link_text(u"Выйти").click()