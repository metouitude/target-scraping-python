import time
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from html.parser import HTMLParser

#   1--Launch driver 

URL = 'https://www.target.com/p/apple-iphone-13-pro-max/-/A-84616123?preselect=84240109#lnk=sametab'
Myoption=webdriver.ChromeOptions()
Myoption.add_argument("--incognito")
#Myoption.add_argument("--headless")

#chrome location to set  executable_path=r"")
driver = webdriver.Chrome(options=Myoption)
driver.get(URL)
driver.implicitly_wait(20)

#   2--Getting variables

# JUST EXPANDING TO SEE ALL ATTRIBUTES


button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div[3]/div[2]/div/div/div[2]/div/button')
button.click()

time.sleep(10)


#   a) fetching for title

product_title = driver.title
print("***TITLE***:",product_title)

#   b)fetching for price

time.sleep(5)
elem = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div[1]/div[1]')
product_price = elem.text
print("***PRICE***:",product_price)

#   c)fetching for description



time.sleep(10)

desc = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]')
product_description = desc.text
print("***DESCRIPTION***:",product_description)
time.sleep(10)

#   d)fetching for highlights

all_highlights = []

highlights = driver.find_elements(By.XPATH,'/html/body/div[1]/div/div[4]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/ul')
#highlights_html = highlights.get_attribute('innerHTML') #innerHTML

for h in highlights:
    all_highlights.append(h.text)

print("***HIGHLIGHTS***:",all_highlights)


#   e) fetching for questions


ALL_QUESTIONS = []

Q_A_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div/div[3]/div[2]/div/div/div[1]/div[2]/ul/li[3]/a/div')
Q_A_button.click()

time.sleep(10)

allquestionsbutton = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div/div[3]/div[2]/div/div/div[3]/div/div/div/div[2]/div[1]/button')
allquestionsbutton.click()

time.sleep(10)


ques = driver.find_elements(By.TAG_NAME, 'h3')
for q in ques:
    if q.text.startswith('Q'):
        #print('###########################')
        #print(q.text)
        ALL_QUESTIONS.append(q.text)

print("***QUESTIONS***:",ALL_QUESTIONS)


# f) fetching for images url

allimagesURLS = []

images = driver.find_elements(By.TAG_NAME, 'img')

for img in images:
    allimagesURLS.append(img.get_attribute('src'))

print('***IMAGES URLS***:',allimagesURLS)

print('*************************OUTPUT*************************')
df = pd.DataFrame(columns=['Title','Price','Description','Highlights','Questions','Images'])
df.loc[0] = [product_title,product_price,product_description,all_highlights,ALL_QUESTIONS,allimagesURLS]
print(df)
np.savetxt('output.txt', df.values, delimiter=',', fmt='%s')

driver.quit()
