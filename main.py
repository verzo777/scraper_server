from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import json

destinazione = "Bergamo, BG"
ospiti = 2

# XPATHS
xpath_consentcookies = '//*[@id="react-application"]/div/div/div[1]/div/div[6]/section/div[2]/div[2]/button'
xpath_consentcookies_7 =  '//*[@id="react-application"]/div/div/div[1]/div/div[7]/section/div[2]/div[2]/button'

xpath_destinazione = '//*[@id="bigsearch-query-location-input"]'
xpath_checkin = '//*[@id="search-tabpanel"]/div/div[3]/div[1]/div/div/div[2]'
xpath_avanti_calendario_checkin = '//*[@id="panel--tabs--0"]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/button/span'

xpath_23calendario_checkin = '//*[@id="panel--tabs--0"]/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[4]/div'
xpath_26calendario_checkout = '//*[@id="panel--tabs--0"]/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[7]/div'

xpath_aggiungiospiti = '//*[@id="search-tabpanel"]/div/div[5]/div[1]/div[1]/div/div[2]'

xpath_aggiungiospiti_piuuno = '//*[@id="stepper-adults"]/button[2]'

xpath_prericerca = '//*[@id="search-tabpanel"]/div/div[5]/div[1]/div[1]/div'

xpath_ricerca = '//*[@id="search-tabpanel"]/div/div[5]/div[1]/div[3]/button'

xpath_avanti_pagina =          '//*[@id="site-content"]/div/div[3]/div/div/div/nav/div/a[5]'
xpath_avanti_pagina_another =  '//*[@id="site-content"]/div/div[3]/div/div/div/nav/div/a[6]'


xpath_annunci =  [ '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[3]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[4]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[5]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[7]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[8]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[9]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[10]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[11]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[12]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[13]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[14]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[15]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[16]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[17]/div/div[2]/div/div/div/div/a',
                   '//*[@id="site-content"]/div/div[2]/div/div/div/div/div[1]/div[18]/div/div[2]/div/div/div/div/a'
                 ]


# xpath pagina annuncio:
xpath_titolo = '//*[@id="site-content"]/div/div[1]/div[1]/div[1]/div/div/div/div/div/section/div/div[1]/span/h1'
xpath_descrizione = '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[1]/h2'
xpath_ospiti =         '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[2]/ol/li[1]'
xpath_cameredaletto =  '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[2]/ol/li[2]'
xpath_letti =  '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[2]/ol/li[3]'
xpath_bagni =  '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[2]/ol/li[4]'
xpath_rate = '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[3]/div[2]'
xpath_rate_superostia = '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[2]/div/div/div/a/div/div[6]/div[1]'
xpath_numerorecensioni = '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[3]/a'
xpath_numerorecensioni_superostia = '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[2]/div/div/div/a/div/div[10]/div[1]'
xpath_prezzopernotte = '//*[@id="site-content"]/div/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/span/span'

def getdata(driver_, xpath_):
    try:
        element = driver_.find_element(By.XPATH, xpath_)
        # Retrieve the text content of the element
        return element.text
    except:
        print("jeez did not find it")
        return ""
    
def getdata_recensioni(driver_, xpath_):

    element = driver_.find_element(By.XPATH, xpath_)
    # Retrieve the text content of the element
    return element.text



