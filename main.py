import random # For random selections

#Lists for destinations, restaurants, transportation, and entertainment.

destinations_list = ["Dallas", "Atlanta", "Baton Rouge", "Denver"]
restaurant_list = ["Texas RoadHouse", "Rafains", "Hard Rock Cafe", "Toby Keith Bar and Grill", "Glorias" ]
transportation_list = ["Bus", "Train", "Horse Carriage", "Uber/LIFT", "Rapid Transit"]
entertainment_list = ["Six Flags", "NBA Game", "UFC: Israel Adesayna vs. Robert Whitaker", "Sea World", "WWE WrestleMania"]

user_trip_details = []
#Stuck on selecting the destinati0n randomly
def user_destination():
    random_destinations = random.choice(destinations_list)
    return random_destinations
    
    
user_selected_destination = user_destination()





def trip_generator():
    trip_on = True
    print("Welcome to the Day Trip Generator, where we help you plan your vacation!")
    choice = input(f"We have selected {user_selected_destination} as your destination.  How does this sound?")
    while trip_on:
        if choice == "y":
            print("Awesome great choice. Let's continue")
            user_trip_details += user_selected_destination
            print(user_trip_details)
            trip_on = False
        else:
            trip_on = True

trip_generator()


    















