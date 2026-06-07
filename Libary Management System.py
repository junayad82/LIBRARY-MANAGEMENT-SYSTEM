library = []
while True:
    print("====LIBRARY MANAGEMENT SYSTEM====")
    print("1. Add Book")
    print("2. View Book")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")
    choice = input("Enter a choice: ")

    # Add Book
    if choice == "1":
        name = input("Book name: ")
        author = input("Author name: ")

        li = {
            "name": name,
            "author": author
        }
        library.append(li)
        print("Book added succesfully")
     
    # View Book
    elif choice == "2":
        if len(library) == 0:
            print("No Book Foundded")
        else:
            for i, library in enumerate(library, start=1):
                print("\nBook List:")
                print(f"{i}.{li['name']}")
    
    # Search Book
    elif choice == "3":
        search_book = input("Inter the book name: ")
        for li in library:
            if li["name"].lower() == search_book.lower():
                print(li)
            else:
               print("No movie founded")
        


