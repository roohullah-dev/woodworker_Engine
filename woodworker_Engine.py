# *************************************** Setup ***************************************
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, csv, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 🏁 Basic Configuration
current_page = 1
max_pages = 5
product = 'salice'
search_term = product.replace(' ', '+')
url = f'https://www.woodworkerexpress.com/search.php?mode=search&page=1'

# 🌐 Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

# 🔍 Perform Product Search
search_bar = driver.find_element(By.ID, "posted_data_substring_main_search")
search_bar.send_keys(product)
search_bar.send_keys(Keys.ENTER)

# 📄 Wait for Search Results to Load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'item-box')))
driver.get(f"https://www.woodworkerexpress.com/search.php?mode=search&page={current_page}&posted_data[substring]={search_term}")

# *************************************** CSV Setup ***************************************
file_path = 'salice_Product.csv'
file_exists = os.path.exists(file_path)
existing_asins = set()

# ✅ Load Existing SKUs to Avoid Duplication
if file_exists:
    with open(file_path, 'r', encoding='utf-8') as rf:
        reader = csv.DictReader(rf)
        for row in reader:
            existing_asins.add(row['SKU'].strip())

# 📝 Open CSV File for Writing or Appending
with open(file_path, 'a' if file_exists else 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow([
            'Title', 'Price', 'SKU', 'Weight',
            'Manufacturer', 'Manufacturer_part',
            'product_url', 'Paragraph',
            *['bullet' + str(i) for i in range(1, 21)],
            *['image' + str(i) for i in range(1, 21)]
        ])

    # ****************************************************************************************
    # 🛡️ FULL SCRAPING LOGIC IS PROTECTED 🛡️
    # The following sections are hidden to protect the core automation engine:
    #
    # - Looping through all product boxes on the page
    # - Opening each product in a new browser tab
    # - Extracting product details (title, price, SKU, manufacturer, etc.)
    # - Checking for duplicate SKUs
    # - Downloading images with format validation
    # - Collecting bullet points and descriptions
    # - Writing structured data into the CSV file
    # - Handling broken links, popups, or missing elements
    # - Paginating through all result pages automatically
    #
    # ⚙️ Want access to the full engine? Let's work together.
    # 📧 Email: roohanitech121@gmail.com
    # 🎯 Fiverr: https://www.fiverr.com/roohullah2020/
    # ****************************************************************************************

# ✅ Quit Browser at End
driver.quit()
