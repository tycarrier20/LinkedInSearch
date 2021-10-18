from bs4 import BeautifulSoup, re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import requests
import time
import random
import string
import csv
import ast

# Define options
options = webdriver.ChromeOptions() 
options.add_argument(r"user-data-dir=C:\Users\sport\AppData\Local\Google\Chrome\User Data")

# specify settings to reduce bot suspicion
options.add_argument("--start-maximized")
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

# add working user-agent
userAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
options.add_argument("user-agent="+userAgent)

# specify the location of chromedriver
browser = webdriver.Chrome(r"C:\Projects\Python\LinkedInSearch\selenium\selenium drivers\chromedriver", options=options)

# remove navigator webdriver flag to reduce bot detection
browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Define companies for url/searching
# Make sure to get the correct company name from the company's LinkedIn URL
companies = [
    'advanced-home-care', 'Aerotek', 'Amazon', 'American-Express', 'att', 'Bank-of-America', 
    'BASF', 'BB&T', 'Belk', 'Center-for-Creative-Leadership', 'Charter-Communications', 'Cisco', 
    'Citrix', 'City-of-Greensboro', 'Coldwell-Banker', 'Collins-Aerospace', 'Cone-Health', 'Culp', 'Deloitte', 
    'Dixon-Hughes-Goodman-LLP', 'Duke-Energy-Corporation', 'Ecolab', 'Edward-Jones', 'enterprise-rent-a-car', 'Ernstandyoung', 
    'Fastenal', 'Fedex', 'Fidelity-Investments', 'The-Fresh-Market', 'gilbarco-veeder-root', 'Glen-Raven', 'haeco-americas', 
    'Harris-Teeter', 'Herbalife', 'IBM', 'Infosys', 'Inmar', 'International-Textile-Group', 'itg-brands', 
    'Kayser-Roth-Corporation', 'KPMG', 'LabCorp', 'Lenovo', 'caci-international-inc', 'Lincoln-Financial-Group', 
    'LPL-Financial', 'MetLife', 'Microsoft', 'NetApp', 'Northwestern-Mutual', 'PepsiCo', 'PNC-Bank', 
    'PPD', 'PrecisionFabricsGroup', 'PWC', 'Ralph-Lauren', 'Red-Hat', 'Renfro-Corporation', 
    'RSM-US-LLP', 'RTI-International', 'SAS', 'Sealy', 'Sears', 'SECU', 'Syngenta', 'tanger-factory-outlet-centers-inc-', 'Target', 
    'TE-Connectivity', 'TIAA', 'Time-Warner-Cable', 'Spectrum', 'unifi-inc.', 'UPS', 'US-Army', 'american-airlines', 'Vanguard', 
    'Verizon', 'VF-Corporation','kontoor-brands','Walmart', 'EnnisFlint', 'market-america-inc-', 'NovantHealth', 'unitedhealth-group', 
    'WellsFargo', 'aldi-usa', 'allegacy', 'allentate', 'apex-analytix', 'arch-u-s-mortgage-insurance', 'bluecrossnc', 
    'bernard-robinson-&-company-llp', 'charles-aris-inc-', 'corning-incorporated', 'daimler_trucks_north_america', 
    'ahold-delhaize', 'epes-transport-system-llc', 'ge', 'hanesbrands-inc-', 'truistfinancialcorporation',
    "lowe's-home-improvement", 'ncino-inc-', 'national-general-insurance', 'old-dominion-freight-line', 
    'procter-and-gamble', 'qorvo', 'rj-reynolds', 'speedway-llc', 'truliant-federal-credit-union', 
    'department-of-veterans-affairs', 'usps', 'volvo-group', 'wake-forest-baptist-health-edu', 'xpologistics'
]

# Specify school by getting the school code from LinkedIn URL (facetSchool in URL)
school = "18798"
employeeTotals ={}

# Set Delay
def delay ():
    time.sleep(random.randint(1,2))

# Find total employees for company
def findEmployees(company,soup):
    total = soup.find("span", {"class": "t-20"})
    employeeTotals[company] = total.text.replace("employees","").strip()

# Loop urls
def iterateCompanies():
    for company in companies: 
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[1])
        browser.get("https://www.linkedin.com/company/"+company+"/people/?facetSchool="+school)
        delay()
        html = browser.page_source
        soup = BeautifulSoup(html, "lxml")
        findEmployees(company, soup)
        delay()
        browser.close()
        browser.switch_to.window(browser.window_handles[0])

# Export results to CSV
def exportCSV():
    with open('School Employees.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Company", "Number of Employees"])
        for key, value in employeeTotals.items():
            writer.writerow([key, value])

# Initiate LinkedIn search and print results to console
iterateCompanies()
print(employeeTotals)

# Export results to CSV
exportCSV()
browser.quit()

print("Search Complete..")