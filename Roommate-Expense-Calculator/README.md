# Roommate Expense Calculator


Welcome to the Roommate Expense Calculator repository! 🏠💡

## Overview

This Python program helps roommates in a hostel room calculate their individual shares of specific expenses. By inputting the rent amount, Internet bill, water bill, gas bill, online food delivery bill, and the number of people living in the room, the program computes the amount each person should contribute.

## How It Works

1. **Input Variables:**
   - `Rent`: The total monthly rent for the room.
   - `Food_Delivery_Bill`: The total spent on online food delivery.
   - `Electricity_Bill`: The electricity bill amount.
   - `Water_Bill`: The water bill amount.
   - `Gas_Bill`: The gas bill amount.
   - `Internet_Bill`: The cost of the Internet service.
   - `Number_of_Roommates`: The number of people sharing the room.

2. **Calculation:**
   - The program adds up the five expenses: 
    `Rent + Food_Delivery_Bill + Electricity_Bill + Water_Bill+Gas_Bill + Internet_Bill `.
   - It then divides the total expenses by the number of roommates: `Share_per_person = Total_Expense / Number_of_Roommates`.

3. **Output:**
   - The program displays the calculated share per person.

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/mudasirmurtaza/roommate-expense-calculator.git
   cd roommate-expense-calculator
   ```

2. Run the Python script:

   ```bash
   python expense_calculator.py
   ```

3. Follow the prompts to input the expense details.

## Example

Suppose:
- Rent amount: $1000
- Internet bill: $50
- Water bill: $30
- Gas bill: $40
- Food delivery bill: $80
- Number of roommates: 3

The calculated share per person would be: $(1000 + 50 + 30 + 40 + 80) / 3 = $400.

## Contributing

Contributions are welcome! If you have any improvements or additional features, feel free to submit a pull request.


Happy expense sharing! 🤝💸

---
