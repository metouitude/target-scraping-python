from re import A
import requests 
from bs4 import BeautifulSoup
import pandas as pd
import os


URL    = "https://www.target.com/p/apple-iphone-13-pro-max/-/A-84616123?preselect=84240109#lnk=sametab"
response     = requests.get(URL)

if response.ok:
    print("****************Upshelf script******************")
    print("****************",response.status_code,"*************")
    print("************************************************")
    
    PageContent = BeautifulSoup(response.text, 'html.parser')

    #Getting description from the page
    div = PageContent.find('div', attrs={'class':'h-padding-b-default'})
    #res.find('span', attrs={'class':'h-text-xl h-text-bold h-padding-r-tight'})

    print(div)



    '''
    if os.path.exists("output.txt"):
        os.remove("output.txt")
        with open("output.txt", "w") as f:
            f.write(str(PageContent))
            f.close()
    else:
        with open("output.txt", "w") as f:
            f.write(str(PageContent))
            f.close()
'''

    

        
 
        


else:
    print("RESPONSE PROBLEM")
    print(response.status_code)