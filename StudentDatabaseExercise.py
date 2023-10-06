# creating lists, so they'll be in scope for later functions
names_list = []
hometown_list = []
favorite_food_list = []


# define function for adding parameters for given list
def build_database(name, hometown, favorite_food):
    names_list.append(name)
    hometown_list.append(hometown)
    favorite_food_list.append(favorite_food)
    print(names_list, hometown_list, favorite_food_list)


# calling function 1

build_database(name="Alex", hometown="Chicago", favorite_food="Steak")
build_database(name="Arthur", hometown="Lansing", favorite_food="Pizza")
build_database(name="Julia", hometown="Minneapolis", favorite_food="Eggs")
build_database(name="Laree", hometown="Detroit", favorite_food="Pasta")
build_database(name="Harpar", hometown="Plymouth", favorite_food="Tacos")
build_database(name="Bryce", hometown="Cheboygan", favorite_food="Sushi")
# prompt = int(input('Which student would you like to learn more about?'
#                    + ' (enter a number 1-' + str(len(names_list)) + "):"))
more_info = str("Would you like to learn about another student? Enter 'y' or 'n': ")


# start of 2nd function
def name_search(student_number, ):
    while True:
        prompt = int(input('Which student would you like to learn more about?'
                           + ' (enter a number 1-' + str(len(names_list)) + "):"))
        # try block to catch out of range error
        try:
            print(f"Student {prompt} is {names_list[(prompt - 1)]}. What would you like to know? ")
            category_prompt = input("Enter: 'hometown' or 'favorite food':")
            # checks for hometown input
            if category_prompt.lower() == "hometown":
                print(f'{names_list[(prompt - 1)]} is from {hometown_list[(prompt - 1)]}.')
                input(more_info)
            # checks for favorite foods input
            elif category_prompt.lower() == "favorite food":
                print(f'{names_list[(prompt - 1)]}\'s favorite food is {favorite_food_list[(prompt - 1)]}.')
                input(more_info)
            # if input is not accepted - loop
            else:
                print("That category does not exist. Please try again. Enter 'hometown' or 'favorite food': ")
            # loop back to function 1
            if more_info.lower() == "y":
                print(prompt)
            elif more_info.lower() != "y":
                break
            #   print("That category does not exist. Please try again.")
        except:
            # prompt not in range (1, len(names_list)):
            print('"I''m sorry there are no students associated with that number,'
                  + 'please enter a number 1-' + str(len(names_list)) + ". ")
        break
        # try block to catch input error
    # while True:


while more_info:

    name_search(0)
