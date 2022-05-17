# -*- coding: cp1252 -*-
from lxml import html
import requests
import ast
import csv
import pandas as pd


##newList = []
##posts = []

##GRAB cars after 2018 from Jumia CI
##for n in range (0, 360):
##    page = requests.get("""https://deals.jumia.ci/posts/search?attributes%5Bcars%5D%5Bmake%5D=&attributes%5Bcars%5D%5ByearMin%5D=2018&attributes%5Bcars%5D%5ByearMax%5D=&attributes%5Bcars%5D%5Btransmission%5D=&attributes%5Bcars%5D%5BmillageMin%5D=&attributes%5Bcars%5D%5BmillageMax%5D=&attributes%5Bcars%5D%5Bfuel%5D=&search-category=195&search-location=421&page={}&xhr=ols8l""".format(n))
##    tree = html.fromstring(page.content)
##    posts.extend(list(map(str,tree.xpath('//article[@class="post-holder product-click  "]/@data-event'))))



##for post in posts:
##    newList.append(ast.literal_eval(post))
##
##
##df = pd.DataFrame.from_dict(newList)

####print (df)
##df.to_csv('sample.csv', header=True, index=False, encoding='UTF-16', errors='surrogatepass')
####df.to_excel('sample.xlsx')    


###-----------------------------------------------------

###GRAB attributes from page
##df = pd.read_excel('jumia_links_2.xlsx')
##mylist = df['link'].tolist()
##annee = []
##marque = []
##transmission = []
##merged = []
##for n in mylist: 
##    page = requests.get(n)
##    tree = html.fromstring(page.content)
##    annee.append({"annee": tree.xpath('//div[@class="post-content"]/div[@class="post-attributes"]/div[@class="new-attr-style"]/h3[text()="Année"]/span/text()')})
##    marque.append({"marque": tree.xpath('//div[@class="post-content"]/div[@class="post-attributes"]/div[@class="new-attr-style"]/h3[text()="Marque"]/span/a/text()')})
##    transmission.append({"transmission": tree.xpath('//div[@class="post-content"]/div[@class="post-attributes"]/div[@class="new-attr-style"]/h3[text()="Transmission"]/span/text()')})
##
##for i in range(0,len(annee)):
##    merged.append(annee[i] |  marque[i] | transmission[i])
##    
##df = pd.DataFrame.from_dict(merged)
##df.to_csv('data_Y_B_T.csv', header=True, index=False, encoding='UTF-16', errors='surrogatepass')


###-----------------------------------------------------

### Code to grab from KIJIJI
##titles = []
##prices = []
##mileages = []
##merged = []
##
##for n in range(1,100):
##    page = requests.get("""https://www.kijiji.ca/b-cars-trucks/ottawa/cars/2018__/page-{}/k0c174l1700185a68""".format(n))
##    tree = html.fromstring(page.content)
##    titles = list(map(str,tree.xpath('//div[contains(@class,"regular-ad")]/div[@class="clearfix"]/div[@class="info"]/div[@class="info-container"]/div[@class="title"]/a[@class="title "]/text()')))
##    prices = list(map(str,tree.xpath('//div[contains(@class,"regular-ad")]/div[@class="clearfix"]/div[@class="info"]/div[@class="info-container"]/div[@class="price"]/text()')))
##    mileages = list(map(str,tree.xpath('//div[contains(@class,"regular-ad")]/div[@class="clearfix"]/div[@class="info"]/div[@class="info-container"]/div[@class="description"]/div[@class="details"]/text()[1]')))
##
##    titles = [{"title":x.replace('\n','').strip()} for x in titles]
##    prices = list(filter(None, [x.replace('\n','').strip() for x in prices]))
##    prices = [{"price":x.replace('\n','').strip()} for x in prices]
##    mileages = [{"km":x.replace('\n','').replace('  ','').strip()} for x in mileages]
##
##    print(len(titles))
##    print(len(prices))
##    print(len(mileages))
##    for i in range(0,len(titles)):
##        merged.append(titles[i] |  prices[i] | mileages[i])
##
##df = pd.DataFrame.from_dict(merged)
##df.to_csv('kijiji_sample.csv', header=True, index=False, encoding='UTF-16', errors='surrogatepass')
##
####        
####    print(len(merged))
####    print(merged)
####        
