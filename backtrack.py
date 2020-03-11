# look at recipes similar to current one and find ways to transform them
# Mainly for transforming cuisines
from collections import Counter
import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

class Backtracker:

	def __init__(self, base_url):
		self.base_url = base_url
		self.current_dish_type = None
	
	def get_similar(self):
		'''
		Backtracks to the previous category of current recipe and finds the links
		those similar recipes
		'''

		page_html = requests.get(self.base_url)
		page_graph = BeautifulSoup(page_html.content, features="html.parser")
		
		breadcrumbs = [(x['href'], " ".join(x.text.split()).replace("Chevron Right", "").rstrip()) for x in page_graph.find_all('a', {'class':'breadcrumbs__link'})]

		self.current_dish_type = f"{breadcrumbs[-1][1]} - {breadcrumbs[-2][1]}"

		print (self.current_dish_type)

		page_html = requests.get(breadcrumbs[-2][0])
		page_graph = BeautifulSoup(page_html.content, features="html.parser")

		similar = [x['href'] for x in page_graph.find_all('a', {'class':'fixed-recipe-card__title-link'})]

		return similar


base_url = 'https://www.allrecipes.com/recipe/245705/baked-chicken-alfredo/'
bt = Backtracker(base_url)
bt.get_similar()