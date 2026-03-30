import customtkinter as ctk
from database import initialize_database
from ui.recipe_list import RecipeList
from ui.recipe_detail import RecipeDetail

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CookbookApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("My Cookbook")
        self.geometry("1000x700")
        self.minsize(800, 600)

        initialize_database()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        self.recipe_list = RecipeList(
            self,
            on_recipe_select=self.on_recipe_select,
            on_add_recipe=self.on_add_recipe
        )
        self.recipe_list.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.recipe_detail = RecipeDetail(
            self,
            on_recipe_change=self.on_recipe_change
        )
        self.recipe_detail.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    def on_recipe_select(self, recipe):
        self.recipe_detail.load_recipe(recipe)

    def on_add_recipe(self):
        self.recipe_detail.clear_form()

    def on_recipe_change(self):
        self.recipe_list.refresh()

    def run(self):
        self.mainloop()