class View:
    def get_person_details(self):
        name = input("Enter name: ")
        address = input("Enter address: ")
        phone = input("Enter phone: ")
        return name, address, phone

    def show_people_list(self, people_list):
        if not people_list:
            print("No people in the list.")
        else:
            print("People List:")
            for person in people_list:
                print(f"Name: {person.name}, Address: {person.address}, Phone: {person.phone}")

    def show_menu(self):
        print("\nMenu:")
        print("1. Add Person")
        print("2. Show All")
        print("3. Exit")
        choice = input("Choose an option: ")
        return choice