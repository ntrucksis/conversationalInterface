# look at recipes similar to current one and find ways to transform them
# Mainly for transforming cuisines
from collections import Counter
# from recipeParser import main as recipe
from lists import cuisines
from lists import meat, seafood, pasta, grains, sauce, seasoning, spices, herbs, fats, dairy, cheese, vegetables, fruits, toppings

ing_type_list = [("meat", meat), ("seafood", seafood),
 ("pasta", pasta), ("grains", grains), ("sauce",sauce), ("seasoning", seasoning), 
 ("spices",spices), ("herbs", herbs), ("fats", fats), ("dairy", dairy),
  ("cheese",cheese), ("vegetables",vegetables), ("fruits", fruits), ("toppings",toppings)]

def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True

class Cuisine:
	'''
	Attempts to classify the recipe as a certain cuisine and makes a tranformation
	to another kind
	Takes in a master recipe dict with all parsed data about the recipe
	'''
	def __init__(self, recipe, steps):
		self.data = recipe
		self.steps = steps
		self.classified_cuisine = None
		self.ingredients = None
	
	def classify(self):
		# print ('the objects')
		# print (self.data)
		ingredients = []
		for i in self.data:
			try:
				key = int(i)
				key = str(key)
			except ValueError:
				continue
			ingredients.append(self.data[key]["name"].lower())

		self.ingredients = ingredients
		
		maximum = 0
		classified_cuisine = None
		for cuisine in cuisines:
			if len(set(ingredients) & set(cuisines[cuisine])) > maximum:
				maximum = len(set(ingredients) & set(cuisines[cuisine]))
				self.classified_cuisine = cuisine

		print (f'\nCurent estimated cuisine type: {self.classified_cuisine}\n')

	def subNameInSteps(self, stepslist, oldname, newname):
		print ('subbing', oldname, newname)
		for i in range(len(stepslist) - 1):
			if oldname in stepslist[i]:
				print ('should replace', oldname, stepslist[i])
				stepslist[i] = stepslist[i].replace(oldname, newname)
		return stepslist

	def transform(self, cuisine):
		cuisine_ingredients = cuisines[cuisine]
		# print (cuisine_ingredients)

		classified = []
		cuis_classified = []

		for i in [x for x in self.data if is_int(x)]:
			ingredient_type = None
			for ing_type in ing_type_list:
				if self.data[i]["name"].lower() in ing_type[1]:
					ingredient_type = ing_type[0]
					break
				else:
					continue
			classified.append((self.data[i]["name"], ingredient_type))

		for ingredient in cuisine_ingredients:
			ingredient_type = None
			for ing_type in ing_type_list:
				if ingredient in ing_type[1]:
					ingredient_type = ing_type[0]
					break
				else:
					continue
			cuis_classified.append((ingredient, ingredient_type))

		# print ('steps',self.steps)
		for ing in classified:
			for cuis_ing in cuis_classified:
				if ing[1] == cuis_ing[1] and ing[0] != cuis_ing[0]:
					for i in self.data:
						try:
							if self.data[i]["name"] == ing[0]:
								self.data[i]["name"] = cuis_ing[0]
						except:
							continue
					print (f'Ingredient transformation: {ing[0]} to {cuis_ing[0]}')
					self.steps = self.subNameInSteps(self.steps, ing[0], cuis_ing[0])

					cuis_classified.remove(cuis_ing)
					break

		# print (self.data)
		return self.data, self.steps


# Testing

# base_url = 'https://www.allrecipes.com/recipe/232233/easy-italian-sausage-spaghetti/?internalSource=staff%20pick&referringId=505&referringContentType=Recipe%20Hub'

# data = recipe(base_url)
# cuisine = Cuisine(data)
# cuisine.classify()
# cuisine.transform('greek')