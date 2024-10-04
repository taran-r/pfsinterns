import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Translator")
        self.root.geometry("600x600")

        self.translator = Translator()

        self.input_label = tk.Label(root, text="Enter Text:")
        self.input_label.pack(pady=10)

        self.input_text = tk.Text(root, height=10, width=40)
        self.input_text.pack(pady=10)

        self.language_label = tk.Label(root, text="Select Language to Translate into:")
        self.language_label.pack(pady=10)

        self.target_lang = ttk.Combobox(root, values=[name.capitalize() for name in LANGUAGES.values()])
        self.target_lang.pack(pady=10)
        self.target_lang.set("English")

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.pack(pady=10)

        self.output_label = tk.Label(root, text="Translated Text:")
        self.output_label.pack(pady=10)

        self.output_text = tk.Text(root, height=10, width=40)
        self.output_text.pack(pady=10)

    def translate_text(self):
        source_text = self.input_text.get("1.0", tk.END).strip()
        target_language = self.get_language_code(self.target_lang.get())
        
        if source_text and target_language:
            try:
                result = self.translator.translate(source_text, dest=target_language)
                self.output_text.delete("1.0", tk.END)  
                self.output_text.insert(tk.END, result.text)  
            except Exception as e:
                messagebox.showerror("Translation Error", f"An error occurred: {e}")

    def get_language_code(self, lang_name):
        """Get the language code from the language name."""
        for code, name in LANGUAGES.items():
            if name.lower() == lang_name.lower():
                return code
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()