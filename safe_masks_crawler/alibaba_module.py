from selenium import webdriver
from random import randint
import time
from selenium.webdriver.common.by import By
import random
import string
import os,sys
from selenium.webdriver.common.action_chains import ActionChains
from pyvirtualdisplay import Display
from selenium.common.exceptions import NoSuchElementException



class crawler:

    def init(url):
        self.url = str(url)


    #chooses PROXY AFTER EACH OTHER
    def randomproxy():
        file = open("./bin/proxy.txt")
        for line in file:
            fields = line.split(";")
        return random.choice(fields)
    ###################################################################################################    

    #checks if Shadow Ban is ON
    def has_error(browser):
        try:
            browser.find_element_by_xpath(("//p[contains(.,'Sorry')]"))
            return False
        except: return True

        if not has_error(browser):
            print('Error found! , aborted!')
            browser.quit()
            os.execv(sys.executable, ['python'] + sys.argv)   
    ###################################################################################################         

    def crawl(url):
        #print("We are now using this proxy:" + randomproxy())

        chrome_option = webdriver.ChromeOptions()
        #chrome_option.add_argument('--proxy-server=%s' % randomproxy())
        # #hrome_option.add_argument('--headless') ,service_args=['--verbose', '--log-path=/tmp/chromedriver.log']
        # display = Display(visible=0, size=(1024, 768))
        # display.start()
        
        browser = webdriver.Chrome("./safe_masks_crawler/bin/chromedriver",options=chrome_option)
        action_chains = ActionChains(browser)

        ##checks if theres internet
        def has_connection(browser):
            try:
                browser.find_element_by_xpath('//span[@jsselect="heading" and @jsvalues=".innerHTML:msg"]')
                return False
            except: return True
        ###################################################################################################

        ##url passed 
        browser.get(url)
        ###################################################################################################


        #if no internet then restart program
        if not has_connection(browser):
            print('No Internet connection, aborted!')
            browser.quit()
            os.execv(sys.executable, ['python'] + sys.argv)
        ##################################################################################################
        time.sleep(2) #time.sleep count can be changed depending on the Internet speed.

        #Saves the picture url of product into variable picture_url 
        picture_field = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/div[1]/div[3]/div/div[1]/div/div[2]/div[1]/div/a/img')
        picture_url = picture_field.get_attribute('src')
        print(picture_url)
        ##################################################################################################
        time.sleep(2) #time.sleep count can be changed depending on the Internet speed.

        ##Saves the name of the manufacturer into variable manufacturer_name
        manufacturer_field = browser.find_element_by_xpath('//*[@id="shopping-ads"]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/a')
        manufacturer_name = manufacturer_field.get_attribute('title')
        print(manufacturer_name)
        ##################################################################################################
        time.sleep(2) #time.sleep count can be changed depending on the Internet speed.        
