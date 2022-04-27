from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome("C:/webdeiver/chromedriver.exe")
import unittest


driver.maximize_window()

def init():
    driver = webdriver.Chrome("C:/webdeiver/chromedriver.exe")
    driver.get("https://www.atid.store")
    driver.maximize_window()
    return driver

def test_store():
    driver=init()
    driver.get("https://www.atid.store")
    #select 2 items from store page
    #Store page
    driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]").click()
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    #Add to cart button
    driver.find_element(By.XPATH, "//html/body/div[1]/div[1]/div/div/main/div/div[2]/div[2]/form/button").click()
    driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]").click()
    #Assert value
    value = driver.find_element(By.XPATH ,"//body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/div[2]/span[2]/span[1]/bdi[1]").get_attribute('250.00')
    cart = driver.find_element(By.XPATH, "//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]/span[1]/span[1]/span[1]/bdi[1]").get_attribute('250.00')
    print(cart)
    print(value)
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//html/body/div[1]/header/div[1]/div[1]/div/div/div/div[2]/div/div/div/nav/div/ul/li[2]/a").click()
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//html/body/div/div[1]/div/div[2]/main/div/ul/li[2]/div[2]/a/h2").click()
    driver.execute_script("window.scrollTo(0,200);")
    #Add to cart
    driver.find_element(By.XPATH, "//html/body/div[1]/div[1]/div/div/main/div/div[2]/div[2]/form/button").click()


def test_men():
    driver=init()
    #select 2 items from men page
    driver.find_element(By.XPATH ,"//header/div[@id='ast-desktop-header']/div[1]/div[1]"
                                  "/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//h2[contains(text(),'ATID Blue Shoes')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    #Add to cart button
    driver.find_element(By.XPATH, "//html/body/div[1]/div[1]/div/div/main/div/div[2]/div[2]/form/button").click()
    value = driver.find_element(By.XPATH, "//h2[contains(text(),'ATID Blue Shoes')]").get_attribute("80.00")
    cart = driver.find_element(By.XPATH,"// body[1] / div[1] / header[1] / div[1] / div[1] / div[1] / div[1] "
                                        "/ div[1] / div[3] / div[3] / div[1] /div[1] / a[1] / span[1] / span[1] / span[1] / bdi[1]").get_attribute("80.00")
    assert value == cart
    driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]"
                                  "/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//html/body/div[1]/header/div[1]/div[1]/div/div/div/div[2]"
                                  "/div/div/div/nav/div/ul/li[2]/a").click()
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//h2[contains(text(),'ATID Green Shoes')]").click()
    #Add to cart
    driver.find_element(By.XPATH, "//html/body/div[1]/div[1]/div/div/main/div/div[2]/div[2]/form/button").click()
    driver.quit()

def test_women():
    driver=init()
    #select 2 items from men page
    #Store page
    driver.find_element(By.XPATH ,"//header/div[@id='ast-desktop-header']/div[1]/div[1]"
                                  "/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]").click()
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    #Add to cart button
    driver.find_element(By.XPATH, "//html/body/div[1]/div[1]/div/div/main/div/div[2]/div[2]/form/button").click()
    driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]"
                                  "/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]").click()
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//h2[contains(text(),'ATID Black Shoes')]").click()
    #Add to cart
    driver.find_element(By.XPATH, "//html/body/div[1]/div[1]/div/div/main/div/div[2]/div[2]/form/button").click()
    driver.quit()

def test_accessories():
    driver=init()
    #select 2 items from men page
    #Store page
    driver.find_element(By.XPATH ,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]"
                                  "/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]").click()
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//h2[contains(text(),'Boho Bangle Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    #Add to cart button
    driver.find_element(By.XPATH, "//html/body/div[1]/div[1]/div/div/main/div/div[2]/div[2]/form/button").click()
    driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]"
                                  "/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]").click()
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//h2[contains(text(),'Black Over-the-shoulder Handbag')]").click()
    #Add to cart
    driver.find_element(By.XPATH, "//html/body/div[1]/div[1]/div/div/main/div/div[2]/div[2]/form/button").click()
    driver.quit()