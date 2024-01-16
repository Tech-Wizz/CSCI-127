import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# Kruize Christensen                    |
# Last Modified: October 30, 2019       |
# ---------------------------------------
# Pokedex
# ---------------------------------------

#print the menu and spaces it from the entry of the user
def print_menu():
    print("1. Print Pokedex")
    print("2. Print Pokemon by Name")
    print("3. Print Pokemon by Number")
    print("4. Count Pokemon with Type")
    print("5. Print Average Pokemon Combat Points")
    print("6. Quit")
    print("\n")

#prints the pokedex drived from the class and the given function
def print_pokedex(pokedex):
    print("\n")
    print("The Pokedex")
    print("-----------")
    for entry in pokedex:
        print(entry)
        
#prints the information of the given pokemon name, if not found it will trigger and if statment that will print a different statment
def lookup_by_name(pokedex, name):
    found = False
    for pokemon in pokedex:
        if str(pokemon.name) == str(name):
            print (pokemon)
            found = True
    if found == False:
        print("There is no Pokemon named",name)
            
#works the same way as the lookup_by_name but works with numbers not names   
def lookup_by_number(pokedex, number):
    found = False
    for pokemon in pokedex:
        if str(pokemon.number) == str(number):
            print (pokemon)
            found = True
    if found == False:
        print("There is no Pokemon number ",number)
        
#adds up how many time the type occurs
def total_by_type(pokedex, pokemon_type):
    n=0
    types = 0
    for pokemon in pokedex:
        if pokemon_type in pokemon.get_types():
            n += 1
    print("Number of Pokemon that contain type",pokemon_type," = ",n)


#adds all the cp together and finds the average
def average_hit_points(pokedex):
    cp = 0
    t = 0
    for pokemon in pokedex:
        t += 1
        cp += pokemon.get_cp() 
    combat_points = round(cp/t,2)
    print("Average Pokemon combat points = ", combat_points)
        
    

#organizes the data given to be in a more presentable/readable manner
class Pokemon:

    def __init__(self,name, number, cp, types):
        self.name = name
        self.number = number
        self.cp = cp
        self.types = types

    def __repr__(self):
        self.entry = "Number: " + str(self.number) + ", " + "Name: " + str(self.name) + ", " + "CP: " + str(self.cp) + ", " + "Type: " + ' and '.join(self.types)
        return self.entry

    def get_types(self):
        return self.types

    def get_name(self):
        return self.name

    def get_cp(self):
        return self.cp
        


# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist[0])               # number
        name = pokelist[1]                      # name
        combat_points = int(pokelist[2])        # hit points
        types = []
        for position in range(3, len(pokelist)):
            types += [pokelist[position]]       # type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex

# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ").lower()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            pokemon_type = input("Enter a Pokemon type: ").lower()
            total_by_type(pokedex, pokemon_type)
        elif choice == 5:
            average_hit_points(pokedex)
        elif choice == 6:
            print("Thank you.  Goodbye!")
        print()

# ---------------------------------------

main()
