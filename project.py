# cart=[]
# print("\nShopping Cart Menu:")
# print("1. Add Item")
# print("2. Remove Item")
# print("3. Update Item")
# print("4. View Cart")
# print("5. Search Item")
# print("6. Slice Cart")
# print("7. Sort Cart")
# print("8. Exit")




# print=(input("choose an option from 1 to 8:"))
# item=input("enter an item")
# cart.append(item)
# print(f"{item} added to cart")

# print=(input("choose an option from 1 to 8:"))
# item=input("enter an item")
# cart.remove(item)
# print(f"{item} remove to cart")


# print=(input("choose an option from 1 to 8:"))
# item=input("enter an item")
# cart.update(item)
# print(f"{item} update to cart")


# print=(input("choose an option from 1 to 8:"))
# item=input("enter an item")
# cart.update(item)
# print(f"{item} update to cart")

# print(cart)

# cart = []

# while True:
#     print("\nShopping Cart Menu:")
#     print("1. Add Item")
#     print("2. Remove Item")
#     print("3. Update Item")
#     print("4. View Cart")
#     print("5. Search Item")
#     print("6. Slice Cart")
#     print("7. Sort Cart")
#     print("8. Exit")

#     choice = input("Choose an option (1-8): ").strip()

#     if choice == '1':
#         item = input("Enter item to add: ").strip()
#         cart.append(item)
#         print(f"'{item}' added to cart.")

#     elif choice == '2':
#         item = input("Enter item to remove: ").strip()
#         if item in cart:
#             cart.remove(item)
#             print(f"'{item}' removed from cart.")
#         else:
#             print(f"'{item}' not found in cart.")

#     elif choice == '3':
#         old_item = input("Enter item to update: ").strip()
#         if old_item in cart:
#             index = cart.index(old_item)
#             new_item = input("Enter new item: ").strip()
#             cart[index] = new_item
#             print(f"'{old_item}' updated to '{new_item}'.")
#         else:
#             print(f"'{old_item}' not found in cart.")

#     elif choice == '4':
#         if not cart:
#             print("Cart is empty.")
#         else:
#             print("\nCart Items:")
#             for i in range(len(cart)):
#                 print(f"{i}: {cart[i]}")
#             print(f"Total items: {len(cart)}")

#     elif choice == '5':
#         item = input("Enter item to search: ").strip()
#         if item in cart:
#             index = cart.index(item)
#             print(f"'{item}' found at position {index}.")
#         else:
#             print(f"'{item}' not found in cart.")

#     elif choice == '6':
#         if not cart:
#             print("Cart is empty.")
#         else:
#             try:
#                 start = int(input("Enter start index: "))
#                 end = int(input("Enter end index: "))
#                 print("Cart slice:", cart[start:end])
#             except ValueError:
#                 print("Invalid index input.")

#     elif choice == '7':
#         if not cart:
#             print("Cart is empty.")
#         else:
#             cart.sort()
#             print("Cart sorted alphabetically.")

#     elif choice == '8':
#         print("Exiting... Thank you for using the shopping cart!")
#         break

#     else:
#         print("Invalid option. Please choose again.")








# student=[]
# while True:
#     print("1. Add Student")
#     print("2. View Student")
#     print("3. Search Student")
#     print("4. Remove Student")
#     print("5.update Student")
#     print("6. Exit")

#     choice=input("choose the option 1-6:")
#     if choice=="1":
#         name=input("Enter the name of the student:")
#         age=int(input("Enyter the age of the sudent:"))
#         student.append({"name":name,"age":age})
#         print("student added successfully")

#     elif choice=="2":
#         print("student details",student)

   
#     elif choice=="3":
#         search=input("enter the name of the student")
#         if search in student:
#             print(f"{search} student found")
#         else:
#             print(f"{search} student not found")

#     elif choice=="4":
#         remove=input("enter the name of the student")
#         if remove in student:
#             student.remove(remove)
#             print(f"{remove} student removed successfully")
#         else:
#             print(f"{remove} student not found")
#     elif choice =="5":
#         old=input("enter the name of the student to update")
#         if old in student:
#             new=input("enter the new name of the student")
#             student[old]=new
#             print(f"{old} student updated successfully")
#         else:
#             print(f"{old} student not found")
#     elif choice=="6":
#         print ("bye then thanks for using")
#         break

#     else:
#         print("invalid choice, please choose from 1-7")





# s


A={"swimming","running","cycling"}
B={"swimming","biking","running"}
common_hobbies=A.intersection(B)
print(common_hobbies)
unique_A=A.difference(B)
print(unique_A)
