import tkinter as tk
from google.cloud import translate_v2 as translate

# Initialize the translation client (after setting up Google API key)
client = translate.Client()

def translate_text():
    source_text = input_text.get("1.0", tk.END).strip()
    target_language = target_lang.get()
    
    if source_text and target_language:
        result = client.translate(source_text, target_language=target_language)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result['translatedText'])

# GUI setup
root = tk.Tk()
root.title("Language Translator")

input_text = tk.Text(root, height=10, width=50)
input_text.pack()

target_lang = tk.StringVar(root)
target_lang.set("es")  # default to Spanish
languages = {"Spanish": "es", "French": "fr", "German": "de"}
target_menu = tk.OptionMenu(root, target_lang, *languages.values())
target_menu.pack()

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

output_text = tk.Text(root, height=10, width=50)
output_text.pack()

root.mainloop()

