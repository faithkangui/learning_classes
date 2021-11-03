class Dog:
  species='canis familiaris'
  def __init__(self, name, age):
    self.name = name
    self.age = age
#instance method
  def __str__(self):
    return f"{self.name} is {self.age} old"

  def speak(self, sound):
    return f"{self.name} barks: {sound}"

simba = Dog("Simba", 6)
print(simba.__str__())
print(type(simba))
#child class inheritance
class JackRussellTerrier(Dog):
  pass
class Dachshund(Dog):
  pass
class Bulldog(Dog):
  pass
#extend the functionality of a parent(override)
class JackRussellTerrier(Dog):
  def speak(self, sound = "Arf"):
    return f"{self.name} says {sound}"

  
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9) 
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim",5)
print(miles.__str__())
print(type(jack))
print(isinstance(miles,JackRussellTerrier))
print(jim.speak("Arf"))
print(jack.speak("Woof"))
print(miles.speak("Grr"))
print(buddy.speak("yap"))