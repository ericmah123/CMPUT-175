# Exercise 1

# 1.

flower = {
    "Daffodil": 0.35,
    "Tulip": 0.33,
    "Crocus": 0.25,
    "Hyacinth": 0.75,
    "Bluebell": 0.50,

}

# 2.

standing_order = {
    "Daffodil": 50,
    "Tulip": 100,
}

# 3.

new_flower = {"Tulip": 0.41}
flower.update(new_flower)

# 4.

standing_order["Hyacinth"] = 30

# 5.

print("You have purchased the following bulbs:")

# setting a count outside the for loop to be able to include it in the final print statements
bulb_count = 0
total_cost = 0

for key, value in sorted(standing_order.items()):
    # runs through key and value, which allowed me to access them separately.

    bulb_name = key[:3].upper()
    bulb_amount = value
    cost = value * flower[key]
    bulb_count += value
    total_cost += cost

    print('{0:<5s} *{1:>4d} = $ {2:>6.2f}'.format(bulb_name, bulb_amount, cost))

print("Thank you for purchasing {0} bulbs from Bluebell Greenhouses.".format(bulb_count))
print("Your total comes to $ {0:.2f}".format(round(total_cost, 2)))
