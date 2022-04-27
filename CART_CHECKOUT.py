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
    driver.find_element(By.XPATH, "//h2[contains(text(),'Boho Bangle Bracelet')]").click()
    # Add to cart
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    #ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    #Anchor Bracelet product
    driver.find_element(By.XPATH, "//h2[contains(text(),'Black Over-the-shoulder Handbag')]").click()
    # Add to cart
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    # ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    #GOLD CHAIN
    driver.find_element(By.XPATH, "// h2[contains(text(), 'Bright Gold Purse With Chain')]").click()
    # Add to cart
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    # ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.find_element(By.XPATH, "// h2[contains(text(), 'Bright Red Bag')]").click()
    # Add to cart
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    # ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "    //h2[contains(text(),'Buddha Bracelet')]").click()
    # Add to cart
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    # ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "// h2[contains(text(), 'Buddha Bracelet')]").click()
    sleep(3)
    # Add to cart
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    # ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    sleep(3)
    driver.quit()

def test_cart2checkout():
    driver = init()
    #ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Anchor Bracelet product
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add to cart button
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    #move to cart page
    driver.find_element(By.XPATH,"//div[contains(@class,'ast-site-header-cart-li')]//bdi[1]").click()
    #write unvalid coupon
    driver.find_element(By.XPATH,"// input[ @ id = 'coupon_code']").send_keys("g-unit")
    driver.find_element(By.XPATH, "//button[contains(text(),'Apply coupon')]").click()
    #Choose shipping method
    driver.execute_script("window.scrollTo(0,1000);")
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_local_pickup1']").click()
    driver.execute_script("window.scrollTo(0,800);")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_flat_rate3']").click()
    driver.execute_script("window.scrollTo(0,800);")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_flat_rate4']").click()
    driver.execute_script("window.scrollTo(0,800);")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_free_shipping2']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to checkout')]").send_keys(Keys.ENTER)
    driver.execute_script("window.scrollTo(0,800);")
    sleep(3)
    driver.quit()

def test_checkout():
    driver = init()
    # ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add Anchor Bracelet product to basket
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add to cart button
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    # move to cart page
    driver.find_element(By.XPATH,"//div[contains(@class,'ast-site-header-cart-li')]//bdi[1]").click()
    # Choose shipping method
    driver.execute_script("window.scrollTo(0,1000);")
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_free_shipping2']").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to checkout')]").send_keys(Keys.ENTER)
    sleep(2)
    driver.execute_script("window.scrollTo(0,200);")
    #Enter shipping details
    driver.find_element(By.XPATH, "//input[@id='billing_first_name']").send_keys("Emanuel")
    driver.find_element(By.XPATH, "//input[@id='billing_last_name']").send_keys("Maharat")
    driver.find_element(By.XPATH, "//input[@id='billing_company']").send_keys("YEMI")
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("YEMI")
    driver.find_element(By.XPATH, "//input[@id='billing_address_2']").send_keys("sharon 11")
    driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("3")
    driver.find_element(By.XPATH, "//input[@id='billing_postcode']").send_keys("5648")
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//input[@id='billing_city']").send_keys("Lod")
    driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("0539829892")
    driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("yemiker@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='ship-to-different-address-checkbox']").click()
    driver.find_element(By.XPATH, "//input[@id='ship-to-different-address-checkbox']").click()
    driver.find_element(By.XPATH, "//textarea[@id='order_comments']").send_keys("bla bla bla")
    #choose shipping method
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_local_pickup1']").click()
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_flat_rate3']").click()
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_flat_rate4']").click()
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_free_shipping2']").click()
    driver.find_element(By.XPATH, "//button[@id='place_order']").click()
    sleep(3)
    driver.quit()


