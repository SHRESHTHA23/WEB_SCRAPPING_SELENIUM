#!/usr/bin/env python
# coding: utf-8

# In[3]:


#because of dynamicly loaded content import selenium

import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options    
import csv
from time import sleep

from selenium.webdriver import ActionChains


# chrome driver is based on chrome 83, and needs local chrome 83 installation, 
# more drivers can be found here https://chromedriver.chromium.org/downloads
# driver is expected in the script path

#DRIVER_PATH = os.path.dirname(os.path.realpath('C:/Users/hp/Downloads/chromedriver_win32/chromedriver') )
driver = webdriver.Chrome('C:/Users/hp/Downloads/chromedriver_win32/chromedriver')

# headless so we dont see the browser
options = Options()
 
#options.headless = True
options.add_argument("--window-size=1920,1200")
#options.add_argument("--headless")  


#setting the querystring top100 to false makes the site load all companies in 1 list
#driver.get('https://www.ycombinator.com/companies/')
driver.get('https://www.ycombinator.com/companies/?top100=false')

#line not needed
#container = driver.find_element_by_class_name("_2qzBrUbZVVQVb-wVo1v1B")

endOfPage = False

#scroll down until all companies are loaded
while not endOfPage:
  currentY = driver.execute_script("return document.body.scrollHeight")
  driver.execute_script("window.scroll(0, document.body.scrollHeight+1)")

  # give the page time to load content
  sleep(1)

  newY = driver.execute_script("return document.body.scrollHeight")
  endOfPage = currentY == newY

#all companies have a class no-hovercard
anchorList = driver.find_elements_by_class_name("no-hovercard")

hrefList =  list(map(lambda x: x.get_attribute("href"), anchorList))

print(str(len(anchorList)) + " companies found")

with open('companies.csv', mode='w') as companyinfo:
  for href in hrefList:

      driver.get(href)
      sleep(1)

      container = driver.find_element_by_class_name("main-box")
      companyHeader = container.find_element_by_tag_name("H1")
      linksContainer = driver.find_element_by_class_name("links")
      companyWebsite = container.find_element_by_tag_name("A")
      
      # for facts tab more information
      #fact1 = driver.find_element_by_xpath("//div[@class='facts']/div[1]")
      #fac1 = fact1.find_element_by_class_name("right")
      #fact2 = driver.find_element_by_xpath("//div[@class='facts']/div[2]")
      #fac2 = fact2.find_element_by_class_name("right")
      #fact3 = driver.find_element_by_xpath("//div[@class='facts']/div[3]")
      #fac3 = fact3.find_element_by_class_name("right")
      
      

      company_writer = csv.writer(companyinfo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      company_writer.writerow([companyHeader.text, companyWebsite.get_attribute("href")])


# In[1]:


#fact1.text,fac1.text ,fact2.text,fac2.text, fact3.text,fac3.text


# In[ ]:




