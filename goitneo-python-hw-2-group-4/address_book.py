from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)
    
class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        
        if self.is_valide(value):
            raise ValueError("Number is not valide format")
        
    def is_valide(self, num:str) -> bool:
        if not len(num) == 10:
            return True
        else:
            return False

class Record:
    def __init__(self, name:str, birthday:Birthday = None):
        self.name = Name(name)
        self.birthday = birthday
        self.phones = []
        
    def add_birthday(self, birthday:Birthday):
        self.birthday = birthday
    
    def add_phone(self, num:str):
        if not num in self.phones:
            new_num = Phone(num)
            if new_num != None:
                self.phones.append(new_num)
    
    def edit_phone(self, old_num:str, new_num:str):
        for phone in self.phones:
            if phone.value == old_num:
                pos = self.phones.index(phone)
                self.phones[pos] = Phone(new_num)
    
    def find_phone(self, num:str) -> str:
        for phone in self.phones:
            if phone.value == num:
                return num

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}
        
    def add_record(self, record:Record):
        self.data[record.name.value] = record
        
    def find(self, name:str) -> Record:
        return self.data[name]
    
    def delete(self, name:str):
        self.data.pop(name)
    