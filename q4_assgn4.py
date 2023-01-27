def find_candies():
    for candies in range(200):
        if candies % 5 == 2 and candies % 6 == 3 and candies % 7 == 2:
            return candies

print("There are", find_candies(), "candies in the bowl.")
