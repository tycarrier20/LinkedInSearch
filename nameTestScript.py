from bs4 import BeautifulSoup, re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time
from time import sleep

# Define options
options = webdriver.ChromeOptions() 
options.add_argument(r"user-data-dir=C:\Users\sport\AppData\Local\Google\Chrome\User Data")

# specify browser and load up page
browser = webdriver.Chrome(r"C:\Projects\selenium\selenium drivers\chromedriver", options=options)

school = "18798"

new_data= ['ALDI', 'Allegacy-Federal-Credit-Union', 'Allen-Tate-Companies', 'apexanalytix', 'ARCH-MI', 'BCBSNC', 'Bernard-Robinson-&-Company', 'Charles-Aris-Executive-Search', 'Corning', 'Daimler-Trucks-NA', 'DelHaize', 'Ennis-Flint', 'Epes-Companies', 'General-Electric-Co.', 'Hanesbrands-Inc.', 'Heritage-Home-Group', "Lowe's-Companies,-Inc.", 'Market-America', 'nCino', 'NGIC', 'Novant-Health', 'ODFL', 'Procter-And-Gamble-Company', 'Qorvo,-Inc.', 'Reynolds-American-Inc.', 'Speedway', 'Truliant', 'U.S.-Department-of-Veterans-Affairs', 'United-Healthcare', 'US-Postal-Service', 'Volvo-Group-NA', 'Wake-Forest-Baptist-Health', 'Wells-Fargo', 'Wendover-Funding-Inc.', 'XPO-Logistics,-Inc.']

data = ["Advanced Homecare",
"Aerotek/TEKsystems",
"ALDI",
"Allegacy Federal Credit Union",
"Allen Tate Companies",
"Amazon",
"American Express",
"apexanalytix",
"ARCH MI",
"AT&T",
"Bank of America",
"BASF",
"BB&T/Truist",
"BCBSNC",
"Belk",
"Bernard Robinson & Company",
"Center for Creative Leadership",
"Charles Aris Executive Search",
"Charter Communications",
"Cisco",
"Citrix",
"City of Greensboro",
"Coldwell Banker",
"Collins Aerospace",
"Cone Health",
"Corning",
"Culp",
"Daimler Trucks NA",
"DelHaize",
"Deloitte",
"Dixon Hughes Goodman LLP",
"Duke Energy Corporation",
"Ecolab",
"Edward Jones",
"Ennis Flint",
"Enterprise",
"Epes Companies",
"EY",
"Fastenal",
"Fedex",
"Fidelity Investments",
"Fresh Market",
"General Electric Co.",
"Gilbarco",
"Glen Raven",
"Haeco",
"Hanesbrands Inc.",
"Harris Teeter",
"Herbalife",
"Heritage Home Group",
"IBM",
"Infosys",
"Inmar",
"International Textile Group",
"ITG",
"Kayser-Roth Corporation",
"KPMG",
"LabCorp",
"Lenovo",
"LGS/CACI",
"Lincoln Financial Group",
"Lowe's Companies, Inc.",
"LPL Financial",
"Market America",
"MetLife",
"Microsoft",
"nCino",
"NetApp",
"NGIC",
"Northwestern Mutual",
"Novant Health",
"ODFL",
"PepsiCo",
"PNC Bank",
"PPD",
"Precision Fabrics Group",
"Procter And Gamble Company",
"Progress Energy",
"PWC",
"Qorvo, Inc.",
"Ralph Lauren",
"Red Hat",
"Renfro Corporation",
"Reynolds American Inc.",
"RSM US LLP",
"RTI International",
"SAS",
"Sealy",
"Sears",
"SECU",
"Speedway",
"Syngenta",
"Tanger",
"Target",
"TE Connectivity",
"TIAA",
"Time Warner Cable/Spectrum",
"Truliant",
"U.S. Department of Veterans Affairs",
"UNIFI",
"United Healthcare",
"UPS",
"US Army",
"US Postal Service",
"USAIR",
"Vanguard",
"Verizon",
"VF Corporation/Kontoor",
"Volvo Group NA",
"Wake Forest Baptist Health",
"Walmart",
"Wells Fargo",
"Wendover Funding Inc.",
"XPO Logistics, Inc."
]

data3 = ['Advanced-Homecare', 'Aerotek/TEKsystems', 'Amazon', 'American-Express', 'AT&T', 'Bank-of-America', 'BASF', 'BB&T/Truist', 'Belk', 'Center-for-Creative-Leadership', 'Charter-Communications', 'Cisco', 'Citrix', 'City-of-Greensboro', 'Coldwell-Banker', 'Collins-Aerospace', 'Cone-Health', 'Culp', 'Deloitte', 'Dixon-Hughes-Goodman-LLP', 'Duke-Energy-Corporation', 'Ecolab', 'Edward-Jones', 'Enterprise', 'EY', 'Fastenal', 'Fedex', 'Fidelity-Investments', 'Fresh-Market', 'Gilbarco', 'Glen-Raven', 'Haeco', 'Harris-Teeter', 'Herbalife', 'IBM', 'Infosys', 'Inmar', 'International-Textile-Group', 'ITG', 'Kayser-Roth-Corporation', 'KPMG', 'LabCorp', 'Lenovo', 'LGS/CACI', 'Lincoln-Financial-Group', 'LPL-Financial', 'MetLife', 'Microsoft', 'NetApp', 'Northwestern-Mutual', 'PepsiCo', 'PNC-Bank', 'PPD', 'Precision-Fabrics-Group', 'Progress-Energy', 'PWC', 'Ralph-Lauren', 'Red-Hat', 'Renfro-Corporation', 'RSM-US-LLP', 'RTI-International', 'SAS', 'Sealy', 'Sears', 'SECU', 'Syngenta', 'Tanger', 'Target', 'TE-Connectivity', 'TIAA', 'Time-Warner-Cable/Spectrum', 'UNIFI', 'UPS', 'US-Army', 'USAIR', 'Vanguard', 'Verizon', 'VF-Corporation/Kontoor', 'Walmart', 'EnnisFlint', 'MarketAmerica', 'NovantHealth', 'UnitedHealthcare', 'WellsFargo', 'aldi-usa', 'allegacy', 'allentate', 'apex-analytix', 'arch-u-s-mortgage-insurance', 'bluecrossnc', 'bernard-robinson-&-company-llp', 'charles-aris-inc-', 'corning-incorporated', 'daimler_trucks_north_america', 'ahold-delhaize', 'epes-transport-system-llc', 'ge', 'hanesbrands-inc-', 'furniture-brands-international', "lowe's-home-improvement", 'ncino-inc-', 'national-general-insurance', 'old-dominion-freight-line', 'procter-and-gamble', 'qorvo', 'rj-reynolds', 'speedway-llc', 'truliant-federal-credit-union', 'department-of-veterans-affairs', 'usps', 'volvo-group', 'wake-forest-baptist-health-edu', 'xpologistics']

# companies = [sub.replace('-', '') for sub in data3]
companies = data3
print(len(companies))
workingNames = []
badNames = []

for company in companies: 
    
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get("https://www.linkedin.com/company/"+company+"/people/?facetSchool="+school)
    
    # Define soup
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    pageDescription = soup.title.text
    if (pageDescription == "(18) Page Not Found | LinkedIn"):
        badNames.append(company)
    else:
        workingNames.append(company)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    

print("Bad Names:")
print(badNames)

print("Working Names:")
print(workingNames)


        