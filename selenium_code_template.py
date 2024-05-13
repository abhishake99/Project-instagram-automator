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

driver=driver_initialisation_normal()
