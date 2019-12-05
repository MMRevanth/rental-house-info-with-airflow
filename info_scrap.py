import requests
from bs4 import BeautifulSoup

base_url="https://www.zolo.ca/toronto-real-estate/houses-for-rent?sc=aw-1362625368-77694165118&gclid=CjwKCAiA8qLvBRAbEiwAE_ZzPYLUBIDAcSXORAUv4kswO2d6gW3ALt-a936eH1lssi__lLj6eB4YkBoCYz0QAvD_BwE"
page=requests.get(base_url)

bsobj=BeautifulSoup(page.text,'html.parser')

info1=bsobj.find(class_='card-listing--location xs-text-5 xs-inline')
#info1=bsobj.find(class_='address link-primary')
#info1=bsobj.find(class_='listing-column text-4')
info1.decompose()


house_list=bsobj.find(class_='listings-wrapper')
#house_list=bsobj.find(class_='card-listing--location xs-text-5 xs-inline')
#house_list=bsobj.find(class_='listing-column text-4')
house_list_addr=house_list.find_all('span')


for info in house_list_addr:
    vacant=info.contents[0]
    print(vacant)





