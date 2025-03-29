# User Sign-Up Validation  

A simple **Python validation system** for user sign-up, ensuring names and email addresses follow standard formats.  

📁 This project is part of the [Mini-Python-Projects](https://github.com/mudasirmurtaza/Mini-Python-Projects) repository and is located in the **User Validation** folder.  

## Overview  

This **User Validation** system checks:  
If a user's **name** is valid (at least 3 characters long).  
If an **email** contains `@` and ends with a **valid domain**.  

##  Features  

- **Name Validation**: Ensures the name is a string and at least **3 characters** long.  
- **Email Validation**:  
  - Must contain `@`.  
  - Must end with a **valid top-level domain** (`.com`, `.net`, `.org`, etc.).  
- **Lightweight & Efficient**: Uses simple Python functions for quick validation.  

##  How to Run  

### 🔹 Prerequisites  
- Python **3.x** installed.  

### 🔹 Steps  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/mudasirmurtaza/Mini-Python-Projects.git
   ```
2. **Navigate to the User Validation directory**  
   ```bash
   cd Mini-Python-Projects/User Validation
   ```
3. **Run the Python script**  
   ```python
   from validation import validate_name, validate_email

   print(validate_name("Mudasir"))  # True
   print(validate_email("mudasir@gmail.com"))  # True
   print(validate_email("mudasir@gmail"))  # False
   ```
4. The script will return **True** for valid inputs and **False** for invalid ones.  

## Code Highlights  

- **`validate_name(name)`**:  
  - Checks if the name is a **string**.  
  - Ensures the name has **more than 2 characters**.  

- **`validate_email(email)`**:  
  - Checks for the presence of **"@"**.  
  - Ensures the email ends with a **valid top-level domain**.  

## Contributing  

Feel free to contribute by adding more validation features or improving the code!  


