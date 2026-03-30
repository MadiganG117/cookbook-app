# Entry point for the cookbook app 

import sys
from pathlib import Path

# Add the project root to the path so imports work correctly
sys.path.insert(0, str(Path(__file__).parent))

from ui.app import CookbookApp

def main():
    app = CookbookApp()
    app.run()

if __name__ == "__main__":
    main()