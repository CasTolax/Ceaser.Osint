#algoritması :
#ana menü gelir ve kullanıcı seçer
#işlem seçildikten sonra istediği özelliği yazar veya kullanır
#terminale sonucu çıkartır
#ve ana menüye dönmesi için seçenek oluşturulur
#ve kullanıcı istediği seçeneği tekrar tıklar


import pyfiglet
import time
import socket
import whois
from ipwhois import IPWhois
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import init, Fore, Style

init()
ascii_banner = pyfiglet.figlet_format("Ceaser")
print(ascii_banner)
print(Fore.LIGHTRED_EX + "A small piece of software, but full of great knowledge.")
print(Fore.RED + "Eğer Selenium ile arama yapacaksanız, lütfen URL'i başta giriniz.")
url = input(Fore.RED + "Tarama için bir URL girin (örn: https://www.google.com): ")

def baslatmaMenu():
    print("1. IP Adres Sorgulama(site)")
    print("2. Selenium ile Web Tarama")
    print("3. Web Driver Bilgisi")
    print("4. Çıkış")
    baslat = input("İstediğiniz seçeneği girin 1/2/3/4: ")
    return baslat

def ipAdresSorgulama():
    try:
        domain_isim = input("Bir domain ismi girin: ")
        domain_isim = domain_isim.replace("https://", "").replace("http://", "").strip("/")
        ip = input("IP girin: ")
        ipwhois = IPWhois(ip)
        result = ipwhois.lookup_rdap()
        domain_bilgi = whois.whois(domain_isim)
        print(f"Domain bilgisi: {domain_bilgi}")

        ip_adresi = socket.gethostbyname(domain_isim)
        print(f"Domain'in IP adresi: {ip_adresi}")
        print(result)
        print("Program sonlandırıldı.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

def seleniumIleWebTarama():
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(5)

        wait = WebDriverWait(driver, 5)
        page_url = driver.current_url
        print(f"Sayfa URL'si: {page_url}")
        body_content = driver.find_element("tag name", "body").text[:300]
        print(f"Sayfa içeriği (ilk 300 karakter): {body_content}")
        headings = driver.find_elements(By.TAG_NAME, "h1")
        for heading in headings:
            print(f"Başlık (h1): {heading.text}")

        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        arama = input("Arama kısmına ne yazılsın?: ")
        search_box.send_keys(arama)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        print("Arama başarıyla tamamlandı")
        print(driver.title)
        driver.quit()
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def webDriverBilgisi():
    print("""driver'lar kısaca senin istediğin web sitesini inceler ve kısaca sana bilgi sunar,ne zaman kuruldu?,kim tarafından?,nerede? ve ayrıca
çıkan ip adresini "IP adresini sorgulama" yerinden ip adresinin bilgilerini alabilirsin""")

def programiBaslat():
    while True:
        baslat = baslatmaMenu()

        if baslat == "1":
            ipAdresSorgulama()
            break
        elif baslat == "2":
            seleniumIleWebTarama()
            break
        elif baslat == "3":
            webDriverBilgisi()
            break
        elif baslat == "4":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz giriş, lütfen tekrar deneyin.")

# Programı başlat
programiBaslat()




    
     
    

 