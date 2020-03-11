# kitchen tools list

kitchenTools = ['barbecue', 'colander', 'grill','baster', 'beanpot',
'brush','blender','basket', 'bowl','knife','pan', 'baking', 'sheet', 'colander', 'timer', 'poacher', 'grater', 'griddle', 'grinder', 'mixer', 'juicer', 'microwave', 'oven', 'peeler',
'pot', 'saucepan', 'strainer', 'steamer', 'skillet', 'scissors', 'sieve', 'skewer', 'tongs', 'whisk',
'wok', 'zester', 'plate', 'peeler', 'mortar', 'pestle', 'scale', 'timer', 'gloves', 'sieve', 'microwave', 'pot']

# kitchen tools with two words
kitchenTools_two = {
    "food": ["processor"],
    "cookie": ["cutter", "sheet", "sheets"],
    "bread": ["knife"],
    "cheese": ["grater, cutter, knife"],
    "pizza": ["wheel", "cutter"],
    'soup': ['ladle'],
    'rolling': ['pin'],
    'baking': ['dish', 'pan', 'sheet', 'sheets']
}

# healthy food substitutions
# key is the unhealthy item
# value: number of substitutions, sub name, quantity
# ex: "butter": [2, "almond butter", .5, "coconut oil", .5] --> 1/2 cup almond butter & 1/2 cup coco oil per cup butter
healthList = {
    "bread crumbs": [1, "rolled oats", 1],
    "butter": [2, "almond butter", .5, "coconut oil", .5], # also cooking spray
    "cream": [1, "evaporated skim milk", 1],
    "cream cheese": [1, "low-fat cottage cheese", 1], # pureed
    "eggs": [1, "egg whites", 2],
    "egg": [1, "egg white", 2],
    "flour": [1, "whole wheat flour", .5],
    "beef": [1, "chicken", 1],
    "milk": [1, "skim milk", 1],
    "sour cream": [1, "greek yogurt", 1],
    "couscous": [1, "quinoa", 1],
    "flour tortillas": [1, "corn tortillas", 1],
    "oatmeal": [1, "quinoa", 1],
    "croutons": [2, "almonds", .5, "walnuts", .5],
    "sugar": [1, "agave", .75],
    "chocolate chips": [1, "cacao nibs", 1],
    "soy sauce": [1, "low-sodium soy sauce", 1],
    "white rice": [1, "brown rice", 1],
    'rice': [1, 'cauliflower rice', 1],
    "bread": [1, "whole wheat bread", 1],
    "vegetable oil": [1, "olive oil", 1],
    "shortening": [1, "fat free margarine", 1],
    "mayonnaise": [2, "greek yogurt", .5, "mayonnaise", .5],
    "bacon": [1, "turkey bacon", 1],
    "pizza crust": [1, "cauliflower crust", 1],
    "taco shell": [1, 'lettuce wrap', 1],
    "parmesan cheese": [1, 'nutritional yeast', 1],
    "feta cheese": [1, 'nutritional yeast', 1],
    "brown sugar": [2, 'agave nectar', .5, 'brown sugar', .5],
    'ricotta cheese': [1, 'cottage cheese', 1],
    'heavy cream': [1, 'evaporated milk', 1],
    'dijon mustard': [1, 'mustard', 1],
    'honey': [1, 'maple syrup', 1]
}

#same format as healthy
unhealthy_list = {
    "skim milk": [1, "milk", 1],
    "evaporated skim milk": [1, "cream", 1],
    "egg whites": [1, "eggs", .5],
    "egg white": [1, "egg", .5],
    "quinoa": [1, "couscous", 1],
    "agave": [1, "sugar", 1],
    "parmesan cheese": [1, 'cheddar cheese', 2],
    "feta cheese": [1, 'gouda cheese', 2],
    "cheese": [1, 'cheddar cheese', 2],
    "salt": [1, 'salt', 1.5],
    "olive oil": [1, 'vegetable oil', 1],
    "butter": [1, 'shortening', 1],
    'brown rice': [1, 'white rice', 1],
    'whole wheat bread': [1, 'white bread', 1],
    'wheat bread': [1, 'white bread', 1],
    'bread': [1, 'white bread', 1],
    'chicken breast': [1, 'chicken thigh', 1],
    'low-fat milk': [1, 'milk', 1],
    'sugar': [1, 'granulated sugar', 1.5],
    'corn tortillas': [1, 'flour tortillas', 1],
    'plain yogurt': [1, 'sweetened yogurt', 1],
    'greek yogurt': [1, 'sweetened yogurt', 1],
    'cottage cheese': [1, 'ricotta cheese', 1],
    'evaporated milk': [1, 'heavy cream', 1],
    'cauliflower rice': [1, 'white rice', 1],
    'mustard': [1, 'honey mustard', 1],
    'honey': [2, 'granulated sugar', 4, 'water', 1]

}

