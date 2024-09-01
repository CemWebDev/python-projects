def display_menu():
    print("--Notebook Application--")
    print("1- Add new notes")
    print("2- See notes")
    print("3- Delete notes")
    print("4- Exit")


def add_notes(notes_list):
    new_note = input("Write your note here: ")
    notes_list.append(new_note)
    print("New note added successfully!")


def view_notes(notes_list):
    if notes_list:
        for index, note in enumerate(notes_list, start=1):
            print(f"{index}- {note}")
    else:
        print("There are no notes. Let's add some!")


def delete_notes(notes_list):
    if notes_list:
        try:
            view_notes(notes_list)
            deleting_index = int(input("Which note do you want to delete? (Enter the note number): ")) - 1
            if 0 <= deleting_index < len(notes_list):
                while True:
                    confirm = input("Are you sure you want to delete this note? (yes/no): ").lower()
                    if confirm == 'yes':
                        removed_note = notes_list.pop(deleting_index)
                        print(f"'{removed_note}' has been deleted.")
                        break
                    elif confirm == 'no':
                        print("Deletion canceled!")
                        break
                    else:
                        print("Please enter 'yes' or 'no'.")
        except ValueError:
            print("Invalid note number!")
    else:
        print("There are no notes. Let's add some!")


def main():
    notes = []
    while True:
        display_menu()
        user_choice = input("Please enter an operation from the menu: (1, 2, 3, 4) ")
        if user_choice == "1":
            add_notes(notes)
        elif user_choice == "2":
            view_notes(notes)
        elif user_choice == "3":
            delete_notes(notes)
        elif user_choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid operation!")


main()
