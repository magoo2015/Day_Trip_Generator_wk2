import random # For random selections


#Lists for destinations, restaurants, transportation, and entertainment.

destinations_list = ["Dallas, Tx", "Atlanta, Ga", "Baton Rouge, La", "Denver, Co"]
restaurant_list = ["Texas RoadHouse", "Rafains", "Hard Rock Cafe", "Toby Keith Bar and Grill", "Glorias" ]
transportation_list = ["Bus", "Train", "Horse Carriage", "Uber/LIFT", "Rapid Transit"]
entertainment_list = ["Six Flags", "NBA Game", "UFC: Israel Adesayna vs. Robert Whitaker", "Sea World", "WWE WrestleMania"]

user_trip_details = [] #Hold user selections here.

#Stuck on selecting the destination randomly
def user_destination():
    dest_confirmed = True
    selected_destination = [""]
    random_destinations = random.choice(destinations_list)
    user_choice = input(f"How does {random_destinations} sound for your destination? Enter y/n: ")

    while dest_confirmed == True:

        if user_choice == "y":
            print("Awesome, lets move on.")
            selected_destination = random_destinations
            user_trip_details.append(selected_destination)
            dest_confirmed = False
        elif user_choice == "n":
            destinations_list.remove(random_destinations) # Put here to remove bad choice.
            random_destinations = random.choice(destinations_list)
            user_choice = input(f"Sorry that does not work for you, how about {random_destinations} Enter y/n: ")
            dest_confirmed = True

#Reuse the format of previous function for remaining functions.


def user_restaurant():
    restaurant_confirmed = True
    selected_restaurant = [""]
    random_restaurants = random.choice(restaurant_list)
    user_choice = input(f"Would you like to dine at {random_restaurants} during your vacation? Enter y/n: ")

    while restaurant_confirmed == True:

        if user_choice == "y":
            print("Great, let's continue!")
            selected_restaurant = random_restaurants
            user_trip_details.append(selected_restaurant)
            restaurant_confirmed = False
        elif user_choice == "n":
            restaurant_list.remove(random_restaurants)
            random_restaurants = random.choice(restaurant_list)
            user_choice = input(f"Back to the drawing board....how would you like {random_restaurants}? Enter y/n:")
            restaurant_confirmed = True


def user_transportation():
    transportation_confirmed = True
    selected_transportation = [""]
    random_transportation = random.choice(transportation_list)
    user_choice = input(f"Would travel by {random_transportation} be acceptable for your vacation?  Enter y/n:  ")

    while transportation_confirmed == True:

        if user_choice == "y":
            print("Good choice, we're almost finished.  Let's continue.")
            selected_transportation = random_transportation
            user_trip_details.append(selected_transportation)
            transportation_confirmed = False
        elif user_choice == "n":
            transportation_list.remove(random_transportation)
            random_transportation = random.choice(transportation_list)
            user_choice = input(f"Sorry that does work for you, how about {random_transportation}? Enter y/n: ")
            transportation_confirmed = True


def user_entertainment():
    entertainment_confirmed = True
    selected_entertainment = [""]
    random_entertainment = random.choice(entertainment_list)
    user_choice = input(f"Have you thought of entertainment ideas, We think {random_entertainment} would be great.  What do you think?  Enter y/n: ")

    while entertainment_confirmed == True:
        
        if user_choice == "y":
            selected_entertainment = random_entertainment
            user_trip_details.append(selected_entertainment)
            entertainment_confirmed = False
        elif user_choice == "n":
            entertainment_list.remove(random_entertainment)
            random_entertainment = random.choice(entertainment_list)
            user_choice = input(f" Ok, How about {random_entertainment}? Enter y/n: ")
            entertainment_confirmed = True


def trip_confirmed():
    print(f"Your selected destination is {user_trip_details[0]}, you will be traveling via {user_trip_details[1]}, for entertainment you have chosen {user_trip_details[2]}, you will be dining at {user_trip_details[3]}")
    user_choice = input(f"Please Enter 'y' to confirm you trip or 'n' to start over.  Enter y/n: ")
    if user_choice == "y":
        print(f"Here is your final confirmation:\n Destination:  {user_trip_details[0]}\n Type of Travel:  {user_trip_details[1]}\n Entertainment:  {user_trip_details[2]}\n Dining:  {user_trip_details[3]}")
        print("Thank you for using the Trip Generator")
    elif user_choice == "n":
        run_trip_generator()
    



def run_trip_generator():
    print("Welcome to the trip generator, where we help you plan your next vacation!")   
    user_destination()
    user_transportation()
    user_entertainment()
    user_restaurant()
    trip_confirmed()

run_trip_generator()

    
















