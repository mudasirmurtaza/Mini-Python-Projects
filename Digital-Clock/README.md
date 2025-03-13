# Digital Clock 

A simple **Digital Clock** built using Python's `tkinter` library. This project displays the current time and date dynamically and updates every second.  

📁 This project is part of the [Mini-Python-Projects](https://github.com/mudasirmurtaza/Mini-Python-Projects) repository and is located in the **Digital Clock** folder.  

##  Overview  

This **Digital Clock** application:  
Displays the current time in **HH:MM:SS AM/PM** format.  
Shows the **current date** in **DD/MM/YYYY** format.  
Updates automatically **every second**.  
Uses a **GUI** for a visually appealing clock display.  

##  Features  

- **Live Time Update**: Refreshes every second to show the current time accurately.  
- **Date Display**: Displays the **current date** below the time.  
- **Custom Styling**: Uses a **pink background** with a bold **Calibri font** for aesthetics.  
- **Lightweight**: Built using only Python’s standard libraries (`tkinter` and `time`).  

## How to Run  

### 🔹 Prerequisites  
- Python **3.x** (Make sure Python is installed on your system)  

### 🔹 Steps  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/mudasirmurtaza/Mini-Python-Projects.git
   ```
2. **Navigate to the Digital Clock directory**  
   ```bash
   cd Mini-Python-Projects/Digital Clock
   ```
3. **Run the script**  
   ```bash
   python digital_clock.py
   ```
4. The **Digital Clock** window will appear, displaying the current time and date!  

## Code Highlights  

- Uses the **`strftime()`** function from the `time` module to format the date and time.  
- The **`after(1000, time)`** method updates the clock **every second**.  
- **`tk.Label()`** is used to display the clock with **custom styling**.  
- Uses **`tkinter`**'s **`mainloop()`** to keep the GUI running.  

## Contributing  

Feel free to contribute by suggesting improvements, reporting issues, or submitting a pull request!  

