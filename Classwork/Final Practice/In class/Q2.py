class Element:

    def __init__(self,number,name):
        self.atomic_number = number
        self.name = name.capitalize

    def __str__(self):
        answer = self.name + "has atomic number" + str(self.atomic_number)
        if self.is_noble_gas():
            answer += " and is a noble gas."
        else:
            answer += "."
        return answer

    def is_noble_gas():
        return True

hydrogen = Element(1, "hydrogen")
print(hydrogen)
helium = Element(2, "helium")
print(helium)
