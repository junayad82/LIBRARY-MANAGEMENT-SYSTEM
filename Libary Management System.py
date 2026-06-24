library = []

while True:

    print("\nLibrary Mnagement System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Show available Book")
    print("8. Show Borrowed Books")
    print("9. Save Data to file")
    print("10. Exit")

    choice = input("Enter your choice: ")

    # Add Book

    if choice == "1":

        title = input("Enter Book name: ")
        author = input("Enter author name: ")

        book = {
            "name": title,
            "author": author,
            "available": True
        }

        library.append(book)

        with open("library.txt", "a") as file:
            file.write(f"{book['name']} {book['author']} | Available\n")

            print("Book added successfully!")

    # View Books

    elif choice == "2":

        if len(library) == 0:

            print("No book available")
        
        else:

            print("\nBook List:")

            for i, book in enumerate(library, start=1):

                status = "✔" if book["available"] else "😢"

                print(
                    f"{i}. {book['name']}",
                    f"Author: {book['author']}",
                    f"Status: {status}"
                )
    
    # Search Book

    elif choice == "3":

        search_book = input("Enter book name: ")

        found = False

        for book in library:

            if search_book.lower() == book["name"].lower():

                status = "Available" if book["available"] else "Borrowed"


                print("Book list:")
                print(f"Title: {book['name']}")
                print(f"Author: {book['author']}")
                print(f"Status: {status}")

                found = True
                break

        if not found:
             print("No book available")         

    # Borrow Book

    elif choice == "4":

        borrow_book = input("Enter Book name: ")

        found = False

        for book in library:

            if borrow_book.lower() == book["name"].lower():

                found = True

                if book["available"]:
                    book["available"] = False

                    print("Book borrowed successfully!")

                else:
                    print("Book already borrowed!")

                break
        if not found:
            print("No book founded")
                                  
    # Return book

    elif choice == "5":

        return_book = input("Enter return book name: ")

        found = False

        for book in library:

            if return_book.lower() == book["name"].lower():

                found = True

                if not book["available"]:
                    book["available"] = True
                    
                    print("Book return successfully")

                
                else:
                    print("This book was not borrwed")

                break

        if not found:
            print("No book founded")
                    
    # Delete book

    elif choice == "6":

        delete_book = input("Enter book name to delete: ")

        found = False

        for book in library:

            if delete_book.lower() == book["name"].lower():

                library.remove(book)
                
                print("Book delete successfully!")

                found = True
                break

        if not found:
            print("No book founded")
                
    # Show available

    elif choice == "7":

        print("Available Book:")

        found = False

        for book in library:

            if book["available"]:

                print(book["name"])

                found = True
                

        if not found:
            print("No available!")
                
    # Brrowed book

    elif choice == "8":

        print("Borrowed book:")

        found = False

        for book in library:

            if not book["available"]:
                print(book["name"])

                found = True
                

        if not found:
            print("No book Borrowed!")
                

    # Save data to file

    elif choice == "9":

        try:
            with open("library.txt", "r") as file:
                data = file.read()

                if data:
                    print("====File Data====")
                    print(data)
                else:
                    print("No save file data")
        
        except FileNotFoundError:
            print("No data available")

    # Exit

    elif choice == "10":

        print("Good bye!")

        break

    else:
        print("Inavalide choice")
        