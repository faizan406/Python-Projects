contacts={}

while True:
    print("\nCOntact Book app")
    print("1.create contact")
    print("2.view contact")
    print("3.Update contact")
    print("4.Delete contact")
    print("5.Search contact")
    print("6.count contact")
    print("7.Exit")
    
    choice=int(input("Enter Your choice = "))
    
    if choice==1:
        name=input("Enter Your name = ")
        if name in contacts:
            print(f"Contact name {name} already exist")
        else:
            age=int(input("Enter age = "))
            email=input("Enter E-mail = ")
            number=int(input("Enter Phone Number"))
            contacts[name]={'age':age,'email':email,'number':number}
            print(f"Contact name {name} has been created successfully")
            
    elif choice==2:
        name=input("Enter Contact name to view = ")
        if name in contacts:
            contact=contacts[name]
            print(f"Name:{name},Age:{age},Mobile number:{number},E-mail:{email}")
        else:
            print("contact not found")
            
    elif choice==3:
        name=input("Enter name want to update")
        if name in contacts:
            age=int(input("Enter Updated Age = "))
            email=input("Enter updated email = ")
            number=input("Enter Updated Number = ")
            contacts[name] ={'age':{age},'email':{email},'number':number}
        else:
            print("Name not found")
            
    elif choice==4:
        name=input("Enter Name want to delete")
        if name in contacts:
            del contacts[name]
            print(f"{name} is deleted successfully")
        else:
            print("Name not found")
            
    elif choice==5:
        search_name=input("Enter name want to search= ")
        found=False
        for name,contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - Name:{name},Age:{age},Number:{number},email:{email}")
                found=True
        if not found:
            print("No contact found with that name")
            
    elif choice==6:
        print("Total contact in your book:{len(contacts)}")
    
    elif choice==7:
        print("Goodbye ...closing the program")
        
    else:
        print("invalid input")
                
            
               