def get_bookings(driver_, months):
    # Initialize an empty list to store the availability data
    availability = []

    for k in range(months):

        # XPath to the table body
        tbody_xpath_superospiti = '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[9]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody'
        tbody_xpath_hostnormali = '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[7]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody'
        tbody_xpath_hostnuovi =    '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[6]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody'
        tbody_xpath_altracombo = '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[8]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody'
        tbody_xpath_altracombo_2 = '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[10]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody'
        
        
        # Find the table body
        tbody = None
        try:
            tbody = driver_.find_element(By.XPATH, tbody_xpath_superospiti)
        except NoSuchElementException:
            try:
                tbody = driver_.find_element(By.XPATH, tbody_xpath_hostnormali)
            except NoSuchElementException as e:

                try:
                    tbody = driver_.find_element(By.XPATH, tbody_xpath_hostnuovi)

                except NoSuchElementException as e:

                    try:
                        tbody = driver_.find_element(By.XPATH, tbody_xpath_altracombo)

                    except NoSuchElementException as e:

                        try:
                            tbody = driver_.find_element(By.XPATH, tbody_xpath_altracombo_2)

                        except NoSuchElementException as e:
                            print("Neither element could be found.")
                            print(e)  # This will print the message from the NoSuchElementException

        # Find all the rows within the table body
        rows = tbody.find_elements(By.TAG_NAME, 'tr')

        # Iterate over each row
        for row in rows:
            # Find all the cells within the row
            cells = row.find_elements(By.TAG_NAME, 'td')
            
            # Iterate over each cell
            for cell in cells:

                try:

                    # Find the div inside the cell that contains the day
                    day_div = cell.find_element(By.TAG_NAME, 'div')
                    if day_div:

                        day = day_div.get_attribute('data-testid')
                        
                        # Get the value of the 'aria-disabled' attribute
                        is_occupied = cell.get_attribute('aria-disabled') == 'true'
                        
                        # Add the day and its availability to the list
                        availability.append({"day": day, 
                                             "booked": is_occupied}
                                            )
                except:
                    pass #empty div

        # At this point, the 'availability' list contains tuples of (day, is_free)
        # where 'day' is a string and 'is_free' is a boolean indicating if the room is free on that day

        # move forward the calendar (if first time, move 2 times)
        try:
            time.sleep(0.5)
            driver_.find_element(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[7]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/button').click()
                                          
            if k ==0:
                time.sleep(0.5)
                driver_.find_element(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[7]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/button').click()
        except NoSuchElementException as e:
            
            try:
                time.sleep(0.5)
                driver_.find_element(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[9]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/button').click()
                if k ==0:
                    time.sleep(0.5)
                    driver_.find_element(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[9]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/button').click()
            except NoSuchElementException as e:
                try:
                    time.sleep(0.5)
                    driver_.find_element(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[8]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/button').click()
                    if k ==0:
                        time.sleep(0.5)
                        driver_.find_element(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[8]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/button').click()
                except NoSuchElementException as e:
                    try:
                        time.sleep(0.5)
                        driver_.find_element(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[6]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/button').click()
                        if k ==0:
                            time.sleep(0.5)
                            driver_.find_element(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[6]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/button').click()
                    except NoSuchElementException as e:   
                        print("fuk it could not find avanti")
                    

 

    return availability



def search(driver, destinazione, ospiti):

    # Go to the page that needs to be scraped
    driver.get('https://www.airbnb.it/')

    time.sleep(5)

    driver.find_element(By.XPATH, xpath_destinazione).send_keys(destinazione)

    time.sleep(1)

    try:

        driver.find_element(By.XPATH, xpath_consentcookies).click()

    except NoSuchElementException as e:
        print(e)
        print("cant find ok cookie consent")
        try:
            driver.find_element(By.XPATH, xpath_consentcookies_7).click()
        except NoSuchElementException as e:
            print(" ok fuk it")

    time.sleep(5)


    try:
        driver.find_element(By.XPATH, '/html/body/div[11]/div/div/section/div/div/div[2]/div/div[1]/button').click()
                                      
    except NoSuchElementException:
        try:
             
            driver.find_element(By.XPATH, '/html/body/div[10]/div/div/section/div/div/div[2]/div/div[1]/button').click()

        except NoSuchElementException:
            print("icone popup not found")
            pass
        



    driver.find_element(By.XPATH, xpath_checkin).click()

    time.sleep(1)

    driver.find_element(By.XPATH, xpath_avanti_calendario_checkin).click()

    time.sleep(1)

    driver.find_element(By.XPATH, xpath_23calendario_checkin).click()

    time.sleep(1)

    driver.find_element(By.XPATH, xpath_26calendario_checkout).click()

    time.sleep(1)

    driver.find_element(By.XPATH, xpath_aggiungiospiti).click()

    for k in range(ospiti) :
        time.sleep(1)

        

        driver.find_element(By.XPATH, xpath_aggiungiospiti_piuuno).click()

    time.sleep(1)


    driver.find_element(By.XPATH, xpath_prericerca).click()


    time.sleep(1)

    driver.find_element(By.XPATH, xpath_ricerca).click()


    time.sleep(1)

    
def scrape_page(driver):

    mydata = []

    for path_annuncio in xpath_annunci:

        try:

            # Open the link in a new tab
            driver.find_element(By.XPATH, path_annuncio).send_keys(Keys.CONTROL + Keys.RETURN)

            time.sleep(1)

            # Switch to the new tab
            driver.switch_to.window(driver.window_handles[1])

            time.sleep(5)


            try:
                driver.find_element(By.XPATH, '/html/body/div[9]/div/div/section/div/div/div[2]/div/div[1]/button').click()
            except:
                print("no translate button")

            listingdata = {}

            listingdata["room_ID"] = str(driver.current_url)[28:].split("?")[0]

            listingdata["titolo"] = getdata(driver, xpath_titolo)
            listingdata["desc"] = getdata(driver, xpath_descrizione)
            listingdata["num_ospiti"] = getdata(driver, xpath_ospiti)
            listingdata["mum_camere_letto"] = getdata(driver, xpath_cameredaletto)
            listingdata["num_letti"] = getdata(driver, xpath_letti)
            listingdata["num_bagni"] = getdata(driver, xpath_bagni)
            listingdata["prezzo_notte"] = getdata(driver, xpath_prezzopernotte)
            try:
                listingdata["rate_medio"] = getdata_recensioni(driver, xpath_rate)
                listingdata["num_recensioni"] = getdata_recensioni(driver, xpath_numerorecensioni)
                listingdata["superostia"] = "n"
            except:
                print("superostia?")
                listingdata["rate_medio"] = getdata(driver, xpath_rate_superostia)
                listingdata["num_recensioni"] = getdata(driver, xpath_numerorecensioni_superostia)
                listingdata["superostia"] = "y"

            


            print("GET BOOKINGS")
            listingdata["bookings"] = get_bookings(driver, 3)

            mydata.append(listingdata)

            # Close the current tab
            driver.close()

            time.sleep(1)

            # Switch back to the original tab
            driver.switch_to.window(driver.window_handles[0])

            time.sleep(1)
        except Exception as e:
            print("********************************")
            print("riscontrato errore durante scraping di un annuncio: ")
            print(e)
            # Switch back to the original tab
            print("Switch back to the original tab")
            driver.switch_to.window(driver.window_handles[0])
            print("********************************")



    print("finita pagina!")
    return mydata

alldata = []
    
# Set up the Selenium WebDriver (you'll need the appropriate driver for your browser)
# e.g., chromedriver for Chrome, geckodriver for Firefox
driver = webdriver.Chrome()

search(driver, destinazione, ospiti)


time.sleep(5)


print("ok now lets get the data!")



for k in range(14):

    print("inizio lavoro pagina ", k)
    time.sleep(5)


    data = scrape_page(driver)

    print("pagina finita, save data and go to next")

    alldata = alldata + data

    try:
        print("goto next page")
        driver.find_element(By.XPATH, xpath_avanti_pagina_another).click()
    except NoSuchElementException:
        print("goto next page other xpath")
        driver.find_element(By.XPATH, xpath_avanti_pagina).click()
    time.sleep(15)


print("aight i got ",len(alldata), " data ")


# Writing JSON data
with open("mydatajson", 'w') as json_file:
    json.dump(alldata, json_file)