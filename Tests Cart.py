from CART_CHECKOUT import  *

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
