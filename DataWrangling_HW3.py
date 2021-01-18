# Python Project for data wrangling (week three CS 512) part 1 of X
# Goal: This file pulls raw data and dumps it into a text file structured as a set of sets, where each set item is one recipe
#   EX: {{recipe 1}, {recipe 2}, .... , {recipe n}}
# Goal cont: The text file will be picked up and used for analysis in a future code
# Authors: Ben Tankus, Tiffany Chan

## CAUTION: Do not run this code for more than 500 calls per day or Ben will get charged


import requests, random, pprint, json

def getData():
    ''' Retrieves a list of n recipes from the spoonacular API.
        'instructions' - Used to list instructions. None if no instructions for recipe
        'vegetarian', 'vegan', 'veryHealthy', 'cheap', 'veryPopular', 'sustainable' - True / False relevant measures 
        'cuisines', 'dishTypes', 'occasions', 'equipment' - key's to access useful list values. not always available
        'ingredients', contains a list of dictionaries. 'name' is the key to access ingredient name. Organized by step
        'title', 'readyInMinutes','sourceUrl', 'image', 'pricePerServing', summary' (maybe for the first 100char?)
        '''

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/informationBulk"

    headers = {
        'x-rapidapi-key': "cbd82fc408msh2e96d8e9a0caf67p152111jsn82703903f8f1",
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

    recipieList = {}
    n = 5 # Number of recipes to pull

    # Loop through numbers
    for k in range(1,n):
        recipeID = random.randint(1,300000)
        querystring = {"ids": str(recipeID)}
        response = requests.request("GET", url, headers=headers, params=querystring, json = True)

        recipe = json.loads(response.text)
        print(type(recipe))

        try:
            recipieList[recipeID] = recipe[0]
        except: # No recipe
            print("recipeID", recipeID, "is bad")
            continue

    with open('Recipe.txt','w') as f:
        f.write("{")
        for item in recipieList.values():
            f.write(str(item) + "," + '\n\n\n')
        f.write("}")

    return recipieList

getData()