import sys
sys.path.append("/home/i1582/Downloads/Mayank_POM_assignment/Testing_Swag") 

from Config.config import *
from selenium import webdriver


def setUp():
    return webdriver.Chrome(executable_path=Config.CHROME_EXECUTABLE_PATH)

# def getDriver():
#     driver = setUp()
#     driver.get(Config.PROJECT_BASE_URL)