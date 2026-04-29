"""
Recipe Detail Panel
The right side panel of the app. Displays a form for viewing, adding,
editing and deleting recipes. Communicates with the app through the
service layer rather than the database directly.
"""

import customtkinter as ctk
from tkinter import messagebox
from services.recipe_service import save_recipe, delete_recipe


class RecipeDetail(ctk.CTkFrame):
    """
    A panel that displays a form for viewing and editing a single recipe.
    Communicates with the rest of the app through callback functions passed
    in from app.py, and with the database through the service layer.
    """

    def __init__(self, parent, on_recipe_change):
        """
        Initialize the recipe detail panel.

        Args:
            parent: The parent window this panel belongs to
            on_recipe_change: Function to call when a recipe is saved or deleted
        """
        super().__init__(parent)

        self.on_recipe_change = on_recipe_change
        self.current_recipe = None

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

        self.save_button = ctk.CTkButton(
            self.button_frame,
            text="Save Recipe",
            command=self.handle_save
        )
        self.save_button.pack(side="left", padx=5)

        self.delete_button = ctk.CTkButton(
            self.button_frame,
            text="Delete Recipe",
            fg_color="red",
            hover_color="darkred",
            command=self.handle_delete
        )
        self.delete_button.pack(side="left", padx=5)

        self.clear_form()

    def load_recipe(self, recipe):
        """
        Populates the form fields with data from a Recipe object.

        Args:
            recipe: A Recipe object to display
        """
        self.current_recipe = recipe
        self.title_var.set(recipe.title)
        self.prep_var.set(recipe.prep_time or "")
        self.cook_var.set(recipe.cook_time or "")
        self.servings_var.set(recipe.servings or "")

        self.ingredients_text.delete("1.0", "end")
        self.ingredients_text.insert("1.0", recipe.ingredients)

        self.instructions_text.delete("1.0", "end")
        self.instructions_text.insert("1.0", recipe.instructions)

        self.notes_text.delete("1.0", "end")
        self.notes_text.insert("1.0", recipe.notes or "")

    def handle_save(self):
        """
        Collects form data and passes it to the service layer to save.
        Displays a success or error message based on the result.
        """
        title = self.title_var.get().strip()
        ingredients = self.ingredients_text.get("1.0", "end").strip()
        instructions = self.instructions_text.get("1.0", "end").strip()
        prep_time = self.prep_var.get().strip()
        cook_time = self.cook_var.get().strip()
        servings = self.servings_var.get().strip()
        notes = self.notes_text.get("1.0", "end").strip()

        recipe_id = self.current_recipe.id if self.current_recipe else None

        success, error = save_recipe(
            recipe_id, title, ingredients, instructions,
            prep_time, cook_time, servings, notes
        )

        if not success:
            messagebox.showerror("Missing Fields", error)
            return

        messagebox.showinfo("Success", "Recipe saved successfully!")
        self.on_recipe_change()
        self.clear_form()

    def handle_delete(self):
        """
        Asks for confirmation then deletes the current recipe if confirmed.
        """
        if not self.current_recipe:
            return

        confirmed = messagebox.askyesno(
            "Delete Recipe",
            f"Are you sure you want to delete '{self.current_recipe.title}'?"
        )

        if confirmed:
            delete_recipe(self.current_recipe.id)
            self.on_recipe_change()
            self.clear_form()

    def clear_form(self):
        """Resets all form fields back to empty."""
        self.current_recipe = None
        self.title_var.set("")
        self.prep_var.set("")
        self.cook_var.set("")
        self.servings_var.set("")
        self.ingredients_text.delete("1.0", "end")
        self.instructions_text.delete("1.0", "end")
        self.notes_text.delete("1.0", "end")