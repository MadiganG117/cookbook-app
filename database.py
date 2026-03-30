import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "cookbook.db"

def get_connection():
    """Create and return a connection to the database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    """Create the recipes table if it doesn't already exist."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            ingredients TEXT NOT NULL,
            instructions TEXT NOT NULL,
            prep_time INTEGER,
            cook_time INTEGER,
            servings INTEGER,
            notes TEXT
        )
    """)

    conn.commit()
    conn.close()

def add_recipe(title, ingredients, instructions, prep_time, cook_time, servings, notes):
    """Add a new recipe to the database."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO recipes (title, ingredients, instructions, prep_time, cook_time, servings, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (title, ingredients, instructions, prep_time, cook_time, servings, notes))

    conn.commit()
    conn.close()

def get_all_recipes():
    """Return a list of all recipes."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recipes ORDER BY title")
    recipes = cursor.fetchall()

    conn.close()
    return recipes

def get_recipe(recipe_id):
    """Return a single recipe by its ID."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recipes WHERE id = ?", (recipe_id,))
    recipe = cursor.fetchone()

    conn.close()
    return recipe

def update_recipe(recipe_id, title, ingredients, instructions, prep_time, cook_time, servings, notes):
    """Update an existing recipe."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE recipes
        SET title = ?, ingredients = ?, instructions = ?, prep_time = ?, cook_time = ?, servings = ?, notes = ?
        WHERE id = ?
    """, (title, ingredients, instructions, prep_time, cook_time, servings, notes, recipe_id))

    conn.commit()
    conn.close()

def delete_recipe(recipe_id):
    """Delete a recipe by its ID."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))

    conn.commit()
    conn.close()