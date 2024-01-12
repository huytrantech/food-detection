class FoodEntity(object):
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def to_dict(self):
        return self.__dict__


class FoodIngredientsRequest(object):
    def __init__(self, ingredients, limit=10, paging=1):
        self.ingredients = ingredients
        self.limit = limit
        self.paging = paging


class FoodUserEntity(object):
    def __init__(self, food_id, user_id, total_click):
        self.food_id = food_id
        self.user_id = user_id
        self.total_click = total_click

    def to_dict(self):
        return self.__dict__
