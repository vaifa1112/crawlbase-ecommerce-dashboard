import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.tokopedia.com/p/otomotif/aksesoris-motor/aksesori-body-motor"

driver.get(url)

WebDriverWait(driver,20).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR,"div[data-testid='divProductWrapper']")
    )
)

time.sleep(3)

for i in range(10):

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    time.sleep(2)

cards = driver.find_elements(
    By.CSS_SELECTOR,
    "div[data-testid='divProductWrapper']"
)

print("Jumlah :",len(cards))

hasil = []

for card in cards:

    try:
        nama = card.find_element(
            By.CSS_SELECTOR,
            "span.css-20kt3o"
        ).text
    except:
        nama = "-"

    try:
        harga = card.find_element(
            By.CSS_SELECTOR,
            "div.css-1m96yvy"
        ).text
    except:
        harga = "-"

    try:
        lokasi = card.find_element(
            By.CSS_SELECTOR,
            "div.css-tpwv51"
        ).text
    except:
        lokasi = "-"

    try:
        link = card.find_element(
            By.XPATH,
            "./ancestor::a"
        ).get_attribute("href")
    except:
        link = "-"

    hasil.append({
        "Nama Produk":nama,
        "Harga":harga,
        "Lokasi":lokasi,
        "Link":link
    })

driver.quit()

df = pd.DataFrame(hasil)

print(df)

df.to_csv(
    "tokopedia.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Selesai")