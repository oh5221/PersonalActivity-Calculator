import tkinter as tk

class CalculatorGUI:
    def __init__(self, window, calculator_functions):
        self.window = window
        self.calculator_functions = calculator_functions

        self.str1 = tk.StringVar()
        self.str1.set(str(self.calculator_functions.disValue))

        self.dis = tk.Entry(self.window, textvariable=self.str1, font='Pretendard 18', justify='right', width=19)
        self.dis.grid(column=0, row=0, columnspan=4, ipadx=23, ipady=30)

        btn_list = [['7', '8', '9', 'C'],
                    ['4', '5', '6', '*'],
                    ['1', '2', '3', '-'],
                    ['0', '/', '+', '='],
                    ['d']
                    ]

        for i, btns in enumerate(btn_list):
            for j, btn in enumerate(btns):
                bt = tk.Button(self.window, text=btn,
                               font='Pretendard 10',
                               width=10, height=5,
                               command=lambda cmd=btn: self.btn_click(cmd)
                               )
                bt.grid(column=j, row=(i + 1))

        self.window.bind('<Key>', self.keyboard_input)

    def btn_click(self, value):
        try:
            value = int(value)
            self.calculator_functions.number_click(value)
        except ValueError:
            self.calculator_functions.operator_click(value)

        self.str1.set(str(self.calculator_functions.disValue))

    def keyboard_input(self, key):
        self.calculator_functions.keyboard_input(key)
        self.str1.set(str(self.calculator_functions.disValue))
