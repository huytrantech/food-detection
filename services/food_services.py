import models


class FoodService(object):
    def __init__(self, mongo_client):
        self.mongo_client = mongo_client
        self.db = self.mongo_client["food_project"]

    def get_name_food_from_ingredients(self, request: models.FoodIngredientsRequest):
        filter_query = {"ingredients": {"$in": ["chicken", "eggplant"]}}

        food_ingredients_collection = self.db["food_ingredients"]

        skip = (request.paging - 1) * request.limit
        data = food_ingredients_collection.find(filter_query).limit(request.limit).skip(skip)
        return data
