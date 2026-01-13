from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == '1':
                name, address, phone = self.view.get_person_details()
                self.model.add(name, address, phone)
            elif choice == '2':
                people = self.model.get_all_people()
                self.view.show_people_list(people)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")