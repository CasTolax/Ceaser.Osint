import whois
import socket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time # gerekli kütüphabeler

domain_isim = input("bir domain isim girin: ")
domain_isim = domain_isim.replace("https://", "").strip("/")

driver = webdriver.Chrome() 
driver.get("https://www.google.com/")
time.sleep(5) 

try:
    search_box = driver.find_element(By.XPATH, "//textarea[@name='q']")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    search_box.send_keys("Selenium")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
     
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    print("arama başarılı")

except Exception as e:
    print("hata: ", e)
finally:
    driver.quit()
     
try:
       
    domain_bilgi = whois.whois(domain_isim) #whois kodları
    print(f"domain bilgisi: {domain_bilgi}")

    ip_adresi = socket.gethostbyname(domain_isim) #socket kodları
    print(f"{domain_isim} IP adresi: {ip_adresi}")
    
except Exception as e:
  
    print(f"hata: {e}")
