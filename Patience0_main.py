#Source: https://stackoverflow.com/questions/38425450/automated-filling-of-web-form-from-a-list-in-python-using-selenium

#Import some magic from Hogwarts that I don't need to think about

from selenium import webdriver
import time
import random
from dotenv import load_dotenv
import os

#Global variables for making the magic happen

chromedriver_location = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chromedriver_location)

#Heritage from when I tried local environment variables (never again)

Credentials
load_dotenv('.env')

# Vaccine Centre Variables with the XPaths for the selection items from the list of available centres:

øksenhallen = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[6]/label'
bellacentre = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[2]/label'

#Arrays of "Patient" Lists pulled from the environment variables, personal data points for Name, Age, Address, choice of centre, etc.

patients = [

[client.run(os.getenv('PATIENT1'))],
[client.run(os.getenv('PATIENT2'))]

]

# For loop that contains the Selenium instructions, it will loop through each of the "Patient" arrays until there are none

	# Note that each step has a Sleep command that waits for a random duration of 2-4 seconds
	# I added this for "fun" as a (totally unessesary but "fun") obfuscation method in case there was anyone at Ramboll or Region H who wanted to find users who were using bots to fill in forms. The idea being that a normal user wouldn't complete a form in under 20 seconds.
	# There's also a delte cookies command for the same reason *shrugs with a "why not?" expression*

for patient in patients:

	# Command for opening the form URL

	driver.get('https://www.regionh.dk/presse-og-nyt/pressemeddelelser-og-nyheder/Sider/Tilmelding-til-at-modtage-overskydende-vaccine-mod-COVID-19.aspx')

	#Global variable for the Submit button on each page

	page_submit = '/html/body/div/form/div[2]/div[3]/input'

	#Page 1 - intro

	time.sleep(random.randint(2,4))
	driver.find_element_by_xpath(page_submit).click()

	#Page 2 - name
	fulde_navn = '//*[@id="t50100775"]'
	time.sleep(random.randint(2,4))	
	driver.find_element_by_xpath(fulde_navn).send_keys(patient[0])

	time.sleep(random.randint(2,4))
	driver.find_element_by_xpath(page_submit).click()

	#Page 3 - age
	alder = '//*[@id="n35965768"]'
	time.sleep(random.randint(2,4))	
	driver.find_element_by_xpath(alder).send_keys(patient[1])
	time.sleep(random.randint(2,4))
	driver.find_element_by_xpath(page_submit).click()
	
	#Page 4 - address
	addresse = '//*[@id="t50088645"]'
	time.sleep(random.randint(2,4))	
	driver.find_element_by_xpath(addresse).send_keys(patient[2])
	time.sleep(random.randint(2,4))
	driver.find_element_by_xpath(page_submit).click()
	
	#Page 5 - postcode
	postkode = '//*[@id="t50088674"]'
	time.sleep(random.randint(2,4))
	driver.find_element_by_xpath(postkode).send_keys(patient[3])
	time.sleep(random.randint(2,4))	
	driver.find_element_by_xpath(page_submit).click()
	
	#Page 6 - phone
	telefon = '//*[@id="n50088775"]'
	time.sleep(random.randint(2,4))
	driver.find_element_by_xpath(telefon).send_keys(patient[4])
	time.sleep(random.randint(2,4))
	driver.find_element_by_xpath(page_submit).click()

	#Page 7 - centre choice
	time.sleep(random.randint(2,4))
	driver.find_element_by_xpath(patient[5]).click()
	time.sleep(random.randint(2,4))
	driver.find_element_by_xpath(page_submit).click()

	#Page 8 & 9 - final submit
	time.sleep(random.randint(2,4))
	driver.find_element_by_xpath(page_submit).click()
	time.sleep(random.randint(2,4))
	driver.find_element_by_xpath(page_submit).click()
	time.sleep(random.randint(2,4))
	driver.delete_all_cookies()

#Once the arrays have been looped through the script waits a few seconds, deletes cookies and then quits. Quitting instead of closing should be the proper way to do it apparently to prevent something called "memory leaks"

time.sleep(random.randint(2,4))

driver.stop_client()
driver.quit()