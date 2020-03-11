from bs4 import BeautifulSoup
import json
import requests
from nltk import pos_tag, word_tokenize
import sys
from lists import healthList, pasta, unhealthSubs, unhealthy_list
#from nutritionInfo import tester

def checkIsInt(key):
  try:
    ind = int(key)
  except ValueError:
    return False
  return True

def makeUnhealthy(steps, recipeTitle, recipeObj):


    print('\nFinding unhealthy substitutions for your ingredients...')

    print(f'\nRecipe Title: Unhealthy {recipeTitle}\n')


    ingredients = []
    for k in recipeObj:
        if checkIsInt(k):
            ingredientObj = {
                "name": f'{recipeObj[k]["name"]}',
                "quantity": f'{recipeObj[k]["quantity"]}',
                "measurement": f'{recipeObj[k]["measurement"]}',
                "preparation": f'{recipeObj[k]["preparation"]}',
                "descriptors": f'{recipeObj[k]["descriptors"]}'
            }
            ingredients.append(ingredientObj)

    old_ingredients = []
    healthy_ingredients = []
    # list of foods that got substituted
    substitutions = []
    # list of foods that got removed
    removed = []
    quant = ""


    # switch out ingredients from unhealthy_list
    for ingredient in ingredients:
        ingredient["name"] = ingredient["name"].lower()
        if ingredient["name"] in unhealthy_list:
            substitutions.append(ingredient["name"])
            #for every substitution ingredient
            ingredientNumber = 1
            while ingredientNumber < len(unhealthy_list.get(ingredient["name"])):
            # adjust quantity
                if unhealthy_list.get(ingredient["name"])[ingredientNumber + 1] != 1:
                    quantity = convertFractoFloat(ingredient["quantity"])
                    new_quantity = quantity * float(unhealthy_list.get(ingredient["name"])[ingredientNumber + 1])
                    quant = str(new_quantity)
                else:
                    quant = ingredient["quantity"]

                #change name
                sub = ingredient["name"]
                name = unhealthy_list.get(ingredient["name"])[ingredientNumber]
                msmt = ingredient["measurement"]
                prep = ingredient["preparation"]
                desc = ""

                ingredientObj = {
                    "substitution": f'{sub}',
                    "name": f'{name}',
                    "quantity": f'{quant}',
                    "measurement": f'{msmt}',
                    "preparation": f'{prep}',
                    "descriptors": f'{desc}'
                }

                healthy_ingredients.append(ingredientObj)
                #try adding to old_ingredients
                old_ingredients.append(ingredientObj)
                ingredientNumber += 2
        else:
            old_ingredients.append(ingredient)

    if removed != []:
        print('Removed Ingredients: ' )
    for ingredient in removed:
        print(ingredient)
        print("\n")

    alreadySubbed = []
    for ingredient in healthy_ingredients:
        # switch out old ingredients from directions
        if ingredient["substitution"] not in alreadySubbed:
            if ingredient["substitution"] in unhealthSubs:
                sub = unhealthSubs.get(ingredient["substitution"])
            else:
                sub = ingredient["name"]

            alreadySubbed.append(ingredient["substitution"])
            indx = 1
            for i in range(len(steps) - 1):
                if ingredient["substitution"] in steps[i]:
                    steps[i] = steps[i].replace(ingredient["substitution"], sub)

    for ingredient in old_ingredients:
        if "substitution" in ingredient:
            if ingredient["name"] == ingredient["substitution"]:
                print(f'Ingredient Name: {ingredient["name"]} (altered quantity)')
            else:
                print(f'Ingredient Name: {ingredient["name"]} (substitution for {ingredient["substitution"]})')
        else:
            print(f'Ingredient Name: {ingredient["name"]}')
        print(f'Ingredient Quantity: {ingredient["quantity"]}')
        print(f'Ingredient Measurement: {ingredient["measurement"]}')
        print(f'Ingredient Preparation: {ingredient["preparation"]}')
        print(f'Ingredient Descriptors: {ingredient["descriptors"]}')
        print('\n')

    print('Steps to Complete the Recipe: \n')
    indx = 1
    for i in range(len(steps) - 1):
        print(f'Step {indx}: {steps[i]}')
        indx += 1

    #make recipeObj
    ingredDict = {}
    for i in range(len(old_ingredients)):
        ingredDict[f'{i}'] = old_ingredients[i]

    return ingredDict, steps

def convertFractoFloat(number):
    total = 0
    num = number.split()
    for n in num:
        frac = n.split('/')
        if len(frac) == 1:
            value = float(frac[0])
        else:
            value = float(frac[0]) / float(frac[1])
        total += value
    return total
