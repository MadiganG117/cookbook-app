class Recipe:
    def __init__(self, id, title, ingredients, instructions, prep_time, cook_time, servings, notes):
        self.id = id
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.servings = servings
        self.notes = notes

    def __str__(self):
        return f"Recipe: {self.title}"