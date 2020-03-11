from bs4 import BeautifulSoup
import json
import requests
from nltk import pos_tag, word_tokenize
import sys
from lists import kitchenTools, kitchenTools_two, measurements, adjectivesInNames, fruits, meat, vegetables
from healthy import makeHealthy
import sizetransform
import transformvegetarian
from cuisine import Cuisine
from unhealthy import makeUnhealthy

def getIngredientsObject(ingredientsList):
    ingredients = []
    last_word = ""
    for i in range(len(ingredientsList)):
        tokenized = pos_tag(word_tokenize(ingredientsList[i]))
        name = ""
        quant = ""
        msmt = ""
        prep = ""
        desc = ""
        q = []
        finished = True
        #print(tokenized)

        for word in tokenized:
            if finished == False:
                prep += word[0] + ' '
            elif word[1] == 'CD':
                q.append(word[0])
                quant += word[0] + " "
            elif word[1] in ['JJ', 'MD', 'VBZ', 'RB']:
                if word[0] in adjectivesInNames:
                    name += word[0] + " "
                else:
                    if word[0] in ['pinch', 'cup', 'can', 'cans', 'packages', 'fluid', 'squares', 'teaspoon', 'jars']:
                        msmt+= word[0] + " "
                    elif word[0] in ['frozen', '3-inch', 'finely', 'coarsely', '1/4-inch']:
                        prep += word[0] + " "
                    elif word[0] in ['nonstick']:
                        desc += word[0] + " "
                    elif word[0] in ['desired', 'such', 'only']:
                        pass
                    else:
                        desc += word[0] + " "
            elif word[1] in ['NN', 'NNS', 'NNP']:
                if word[0] not in measurements:
                    if word[0] in ['ground', 'pieces', 'room', 'temperature', 'chunks', 'florets', 'strips', 'thickness']:
                        if word[0] == 'strips':
                            prep += "cut into " + word[0] + " "
                        else:
                            prep += word[0] + " "
                    elif "®" in word[0]:
                        pass
                    elif word[0] in ['semisweet', 'medium', 'skinless', 'boneless', 'flavor']:
                        desc += word[0] + " "
                    else:
                        name += word[0] + " "
                else:
                    if word[0] in ['frying']:
                        desc += 'for ' + word[0] + ' '
                    else:
                        msmt += word[0] + " "
            elif word[1] in ['VBD', 'VBN', 'VB', 'VBG', 'VBP']:
                if word[0] in ['minced', 'beaten', 'drained']:
                    prep += word[0] + " "
                elif word[0] in ['grapeseed', 'sesame', 'baking', 'cake', 'whipping', 'taco', 'seasoning', 'bacon', 'tomato', 'sauce', 'whipped', 'topping']:
                    name += word[0] + " "
                elif word[0] in fruits or word[0] in meat or word[0] in vegetables:
                    name += word[0] + " "
                elif word[0] in ['needed', 'desired', 'to', 'state']:
                    pass
            elif word[1] in ['DT']:
                if word[0] == 'any':
                    desc += word[0] + ' '
                else:
                    if last_word == 'and':
                        prep = prep[:-1]
                        prep += ', '
                    prep += word[0] + " "
            elif word[1] == 'FW':
                if word[0] in ['paprika']:
                    name += word[0] + " "
            elif word[1] == 'IN':
                if word[0] == 'into':
                    if last_word == 'cut':
                        finished = False
                        prep += 'cut into' + ' '

            last_word = word[0] #keep track of previous word


        if len(q) > 1:
            tmp = q[1:]
            #print(tmp)
            for element in tmp:
                if element not in ['1/4', '1/2', '3/4', '1/3', '2/3']:
                    msmtPart = element + " "
                    quant = quant[:2]
                    msmt = msmtPart + msmt
                else:
                    pass

        name = name[:-1]
        quant = quant[:-1]
        msmt = msmt[:-1]
        #print(prep)
        prep = prep[:-1]
        desc = desc[:-1]

        ingredientObj = {
            "name": f'{name}',
            "quantity": f'{quant}',
            "measurement": f'{msmt}',
            "preparation": f'{prep}',
            "descriptors": f'{desc}'
        }

        if 'cooking spray' in name:
            ingredients.append(ingredientObj)
        # So that we don't add the recipe section names to the ingredients
        if quant != "":
            ingredients.append(ingredientObj)

    return ingredients

