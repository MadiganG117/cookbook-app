"""
Recipe List Panel
The left side panel of the app. Displays a scrollable, searchable list
of all recipes and a button to add new ones.
"""

import customtkinter as ctk
from services.recipe_service import get_all_recipes


class RecipeList(ctk.CTkFrame):
    """
    A panel that displays all recipes in a scrollable list with a search bar.
    Communicates with the rest of the app through callback functions passed in
    from app.py.
    """

    def __init__(self, parent, on_recipe_select, on_add_recipe):
        """
        Initialize the recipe list panel.

        Args:
            parent: The parent window this panel belongs to
            on_recipe_select: Function to call when a recipe is clicked
            on_add_recipe: Function to call when Add Recipe is clicked
        """
        super().__init__(parent)

        self.on_recipe_select = on_recipe_select
        self.on_add_recipe = on_add_recipe
        self.recipes = []

        # Search bar
        self.search_var = ctk.StringVar()
        self.search_var.trace("w", self.filter_recipes)
        self.search_bar = ctk.CTkEntry(
            self,
            placeholder_text="Search recipes...",
            textvariable=self.search_var
        )
        self.search_bar.pack(padx=10, pady=10, fill="x")

        # Scrollable recipe list
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="My Recipes")
        self.scroll_frame.pack(padx=10, pady=5, fill="both", expand=True)

        # Add recipe button
        self.add_button = ctk.CTkButton(
            self,
            text="+ Add Recipe",
            command=self.on_add_recipe
        )
        self.add_button.pack(padx=10, pady=10, fill="x")

        self.load_recipes()

    def load_recipes(self):
        """Fetches all recipes from the service layer and displays them."""
        self.recipes = get_all_recipes()
        self.display_recipes(self.recipes)

    def display_recipes(self, recipes):
        """
        Clears the list and redraws it with the provided recipes.

        Args:
            recipes: A list of Recipe objects to display
        """
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        if not recipes:
            ctk.CTkLabel(self.scroll_frame, text="No recipes yet!").pack(pady=20)
            return

        for recipe in recipes:
            btn = ctk.CTkButton(
                self.scroll_frame,
                text=recipe.title,
                anchor="w",
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                command=lambda r=recipe: self.on_recipe_select(r)
            )
            btn.pack(fill="x", padx=5, pady=2)

    def filter_recipes(self, *args):
        """Filters the displayed recipes based on the search bar input."""
        search_term = self.search_var.get().lower()
        filtered = [r for r in self.recipes if search_term in r.title.lower()]
        self.display_recipes(filtered)

    def refresh(self):
        """Reloads recipes from the service layer and redraws the list."""
        self.load_recipes()