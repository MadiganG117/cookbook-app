import customtkinter as ctk
from tkinter import messagebox
from database import add_recipe, update_recipe, delete_recipe

class RecipeDetail(ctk.CTkFrame):
    def __init__(self, parent, on_recipe_change):
        super().__init__(parent)

        self.on_recipe_change = on_recipe_change
        self.current_recipe = None
        self.is_editing = False

        # Title
        self.title_var = ctk.StringVar()
        self.title_entry = ctk.CTkEntry(
            self,
            textvariable=self.title_var,
            font=ctk.CTkFont(size=20, weight="bold"),
            placeholder_text="Recipe Title"
        )
        self.title_entry.pack(padx=20, pady=(20, 10), fill="x")

        # Details row (prep time, cook time, servings)
        self.details_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.details_frame.pack(padx=20, pady=5, fill="x")

        self.prep_var = ctk.StringVar()
        self.cook_var = ctk.StringVar()
        self.servings_var = ctk.StringVar()

        ctk.CTkLabel(self.details_frame, text="Prep (mins):").grid(row=0, column=0, padx=5)
        ctk.CTkEntry(self.details_frame, textvariable=self.prep_var, width=70).grid(row=0, column=1, padx=5)

        ctk.CTkLabel(self.details_frame, text="Cook (mins):").grid(row=0, column=2, padx=5)
        ctk.CTkEntry(self.details_frame, textvariable=self.cook_var, width=70).grid(row=0, column=3, padx=5)

        ctk.CTkLabel(self.details_frame, text="Servings:").grid(row=0, column=4, padx=5)
        ctk.CTkEntry(self.details_frame, textvariable=self.servings_var, width=70).grid(row=0, column=5, padx=5)

        # Ingredients
        ctk.CTkLabel(self, text="Ingredients", font=ctk.CTkFont(weight="bold")).pack(padx=20, pady=(10, 0), anchor="w")
        self.ingredients_text = ctk.CTkTextbox(self, height=120)
        self.ingredients_text.pack(padx=20, pady=5, fill="x")

        # Instructions
        ctk.CTkLabel(self, text="Instructions", font=ctk.CTkFont(weight="bold")).pack(padx=20, pady=(10, 0), anchor="w")
        self.instructions_text = ctk.CTkTextbox(self, height=180)
        self.instructions_text.pack(padx=20, pady=5, fill="x")

        # Notes
        ctk.CTkLabel(self, text="Notes", font=ctk.CTkFont(weight="bold")).pack(padx=20, pady=(10, 0), anchor="w")
        self.notes_text = ctk.CTkTextbox(self, height=80)
        self.notes_text.pack(padx=20, pady=5, fill="x")

        # Buttons
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(padx=20, pady=20, fill="x")

        self.save_button = ctk.CTkButton(self.button_frame, text="Save Recipe", command=self.save_recipe)
        self.save_button.pack(side="left", padx=5)

        self.delete_button = ctk.CTkButton(self.button_frame, text="Delete Recipe", fg_color="red", hover_color="darkred", command=self.delete_recipe)
        self.delete_button.pack(side="left", padx=5)

        self.clear_form()

    def load_recipe(self, recipe):
        self.current_recipe = recipe
        self.title_var.set(recipe["title"])
        self.prep_var.set(recipe["prep_time"] or "")
        self.cook_var.set(recipe["cook_time"] or "")
        self.servings_var.set(recipe["servings"] or "")

        self.ingredients_text.delete("1.0", "end")
        self.ingredients_text.insert("1.0", recipe["ingredients"])

        self.instructions_text.delete("1.0", "end")
        self.instructions_text.insert("1.0", recipe["instructions"])

        self.notes_text.delete("1.0", "end")
        self.notes_text.insert("1.0", recipe["notes"] or "")

    def save_recipe(self):
        title = self.title_var.get().strip()
        ingredients = self.ingredients_text.get("1.0", "end").strip()
        instructions = self.instructions_text.get("1.0", "end").strip()
        prep_time = self.prep_var.get().strip()
        cook_time = self.cook_var.get().strip()
        servings = self.servings_var.get().strip()
        notes = self.notes_text.get("1.0", "end").strip()

        if not title or not ingredients or not instructions:
            messagebox.showerror("Missing Fields", "Title, ingredients and instructions are required!")
            return

        prep_time = int(prep_time) if prep_time.isdigit() else None
        cook_time = int(cook_time) if cook_time.isdigit() else None
        servings = int(servings) if servings.isdigit() else None

        if self.current_recipe:
            update_recipe(self.current_recipe["id"], title, ingredients, instructions, prep_time, cook_time, servings, notes)
        else:
            add_recipe(title, ingredients, instructions, prep_time, cook_time, servings, notes)

        self.on_recipe_change()
        self.clear_form()

    def delete_recipe(self):
        if self.current_recipe:
            delete_recipe(self.current_recipe["id"])
            self.on_recipe_change()
            self.clear_form()

    def clear_form(self):
        self.current_recipe = None
        self.title_var.set("")
        self.prep_var.set("")
        self.cook_var.set("")
        self.servings_var.set("")
        self.ingredients_text.delete("1.0", "end")
        self.instructions_text.delete("1.0", "end")
        self.notes_text.delete("1.0", "end")

        