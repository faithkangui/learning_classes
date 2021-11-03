class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

simba = Dog("simba", "2")
print(simba.description())
print(simba.speak("woof woof"))
simba.species = "felis silviris"
print(simba.species)

tusker = Dog("tusker", "7")
print(tusker.description())
print(tusker.speak("woof woof"))
print(tusker.age)
print(tusker.name)
print(tusker.species)

lex = Dog("lex", "3")
print(lex.description())
print(lex.speak("woof woof"))

tequila = Dog("tequila", "9")
print(tequila.description())
print(tequila.speak("bow bow"))

scobby = Dog("scobby", "8")
print(scobby.description())
print(scobby.speak("bow bow"))

kiki = Dog("kiki", "4")
print(kiki.description())
print(kiki.speak("woof woof"))