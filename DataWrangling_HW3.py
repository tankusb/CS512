# Python Project for data wrangling (week three CS 512) part 1 of X
# Goal: This file pulls raw data and dumps it into a text file structured as a set of sets, where each set item is one recipe
#   EX: {{recipe 1}, {recipe 2}, .... , {recipe n}}
# Goal cont: The text file will be picked up and used for analysis in a future code
# Authors: Ben Tankus, Tiffany Chan

## CAUTION: Do not run this code for more than 500 calls per day or Ben will get charged


import requests, random, pprint, json, pandas as pd, fsspec, matplotlib.pyplot, csv

# Gets data from recipe site
def getData():
    ''' Retrieves a list of n recipes from the spoonacular API.
        'instructions' - Used to list instructions. None if no instructions for recipe
        'vegetarian', 'vegan', 'veryHealthy', 'cheap', 'veryPopular', 'sustainable' - True / False relevant measures 
        'cuisines', 'dishTypes', 'occasions', 'equipment' - key's to access useful list values. not always available
        'ingredients', contains a list of dictionaries. 'name' is the key to access ingredient name. Organized by step
        'title', 'readyInMinutes','sourceUrl', 'image', 'pricePerServing', summary' (maybe for the first 100char?)
        equipment - recipe[0]['analyzedInstructions']['steps'][stepNumberInList]['equipment']
        '''

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/informationBulk"

    headers = {
        'x-rapidapi-key': "cbd82fc408msh2e96d8e9a0caf67p152111jsn82703903f8f1",
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

    recipeDict = {}
    n = 15 # Number of recipes to pull

    for k in range(1,n):
        recipeID = random.randint(1,300000)
        querystring = {"ids": str(recipeID)}
        response = requests.request("GET", url, headers=headers, params=querystring, json = True)
        recipe = json.loads(response.text)

        # Fill data dict with easy entries
        try:
            recipeDict[recipeID] = {"cuisines" : recipe[0]['cuisines'], 
                                    'dishTypes': recipe[0]['dishTypes'], 
                                    'spoonScore': recipe[0]['spoonacularScore'], 
                                    'Vegan': recipe[0]['vegan'], 
                                    'Vegetarian': recipe[0]['vegetarian'],
                                    'ImageURL': recipe[0]['image'],
                                    'Title': recipe[0]['title'],
                                    'SourceURL': recipe[0]['sourceUrl'],
                                    'readyInMinutes': recipe[0]['readyInMinutes'],
                                    'PricePerServing': recipe[0]['pricePerServing'],
                                    'Summary': recipe[0]['summary'][:200].replace("</b>", "").replace("<b>", "").replace("</a>", "").replace("<a>", "")
                                    }

        except:
            print('Bad Recipe')
            continue

        print("Clean Recipe")
        
        # Add equipment to data dict
        equipmentList = []
        try:
            for step in recipe[0]['analyzedInstructions'][0]['steps']:
                pass
                for equipment in step['equipment']:
                    if equipment['name'] not in equipmentList:
                        equipmentList.append(equipment['name'])
        except Exception as e2:
                print('Likely no equipment required', e2) 
                continue  
        recipeDict[recipeID]['equipment'] = equipmentList    

    # Write dataDict to file
    f = open('Recipe.txt', 'w')
    for key, val in recipeDict.items():
        f.write( str(key) + ':' + str(val) )
        #print('writen')
    f.close()
    return recipeDict

# JSON converter >> Dict to JSON
def convertJson(recipeDict):
    '''Takes recipeDict and converts it to json file type'''
    jsonObj = json.dumps(recipeDict)
    with open('jsonRecipe.json','w') as f:
        f.write(jsonObj) 
    return jsonObj
    

def jsonToCSV(jsonObj): 
    '''Takes json file and converts it to csv'''
    df = pd.read_json('jsonRecipe.json')
    dfTransp = df.T
    dfTransp.index.name = "id"
    fileName = 'csvRecipe.csv'
    dfTransp.to_csv(fileName, index = True)
    return fileName   # USED IN CSVtoJSON FUNCTION

def CSVtoJSON(csvLoc):
    '''Takes CSV file and converts it to JSON'''
    dfCSV = pd.read_csv(csvLoc)
    dfCSV.T.to_json('recipes.json') # TRANSPOSE DF BACK TO MAINTAIN OBJECT:NAMEPAIR JSON FORMAT
    
    

# >>>>>>>>>>>> MAIN SCRIPT <<<<<<<<<<<<<<<<
recipeDict = getData()   # GRAB DATA
jsonObj = convertJson(recipeDict) # CONVERT ORIGINAL DATA PULL TO JSON FORMAT
CSVFileLoc = jsonToCSV(jsonObj)  # CONVERT JSON TO CSV
CSVtoJSON(CSVFileLoc) # CONVERT CSV TO JSON

df = pd.read_csv(CSVFileLoc)
# Plot
fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111)
ax.hist(df['readyInMinutes'])
ax.set_title("HW3 Matplotlib Load Data Proof")
ax.set_xlabel('Ready in Minutes')
matplotlib.pyplot.show()
