import random # For random selections

#Lists for destinations, restaurants, transportation, and entertainment.

destinations_list = ["Dallas, Tx", "Atlanta, Ga", "Baton Rouge, La", "Denver, Co"]
restaurant_list = ["Texas RoadHouse", "Rafains", "Hard Rock Cafe", "Toby Keith Bar and Grill", "Glorias" ]
transportation_list = ["Bus", "Train", "Horse Carriage", "Uber/LIFT", "Rapid Transit"]
entertainment_list = ["Six Flags", "NBA Game", "UFC: Israel Adesayna vs. Robert Whitaker", "Sea World", "WWE WrestleMania"]

user_trip_details = []

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
            random_destinations = random.choice(destinations_list)
            user_choice = input(f"Sorry that does not work for you, how about {random_destinations} Enter y/n: ")
            dest_confirmed = True



user_destination()
print(f"Your selected destination is {user_trip_details[0]}")       
    
    






# def trip_generator():
#     trip_on = True
#     print("Welcome to the Day Trip Generator, where we help you plan your vacation!")
#     choice = input(f"We have selected {user_selected_destination} as your destination.  How does this sound?")
#     while trip_on:
#         if choice == "y":
#             print("Awesome great choice. Let's continue")
#             user_trip_details += user_selected_destination
#             print(user_trip_details)
#             trip_on = False
#         else:
#             trip_on = True

# trip_generator()


    















