#To Do:
# - Secrets using the local file that isn't pushed to Github
# - Set up in Heroku & test (using var files to host the private data)
# - Find out how to track the success of the form fill (is there a server / browser response for success?)
# furure steps
	#- Django page with a form for creating new users (signup could be texting a DK number, which returns a one time code for entering the page, the data entered expires after 30 days)
	#- Texting the number with the text "Vaccinated" could also then remove a user that matches the phone number

from selenium import webdriver
import time

#variables with dummy fill data
name = 'Jokab Jacob'
age = '15'
address = 'Amager 2'
postcode = '2300'
phone = '11100223'

chromedriver_location = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chromedriver_location)

#options = webdriver.chrome.options.Options()
#options.add_argument("--disable-extensions") # optional and off-topic, but it conveniently prevents the popup 'Disable developer mode extensions' 
#driver = webdriver.Chrome(chrome_options=options)

###FIRST RUN###

driver.get('https://www.regionh.dk/presse-og-nyt/pressemeddelelser-og-nyheder/Sider/Tilmelding-til-at-modtage-overskydende-vaccine-mod-COVID-19.aspx')


#Page 1 - intro

page_submit = '/html/body/div/form/div[2]/div[3]/input'
driver.find_element_by_xpath(page_submit).click()

#Page 2 - name

fulde_navn = '//*[@id="t50100775"]'
driver.find_element_by_xpath(fulde_navn).send_keys(name)
driver.find_element_by_xpath(page_submit).click()

#Page 3 - age

alder = '//*[@id="n35965768"]'
driver.find_element_by_xpath(alder).send_keys(age)
driver.find_element_by_xpath(page_submit).click()

#Page 4 - address

addresse = '//*[@id="t50088645"]'
driver.find_element_by_xpath(addresse).send_keys(address)
driver.find_element_by_xpath(page_submit).click()

#Page 5 - postcode

postkode = '//*[@id="t50088674"]'
driver.find_element_by_xpath(postkode).send_keys(postcode)
driver.find_element_by_xpath(page_submit).click()

#Page 5 - phone

telefon = '//*[@id="n50088775"]'
driver.find_element_by_xpath(telefon).send_keys(phone)
driver.find_element_by_xpath(page_submit).click()

#Page 6 - centre choice (øksenhallen)

centre = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[6]/label'
driver.find_element_by_xpath(centre).click()
driver.find_element_by_xpath(page_submit).click()

#Page 7 - final submit

driver.find_element_by_xpath(page_submit).click()

driver.find_element_by_xpath(page_submit).click()

driver.delete_all_cookies()

time.sleep(8)

#driver.stop_client()
#driver.close()

###SECOND RUN###

driver.get('https://www.regionh.dk/presse-og-nyt/pressemeddelelser-og-nyheder/Sider/Tilmelding-til-at-modtage-overskydende-vaccine-mod-COVID-19.aspx')


#Page 1 - intro

page_submit = '/html/body/div/form/div[2]/div[3]/input'
driver.find_element_by_xpath(page_submit).click()

#Page 2 - name

fulde_navn = '//*[@id="t50100775"]'
driver.find_element_by_xpath(fulde_navn).send_keys(name)
driver.find_element_by_xpath(page_submit).click()

#Page 3 - age

alder = '//*[@id="n35965768"]'
driver.find_element_by_xpath(alder).send_keys(age)
driver.find_element_by_xpath(page_submit).click()

#Page 4 - address

addresse = '//*[@id="t50088645"]'
driver.find_element_by_xpath(addresse).send_keys(address)
driver.find_element_by_xpath(page_submit).click()

#Page 5 - postcode

postkode = '//*[@id="t50088674"]'
driver.find_element_by_xpath(postkode).send_keys(postcode)
driver.find_element_by_xpath(page_submit).click()

#Page 5 - phone

telefon = '//*[@id="n50088775"]'
driver.find_element_by_xpath(telefon).send_keys(phone)
driver.find_element_by_xpath(page_submit).click()

#Page 6 - centre choice (øksenhallen)

centre = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[2]/label'
driver.find_element_by_xpath(centre).click()
driver.find_element_by_xpath(page_submit).click()

#Page 7 - final submit

driver.find_element_by_xpath(page_submit).click()

driver.find_element_by_xpath(page_submit).click()

driver.delete_all_cookies()

time.sleep(3)

driver.stop_client()
driver.quit()