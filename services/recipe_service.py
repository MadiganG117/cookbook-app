"""
Recipe Service Layer
Sits between the UI and the database, handling all business logic
and converting raw database rows into proper Recipe objects.
The UI should only ever talk to this file, never to database.py directly.
"""

from database import (
    get_all_recipes as db_get_all,
    get_recipe as db_get_one,
    add_recipe as db_add,
    update_recipe as db_update,
    delete_recipe as db_delete
)
from models.recipe import Recipe


def get_all_recipes():
    """
    Fetches all recipes from the database and converts them into Recipe objects.
    
    Returns:
        A list of Recipe objects sorted alphabetically by title
    """
    rows = db_get_all()
    return [Recipe.from_db_row(row) for row in rows]


def get_recipe(recipe_id):
    """
    Fetches a single recipe by its ID and converts it into a Recipe object.
    
    Args:
        recipe_id: The unique ID of the recipe to fetch
        
    Returns:
        A Recipe object, or None if not found
    """
    row = db_get_one(recipe_id)
    return Recipe.from_db_row(row) if row else None


def save_recipe(recipe_id, title, ingredients, instructions, prep_time, cook_time, servings, notes):
    """
    Validates recipe data and either creates a new recipe or updates an existing one.
    
    Args:
        recipe_id: If provided, updates the existing recipe. If None, creates a new one.
        title: Name of the recipe
        ingredients: Ingredients as a string
        instructions: Instructions as a string
        prep_time: Preparation time in minutes
        cook_time: Cooking time in minutes
        servings: Number of servings
        notes: Personal notes
        
    Returns:
        A tuple of (success, error_message)
        success is True if saved successfully, False if validation failed
        error_message is None on success, or a string describing the problem
    """
    # Validate required fields
    if not title:
        return False, "Title is required!"
    if not ingredients:
        return False, "Ingredients are required!"
    if not instructions:
        return False, "Instructions are required!"

    # Convert time and servings to integers if provided
    prep_time = int(prep_time) if str(prep_time).isdigit() else None
    cook_time = int(cook_time) if str(cook_time).isdigit() else None
    servings = int(servings) if str(servings).isdigit() else None

    # Update or create depending on whether recipe_id is provided
    if recipe_id:
        db_update(recipe_id, title, ingredients, instructions, prep_time, cook_time, servings, notes)
    else:
        db_add(title, ingredients, instructions, prep_time, cook_time, servings, notes)

    return True, None


def delete_recipe(recipe_id):
    """
    Deletes a recipe by its ID.
    
    Args:
        recipe_id: The unique ID of the recipe to delete
    """
    db_delete(recipe_id)