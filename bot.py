from time import sleep
from secrets import pw,email
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)    
class Bot(): 

    def __init__(self):
        self.login(email,pw)
        
    def login(self,username,password):
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get('https://www.facebook.com/')
        sleep(5)
        
        email_text = self.driver.find_element_by_id('email')
        email_text.send_keys(username)

        pass_text = self.driver.find_element_by_id('pass')
        pass_text.send_keys(password)

        pass_text = self.driver.find_element_by_xpath('//button[@class="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy"]')
        pass_text.submit()
        sleep(3)
        
        postarea=self.driver.find_element_by_xpath("//div[@class='m9osqain a5q79mjw gy2v8mqq jm1wdb64 k4urcfbm qv66sw1b']")
        postarea.click()
        sleep(3)
        activepostarea=self.driver.switch_to_active_element()
        activepostarea.send_keys("Hello Programmer")
        
        button=self.driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 d1544ag0 tw6a2znq s1i5eluu tv7at329']")
        button.click()
    


def main():
    while True:
        my_bot = Bot()
        sleep(60*60) # one hour
if __name__ == '__main__':
    main()
            
            
            
