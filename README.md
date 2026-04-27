# My Cookbook App

A desktop cookbook application built with Python that lets you store, organize, and search your personal recipe collection. This project was built to explore AI-assisted development and demonstrate real-world Python skills including database management and desktop UI design. Planned features include recipe categorization, web recipe importing, and an AI chatbot assistant.

---

## Features
- Add, edit and delete recipes
- Store recipe title, ingredients, instructions, prep time, cook time, servings and personal notes
- Search recipes by name in real time
- All recipes saved permanently to a local database

---

## Tech Stack
- **Python** — core programming language
- **CustomTkinter** — modern desktop UI library
- **SQLite** — lightweight local database for storing recipes
- **Git/GitHub** — version control and project hosting

---

## Installation & Setup

1. Clone the repository
2. Navigate into the project folder
cd cookbook-app
3. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Run the app
 python main.py

 ---

## Project Structure

cookbook-app/
├── main.py              # Entry point, launches the app
├── database.py          # All database logic (add, read, update, delete recipes)
├── models/
│   └── recipe.py        # Recipe class blueprint
├── ui/
│   ├── app.py           # Main window, connects all panels together
│   ├── recipe_list.py   # Left panel, recipe list and search bar
│   └── recipe_detail.py # Right panel, recipe form and detail view
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation

---

## Future Improvements
- Recipe categorization and filtering by category
- Import recipes directly from websites via URL
- AI chatbot assistant for recipe suggestions and cooking questions
- UI improvements and custom theming
- Recipe photo support
- Custom app logo and executable so the app can be launched by clicking an icon like a normal desktop app