measurement_conversions = {
    "ounces": ["oz", 1, 'ounce', 1, 'pound', 16, 'pounds', 16, 'lbs', 16, 'cups', 8, 'cup', 8],
    "oz": ["oz", 1, 'ounce', 1, 'pound', 16, 'pounds', 16, 'lbs', 16, 'cups', 8, 'cup', 8],
    "ounce": ["oz", 1, 'ounce', 1, 'pound', 16, 'pounds', 16, 'lbs', 16, 'cups', 8, 'cup', 8],
    "cup": ["pint", 2, "quart", 4, "gallon", 16],
    "cups": ["pint", 2, "quart", 4, "gallon", 16],
    "tbsp": ["cup", 16, "tablespoon", 1, "tablespoons", 1],
    "tbsps": ["cup", 16, "tablespoon", 1, "tablespoons", 1],
    "tablespoons": ["cup", 16, "tablespoon", 1, "tablespoons", 1],
    "tablespoon": ["cup", 16, "tablespoon", 1, "tablespoons", 1],
    "tsp": ["tbsp", 3, "tablespoon", 3, "tablespoons", 3],
    "tsps": ["tbsp", 3, "tablespoon", 3, "tablespoons", 3],
    "teaspoon": ["tbsp", 3, "tablespoon", 3, "tablespoons", 3],
    "teaspoons": ["tbsp", 3, "tablespoon", 3, "tablespoons", 3]
}

healthSubs = {
    "butter": "almond butter and coconut oil",
    "croutons": "almonds and walnuts",
    "mayonnaise": "greek yogurt and mayonnaise",
}

unhealthSubs = {
    'honey': "granulated sugar and water"
}



