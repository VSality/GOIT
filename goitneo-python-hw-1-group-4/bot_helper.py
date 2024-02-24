

def parse_input(user_input:str):

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args:list, contacts:dict):

    name, phone = args
    contacts[name] = phone
    return "Contact added."

def chnge_contact(args:list, contacts:dict):

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Warning: Contact not found!"
    
def phone(args:list, contacts:dict):

    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Warning: Contact not found!"
    
def all(contacts:dict):

    if len(contacts) > 0:
        text_res = ""
        for name, phone in contacts.items():
            text_res += f"{name}: {phone}\n"

        return text_res
    else:
        return "Warning: Contacts list is empty!"
    

def main():

    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(chnge_contact(args, contacts))

        elif command == "phone":
            print(phone(args, contacts))

        elif command == "all":
            print(all(contacts))
        else:
            print("Error: Invalid command.")

if __name__ == "__main__":
    main()