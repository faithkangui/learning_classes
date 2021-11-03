class CalculatorApp:
  def __init__(self, number1, number2):
    self.number1 = number1
    self.number2 = number2

  def add(self):
    return self.number1 + self.number2
  def subtract(self):
    return self.number1 - self.number2
  def divide(self):
    return self.number1 / self.number2

  def multiply(self):
    return self.number1 * self.number2

calculate = CalculatorApp(3, 4)
result = calculate.add()
print(result)

calculate = CalculatorApp(9, 4)
result = calculate.subtract()
print(result)

calculate = CalculatorApp(8, 4)
result = calculate.divide()
print(result)

calculate = CalculatorApp(3, 4)
result = calculate.multiply()
print(result)