#Source: https://stackoverflow.com/questions/38425450/automated-filling-of-web-form-from-a-list-in-python-using-selenium
from selenium import webdriver
import time
import random
chromedriver_location = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chromedriver_location)

#Centre Variables:
øksenhallen = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[6]/label'
bellacentre = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[2]/label'

#patient lists
patients = [

['Jokab Jacob', '11', 'Amager 44, 2TV', '2311', '35263845',øksenhallen],
['Johkim Samson', '12', 'Vanløsevej 44, ST TH', '1921', '37282930',bellacentre]

]

for patient in patients:

	driver.get('https://www.regionh.dk/presse-og-nyt/pressemeddelelser-og-nyheder/Sider/Tilmelding-til-at-modtage-overskydende-vaccine-mod-COVID-19.aspx')

	#Page 1 - intro
	page_submit = '/html/body/div/form/div[2]/div[3]/input'
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

time.sleep(random.randint(2,4))

driver.stop_client()
driver.quit()