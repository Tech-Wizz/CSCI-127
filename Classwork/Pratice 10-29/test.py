
scor_differences ={}
scor_differences["October 7, 2017"] = 8
scor_differences["October 14, 2017"] = -12
scor_differences["October 21, 2017"] = 3

wins = 0
losses = 0

for difference in scor_differences.values():
    if difference > 0:
        wins += 1
    else:
        losses += 1
   
def main():
    print(wins,"wins-",losses,"losses")



# class Appliance():
#     def __init__(self,manufacturer):
#         self.manufacturer = manufacturer

#         def get_manufacturer(self):
#             return self.manufacturer


# class Refrigerator(Appliance):
#     def __init__(self, manufacturer, refrigerant):
#         super().__init__(manufacturer)
#         self.refrigerant = refrigerant

#     def __str__(self):
#         result = "The" + self.get_manufacturer()
#         result += " refrigerator contains refrigerant "
#         result += self.refrigerant
#         return result



# my_refrigerator = Refrigerator("Samsung","R134a")
# print(my_refrigerator)

