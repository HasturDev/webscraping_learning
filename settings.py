## settings.py

# for Chrome driver 
from shutil import which
  
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['--headless']  

DOWNLOADER_MIDDLEWARES = {
    'domain_scraper.selenium_middleware.SeleniumMiddleware': 800,
}
