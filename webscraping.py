from mimetypes import init
import requests
from bs4 import BeautifulSoup as bs

class scrapper:
    def __init__(self):
        print('The Web scrapper')

        user_name=self.get_user_input()
        url=self.create_url(user_name)
        r=requests.get(url)
        soup=self.fetch_html(r)
        profile_img=self.fetch_img(soup)
        print([profile_img])


    def get_user_input(self):
        name= input('Enter Github username')
        return name
    
    def create_url(self,usr_name):
        url='https://github.com/'+usr_name
        return url
    
    def fetch_html(self,r):
        soup=bs(r.content,'html.parser')
        print(soup)
        return soup
    def fetch_img(self,soup):
        img=soup.find('img',{'alt' : 'Avatar'})['src']
        return img

    

ws=scrapper()


