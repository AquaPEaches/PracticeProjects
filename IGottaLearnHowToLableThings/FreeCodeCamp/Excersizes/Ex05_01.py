my_list = []  # Initialize an empty list

while True:
    print("\nMenu:")
    print("1. Addition")
    print("2. Insertion")
    print("3. Deletion")
    print("4. Count")
    print("5. Sum")
    print("6. Maximum")
    print("7. Minimum")
    print("8. Print")
    print("9. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        num = int(input("Enter the integer to add: "))
        my_list.append(num)
    elif choice == 2:
        num = input(("Enter the integer to insert: "))
        index = int(input("Enter the index to insert at: ")) 
    elif choice == 3:
        num = int(input("Enter the integer to delete: "))
        
        if num in my_list:
            my_list.remove(num)
        else:
            print("Element was not found....")   

        pass
    elif choice == 4:

        num = input("Enter the integer amount: ")
        Count = my_list.count(num)

        print(f"ofc the integer{num} is in the number {Count} of the list")

        print(Count)
    elif choice == 5:
        num = sum(my_list)
        print(f"The total of your list is {num} now go do something else....")
    elif choice == 6:
        if my_list:
            max_value = max(my_list)
            print(f"max value in the list {max_value}")
        else:
            print("list is empty")
    elif choice == 7:
        if my_list:
            min_value = min(my_list)
            print(f"min value in the list {min_value}")
        else:
            print("list is empty")
    elif choice == 8:
        print(f"current list is: {my_list}")
    elif choice == 9:
        break
    else:
        print("Invalid choice. Please choose a valid expression! ")
