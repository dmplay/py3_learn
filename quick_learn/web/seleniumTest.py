# !/usr/bin/python
# -*- coding: UTF-8 -*-
'''
browser.find_elements_by_class_name(name)使用CSS 类name 的元素
browser.find_elements_by_css_selector(selector)匹配CSS selector 的元素
browser.find_elements_by_id(id)匹配id 属性值的元素
browser.find_elements_by_link_text(text)完全匹配提供的text 的<a>元素
browser.find_elements_by_partial_link_text(text)包含提供的text 的<a>元素
browser.find_elements_by_name(name)匹配name 属性值的元素
browser.find_elements_by_tag_name(name)匹配标签name 的元素(大小写无关，<a>元素匹配'a'和'A')

tag_name 标签名，例如 'a'表示<a>元素
get_attribute(name) 该元素name 属性的值
text 该元素内的文本，例如<span>hello</span>中的'hello'
clear() 对于文本字段或文本区域元素，清除其中输入的文本
is_displayed() 如果该元素可见，返回True，否则返回False
is_enabled() 对于输入元素，如果该元素启用，返回True，否则返回False
is_selected() 对于复选框或单选框元素，如果该元素被选中，选择True，否则返回False
location 一个字典，包含键'x'和'y'，表示该元素在页面上的位置

browser.back()点击“返回”按钮。
214 Python 编程快速上手——让繁琐工作自动化
browser.forward()点击“前进”按钮。
browser.refresh()点击“刷新”按钮。
browser.quit()点击“关闭窗口”按钮。
'''
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#chromedriver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
#os.environ["webdriver.chrome.driver"] = chromedriver

browser = webdriver.Firefox()
browser.get('http://www.baidu.com')
#browser.save_screenshot("D:\\dmplay\\test\\baidu.png")
cookies =browser.get_cookies()
print(cookies)
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)