# -----------------------------------------------------
# CSCI 127, Lab 8
# October 22, 2019
# Kruize Christensen
# -----------------------------------------------------


class Contact:

    def __init__(self,first,last,phone):
        self.title = ""
        self.first = first
        self.last = last
        self.phone = phone

    def print_entry(self):
        self.name = self.first + " " + self.last
        self.sirname = self.title + self.name
        print('{:24s}{:12s}'.format(self.sirname,self.phone))
    
    def set_first_name(self,first):
        self.first = first

    def set_title(self,title):
        self.title = title + " "

    def get_cell_number(self):
        return self.phone

    def get_area_code(self):
        return self.phone[0:3]
# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        person.print_entry()
    print("-----------\n")

# -----------------------------------------------------

def main():
    champ = Contact("???", "Bobcat", "406-994-0000")
    president = Contact("Waded", "Cruzado", "406-994-CATS")
    professor = Contact("John", "Paxton", "406-994-4780")

    contacts = [champ, president, professor]

    print_directory(contacts)

    champ.set_first_name("Champ")
    president.set_title("President")
    professor.set_title("Professor")

    print_directory(contacts)

    print("The area code for cell number", champ.get_cell_number(), "is", \
           champ.get_area_code())

# -----------------------------------------------------

main()