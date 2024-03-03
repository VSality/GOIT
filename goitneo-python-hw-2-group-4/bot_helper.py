
class NotFoundError(Exception):
    pass

class ContactsEmptyError(Exception):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Such name is not found."
        except IndexError:
            return "Such name is not found."
        except NotFoundError:
            return "Contact not found."
        except ContactsEmptyError:
            return "Contacts is empty. Add some Contacts"

    return inner


def parse_input(user_input:str):
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args:list, contacts:dict) -> str:
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def chnge_contact(args:list, contacts:dict) -> str:
    
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return NotFoundError
   
@input_error 
def phone(args:list, contacts:dict) -> str:

    name = args[0]
    return contacts[name]
        
@input_error   
def all(contacts:dict) -> str:

    if len(contacts) > 0:
        text_res = ""
        for name, phone in contacts.items():
            text_res += f"{name}: {phone}\n"

        return text_res
    else:
        raise ContactsEmptyError
    

def main():

    contacts = dict()
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