import tkinter as tk
import random

# List of Thai consonants and their names
thai_consonants = {
    "ก": "gor kai", "ข": "kho khai", "ฃ": "kho khuat", "ค": "kho khwai", "ฅ": "kho khon",
    "ฆ": "kho rang", "ง": "ngo ngu", "จ": "cho chan", "ฉ": "cho ching", "ช": "cho chang",
    "ซ": "so so", "ฌ": "cho cho", "ญ": "yo ying", "ฎ": "do chada", "ฏ": "to patak",
    "ฐ": "tho than", "ฑ": "tho montho", "ฒ": "tho phuthao", "ณ": "no nen", "ด": "do dek",
    "ต": "to tao", "ถ": "tho thung", "ท": "tho thahan", "ธ": "tho thong", "น": "no nu",
    "บ": "bo baimai", "ป": "po pla", "ผ": "pho phung", "ฝ": "fo fa", "พ": "pho phan",
    "ฟ": "fo fan", "ภ": "pho samphao", "ม": "mo ma", "ย": "yo yak", "ร": "ro ruea",
    "ล": "lo ling", "ว": "wo waen", "ศ": "so sala", "ษ": "so ruea", "ส": "so sua", "ห": "ho hip",
    "ฬ": "lo chu-la", "อ": "o ang", "ฮ": "ho nok-huk"
}

class ThaiConsonantFlashcards:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcard Game")
        
        # Create a label to display the consonant
        self.label = tk.Label(root, font=("Arial", 50), width=4, height=2)
        self.label.pack(pady=20)
        
        # Button to show random consonant
        self.show_button = tk.Button(root, text="Show Consonant", font=("Arial", 20), command=self.show_consonant)
        self.show_button.pack(pady=10)
        
        # Button to show consonant name
        self.name_button = tk.Button(root, text="Show Name", font=("Arial", 20), command=self.show_name)
        self.name_button.pack(pady=10)
        
        # Label to show the name (initially hidden)
        self.name_label = tk.Label(root, font=("Arial", 30), width=12, height=2)
        self.name_label.pack(pady=20)
        self.name_label.pack_forget()

        # Store the current consonant
        self.current_consonant = None

    def show_consonant(self):
        """Display a random consonant from the list."""
        self.name_label.pack_forget()  # Hide the name label
        self.current_consonant = random.choice(list(thai_consonants.keys()))
        self.label.config(text=self.current_consonant)

    def show_name(self):
        """Display the name of the consonant."""
        name = thai_consonants[self.current_consonant]
        self.name_label.config(text=name)
        self.name_label.pack()

if __name__ == "__main__":
    # Create the main window (root)
    root = tk.Tk()

    # Create the flashcard game
    game = ThaiConsonantFlashcards(root)

    # Run the GUI loop
    root.mainloop()
#pointless change to make a commit
