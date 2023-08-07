import os
import json


class Contact_Manager:
    def design_(self):
        print("-"*40)
        print("\n\n\n")
        print("-"*8,"Contact Management System","-"*8)
        print("\n\n","-" * 40)

    def adding_contact(self,name, contact):
        data_set = {name: contact}
        try:
            file = "Contact_Manager.txt"
            if not os.path.exists(file):
                f = open(file, "w")
                f.close()
            with open(file, "a") as f:
                json_data = json.dumps(data_set)
                f.write(json_data + "\n")

            print("\nContact added successfully..")
        except :
            print("Contact could not be added!")

    def search_contact(self,name):
        try:
            file = "Contact_Manager.txt"
            found = False

            if not os.path.exists(file):
                print("File is empty, add some contact details first..!")
            else:
                with open(file, "r") as f:
                    for line in f:
                        data = json.loads(line)
                        if name in data:
                            result = data[name]
                            print("Contact found!")
                            print(f"Name: {name}, Number: {result}")
                            found = True
                            break  # Exit the loop after finding the contact

            if not found:
                print("Contact not found!")

        except :
            print("Something went wrong..!")

    def delete_contact_by_name(self,name):
        try:
            file = "Contact_Manager.txt"
            found = False
            updated_data = []

            if not os.path.exists(file):
                print("File is empty, add some contact details first..!")
            else:
                with open(file, 'r') as f:
                    lines = f.readlines()

                for line in lines:
                    user_data = json.loads(line)
                    if name not in user_data.keys():
                        updated_data.append(user_data)
                    else:
                        print("Contact Deleted Successfully!")
                        found = True


                with open(file, 'w') as f:
                    for data in updated_data:
                        f.write(json.dumps(data) + "\n")
                if not found:
                    print("User Not Found!")

        except :
            print("Something went wrong..!")

    def delete_contact_by_contact(self, contact):
        try:
            file = "Contact_Manager.txt"
            found = False
            updated_data = []

            if not os.path.exists(file):
                print("File is empty, add some contact details first..!")
            else:
                with open(file, 'r') as f:
                    lines = f.readlines()

                for line in lines:
                    user_data = json.loads(line)
                    if contact not in user_data.values():
                        updated_data.append(user_data)
                    else:
                        print("Contact Deleted Successfully!")
                        found = True

                with open(file, 'w') as f:
                    for data in updated_data:
                        f.write(json.dumps(data) + "\n")
                if not found:
                    print("User Not Found!")

        except :
            print("Something went wrong..!")

    def update_contact(self):
        try:
            file = "Contact_Manager.txt"
            total_data = []

            if not os.path.exists(file):
                print("File is empty, add some contact details first..!")
            else:
                choice = input("Choose the Name to update the contact: ")
                new_contact = input("Enter new number: ")
                found = False

                with open(file, 'r') as f:
                    lines = f.readlines()

                for line in lines:
                    user_data = json.loads(line)
                    if choice in user_data.keys():
                        user_data[choice] = new_contact
                        print("Contact Updated Successfully!")
                        found = True
                    total_data.append(user_data)

                if not found:
                    print("User not found!")

                with open(file, 'w') as f:
                    for data in total_data:
                        json_data = json.dumps(data)
                        f.write(json_data + "\n")

        except :
            print("Something went wrong..!")


person = Contact_Manager()
def main_menu():
    while True:
        try:
            person.design_()
            print("1.Add Contact")
            print("2.Search Contact By Name")
            print("3.Delete By Name")
            print("4.Delete By Number")
            print("5.Update")
            print("6.Exit")
            choice = int(input("enter choice: "))
            if choice ==1 :
                os.system("cls")
                person.design_()
                name = input("Enter name: ")
                contact = int(input("Enter contact no: "))
                person.adding_contact(name,contact)
            elif choice ==2 :
                os.system("cls")
                person.design_()
                name = input("Enter name: ")
                person.search_contact(name)
            elif choice ==3:
                os.system("cls")
                person.design_()
                name = input("Enter name: ")
                person.delete_contact_by_name(name)
            elif choice ==4:
                os.system("cls")
                person.design_()
                number = int(input("Enter number: "))
                person.delete_contact_by_contact(number)
            elif choice ==5:
                os.system("cls")
                person.design_()
                person.update_contact()
            elif choice ==6:
                break
        except:
            print("Enter Valid Number!")
main_menu()