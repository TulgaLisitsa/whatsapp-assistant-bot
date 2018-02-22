
import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from xml.dom import minidom
from tqdm import tqdm
import datetime
from datetime import datetime

import os

browser = webdriver.Chrome("/home/oxygen_/Documents/chromedriver")

s = "https://web.whatsapp.com/"
browser.get(s)


time.sleep(5)

browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[3]/label/input').click()


time.sleep(10)

commands = ["/quote","/funfact","/time","/joke","/calc","/conv","/lyrics","/define","/news","/weather","/wikipedia"]

browser.find_element_by_xpath('//div[@class="_25Ooe"]/span[@title="BOT"]').click()

time.sleep(7)
print("loop")
while True:
	lst_cmd = browser.find_elements_by_xpath('//div[@class="_3zb-j ZhF0n"]/span[last()]')
	lst_cmd_text = lst_cmd[-1].text
	lst_timer = browser.find_elements_by_xpath('//span[@class="_3EFt_"][last()]')
	lst_time = lst_timer[-1].text
	ssstr = datetime.now().strftime('%I:%M')
	print(lst_time)
	if(ssstr[0] == str('0')):
		system_hr =ssstr[1:2]
	else:
		system_hr = ssstr[0:2]
	system_min = ssstr[3:5]
	if(len(lst_time) == 7):
		wht_hr = lst_time[0:1]
	else:
		wht_hr = lst_time[0:2]
	wht_min = lst_time[2:4]
	print(str(system_hr) + " " + str(system_min))
	print()
	print(str(wht_hr)+ " " +str(wht_min))
	if(system_hr == wht_hr and system_min == wht_min):
	# print(lst_cmd_text)
		if(lst_cmd_text == '/quote'):
			ele = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
			ele.send_keys("motherfucker!!")
			btn = browser.find_element_by_class_name("_2lkdt")
			btn.click()






# while(True):
# 	if(wht_hr == system_hr and wht_min == system_min):
# 		lst_cmd_text = str(browser.find_element_by_xpath('//div[@class="_3zb-j ZhF0n"]/span[last()]').text)
# 		if(lst_cmd_text == '/quote'):
# 			ele = browser.find_element_by_xpath('//div[@class="_3F6QL _2WovP"]')
# 			ele.click().send_keys("you got me!!")


time.sleep(1000000)
