import matplotlib.pyplot as plt
currencies = ["Euro","Pound","swiss Franc","Sri Lankan Rupee"]
conversions = [1.11,1.31,1.01,.0055]

plt.figure("Question 4")
plt.scatter(currencies,conversions,color=('r','g','r','g'),marker="*")
plt.xlabel("Currency")
plt.ylabel("Conversion To $")
plt.title("Currency Conversion Visualization")
plt.show()
