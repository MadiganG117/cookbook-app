class Recipe:
    """
    Represents a single recipe in the cookbook.
    This class acts as a structured container for recipe data,
    converting raw database rows into clean, usable objects.
    """

    def __init__(self, id, title, ingredients, instructions, prep_time, cook_time, servings, notes):
        """
        Initialize a Recipe object with all its fields.
        
        Args:
            id: Unique identifier from the database
            title: Name of the recipe
            ingredients: List of ingredients as a string
            instructions: Step by step cooking instructions as a string
            prep_time: Preparation time in minutes
            cook_time: Cooking time in minutes
            servings: Number of servings the recipe makes
            notes: Personal notes about the recipe
        """
        self.id = id
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.prep_time = prep_time or 0
        self.cook_time = cook_time or 0
        self.servings = servings or 1
        self.notes = notes or ""

    def total_time(self):
        """Returns the total time needed by adding prep and cook time together."""
        return self.prep_time + self.cook_time

    def __str__(self):
        """Returns a readable string representation of the recipe."""
        return f"Recipe: {self.title}"

    @classmethod
    def from_db_row(cls, row):
        """
        Converts a raw database row into a Recipe object.
        This is used by the service layer every time it fetches data from the database.
        
        Args:
            row: A sqlite3.Row object returned from the database
            
        Returns:
            A fully populated Recipe object
        """
        return cls(
            id=row["id"],
            title=row["title"],
            ingredients=row["ingredients"],
            instructions=row["instructions"],
            prep_time=row["prep_time"],
            cook_time=row["cook_time"],
            servings=row["servings"],
            notes=row["notes"]
        )