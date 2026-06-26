import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# =====================================
# KONFIGURASI CHROME
# =====================================

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")
wait = WebDriverWait(driver, 20)

# =====================================
# URL
# =====================================

url = "https://www.tokopedia.com/p/otomotif/aksesoris-motor/aksesori-body-motor"
driver.get(url)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='divProductWrapper']")))
time.sleep(5)

# =====================================
# AUTO SCROLL  (hanya sekali di awal)
# =====================================

def auto_scroll(scroll_count=20):
    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(scroll_count):
        print(f"Scroll {i+1}")
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print("Scroll selesai")

# =====================================
# FUNGSI SCRAPE  (dengan stale retry)
# =====================================

def scrape_page():
    hasil = []

    # Re-fetch cards setiap kali fungsi dipanggil agar tidak stale
    cards = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='divProductWrapper']")
    print(f"Jumlah Card : {len(cards)}")

    for i, card in enumerate(cards):
        # ---- Retry wrapper untuk StaleElementReferenceException ----
        for attempt in range(3):
            try:
                try:
                    nama = card.find_element(By.CSS_SELECTOR, "span.css-20kt3o").text
                except:
                    nama = "-"

                try:
                    harga = card.find_element(By.CSS_SELECTOR, "div.css-1m96yvy").text
                except:
                    harga = "-"

                try:
                    link = card.find_element(By.XPATH, "./ancestor::a").get_attribute("href")
                except:
                    link = "-"

                semua = card.text.split("\n")  # <-- baris yang sering stale

                rating  = "-"
                terjual = "-"
                toko    = "-"
                lokasi  = "-"

                for t in semua:
                    if "terjual" in t.lower():
                        terjual = t
                    try:
                        float(t)
                        rating = t
                    except:
                        pass

                # Lokasi
                for t in semua:
                    for keyword in ["kab", "kota", "jakarta", "bandung",
                                    "surabaya", "bekasi", "tangerang", "depok"]:
                        if keyword in t.lower():
                            lokasi = t
                            break
                    if lokasi != "-":
                        break

                # Nama toko (baris sebelum lokasi)
                if lokasi != "-":
                    try:
                        idx  = semua.index(lokasi)
                        toko = semua[idx - 1] if idx > 0 else "-"
                    except:
                        toko = "-"

                hasil.append({
                    "Nama Produk": nama,
                    "Harga":       harga,
                    "Rating":      rating,
                    "Terjual":     terjual,
                    "Toko":        toko,
                    "Lokasi":      lokasi,
                    "Link":        link,
                })
                break  # sukses, keluar dari retry loop

            except StaleElementReferenceException:
                print(f"  [WARN] Card {i} stale, retry {attempt+1}/3...")
                time.sleep(1)
                # Re-fetch seluruh card list lalu ambil index yang sama
                cards = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='divProductWrapper']")
                if i < len(cards):
                    card = cards[i]
                else:
                    break  # card sudah hilang dari DOM

    return hasil

# =====================================
# MULTI HALAMAN
# =====================================

SEMUA_DATA   = []
TOTAL_HALAMAN = 5

for page in range(TOTAL_HALAMAN):
    print("=" * 60)
    print(f"HALAMAN {page + 1}")

    # Scroll hanya di halaman pertama; di halaman berikutnya cukup tunggu load
    if page == 0:
        auto_scroll(20)
    else:
        time.sleep(5)

    data = scrape_page()
    SEMUA_DATA.extend(data)
    print(f"Total sementara : {len(SEMUA_DATA)}")

    try:
        tombol = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Laman berikutnya']")
        driver.execute_script("arguments[0].click();", tombol)
        time.sleep(5)
    except:
        print("Sudah halaman terakhir")
        break

driver.quit()

# =====================================
# SIMPAN HASIL
# =====================================

df = pd.DataFrame(SEMUA_DATA)
df.drop_duplicates(subset="Link", inplace=True)

df.to_csv("tokopedia_aksesorisMotor.csv",   index=False, encoding="utf-8-sig")
df.to_excel("tokopedia_aksesorisMotor.xlsx", index=False)

print("=" * 60)
print(df.head())
print()
print(f"TOTAL DATA : {len(df)}")
print("CSV berhasil")
print("Excel berhasil")