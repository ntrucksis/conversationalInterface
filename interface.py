# main file to be run when interacting with the conversational interface
from recipeParser import getRecipeData


def main(recipeUrl):
	
	title, recipeObj = getRecipeData(recipeUrl)

	print (f'\nGreat! Lets get started with making {title}.')

	asking = True
	while (asking):
		print ('Would you like to:')
		print ('(1) Go over ingredients')
		print ('(2) Go over recipe steps')
		choice = input()

		if choice == '1':
			print ('Yeah, lets go over the ingredients')
			asking = False
			# call function for going over ing here
		if choice == '2':
			print ('Sure, let\'s begin with the recipe steps')
			asking = False
			# call function for steps here
		else:
			print ('Please enter 1 or 2 for one of the options')






if __name__ == '__main__':
	recipeUrl = input('\nWelcome to **BOT NAME**.\nPlease provide a recipe URL from AllRecipes.com:\n')
	main(recipeUrl)

# https://www.allrecipes.com/recipe/245705/baked-chicken-alfredo/