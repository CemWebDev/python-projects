def display_menu():
    print("--Notebook Application--")
    print("1-Add new notes")
    print("2-See notes")
    print("3-Delete notes")
    print("4-Exit")
    
    
    
def add_notes(notes_list):
    new_note = input("Write you note here: ")
    notes_list.append(new_note)
    print("New note added successfully!")
    
def view_notes(notes_list):
    if notes_list:
        for index, note in enumerate(notes_list, start=1):
            print(f"{index}-{note}")
    else:
        print("There no any notes, let's add some!")


def main():
    display_menu()
    notes = []
    while True:
        user_choice = input("Please enter an operation from the menu: (1, 2, 3, 4) ")
        if user_choice == "1":
            add_notes(notes)
        elif user_choice == "2":
            print()
        elif user_choice == "3":
            print()
        elif user_choice == "4":
            print("Exit...")
            break
        else:
            print("Invalid operation!") 