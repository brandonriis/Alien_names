# - Uses try and except to validate inputs (Look at workbook 8)

# Main Function
def main():

    # Main Menu
    print("\n---Main Menu---")
    print("A - Aliens")
    print("E - Extend")
    print("X - Exit Program")
    print("")
    choice = str.upper(input("Please select an option from the menu: "))

    # TEST
    # print(choice)

    # Function Selection
    if(choice == "A"):
        aliens()

    elif(choice == "E"):
        extended()

    elif(choice == "X"):
        exit()

    else:
        print("\nPlease enter a valid choice!\n")
        main()


def aliens():

    # Complete list for testing - Need to add last actor in the console
    # actor_names = ["Andrei Stephens", "Harry Venables", "Stephanie Myrah",
    #                "Dianne Davies", "Yuan Spield", "Ness Helter", "Sadiq Elbahi",
    #                "Fred Brynn", "Zeng Ergan",]

    # Create actors name list
    actor_names = []

    # While loop adding actors names to "actor_name" list
    exit = "Y"
    while (exit != "N"):
        name = input("\nPlease enter the actors first and last name: ")
        actor_names.append(name)
        exit = input("\nDo you want to enter another name? Y/N : ").upper()

    # Create alien names list
    alien_names = []

    # For every actor name, split it in two and then preform the alien name conversion
    for i in range(len(actor_names)):
        name = actor_names[i]
        splitfirst, splitlast = name.split()

        # Testing
        # print(splitfirst)
        # print(splitlast)

        firstslice = splitfirst[0:2]
        lastslice = splitlast[0:3]
        firstreverse = str.lower(firstslice[::-1])
        alien = lastslice + firstreverse
        alien_names.append(alien)

    # Testing
    # print(actor_names)
    # print(alien_names)
    # print("stop")

    # Print out all the alien names
    print("-Ref-  -Alien Name-")
    for i in range(len(alien_names)):
        print(" ", i, "     ", alien_names[i])

    # Ask if user want to delete a name and then run the delete function
    choice_remove = input("Would you like to delete an name?: Y/N ").upper()
    if choice_remove == "Y":
        alien_names = delete_from_list(alien_names)

    # Testing
    # print(alien_names)
    # input("stop")

    # Send the alien names to the vowel remove function and return the list
    # and a no vowel list as well
    alien_names, alien_no_vowels = remove_vowels(alien_names)

    # Testing
    # print(alien_names)
    # print(alien_no_vowels)

    # Send the alien names list and the actors list to the final name function
    final_name(alien_names, actor_names)


def delete_from_list(alien_names):

    # Remove name from the list based on the user input
    choice_remove = "Y"
    while choice_remove == "Y":
        remove = int(input("Which reference would you like to delete?: "))

        alien_names.pop(remove)

        print("-Ref-  -Alien Name-")

        for i in range(len(alien_names)):
            print(" ", i, "     ", alien_names[i])

        choice_remove = input("Would you like to remove another name? Y/N :").upper()

    # Return list to the alien function
    return alien_names


def remove_vowels(alien_names):

    # Create no vowel list and define vowels in another list
    no_vowels_list = []
    vowels = ["a", "e", "i", "o", "u"]

    # Search each name in the alien list to see if the contain any letter from the vowel
    # list, moving the name to another list if they don't
    for word in alien_names:
        no_vowels = True

        for letter in word:
            if letter in vowels:
                no_vowels = False

        if no_vowels == True:
            no_vowels_list.append(word)

    # Remove any name that is in the no vowel list from the alien name list
    alien_names = [x for x in alien_names if x not in no_vowels_list]

    # Return both lists to the alien function
    return alien_names, no_vowels_list


def final_name(alien_names, actor_names):

    # For every name in the list take the first 3 letters and combine them into one
    # string
    finished_name = ""
    for x in range(len(alien_names)):
        name = alien_names[x][0:3]
        finished_name = finished_name + name

    # Split the combined name and format it as a name
    first_name = finished_name[0:5].title()
    last_name = finished_name[6:].title()

    # Print the final name as well as the alien list and the actors list.
    print("\n-----", first_name, last_name, "Presents: -----")

    print("\n-Ref-  -Alien Name-")
    for i in range(len(alien_names)):
        print(" ", i, "     ", alien_names[i])

    print("\n-Ref-  -Actor Names-")
    for i in range(len(actor_names)):
        print(" ", i, "     ", actor_names[i])



def extended():

    print("Extended")
    main()


main()

