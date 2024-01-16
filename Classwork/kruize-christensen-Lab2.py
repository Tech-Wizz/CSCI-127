# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Lab 2: Tax Calculator                 |
# Kruize Christensen                    |
# Date: September 10, 2019              |
# ---------------------------------------
# Calculate the amount of tax owed by an|
# unmarried taxpayer in tax year 2018.  |
# ---------------------------------------

def unmarried_individual_tax(income):
    tax_owed = 0
    if (income<9700):
        tax_owed = income *.1
    elif (income<39475):
        tax_owed = ((.12*(income-9700))+.1*9700)
    elif (income<84200):
        tax_owed = ((.22*(income-39475))+.12*(29775)+.1*9700)
    elif (income<160725):
        tax_owed = ((.24*(income-84200))+.22*(44725)+.12*(29775)+.1*9700)
    elif (income<204100):
        tax_owed =((.32*(income-160725))+.24*(76525)+.22*(44725)+.12*(29775)+.1*9700)
    elif (income<510300):
        tax_owed = ((.35*(income-204100))+.32*(43375)+.24*(76525)+.22*(44725)+.12*(29775)+.1*9700)
    elif (income>=510300):
        tax_owed = ((.37*(income-510300))+.35*(306200)+.32*(43375)+.24*(76525)+.22*(44725)+.12*(29775)+.1*9700)
    return (tax_owed)

# ---------------------------------------

def process(income):
    print("The 2018 taxable income is ${:.2f}".format(income))
    tax_owed = unmarried_individual_tax(income)
    print("An unmarried individual owes ${:.2f}\n".format(tax_owed))

#---------------------------------------

def main():
    process(5000)      # test case 1
    process(20000)     # test case 2
    process(50000)     # test case 3
    process(100000)    # test case 4
    process(200000)    # test case 5
    process(400000)    # test case 6
    process(600000)    # test case 7

# ---------------------------------------

main()

