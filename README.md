# This program allows you to see how many alumni from your university work for a particular company or list of companies

## IMPORTANT: 
- DO NOT USE PERSONAL LINKEDIN ACCOUNT WHEN RUNNING THIS PROGRAM
- Before running program, make sure you have a non-primary LinkedIn account created and have logged into it in your chrome browser
- You will need to use a non-primary account in case the account gets locked out/restricted since LinkedIn doesn't like web scrapers ;)
- Many measures are taken in the code to prevent account getting locked out/restricted, but there is always a chance of the bot being recognized

## Dependencies
- Node.js: https://nodejs.org/en/download/
- Python: https://www.python.org/downloads/
- BeautifulSoup: https://www.geeksforgeeks.org/beautifulsoup-installation-python/
- Selenium: https://www.geeksforgeeks.org/how-to-install-selenium-in-python/
- Google Chrome: https://www.google.com/chrome/
- Chrome Driver: https://chromedriver.chromium.org/downloads
- Code Editor: https://code.visualstudio.com/Download (ex.)

## How to change companies
- Feel free to change the companies you want to search for in the `companies` object. Just make sure the company names is the correct company name from the LinkedIn URL (ex.  `lowe's-home-improvement` from the https://www.linkedin.com/company/lowe's-home-improvement/ url)
- 106 popular companies are already listed as an example

## How to change school
- To get desired school code for the URL complete the following steps (E.g.):
    1. Go to https://www.linkedin.com/company/att/people/ and search "Massachusetts Institute of Technology" 
    2. Click on "Massachusetts Institute of Technology" in the "Where they studied" section
    3. You should see the URL update. Get the five-digit code from the part of the URL that says "facetSchool"
    4. Replace five-digit code in the `school` variable in `LinkedInSearch.py`

## Other Notes
- Run by typing `python LinkedInSearch.py` in terminal
- Program will launch chrome tabs repeatedly and do quick searches to scrape the data. Don't interfere when program is running 
- Program takes about 4-5 seconds per company search on average computer speed
- When the program finishes running, there will be an outputted excel sheet in your project's directory including the results