def getTools(directionsList):
    toolsBuilder = ""
    for i in range(len(directionsList)):
        tokenized = pos_tag(word_tokenize(directionsList[i]))
        for t in range(len(tokenized)):
            if (tokenized[t][1] == 'NN' or tokenized[t][1] == 'NNS') and tokenized[t][0] not in toolsBuilder:
                #if single word
                if tokenized[t][0] in kitchenTools:
                    toolsBuilder += tokenized[t][0] + ', '
                #if two words
                if t < len(tokenized) - 1:
                    if tokenized[t][0] in kitchenTools_two and tokenized[t+1][0] in kitchenTools_two[tokenized[t][0]]:
                        toolsBuilder += tokenized[t][0] + ' ' + tokenized[t+1][0] + ', '
    toolsBuilder = toolsBuilder[:-2]
    toolsObj = {
        "tools": f'{toolsBuilder}'
    }
    return toolsObj

def getRecipeSoup(recipeUrl):
    # make web request to recipe web page
    response = requests.get(recipeUrl)
    # initialize beautiful soup object from web response
    soup = BeautifulSoup(response.text, features="html.parser") # changed to html.parser so we dont have to install a new one
    return soup

def getIngredientsList(recipeSoup):
    # access & format the ingredients list
    flag = 0
    ingredients = recipeSoup.find_all("li", class_="checkList__line")
    if not ingredients:
        flag = 1
        ingredients = recipeSoup.find_all("span", class_="ingredients-item-name")
    ingredientsResult = []
    if not flag:
        for ingredient in ingredients:
            ingredientsResult.append(ingredient.label.text)
    else:
        for ingredient in ingredients:
            ingredientsResult.append(ingredient.get_text())
    # cut off the "add more ingredients" text from the page
    ingredientsResult = ingredientsResult[:len(ingredientsResult)-3]
    return ingredientsResult

def getDirections(recipeSoup):
    alldirections = []
    directions = recipeSoup.find_all("span", class_="recipe-directions__list--item")
    if not directions:
        directions = recipeSoup.find_all("div", class_="section-body")
    for direction in directions:
        text = direction.get_text()
        alldirections.append(text)
    return alldirections

def getPrimaryMethods(directionsList):
    primaryMethodsBuilder = ""
    for i in range(len(directionsList)):
        directionLower = directionsList[i].lower()
        tokenized = pos_tag(word_tokenize(directionLower))
        for word in tokenized:
            if word[0] in ['bake', 'heat', 'cook', 'boil']:
                if word[0] not in primaryMethodsBuilder:
                    primaryMethodsBuilder += word[0] + ", "
    primaryMethodsBuilder = primaryMethodsBuilder[:-2]
    primaryMethodsObj = {
        "primaryMethods": f'{primaryMethodsBuilder}'
    }
    return primaryMethodsObj

def getSecondaryMethods(directionsList):
    secMethodsBuilder = ""
    for i in range(len(directionsList)):
        directionLower = directionsList[i].lower()
        tokenized = pos_tag(word_tokenize(directionLower))
        for word in tokenized:
            if word[0] in ['mix', 'stir', 'shake', 'pour', 'ladle', 'toss', 'drain', 'top', 'crumble', 'spray', 'combine', 'season']:
                if word[0] not in secMethodsBuilder:
                    secMethodsBuilder += word[0] + ", "
    secMethodsBuilder = secMethodsBuilder[:-2]
    secondaryMethodsObj = {
        "secondaryMethods": f'{secMethodsBuilder}'
    }
    return secondaryMethodsObj

