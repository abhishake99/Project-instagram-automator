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


def driver_initialisation():
    service = Service(executable_path='C:/chromedriver.exe')
    options = webdriver.ChromeOptions()
    # options.add_argument('--proxy-server={}'.format(curr_proxy))
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver,10)
    return driver

driver=driver_initialisation()