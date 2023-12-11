spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [name["name"] for name in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [ spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5 ]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_list = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_list)
    

def get_average_heat_level(spicy_foods):
    total = 0
    for food in spicy_foods:
        total += food['heat_level']
    
    return total / len(spicy_foods)
        

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

# def get_names(spicy_foods):
#     names = []
#     for food in spicy_foods:
#         names.append(food['name'])
#     return names

# def get_spiciest_foods(spicy_foods):
#     spiciest_food = []
#     for food in spicy_foods:
#         spice_level = food["heat_level"]
#         if spice_level > 5:
#            spiciest_food.append(food)
#            return spicy_foods

# def print_spicy_foods(spicy_foods):
#     for food in spicy_foods:
#         name = food['name']
#         spiciness_level = food['spiciness_level']
#         heat_level = '🌶' * spiciness_level
#         print(f"{name} | Heat Level: {heat_level}")

# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     cuisine_foods = dict()
#     for food in spicy_foods:
#         if food["cuisine"] == cuisine:
#             cuisine_foods[food["name"]] = food
#     return cuisine_foods

# def print_spiciest_foods(spicy_foods):
#     for food in spicy_foods:
#         if food["heat_level"] > 5:
#             name = food['name']
#             spiciness_level = food['spiciness_level']
#             heat_level = '🌶' * spiciness_level
#             print(f"{name} | Heat Level: {heat_level}")  
    

# def get_average_heat_level(spicy_foods):
#     heat_level = 0
#     for food in spicy_foods:
#         heat_level += food["heat_level"]
#         average = heat_level / len(food)
#         return average

# def create_spicy_food(spicy_foods, spicy_food):
#     spicy_food = dict()
#     spicy_food["name"] = spicy_food["name"]
#     spicy_food["cuisine"] = spicy_food["cuisine"]
#     spicy_food["heat_level"] = spicy_food["heat_level"]
#     spicy_foods.append(spicy_food)
#     return spicy_foods


# ===============================================================

# def get_names(spicy_foods):
#     food_names = [food["name"] for food in spicy_foods]
#     return food_names

#     pass

# def get_spiciest_foods(spicy_foods):
#     return [food for food in spicy_foods if food["heat_level"] > 5]
#     pass

# def print_spicy_foods(spicy_foods):
#     for food in spicy_foods:
#         heat_level = "🌶" * food["heat_level"]
#         print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
#     pass

# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#      for food in spicy_foods:
#         if food["cuisine"] == cuisine:
#             return food
#      return None

#      pass

# def print_spiciest_foods(spicy_foods):
#     spiciest = get_spiciest_foods(spicy_foods)
#     if spiciest:
#         print_spicy_foods(spiciest)
#     pass

# def get_average_heat_level(spicy_foods):
#      total_heat = sum(food["heat_level"] for food in spicy_foods)
#      return total_heat // len(spicy_foods)
#      pass

# def create_spicy_food(spicy_foods, spicy_food):
#     modified_spicy_foods = spicy_foods.copy()
#     modified_spicy_foods.append(spicy_food)
#     return modified_spicy_foods



#     pass