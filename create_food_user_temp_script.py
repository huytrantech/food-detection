import provider
import models
import random
mongo_client = provider.init_client(username="mongo",password="12345678")

db = mongo_client["food_project"]
food_user_col = db["food_user"]
food_ingredients_col = db["food_ingredients"]

min_click = 0
max_click = 100

food_data_cursor = food_ingredients_col.find({})
food_data = []
for i in food_data_cursor:
    food_data.append(i)


for i in range(1,21):
    food_user_arr = []
    rand_rate_food = random.randint(5,len(food_data))
    for j in range(rand_rate_food):
        rand_food_index = random.randint(0,len(food_data)-1)
        food_item = food_data[rand_food_index]
        rand_total_click = random.randint(min_click, max_click)
        food_user_entity = models.FoodUserEntity(food_item["_id"], i, rand_total_click)
        food_user_arr.append(food_user_entity.to_dict())

    food_user_col.insert_many(food_user_arr)

mongo_client.close()

