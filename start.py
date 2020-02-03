from restaurant_control import RestaurantControl

if __name__ == "__main__":
    restaurant = RestaurantControl()

    while True:
        print('\nOperation: my_order\n')
        restaurant.my_order()
