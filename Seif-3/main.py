from animals_model import Animal, Dog, Cat

# יצירת רשימה של חיות
animals = [Dog(), Cat()]

# לולאה לעבור על הרשימה
for animal in animals:
    # בדיקה אם האובייקט הוא מסוג Animal
    if isinstance(animal, Animal):
        print(animal.speak())