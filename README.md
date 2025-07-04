--------------------------------------🧰 WoodworkerExpress Scrapping Engine--------------------------------------
A smart Python scraper designed to extract detailed product information and high-resolution images from WoodworkerExpress.com. This automation script uses Selenium to browse product listings, extract essential product details, capture image URLs, and store them neatly into a CSV file.

⚙️ Features:                                                                                                                                                        
🔍 Product Detail Scraper                                                                                                                                            
Extracts: Title, Price, SKU, Weight, Manufacturer, Manufacturer's Part, Paragraph Description, Bullets, and Images.                                     
📸 Image Scraper with Format Filtering                                                                                                  
Downloads only clean product images by avoiding videos, documents, and corrupted URLs.                                                                                       
🧠 Duplicate Detection                                                                                                              
Skips previously scraped SKUs to prevent redundancy.                                                                                     
📄 Structured CSV Export                                                                                                   
Data is saved in a structured CSV format (salice_Product.csv) with up to 20 bullets and 20 image links per product.                                                                          
➡️ Multi-Page Navigation                                                                                                
Scrapes from one page to another up to the desired number of pages.                                                                                             
🖼️ Multi-Tab Handling                                                                                                       
Opens product links and image links in new tabs, mimicking natural behavior.                                                                                             
❌ Popup/Image Error Handling                                                                                                            
Detects and safely handles missing data, broken images, or unsupported formats.                                                                                     

🛠️ Technologies Used:                                                                                                 
Python 3.9+                                                                         
Selenium WebDriver                                                                                                                
ChromeDriver                                                                                                                      
WebDriver Manager (optional)                                                                                                 
CSV (for storage)                                                                                             
XPath / Class Selectors                                                                            
Smart Delays (time.sleep, WebDriverWait)                                                                                                            

🚀 How It Works                                                                                                                                         
---> Starts browser and performs a keyword search (e.g. salice).                                                                                               
---> Scrapes each product on the page.                                                                                                                                 
---> Opens product details in a new tab.                                                                                                                             
---> Collects all relevant information (text + images).                                                                                                                         
---> Skips duplicates based on SKU.                                                                                                                     
---> Saves all to a local CSV file.                                                                                                                   
---> Clicks next page and repeats the process.                                                                                                               

📩 Hire Me:                                                                                                                                                        
Need a custom scraping tool like this for your e-commerce needs?                                                                                        
✅ Amazon | ✅ AliExpress | ✅ eBay | ✅ Shopify | ✅ Etsy

📧 Email: roohanitech121@gmail.com
🎯 Fiverr: https://www.fiverr.com/users/roohullah2020/

🌟 Let’s Automate Your Scraping Tasks!                                                                                                        
Efficient scraping saves time, money, and effort. Whether you're a seller, researcher, or competitor analyst — this tool can be your data powerhouse! 💼📊
