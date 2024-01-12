import pandas
import models
import provider


def parse_food_ingredients_data():
    data = pandas.read_csv('datasets/food_data/food_and_ingredients.data')
    food_arr = []
    for index, row in data.iterrows():
        food_element = models.FoodEntity(row["name"], row["ingredients"].split("-"))
        food_arr.append(food_element)
    return food_arr


def save_data_mongo():
    food_data = parse_food_ingredients_data()
    food_data_dict = []
    for e in food_data:
        food_data_dict.append(e.to_dict())
    mongo_client = provider.init_client(username="mongo", password="12345678")
    my_db = mongo_client["food_project"]
    my_collection = my_db["food_ingredients"]
    my_collection.insert_many(food_data_dict)


save_data_mongo()
