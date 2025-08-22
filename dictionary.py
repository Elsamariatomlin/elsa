dict= [{"Name":"appple","price":100,"Quantity":10},
      {"Name":"orange","price":200,"Quantity":20},
      {"Name":"mango","price":300,"Quantity":30},
      {"Name":"grapes","price":400,"Quantity":40}]


while True:
    print("MENU")
    print("1.add item")
    print("2.view item")
    print("3.update item")
    print("4.remove item")
    print("5.exit")
    
    choice=input("choose the option 1-5:")
    if choice=="1":
        name=input("Enter the name of the item:")
        price=float(input("Enyter the price of the item:"))
        quantity=int(input("Enyter the quantity of the item:"))
        dict.append({"Name":name,"price":price,"Quantity":quantity})
        print("item added successfully")
    elif choice =="2":
        print("fruit details",dict)
    
    elif  choice =="3":
        old_item=input("enter the name of the item you want to update:")
        if old_item in dict:
            new_item=input("enter the new name of the item:")
            dict[old_item]=new_item
            new_name=input("enter the new name of the items:")
            new_price=float(input("enter the new price of the item:"))
            new_quantity=int(input("enter the new quantity of the item:"))
           
            print("updated successfully")
        else:
         print("sorry item is not found")

    elif choice =="4":
        new=input("enter the item you want remove")
        dict.remove(new)
        print("items are removed successfully")

    elif choice =="5":
        print("bye then thanks for using")
        break

    else:
        print("invalid choice, please choose from 1-5")