# top ingedients for each cuisine so we know how to transform and classify recipes
cuisines = {
    "brazilian": ["onions", "olive oil", "lime", "coconut milk", "totatoes", "condensed milk", "chicken", "steak", "fish"],

    "british": ["flour", "butter", "milk" "eggs", "heavy cream", "baking powder", "unsalted butter", "chicken", "steak", "fish",
    "whipped butter", "european style butter", "chicken", "beef"],

    "cajun": ["garlic", "green bell pepper", "butter", "andouille sausage",
    "creole seasoning", "cajun seasoning", "celery ribs", "celery", "chicken", "steak", "fish", "tilapai", "carp", "cod",
    ],

    "chinese": ["soy sauce", "sesame oil", "corn starch", "sugar", "five-spice powder","hoisin sauce", "oyster sauce", " peanut oil",
     "white rice", "rice","bok choy", "wasabi", "chicken", "beef", "sesame seeds"],

    "filipino": ["garlic", "onions", "soy sauce", "cooking oil", "bay leaf", "bay leaves", "fish sauce", "ground cinnamon",
    "crayfish", "oyster", "roe", "caviar"],

    "french": ["sugar", "flour", "unsalted butter", "olive oil", "shallots", "goat cheese"],

    "greek": ["olive oil", "dried oregano", "garlic cloves", "garlic", "oregano", "feta cheese", "feta",
     "cucumber", "lemon juice", "lamb", "fenugreek"],

    "indian": ["onions", "garam masala", "ground turmeric", "turmeric", "masala", "tikki masala", "garam masala", "cumin seed", "green chilies",
    "coconut milk", "ground cinnamon"],

    "irish": ["flour", "butter", "onions", "potatoes", "buttermilk", "baking powder", "milk", "whipped butter", "european style butter", "goat cheese"],

    "italian": ["olive oil", "garlic cloves", "garlic", "grated parmesan", "parmesan", "basil", "e.v. olive oil",
    "black pepper", "basil", "spagehetti", "fettuccine", "lunguine", "penne", "rigatoni", "orecchiette",
 "farfalle", "pappardelle", "fusilli", "rigatoni", "orzo", "tortellini", "ziti",
 "ravioli", "macaroni", "cappelletti", "lasagne", "gnocci", "rotini", "olives", "black olives", "alfredo", "marinara",
 "sausage", "goat cheese"],

    "jamaican": ["onions", "garlic", "ground allspice", "allspice", "thyme", "sausage", "ground cinnamon"],

    "japanese": ["soy sauce", "mirin", "sugar", "shichimi", "sake", "rice vinegar", "scallions", "oyster", "clam", "mussel", "fish", "eel", "salmon",
    "octopus", "squid", "white rice", "rice", "bok choy",  "wasabi", "crayfish", "oyster", "roe", "caviar", "sesame seeds"],

    "korean": ["soy sauce", "sesame oil", "garlic", "green onions", "sugar", "gochujang", "kimchi", "toasted sesame seeds", "sesame seeds", "sesame oil",
    "beef", "bok choy", "wasabi", "crayfish", "oyster", "roe", "caviar"],

    "mexican": ["onions", "ground cumin", "cumin", "garlic", "olive oil", "adobo", "corn tortillas", "salsa", "flour tortilla", "tortilla",
    "black beans", "avocado", "chicken", "steak", "fish", "adobo", "chili powder", ],

    "moroccan": ["olive oil", "ground cumin", "cumin", "onions", "garlic cloves", "garlic", "couscous", "chickpeas",
     "ground ginger", "cinnamon", "ginger", "coriander", "ground cinnamon", "saffron", "turmeric", "cumin", "cardamom", "mace", ],

    "spanish": ["olive oil", "garlic cloves", "garlic", "e.v. olive oil", "e.v. olive oil", "white wine", "red bell pepper", "parsley", "tomatoes",
    "rice"],

    "thai": ["fish sauce", "garlic", "coconut milk", "vegetable oil", "lemongrass", "peanuts", "lime juice",
    "rice", "white rice",],

    "vietnamese": ["fish sauce", "sugar", "garlic", "beansprouts", "cucumber", "rice vinegar", "lemongrass",
    "rice", "bok choy", "wasabi", "crayfish", "oyster", "roe", "caviar"],
}


# master list of types of ingredients so we know how to replace them
meat = ["lamb", "chicken", "steak", "fish", "tuna", "salmon", "ribeye",
"rib-eye", "flank", "bacon", "pork", "beef", "duck", "turkey", "ham",
"mutton", "sausage", "poultry", "venison", "red meat", "veal", "white meat",
"goat", "anchovy", "hot dog", "salami", "meatball", "quail", "breast", "chicken breast",
"chicken thigh", "chicken wing", "liver", "andouille sausage"]

seafood = ["oyster", "clam", "mussel", "fish", "eel", "salmon", "trout", "shrimp",
 "swordfish", "tuna", "tilapai", "carp", "cod", "octopus", "herring", "squid", "catfish",
  "lobster", "anchovy", "scallop", "mahi-mahi", "crayfish", "oyster", "roe", "caviar",
   "monkfish", "abalone", "skate", "mackerel"]

pasta = ["spaghetti", "fettuccine", "lunguine", "penne", "rigatoni", "orecchiette",
 "farfalle", "pappardelle", "fusilli", "rigatoni", "orzo", "tortellini", "ziti",
 "ravioli", "macaroni", "cappelletti", "lasagne", "gnocci", "rotini", "elbow macaroni"]

grains = ["rice", "barley", "quinoa", "oat", "millet", "maize",
"rye", "whole grain", "wild rice", "brown rice", "white rice"]

sauce = ["alfredo", "marinara", "soy sauce", "mushroom sauce", "steak sauce",
 "barbecue", "bbq", "sauce", "salsa", "hollandaise", "mayonnaise", "cocktail sauce",
  "hot sauce", "peanut sauce", "bechamel sauce", "bechamel", "sweet and sour", "oyster sauce",
  "tomato sauce", "hoisin", "hoisin sauce", "pesto", "pesto sauce", "tartar", "chimichurri",
  "creole sauce", "worcestershire", "mirin", "katchup", "relish", "hoisin sauce", "fish sauce"]

