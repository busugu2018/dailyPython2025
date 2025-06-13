hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in  
                            #the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

hat_list[2] = int(input("Enter number: "))
print("New list is " + str(hat_list))


# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
print("New list is " + str(hat_list))