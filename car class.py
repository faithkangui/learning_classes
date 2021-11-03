class Car:

  def __init__(self, color, miles):
    self.color = color
    self.miles = miles

  def __str__(self):
    return f"The {self.color} car has {self.miles} miles."

blue = Car("blue", "20,000")
red = Car("red", "30,000")

print(blue.__str__())
print(red.__str__())