seasoning = ["pepper", "salt", "cinnamon", "chili powder", "ground cinnamon",
"chili flakes", "cumin", "ginger", "ground ginger", "nutmeg", "paprika",
"oregano", "dried oregano", "bay leaf", "bay leaves", "cayenne",
"cayenne pepper", "paprika", "tarragon", "creole seasoning", "cajun seasoning"]

spices = ["adobo", "chili powder", "masala", "five-spice powder", "curry powder",
 "allspice", "lemon pepper", "taco", "shichimi", "old bay", "tikki masala", "tandoori masala", "garlic salt",
 "nutmeg", "ginger", "saffron", "turmeric", "cumin", "cardamom", "mace", "fenugreek", "vanilla", "paprika",
 "fennel", "clove", "garlic", "black pepper", "coriander", "star anise", "anise", "mustard seed", "garam masala",
  "chili powder", "onion powder", "ground turmeric", "cumin seed"]

herbs = ["basil", "parsley", "rosemary", "thyme", "oregano", "sage", "chives", "mint", "dill", "lavender", "tarragon", "majoram", "coriander",
"fennel", "chervil", "lemongrass", "cilantro", "pepperming", "chamomile", "anise", "arugula"]

fats = ["olive oil", "almond butter", "butter", "unsalted butter", "e.v. olive oil", "avocado oil",
 "sesame oil", "almond oil", "sunflower oil", "peanut oil", "canola oil", "grapeseed oil", "soybean oil",
 "whipped butter", "european style butter", "peanut butter", "sesame oil"]

dairy = ["milk", "goat milk", "yogurt", "ice cream", "cottage cheese", "buttermilk",
"sour cream", "cream cheese", "oat milk", "almond milk", "soy milk", "heavy cream", "coconut milk"]

cheese = ["cheese", "parmesan", "parmesan cheese", "feta", "goat cheese", "feta cheese",
 "blue cheese", "cheddar cheese", "gouda cheese", "camembert", "queso", "asiago cheese",
  "mascarpone", "monterey jack cheese", "provolone", "gorgonzola", "cream cheese"]

vegetables = ["asparagus", "lettuce", "celery", "brussels sprout", "broccoli", "cabbage", "spinach", "potato", "carrot", "kale", "curly kale",
"okra", "artichoke", "radish", "rhubarb", "pumpkin", "watercress", "cauliflower", "onion", "eggplant", "beetroot", "tomato", "parsnip", "arugula",
"cucumber", "pea", "turnip", "collard", "sweet potato", "ginger", "chives", "bean", "black beans", "pinto beans", "corn", "sweet corn",
"chesnut", "bok choy", "dill", "wasabi", "zucchini", "leek", "shallot", "beets", "beansprouts", "bell pepper", "mushrooms","onions"]

fruits = ["berry", "apple", "papaya", "blueberry", "raspberry", "pear", "pineapple", "mango",
 "apricot", "avocado", "banana", "cherry", "lemon", "grapefruit", "orange", "grape", "pomegranate",
 "tangerine", "plum", "tomato", "watermelon", "clementine", "strawberry", "kiwi", "elderberry", "cranberry",
  "blackberry", "lime"]

toppings = ["sesame seeds", "toasted sesame seeds"]

measurements = ["package", "cup", "teaspoon", "tablespoon", "ounce", "teaspoons", "pound", "pounds",
 "tablespoons", "pint", "pinch", "cups", "ounces", "slices", "packages", "cloves", "frying", "drop",
 "packet", "fluid", "head", "inch", "container", "cubes", "cube", "quart", "quarts", "halves", "jar"]

adjectivesInNames = ["black", "olive", "maple", "beef", "garlic", "sour", "lemon", "heavy", "yellow",
 "chocolate", "vegetable", "lime", "angel", "bread", "cheese", "chorizo", "chipotle",
 "jalapeno", "sazon", "spaghetti", "brownie", "chocolate", "candy", "tomato", "lamb"]
