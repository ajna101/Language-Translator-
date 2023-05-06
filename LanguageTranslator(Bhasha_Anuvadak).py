from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator
from ttkthemes import ThemedStyle

def translate_text():
    source_text = text_input.get("1.0", END).strip()
    target_lang = combo_language.get()

    if not source_text:
        messagebox.showerror("Error", "Please enter the text to translate.")
        return

    if not target_lang:
        messagebox.showerror("Error", "Please select the target language.")
        return

    translator = Translator()
    try:
        translation = translator.translate(source_text, dest=target_lang)
        translated_text = translation.text
        text_output.delete("1.0", END)
        text_output.insert(END, translated_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# the main window
window = Tk()
window.title("Language Translator")
window.geometry("400x300")

#themed style to the window
style = ThemedStyle(window)
style.set_theme("arc")

#the input text area
label_input = Label(window, text="Enter the text to translate:")
label_input.pack(pady=10)
text_input = Text(window, height=5)
text_input.pack()

#language selection combobox
label_language = Label(window, text="Select the target language:")
label_language.pack(pady=10)
combo_language = ttk.Combobox(window, state="readonly")
combo_language["values"] = ("English", "Spanish", "French", "German", "Hindi", "Italian", "Japanese")
combo_language.pack()

#translate button
btn_translate = ttk.Button(window, text="Translate", command=translate_text)
btn_translate.pack(pady=10)

#output text area
label_output = Label(window, text="Translated text:")
label_output.pack(pady=10)
text_output = Text(window, height=5)
text_output.pack()

# For watermark
watermark_label = Label(window, text="Created by Kunal", anchor="se", foreground="gray")
watermark_label.pack(side="bottom", padx=10, pady=10)

# Start the GUI main loop
window.mainloop()
