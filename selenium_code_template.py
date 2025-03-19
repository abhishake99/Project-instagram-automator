import time  
import random
import requests as rq
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from lxml import etree
import datetime
import pandas as pd
import re
import warnings
from tqdm import tqdm
import uuid
import urllib
import os
import subprocess
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import undetected_chromedriver as uc
warnings.filterwarnings("ignore")

def createwebdriver(driver):
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service

    service = Service(r"C:\chromedriver.exe")
    try:
        driver.close()
        driver.quit()
    except:
        pass
    
    print('in createwebdriver')
    chrome_options = Options()
    chrome_options.binary_location="C:\\chrome-win64\\chrome.exe"

    try:
        driver = webdriver.Chrome(service=service,options=chrome_options)
    except:
        print('IN EXCEPTION')
        service = Service(r"C:\olddriver\chromedriver.exe")
        driver = webdriver.Chrome(service=service,options=chrome_options)

    driver.maximize_window()
    driver.get('chrome://settings/')
    driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.7);')

    return driver

def driver_initialisation_translation():
    service = Service(executable_path='C:/chromedriver.exe')
    options = webdriver.ChromeOptions()
    # options.add_argument('--proxy-server={}'.format(curr_proxy))
    prefs = {
        "translate_whitelists": {"id":"en"},
        "translate":{"enabled":"true"}
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=service, options=options)
    # wait = WebDriverWait(driver,10)
    time.sleep(15)
    return driver

def driver_initialisation_normal():
    service = Service(executable_path='C:/chromedriver.exe')
    options = webdriver.ChromeOptions()
    # options.add_argument('--proxy-server={}'.format(curr_proxy))
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver,10)
    return driver

def driver_initialisation_undetected():
    
    options = uc.ChromeOptions()
    prefs = {"profile.default_content_settings.geolocation": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--deny-permission-prompts")
    driver = uc.Chrome(options=options)
    return driver

def mobile_emulation_driver(self):

    service = Service(executable_path='C://latest_chrome_driver//chromedriver.exe')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36')
    chrome_options.add_argument("--window-size=200,1000")
    chrome_options.page_load_strategy = 'eager'
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("force-device-scale-factor=1.5")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def driver_initialisation_profile(username='Administrator'):
    
    user_data_dir = "C:/Users/{0}/AppData/Local/Google/Chrome/User Data".format(username)
    profile_directory = "Profile 2"
    service = Service(executable_path='C:/latest_chrome_driver/chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument(f"--profile-directory={profile_directory}")
    options.add_argument("--no-sandbox")  # Add this
    options.add_argument("--disable-dev-shm-usage")  # Add this
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)
    return driver
