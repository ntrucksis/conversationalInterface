urlcat="https://www.allrecipes.com/recipes/155/everyday-cooking/vegetarian/breakfast-and-brunch"
pagecat = requests.get(urlcat)
soupcat = BeautifulSoup(pagecat.content, 'html.parser')
urls=soupcat.findAll("a")#.text
#urls
links=[]
#import pprint
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(urls[10])
#urls[10].attrs["href"]
for tag in urls:
  oneurl=tag.get("href")
  if oneurl:
    if ("/recipe/" in oneurl):
      links.append(oneurl)
links
