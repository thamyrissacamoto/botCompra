import pyautogui
import pygame
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 


#Path para abrir o Chrome
driver = webdriver.Chrome(executable_path=r"") 

#Link
driver.get("https://www.amazon.com/")

#Informações
username = ""
password = ""

VALOR_MAX = 1100.00

driver.find_element_by_xpath("//*[@id='nav-signin-tooltip']/a/span").click()

# Login
user = driver.find_element_by_xpath("//*[@id='ap_email']") 
user.clear() 
user.send_keys(username)
driver.find_element_by_xpath("//*[@id='continue']").click()

time.sleep(0.001)
passw = driver.find_element_by_xpath("//*[@id='ap_password']")
passw.clear()
passw.send_keys(password)
driver.find_element_by_xpath("//*[@id='signInSubmit']").click()

pyautogui.hotkey("ctrlleft", "w")
driver.get("https://www.amazon.com/ASUS-GeForce-Graphics-DisplayPort-Bearings/dp/B08HH5WF97/ref=sr_1_1?dchild=1&keywords=ASUS+TUF+Gaming+NVIDIA+GeForce+RTX+3080+OC+Edition+Graphics+Card-+PCIe+4.0%2C+10GB+GDDR6X%2C+HDMI+2.1%2C+DisplayPort+1.4a%2C+Dual+Ball+Fan+Bearings&qid=1622000953&s=electronics&sr=1-1")

time.sleep(1)
disponivel = False
while not disponivel:
    try:
        driver.find_element_by_xpath("//*[@id='outOfStock']")
        #driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[8]/div[4]/div[1]/div[4]/div/div/div/form/div/div/div[4]/div[1]/span/span/input") 
        print("\nIh, não foi dessa vez :(")
        time.sleep(0.001)
        driver.refresh()      
    except:
        comprar = driver.find_element_by_id("buy-now-button")
        valor = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[9]/div[4]/div[1]/div[4]/div/div/div/form/div/div/div/div/div[2]/div/span[1]')
        valor = float(valor.text.replace('$', ''))
        print("\nValor:", valor)
        if valor <= VALOR_MAX:
            pygame.init()
            pygame.mixer.music.load("01.mp3")
            pygame.mixer.music.play()
            pygame.event.wait()
            time.sleep(2)
            print("BORAAA COMPRAR :)")
            comprar.click()
            disponivel = True
        else:   
            print("Muito caro, cê ta doido\n")
            disponivel = False
            break



#Para TESTE, deixar DESLIGADO
buy = driver.find_element_by_xpath("//*[@id='turbo-checkout-pyo-button']")
buy.click()
print("Compra feita com sucesso\n")
