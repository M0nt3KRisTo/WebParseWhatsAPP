from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import os.path
from os import path
from colorama import Fore, Back, Style
import colorama
import time
colorama.init(convert=True)


class colors():
	YEL = Fore.YELLOW
	RED = Fore.RED
	GREEN = Fore.GREEN
	RES = Fore.RESET
def checklogin():
	try:
	    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((
	        By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[4]/div/div/div[1]'
	    )))
	    return True
	except:
	    return False
print(colors.YEL + """
 __        ___           _                         
 \ \      / / |__   __ _| |_ ___  __ _ _ __  _ __  
  \ \ /\ / /| '_ \ / _` | __/ __|/ _` | '_ \| '_ \ 
   \ V  V / | | | | (_| | |_\__ \ (_| | |_) | |_) |
    \_/\_/  |_| |_|\__,_|\__|___/\__,_| .__/| .__/ 
                                      |_|   |_|    чекер номеров""")


driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://web.whatsapp.com/")
while(not checklogin()):
	print("[+] Для продолжения отсканируйте QR-код на смартфоне...")
	try:
	    WebDriverWait(driver, timeout=50).until(EC.presence_of_element_located((
	        By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[4]/div/div/div[1]'
	    )))
	    print(colors.GREEN + "[+] Вы успешно вошли [+]" + colors.GREEN)
	except:
	    print(colors.RED + "[-] Ошибка авторизации [-]" + colors.RED)
def checknumber(number):
	driver.get("https://web.whatsapp.com/send?phone="+number+"&text&app_absent=0")
	time.sleep(2)
	try:
		WebDriverWait(driver, timeout=30).until(EC.presence_of_element_located((
		By.XPATH, '//*[@id="side"]'
		)))
		try:
			WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((
			By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/header/div[1]/div/div/span'
			)))
			return True
		except:
			return False
	except:
			return False
def progress(count, total, suffix=''):
	bar_len = 60
	filled_len = int(round(bar_len * count / float(total)))
	percents = round(100.0 * count / float(total), 1)
	bar = '=' * filled_len + '-' * (bar_len - filled_len)
	sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
	sys.stdout.flush()
txtfile = False
while txtfile == False:
	txtfile_name=input("[!] Введите название файла с номерами в формате txt: [!]")
	txtfile=path.exists(txtfile_name)
my_file = open(txtfile_name, "r")
content_list ={x.replace("\n", "") for x in my_file.readlines()} 
total=len(content_list)
working=0
for idx, val in enumerate(content_list,start=1):
	progress(idx, total, suffix='Checking : ['+val+'] | Valid  : ['+str(working)+']')
	if checknumber(val):
		working+=1
		file_object = open('Хорошие_номера.txt', 'a')
		file_object.write(val+"\n")
		file_object.close()

print("Данные сохранены в файле 'Проверенные.txt'")
