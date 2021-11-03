class Dog:
  def __init__(self, name,age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name} is {self.age} old."
  def speak(self,sound):
    return f"{self.name} says {sound}"

class GoldRetriver(Dog):
  def speak(self,sound = "Bark"):
    return super.speak(sound)