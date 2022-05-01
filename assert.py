from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import *


driver = webdriver.Chrome("C:/webdeiver/chromedriver.exe")

def init():
    driver = webdriver.Chrome("C:/webdeiver/chromedriver.exe")
    driver.get("https://www.atid.store")
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver

def test_accessories():
    driver=init()
    #ACCOSSORIES PAGE
    driver.find_element(By.XPATH ,"//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    sleep(3)
    #Anchor Bracelet product
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    #Add to cart button
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    #ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    value = driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").get_attribute("innerText")
    assert value == "250.00 ₪"
    driver.quit()
"
