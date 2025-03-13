# Simple Text Editor 

A basic **Text Editor** built using Python's `tkinter` library. This lightweight editor allows users to create, open, and save text files conveniently.  

📁 This project is part of the [Mini-Python-Projects](https://github.com/mudasirmurtaza/Mini-Python-Projects) repository and is located in the **Text Editor** folder.  

## Overview  

This **Text Editor** provides essential functionalities such as:  
Creating a **new file** (clears the current text).  
**Opening** an existing `.txt` file.  
**Saving** the file after making edits.  
A simple **menu bar** with file options.  

##  Features  

- **New File**: Clears the text area for fresh content.  
- **Open File**: Loads text from an existing file.  
- **Save File**: Saves the content to a `.txt` file.  
- **User-Friendly Interface**: Minimalistic design with a menu bar.  
- **Resizable Window**: The editor expands dynamically.  
- **Text Formatting**: Uses `Calibri` font with **word wrapping** enabled.  

## How to Run  

### 🔹 Prerequisites  
- Python **3.x** (Make sure Python is installed on your system)  

### 🔹 Steps  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/mudasirmurtaza/Mini-Python-Projects.git
   ```
2. **Navigate to the Text Editor directory**  
   ```bash
   cd Mini-Python-Projects/Text Editor
   ```
3. **Run the script**  
   ```bash
   python text_editor.py
   ```
4. The **Text Editor** window will open, allowing you to create and edit files!  

## Code Highlights  

- Uses **`tkinter.Text`** to create a text area for editing.  
- **Menu Bar** with `File` options (`New`, `Open`, `Save As`, `Exit`).  
- **`filedialog.askopenfilename()`** and **`filedialog.asksaveasfilename()`** for file handling.  
- **`messagebox.showinfo()`** to confirm file-saving actions.  

## Contributing  

Feel free to contribute by suggesting improvements, reporting issues, or submitting a pull request!  

