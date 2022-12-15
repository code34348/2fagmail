import time, os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
print('Enter the gmail and password with space between in one line:')
gmailId, passWord = map(str, input().split())

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.gmail.com")
driver.find_element_by_name("identifier").send_keys(gmailId)
driver.find_element_by_id("identifierNext").click()
time.sleep(1);
driver.find_element_by_name("password").send_keys(passWord)
driver.find_element_by_id("passwordNext").click()
while not os.path.exists(codePath):
    time.sleep(1)
fcode = open(codePath, "r")
code = fcode.readline()
driver.find_element_by_name("idvPin").send_keys(code.split("\n")[0])
driver.find_element_by_id("idvPreregisteredPhoneNext").click()


