# --------------------------------------
# Simulate rolling 2 dice and plot the results.
# --------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------

def generate_rolls(how_many):
    result = np.ndarray(how_many, dtype=int)
    
    for roll in range(how_many):
        result[roll] = np.random.randint(1, 7) + np.random.randint(1, 7)
        
    return result

# --------------------------------------

def main():
    rolls = generate_rolls(100000)

    plt.hist(rolls, bins=np.arange(2, 14),facecolor='b', align='left')  # generate histogram
    plt.xticks(np.arange(2, 13))
    
    plt.xlabel('Value')
    plt.ylabel('Occurrences')
    plt.title('Histogram of Dice Rolls')
    plt.grid(True)
    plt.show()
    
# --------------------------------------

if __name__ == "__main__":
    main()
