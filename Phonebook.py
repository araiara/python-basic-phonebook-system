"""
    This is the assignment for the Python Workshop.
    This assignment is a phonebook system that stores the ID, name, phone number, and email of a person.
    The data structures used are: String, List, and Dictionary
    Functionalities: Add, store, remove, update, and search.
    
    Author: Arsana Rai
    Date: 17th June 2020
"""

from csv import DictReader, DictWriter
from datetime import date

filename = "phonebook_assignment.csv"

def add_item(phonebook, *, person_id, name, number, email): 
    bookitem = {"person_id": "", "fullname": "", "number": "", "email": ""} 
    bookitem["person_id"] = person_id
    bookitem["fullname"] = name
    bookitem["number"] = number
    bookitem["email"] = email
    phonebook.append(bookitem)

def list_items(phonebook):
    """
        This function lists the items stored in the list.
    """
    print("\nID\t Full Name\t Phone Number\t Email\n", "=" * 50, end="\n")
    for item in phonebook:
        print("{}\t {}\t {}\t {}".format(
            item["person_id"], item["fullname"], item["number"], item["email"]
        ))
    print("=" * 51)

def search_item(phonebook, keyword):
    """
        This function performs search based on person name.
    """
    for index, item in enumerate(phonebook):
        if keyword in item["fullname"]:
            print("DATA FOUND: {}/{}/{}/{} \nIndex: {}".format(
                item["person_id"], item["fullname"], item["number"], item["email"], index
            ))

def is_duplicate(phonebook, person_id, number, email):
    """
        This function returns True if ID, Phone number, and Email are repetitive.
        It also validates the repetitive fields.
    """
    value = ""
    for item in phonebook:
        if item["person_id"] == person_id or item["number"] == number or item["email"] == email:
            if item["person_id"] == person_id:
                value += "\n- ID"
            if item["number"] == number:
                value += "\n- Phone number"
            if item["email"] == email:
                value += "\n- Email"
            print("\n== Please enter again. ==\nThe value must be unique in: {}".format(value))
            return True

def remove_item(phonebook, item_id):
    """
        This function removes an entry based on ID.
    """
    for index, item in enumerate(phonebook):
        if item["person_id"] == item_id:
            phonebook.pop(index)
    print("\n== Successfully removed the entry. ==")

def update_item(phonebook, item_id):
    """
        This function updates an entry based on ID.
    """
    update_name = input("Please enter the new name: ")
    update_number = input("Please enter the new phone number: ")
    update_email = input("Please enter the new email: ")
    target = None
    for index, item in enumerate(phonebook):
        if item["person_id"] == item_id:
            target = index
    target_item = phonebook[target]
    phonebook.pop(target)
    target_item.update({"fullname": update_name, "number": update_number, "email": update_email})
    phonebook.insert(target, target_item)
    print("\n== Successfully updates entries ==")


def add_action(phonebook):
    """
        This function takes input from the user.
        It also validates all the empty fields.
    """
    while True:
        person_id = input("\nEnter ID: ")
        fullname = input("Enter your name: ")
        number = input("Enter your phone number: ")
        email = input("Enter your email address: ")

        if (person_id.strip() and fullname.strip() and number.strip() and email.strip()):

            """ to check the uniqueness of the ID, Email, and Phone number """
            duplicate = is_duplicate(phonebook, person_id, number, email) 
            if not duplicate:
                add_item(phonebook, person_id=person_id, name=fullname, email=email, number=number)
                char = input("\nDo you want to continue? [y/yes]: ")
                if not (char.lower() == "y" or char.lower() == "yes"):
                    break
            else:
                continue
        else:
            value = ""
            if not person_id:
                value += "\n- ID"
            if not fullname:
                value += "\n- Name"
            if not number:
                value += "\n- Phone number"
            if not email:
                value += "\n- Email"
            print("\n== Please enter again. ==\nEmpty values detected in: {}".format(value))
    
def write_to_csv(phonebook, filename):
    """
        This function appends the entries to the csv file.
    """
    with open(filename, "w+") as csvFile:
        writer = DictWriter(csvFile, fieldnames=["person_id", "fullname", "number", "email"])
        writer.writeheader()
        for each in phonebook:
            writer.writerow(each)

def cli():
    global filename
    phonebook = []

    try:
        with open(filename, "r") as csvFile:
            #keyword/named argument
            reader = DictReader(csvFile, fieldnames=["person_id", "fullname", "number", "email"])
            next(reader)
            phonebook.extend(reader)
    except:
        csvFile = open(filename, "w")
            
    print("\t=== WELCOME TO THE PHONEBOOK SYSTEM ===")
    print("\tDate:", date.today())
    while True:
        print("""
            ====Please select an ACTION ====
            A: Add
            L: List
            S: Search
            R: Remove
            U: Update
            E: Exit
        """)
        action = input("Enter your choice here: ")
        if action.upper() == "A":
            #add action
            add_action(phonebook)
        elif action.upper() == "L":
            #list action
            list_items(phonebook)
        elif action.upper() == "S":
            #search action
            keyword = input("Enter a keyword to search: ")
            search_item(phonebook, keyword)
        elif action.upper() == "R":
            #remove action
            item_id = input("Enter the ID to remove: ")
            remove_item(phonebook, item_id)
        elif action.upper() == "U":
            #update action
            item_id = input("Enter the ID to update: ")
            update_item(phonebook, item_id)
        elif action.upper() == "E":
            write_to_csv(phonebook, filename)
            csvFile.close()
            break
        else:
            print("Invalid action selected.")

if __name__ == "__main__":
    cli()
        
