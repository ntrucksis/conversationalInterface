# main file to be run when interacting with the conversational interface
from recipeParser import getRecipeData
import re

def google_query(qstr):
  searchstr = "https://www.google.com/search?q="
  searchtokens = qstr.split()
  for token in searchtokens:
    searchstr = searchstr + token + '+'
  searchstr = searchstr[:-1]
  return searchstr

def youtube_query(qstr):
  searchstr = "https://www.youtube.com/results?search_query="
  searchtokens = qstr.split()
  for token in searchtokens:
    searchstr = searchstr + token + '+'
  searchstr = searchstr[:-1]
  return searchstr

def main(recipeUrl):
	
	title, recipeObj = getRecipeData(recipeUrl)
	print (recipeObj)
	current_step = 1

	print (f'\nGreat! Lets get started with making {title}.')

	# phase 1
	function_to_call = None
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
		elif choice == '2':
			print ('Sure, let\'s begin with the recipe steps')
			asking = False
			# call function for steps here
			# remember to increment current_step
		else:
			print ('Please enter 1 or 2 for one of the options')

	# start phase 2
	asking = True
	while(asking and current_step <= len(recipeObj["steps"])):
		print (f'Should I continue to step #{current_step}?')
		choice = input()

		if re.search(r'\byes\b',choice.lower()):
			# print out the step
			print (f'Step #{current_step} is: {recipeObj["steps"][current_step - 1]}')
			current_step += 1

		if re.search(r'\bhow\b',choice.lower()):
			pass
		if re.search(r'\bshow me\b',choice.lower()):
			pass

if __name__ == '__main__':
	recipeUrl = input('\nWelcome to **BOT NAME**.\nPlease provide a recipe URL from AllRecipes.com:\n')
	main(recipeUrl)

# https://www.allrecipes.com/recipe/245705/baked-chicken-alfredo/
