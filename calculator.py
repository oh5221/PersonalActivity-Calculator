class CalculatorFunctions:
    def __init__(self):
        self.disValue = 0
        self.operator = {'+': 1, '-': 2, '/': 3, '*': 4, 'C': 5, '=': 6, 'd': 7}
        self.stoValue = 0
        self.opPre = 0

    def number_click(self, value):
        self.disValue = (self.disValue * 10) + value
        return self.disValue

    def clear(self):
        self.stoValue = 0
        self.opPre = 0
        self.disValue = 0
        return self.disValue

    def keyboard_input(self, key):
        op = self.operator.get(key.char, None)
        numbers = '1234567890'

        if key.char in numbers:
            self.number_click(int(key.char))
        elif op is not None:
            self.operator_click(key.char)
        elif key.keysym == "Return":
            self.operator_click('=')
        elif key.keysym == "Escape":
            self.clear()
        elif key.keysym == "BackSpace":
            self.disValue //= 10
        return self.disValue

    def operator_click(self, value):
        op = self.operator[value]

        if op == 5:
            self.clear()
        elif self.disValue == 0:
            self.opPre = 0
        elif self.opPre == 0:
            self.opPre = op
            self.stoValue = self.disValue
            self.disValue = 0
        elif op == 6:
            self.calculate_result()
        elif op == 7:
            self.disValue = self.disValue // 10
        else:
            self.clear()

    def calculate_result(self):
        if self.opPre == 1:
            self.disValue = self.stoValue + self.disValue
        elif self.opPre == 2:
            self.disValue = self.stoValue - self.disValue
        elif self.opPre == 3:
            self.disValue = self.stoValue / self.disValue
        elif self.opPre == 4:
            self.disValue = self.stoValue * self.disValue

        self.stoValue = 0
        self.opPre = 0
