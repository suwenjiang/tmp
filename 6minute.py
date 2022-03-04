__author__ = 'jiangmb'

from bs4 import BeautifulSoup
import requests


url="http://www.bbc.co.uk/learningenglish/english/features/6-minute-english/ep-150903"

page_content=requests.get(url)




print (page_content.content)







