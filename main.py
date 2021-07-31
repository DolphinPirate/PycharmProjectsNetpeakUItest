from _ast import Assert
from selenium import webdriver

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("https://netpeak.ua/")
workInNetPeak = driver.find_element_by_link_text("Карьера")
workInNetPeak.click()
IwantWorkAtNetPeak = driver.find_elements_by_xpath("//a[contains(text(),'Я хочу работать в Netpeak')]")
IwantWorkAtNetPeak.click()
cvNetpeak = driver.find_elements_by_xpath("//input[@name='up_file']")
cvNetpeak.send_kays('./1.png')
driver.getPageSource().contains("Ошибка: данные файла не были переданы.")
driver.find_element_by_id('inputName').send_keys('Artem')
driver.find_element_by_id('inputLastname').send_keys('Medvynskyi')
driver.find_element_by_id('inputEmail').send_keys('medvynskyi.artem@gmail.com')
driver.find_element_by_name('by').is_selected('1996')
driver.find_element_by_name('bm').is_selected('январь')
driver.find_element_by_name('bd').is_selected('29')
driver.find_elements_by_id('inputPhone').send_kays('380671190166')
driver.find_element_by_id('submit').click()
Assert.assertEquals(driver.getPageSource().contains("Все поля являются обязательными для заполнения"))
driver.find_element_by_xpath("//a[contains(text(),'Курсы')]").click()


