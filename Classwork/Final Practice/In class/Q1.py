def calculate_calories(order, nutrition):
    answer = 0
    for item, count in my_order:
        for sales_item, calories in nutrition:
            if item == sales_item:
                answer += count * calories
    return answer

nutrition_info = [["big mac ", 850], ["chicken", 440],["fries",340],["coke",290], ["cookie",170]]

my_order = [["big mac",2],["fries",1],["coke",1]]

print("Calories in order =" + calculate_calories(my_order, nutrition_info))
