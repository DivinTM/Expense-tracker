expense_tracker={}
z=0
total=1
d=0
print("***************************************************************")
amount=int(input("Enter the amount: "))
while True:
    print("***************************************************************")
    print("1.Insertion")
    print("2.Balance")
    print("3.Display")
    print("4.Add amount")
    print("5.Delete")
    print("6.Exit")
    print("***************************************************************")
    ch=int(input("Enter the choice: "))
    print("***************************************************************")


    if ch==1:
        if total<=0:
            print("*Your wallet is empty. Please check your balance. Add amount*")
        else:
            item=input("Enter the item: ")
            # all letters capital letter
            item=item.upper()
            price=int(input("Enter the price: "))

            b=0
            for i,j in expense_tracker.items():
                b=b+j
            cost=b
            total=cost+price
            # print(total)
            if total > amount:
                print("*Your wallet is low. Please check your balance*")
            
            else:
                if item in expense_tracker:
                    z=0
                    for i,j in expense_tracker.items():
                        if item==i:
                            z=z+j
                    z=z+price
                    expense_tracker[item]=z
                    print("*Entered*")
                else:
                    expense_tracker[item]=price
                    print("*Entered*")
                    b=0
                    for i,j in expense_tracker.items():
                        b=b+j
                    cost=b
                    total=amount-cost
            

            
    elif ch==2:
        b=0
        for i,j in expense_tracker.items():
            b=b+j
        cost=b
        total=amount-cost
        print("Full amount"," "*14,":",amount)
        print("Extra added amount"," "*7,":",d)
        print("Cost"," "*21,":",cost)
        print("Balance amount"," "*11,":",total)

    elif ch==3:
        if len(expense_tracker)==0:
            print("Items"," "*25,":","Price")
            print("---------------------------------------------------------------")
            print(" "*15,"*No Items*")

        else:
            print("Items"," "*25,":","Price")
            print("---------------------------------------------------------------")
            for i,j in expense_tracker.items():
                print(i," "*(30-len(i)),':',j)

    elif ch==4:
        add_amount=int(input("Enter the amount : "))
        d=d+add_amount
        amount=amount+add_amount
        print("*Amount added*")
        total=amount
        print("*Check balance*")

    elif ch==5:
        Item=input("Enter the name: ")
        # all letters capital letter
        Item=Item.upper()
        if Item in expense_tracker:
            expense_tracker.pop(Item)
            print("*Deleted*")
        else:
            print("It's not in it.")
        

    elif ch==6:
        print("*EXIT*")
        print("***************************************************************")
        exit()

    
    else:
        print("Entered value not matching")