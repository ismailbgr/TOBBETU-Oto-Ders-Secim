import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# gereksiz uyarıları gizle
# versiyonlar sabitlendiği için ilerde deprecated olacak özellikler için uyarı veriyor
warnings.filterwarnings("ignore")

email = ""
password = ""
try:
    # emaili email.txt den oku
    with open("email.txt", "r") as f:
        email = f.read()
        f.close()

    # şifreyi password.txt den oku
    with open('pass.txt', 'r') as f:
        password = f.read()
        f.close()
except FileNotFoundError:
    print("email.txt veya pass.txt dosyaları bulunamadı.")
    exit()

# ana sayfaya git
driver.get("https://ubs.etu.edu.tr/")

# giriş yap tuşunun görünmesini bekle
wait = WebDriverWait(driver, 1000000)
login_button = wait.until(
    EC.visibility_of_element_located((By.ID, "btnLogin")))

# giriş yap
username_field = driver.find_element_by_id("txtLogin")
password_field = driver.find_element_by_id("txtPassword")
username_field.send_keys(email)
password_field.send_keys(password)

# giriş yap butonuna tıkla
login_button.click()

# okulun logosunun görünmesini bekle
wait = WebDriverWait(driver, 1000000)
school_logo = wait.until(EC.visibility_of_element_located(
    (By.ID, "ctl00_imgMusteriLogo")))

# ders seçim ekranına git
driver.get("https://ubs.etu.edu.tr/Ogrenci/Ogr0249/Default.aspx")

print("Ders Seçme işlemi bittikten sonra tarayıcıyı kapatabilirsiniz")

# chromeun açık kalması için sahte bekleme
wait = WebDriverWait(driver, 1000000)
course_selection_page = wait.until(
    EC.visibility_of_element_located((By.ID, "DummyId")))