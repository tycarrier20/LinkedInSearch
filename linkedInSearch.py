from bs4 import BeautifulSoup, re
from selenium import webdriver
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

# specify browser and load up page
browser = webdriver.Chrome(r"C:\Projects\selenium\selenium drivers\chromedriver", options=options)

# Define variables for url/searching
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

# companies = ['advanced-home-care', 'Aerotek']
school = "18798"
employeeTotals ={}

######
# Search by DEGREE

# degrees = [
#     "Business Administration and Management, General", "Accounting",
#     "Information Technology", "Computer Science","Finance, General",
#     "Marketing", "Economics", "Operations Management and Supervision",
#     "Business/Commerce, General", "Business, Management, Marketing, and Related Support Services",
#     "School of Business, Economics and Law at the University of Gothenburg",
#     "Accounting and Finance", "Organizational Leadership"
# ]

# def findDegrees():
#     # Find all listed degrees
#     html = browser.page_source
#     soup = BeautifulSoup(html, "lxml")
#     pageDescription = soup.title.text
#     print("TITLE: " + pageDescription)
    
#     # Select the div that contains list of fields of study
#     degreesPresent = soup.find_all("div", {"class": "artdeco-card p4 m2 org-people-bar-graph-module__field-of-study"})
   
#     # Convert html to string
#     for i in range(0, len(degreesPresent)):
#         degreesPresent[i] = degreesPresent[i].text
        
#     # Convert array to string
#     degreesPresentString = ""
#     for i in degreesPresent: 
#         degreesPresentString += i  
    
#     # Remove unnecessary instances and convert to array
#     degreesPresentArray = degreesPresentString.split('\n')

#     # Remove any irrelevant values in array
#     unwanted = {'', '          What they studied', '    Add', ' ', '        '}
#     degreesList = [e for e in degreesPresentArray if e not in unwanted]

#     # Extract numbers and convert to int array
#     numberOfDegrees = list(next(zip(*map(str.split, degreesList))))
#     for i in range(0, len(numberOfDegrees)): 
#         numberOfDegrees[i] = int(numberOfDegrees[i]) 
    
#     sumDegrees = sum(numberOfDegrees)

#     print (degreesList)
#     print(numberOfDegrees)
#     print(sumDegrees)
#     print(len(degreesList))
#     print(type(degreesList))


########

# Set Delay
def delay ():
    time.sleep(random.randint(1,2))

# Find total employees for company
def findEmployees(company,soup):
    total = soup.find("span", {"class": "t-20"})
    employeeTotals[company] = total.text.replace("employees","").strip()

# Export results to CSV
def exportCSV():
    with open('UNCG Employees (LinkedIn).csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Company", "Number of Employees"])
        for key, value in employeeTotals.items():
            writer.writerow([key, value])

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
        # browser.find_element_by_xpath("//button[@aria-label='Next']")\
        #     .click()
        # findDegrees()
        
# Initiate LinkedIn search
iterateCompanies()
print(employeeTotals)

# Export results to CSV
exportCSV()
browser.quit()

print("Search Complete..")

### NOTES

# Wendover Funding Inc. not on LinkedIn - no data for this company
# Create aggregates for joint companies like Truist+BB&T