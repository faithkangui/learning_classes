class Student:
  def __init__(self, name):
    print(">> init" + name)
    self.name = name

  def set_name(self, name):
    self.name = name
  
  def get_name(self):
    print("my name is " + self.name)
    return self.name

faith = Student("Faith")
faith.set_name("shiku")
dio = Student("Diana")

print ("first instance name is " + faith.get_name())
print ("second instance name is " + dio.get_name())

# 
