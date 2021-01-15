from selenium import webdriver
import time
import pandas as pd
chrome_path = "/Users/mertozlutiras/Desktop/MERT/work/zew/chromedriver"
url = "https://tenders.procurement.gov.ge/dispute/"
custom_options = webdriver.ChromeOptions()

prefs = {
    "translate_whitelists": {"ka":"en"},
    "translate":{"enabled":"True"}
}
custom_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(chrome_path, chrome_options=custom_options)

driver.get(url)

## Önce id leri topluyoruz
## Sonra bunları url'e besleyip ordan datayı alacağız
    # Dataları içeren url: https://tenders.procurement.gov.ge/dispute/engine/controller.php?action=showapp&app_id=27926
ids = []
word = driver.find_elements_by_tag_name("tr")

while (word[0] not in ids): 
    for element in word:
        ids.append(element.get_attribute("id"))
    time.sleep(5)
        # This url takes to next page
    next_page = "https://tenders.procurement.gov.ge/dispute/engine/controller.php?action=search_app&page=next&_=1604776285472"
    driver.get(next_page)
    word = driver.find_elements_by_tag_name("tr")


   
## ı keep the origianl ids and created a copy of it to preprocess as ids2
ids = ids[:10000]
ids2 = ids.copy()
ids2 = ids2[:9645]
print(ids)

## 8439 ids of all items are taken in ids2

ids2 = [ i for i in ids2 if i != '']
print(len(ids2)) 

## IDs are written in a csv file
ids3 = pd.DataFrame(ids2)
ids3.to_csv('/Users/mertozlutiras/Desktop/MERT/work/zew/IDs.csv', index=False)

## Read csv
ids4 = pd.read_csv("/Users/mertozlutiras/Desktop/MERT/work/zew/IDs.csv")
ids4 = ids4.values.tolist()

data = {}
chrome_path = "/Users/mertozlutiras/Desktop/MERT/work/zew/chromedriver"
custom_options = webdriver.ChromeOptions()

prefs = {
    "translate_whitelists": {"ka":"en"},
    "translate":{"enabled":"True"}
}
custom_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(chrome_path, chrome_options=custom_options)

for i in ids4:
    id = i[0][1:]
    url2 = f"https://tenders.procurement.gov.ge/dispute/engine/controller.php?action=showapp&app_id={id}"
    print(url2)
    driver.get(url2)
    time.sleep(2)
    applicant = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/strong[1]/font[1]/font[1]")
    data[id] = applicant.text
    time.sleep(2)

driver = webdriver.Chrome(chrome_path, chrome_options=custom_options)
driver.get(f"https://tenders.procurement.gov.ge/dispute/engine/controller.php?action=showapp&app_id={i}")
applicant = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/strong[1]/font[1]/font[1]")
data[i] = applicant.text
print(data)

len(ids4)
