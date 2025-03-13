import tkinter as tk
from tkinter import filedialog, messagebox

#This function will make sure to clear the text when user wants to create a new file.
#Using Del() method of text widget
def new_file():
    text.delete(1.0, tk.END)
    
#This function will allow user to open existing text files.
def open_file():
    file_path = filedialog.askopenfilename(defaultextension='txt', filetypes=[("Text Files", '*.txt')])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

#This function will allow users to save the files.
def save_file():
    file_path = filedialog.askopenfilename(defaultextension= ".txt", filetypes=[("Text Files", '*.txt')])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo("Info", "File saves sucessfully!")
            
root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#This will make text appear with in editor.
text = tk.Text(root, wrap=tk.WORD, font=("Calibri",12), fg = "black")
text.pack(expand=tk.YES, fill=tk.BOTH)

##Main Loop= Method of tkinter module which puts window loop and wait for user input.
root.mainloop()


