class Parrot:
   species = "bird"
   def __init__(self, name, age):
      self.name = name
      self.age = age

   #instance method
   def description(self):
      return f"{self.name} is {self.age} years old"

   #another instance method
   def speak(self, sound):
      return f"{self.name} says {sound}"

coco = Parrot("coco", "4")
print(coco.description())
print(coco.speak("yoh"))