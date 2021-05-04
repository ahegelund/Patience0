from selenium import webdriver
chromedriver_location = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chromedriver_location)
driver.get('https://www.regionh.dk/presse-og-nyt/pressemeddelelser-og-nyheder/Sider/Tilmelding-til-at-modtage-overskydende-vaccine-mod-COVID-19.aspx')

#Page 1 - intro

page_submit = '/html/body/div/form/div[2]/div[3]/input'
driver.find_element_by_xpath(page_submit).click()

#Page 2 - name

fulde_navn = '//*[@id="t50100775"]'
driver.find_element_by_xpath(fulde_navn).send_keys('Jakob Jokab')
driver.find_element_by_xpath(page_submit).click()

#Page 3 - age

alder = '//*[@id="n35965768"]'
driver.find_element_by_xpath(alder).send_keys('22')
driver.find_element_by_xpath(page_submit).click()

#Page 4 - address

addresse = '//*[@id="t50088645"]'
driver.find_element_by_xpath(addresse).send_keys('Hovedbanegården 22')
driver.find_element_by_xpath(page_submit).click()

#Page 5 - postcode

postcode = '//*[@id="t50088674"]'
driver.find_element_by_xpath(postcode).send_keys('1111')
driver.find_element_by_xpath(page_submit).click()

#Page 5 - phone

phone = '//*[@id="n50088775"]'
driver.find_element_by_xpath(phone).send_keys('1111')
driver.find_element_by_xpath(page_submit).click()

#Page 6 - centre choice (øksenhallen)

centre = '/html/body/div/form/div[1]/div/table/tbody/tr[2]/td/div/span[6]/label'
driver.find_element_by_xpath(centre).click()
driver.find_element_by_xpath(page_submit).click()

#Page 7 - final submit

driver.find_element_by_xpath(page_submit).click()
driver.find_element_by_xpath(page_submit).click()