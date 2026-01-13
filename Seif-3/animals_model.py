from abc import ABC, abstractmethod

# מחלקה מופשטת בסיסית
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# מחלקה קונקרטית: כלב
class Dog(Animal):
    def speak(self):
        return "Woof!"

# מחלקה קונקרטית: חתול
class Cat(Animal):
    def speak(self):
        return "Meow!"