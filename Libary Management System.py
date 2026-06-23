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
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        
        book = {
            "title": title,
            "author": author,
            "available": True
        }
        library.append(book)
        print("Book added succesfully")
     
    # View Book
    elif choice == "2":
        if len(library) == 0:
            print("No Book Avalable")
        else:
            for i, book in enumerate(library, start=1):
                status = "Available" if book ["available"] else "Borrowed"
                print(
                    f"{i}.{book['title']} | "
                    f"Author: {book['author']} | "
                    f"Status: {book['status']}"
                )
    
    # Search Book
    elif choice == "3":
         search = input("Enter search title: ")
         found = False
         for book in library:
             if search.lower() == book["title"].lower():
                 status = "Available" if book ["availabl e"] else "Borrowed"
                 print("\nBool title list:")
                 print(f"Title: {book['title']}")
                 print(f"Author: {book['author']}")
                 print(f"Status:{status}")
                 found = True
                 break
             if not found:
                 print("No book available")
    
    # Brrow book
    elif choice == "4":
        search_title = input("Enter book title to brrowed: ")
        found = False
        for book in library:
            if search_title.lower() == book["title"].lower():
                if book["available"]:
                    book["available"] = False
                    print("Book borrowed successfully")
                else:
                    print("Book already borrowed")
                    found = True
                    break
                if not found:
                    print("Book not foud.")    
    
    # Return book
    elif choice == "5":
        return_book = input("Enter return title: ")
        found = False
        for book in library:
            if return_book.lower() == book["available"].lower():
                if not book["available"]:
                    book["available"] = True
                    print("Book return successfully")
                else:
                    print("This book was not borrwed")
                found = True
                break
            if not found:
                print("Book was not found")

    # Delete Book
    elif choice == "6":
        delete_book = input("Inter book title to delete: ")
        found = False
        for book in library:
            if delete_book.lower() == book["title"].lower():
                library.remove(book)
                print("Book remove successfully")
                found = True
                break
            if not found:
                print("Book title not founded")
    
    # Exit
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

                



         
        


