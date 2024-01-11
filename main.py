import tkinter as tk
from gui import CalculatorGUI
from calculator import CalculatorFunctions

if __name__ == "__main__":
    CalWindow = tk.Tk()
    CalWindow.title('Calculator')

    calculator_functions = CalculatorFunctions()
    calculator_gui = CalculatorGUI(CalWindow, calculator_functions)

    CalWindow.mainloop()