def getSteps(directionsList):
    steps = []
    for i in range(len(directionsList)):
        step = directionsList[i].replace('Watch Now', '').rstrip()
        steps.append(step)
    return steps

#Print recipe object code
def printObject(recipeObject, steps_list, title):
  print(f'\nRecipe Title: {title}\n')
  for k in recipeObject:
    if sizetransform.checkIsInt(k):
      print(f'Ingredient Name: {recipeObject[k]["name"]}')
      print(f'Ingredient Quantity: {recipeObject[k]["quantity"]}')
      print(f'Ingredient Measurement: {recipeObject[k]["measurement"]}')
      print(f'Ingredient Preparation: {recipeObject[k]["preparation"]}')
      print(f'Ingredient Descriptors: {recipeObject[k]["descriptors"]}')
      print('\n')
    else:
      break

  print(f'Tools for Recipe: {recipeObject["tools"]}\n')

  print(f'Primary Cooking Methods: {recipeObject["primaryMethods"]}\n')

  print(f'Secondary Cooking Methods: {recipeObject["secondaryMethods"]}\n')

  print('Steps to Complete the Recipe: \n')
  indx = 1
  for i in range(len(steps_list) - 1):
    print(f'Step {indx}: {steps_list[i]}')
    indx += 1

  return


def main(recipeUrl):
    # create soup object that represents the input recipe's web page
    recipeSoup = getRecipeSoup(recipeUrl)
    # access the recipe's title
    recipeTitle = recipeSoup.title.string.split('- ')[0]
    # form list of text where ingredients are written from the web page
    ingredientsList = getIngredientsList(recipeSoup)
    # create ingredients objects for each ingredient
    # ingredients object has fields for name, quantity, measurement, preparation, description
    ingredients = getIngredientsObject(ingredientsList)
    # get list of words from recipe directions
    directionsList = getDirections(recipeSoup)
    # get tools from directionsList
    tools = getTools(directionsList)
    # get primary cooking methods from direcions list
    primaryMethods = getPrimaryMethods(directionsList)
    # get secondary cooking methods from directions list
    secondaryMethods = getSecondaryMethods(directionsList)
    # get steps from list of directions
    steps = getSteps(directionsList)
    # initialize dicitonary that will hold all individual ingredient dictionaries
    ingredDict = {}
    # assign number to each ingredient dictionary and add them to wrapper dictionary
    for i in range(len(ingredients)):
        ingredDict[f'{i}'] = ingredients[i]
    # create large dictionary that holds all ingredients, tools, primary and secondary cooking methdos
    recipeObj = {**ingredDict , **tools , **primaryMethods , **secondaryMethods}

    print(f'\nRecipe Title: {recipeTitle}\n')

    print('Steps to Complete the Recipe: \n')
    indx = 1
    for i in range(len(steps) - 1):
        print(f'Step {indx}: {steps[i]}')
        indx += 1

    vegetarianingredients = []
    vegsubstitutes = ['tofu', 'tempeh', 'seitan']
    brothReplacements = ['beef broth', 'chicken broth']
    meatreplacements = ['beef', 'chicken', 'turkey']
    measureslist = ['pound', 'pounds', 'ounce', 'ounces', 'oz', 'lb', 'kilogram', 'kilograms', 'package']

    transforming = True
    while (transforming):
        print ('\n')
        print ('Apply a transformation?')
        print ('\n')
        print ('(0) Done, show me my final recipe!')
        print ('(1) Make healthy?')
        print ('(2) Make vegetarian?')
        print ('(3) Double size?')
        print ('(4) Halve size?')
        print ('(5) Make non-vegetarian?')
        print ('(6) Change cuisine?')
        print ('(7) Make less healthy?')
        print ('(8) Start over with new recipe?')
        choice = input()

        if choice == '0':
            transforming = False
            print ('Here is your recipe:')
            printObject(recipeObj, steps, recipeTitle)
            break

        if choice == '1':
            healthy_ingredDict, steps = makeHealthy(steps, recipeTitle, recipeObj)
            recipeObj = {**healthy_ingredDict , **tools , **primaryMethods , **secondaryMethods}
            print('\n')
            continue

        if choice == '2':
            if not (vegetarianingredients):
                searchlist = transformvegetarian.getpagesearch("https://www.allrecipes.com/recipes/87/everyday-cooking/vegetarian/?page=4")
                vegetarianingredients = transformvegetarian.getVegIngreds(searchlist)
            recipeObj, steps = transformvegetarian.changeToVeg(recipeObj, vegetarianingredients, vegsubstitutes, steps)
            printObject(recipeObj, steps, recipeTitle)
            continue

        # choice = input('Double size? (y/n): ')
        if choice == '3':
            recipeObj = sizetransform.doubleSize(recipeObj)
            printObject(recipeObj, steps, recipeTitle)
            continue

        # choice = input('Halve size? (y/n): ')
        if choice == '4':
            recipeObj = sizetransform.halfSize(recipeObj)
            printObject(recipeObj, steps, recipeTitle)
            continue

        # choice = input('Make non-vegetarian? (y/n): ')
        if choice == '5':
            if not (vegetarianingredients):
                searchlist = transformvegetarian.getpagesearch("https://www.allrecipes.com/recipes/87/everyday-cooking/vegetarian/?page=4")
                vegetarianingredients = transformvegetarian.getVegIngreds(searchlist)
            recipeObj, steps = transformvegetarian.changeFromVeg(recipeObj, vegetarianingredients, meatreplacements, brothReplacements, vegsubstitutes, measureslist, steps)
            printObject(recipeObj, steps, recipeTitle)
            continue

        if choice == '6':
            cuisine = Cuisine(recipeObj, steps)
            cuisine.classify()
            print ('Select a cuisine to transform to:')
            print ('(1) British')
            print ('(2) Cajun')
            print ('(3) Chinese')
            print ('(4) French')
            print ('(5) Greek')
            print ('(6) Indian')
            print ('(7) Italian')
            print ('(8) Japanese')
            print ('(9) Mexican')

            choice = input()
            if choice == '1':
                recipeObj, steps = cuisine.transform('british')
                printObject(recipeObj, steps, recipeTitle)
                continue
            if choice == '2':
                recipeObj, steps = cuisine.transform('cajun')
                printObject(recipeObj, steps, recipeTitle)
                continue
            if choice == '3':
                recipeObj, steps = cuisine.transform('chinese')
                printObject(recipeObj, steps, recipeTitle)
                continue
            if choice == '4':
                recipeObj, steps = cuisine.transform('french')
                printObject(recipeObj, steps, recipeTitle)
                continue
            if choice == '5':
                recipeObj, steps = cuisine.transform('greek')
                printObject(recipeObj, steps, recipeTitle)
                continue
            if choice == '6':
                recipeObj, steps = cuisine.transform('indian')
                printObject(recipeObj, steps, recipeTitle)
                continue
            if choice == '7':
                recipeObj, steps = cuisine.transform('italian')
                printObject(recipeObj, steps, recipeTitle)
                continue
            if choice == '8':
                recipeObj, steps = cuisine.transform('japanese')
                printObject(recipeObj, steps, recipeTitle)
                continue
            if choice == '9':
                recipeObj, steps = cuisine.transform('mexican')
                printObject(recipeObj, steps, recipeTitle)
                continue

        if choice == '7':
            unhealthy_ingredDict, steps = makeUnhealthy(steps, recipeTitle, recipeObj)
            recipeObj = {**unhealthy_ingredDict , **tools , **primaryMethods , **secondaryMethods}
            print('\n')
            continue

        if choice == '8':
            recipeUrl = input('\nProvide a url for your recipe: ')
            main(recipeUrl)

if __name__ == '__main__':
    recipeUrl = input('Provide a url for your recipe: ')
    main(recipeUrl)
