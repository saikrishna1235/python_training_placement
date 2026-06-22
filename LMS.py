#wap a program on LMS(Library Management System) without functions


books = []
issued_books = {}

while True:
    print("\n" + "="*50)
    print("        LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. View Issued Books")
    print("8. Exit")
    print("="*50)
    
    choice = input("Enter your choice (1-8): ")
    

    if choice == '1':
        print("\n--- Add Book ---")
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        quantity = int(input("Enter Quantity: "))
        
        book_exists = False
        for book in books:
            if book['id'] == book_id:
                book['quantity'] += quantity
                book_exists = True
                print(f"✓ Quantity updated for '{book_name}'")
                break
        
        if not book_exists:
            books.append({
                'id': book_id,
                'name': book_name,
                'author': author,
                'quantity': quantity
            })
            print(f"✓ Book '{book_name}' added successfully!")
    
   
    elif choice == '2':
        print("\n--- All Books in Library ---")
        if len(books) == 0:
            print("No books available in the library!")
        else:
            print(f"\n{'ID':<10}{'Name':<25}{'Author':<20}{'Available':<10}")
            print("-" * 65)
            for book in books:
                print(f"{book['id']:<10}{book['name']:<25}{book['author']:<20}{book['quantity']:<10}")
    
   
    elif choice == '3':
        print("\n--- Search Book ---")
        search_term = input("Enter Book Name or ID to search: ").lower()
        found = False
        
        for book in books:
            if search_term in book['name'].lower() or search_term in book['id'].lower():
                print(f"\nBook Found!")
                print(f"ID: {book['id']}")
                print(f"Name: {book['name']}")
                print(f"Author: {book['author']}")
                print(f"Available: {book['quantity']}")
                found = True
                break
        
        if not found:
            print(f"✗ Book '{search_term}' not found!")
    
   
    elif choice == '4':
        print("\n--- Issue Book ---")
        book_id = input("Enter Book ID to issue: ")
        member_name = input("Enter Member Name: ")
        
        found = False
        for book in books:
            if book['id'] == book_id:
                if book['quantity'] > 0:
                    book['quantity'] -= 1
                    
                    if book_id not in issued_books:
                        issued_books[book_id] = []
                    
                    issued_books[book_id].append({
                        'member': member_name,
                        'book_name': book['name']
                    })
                    print(f"✓ Book '{book['name']}' issued to {member_name}!")
                else:
                    print(f"✗ Book out of stock!")
                found = True
                break
        
        if not found:
            print(f"✗ Book ID '{book_id}' not found!")
    
  
    elif choice == '5':
        print("\n--- Return Book ---")
        book_id = input("Enter Book ID to return: ")
        member_name = input("Enter Member Name: ")
        
        if book_id in issued_books and len(issued_books[book_id]) > 0:
            for i, issue in enumerate(issued_books[book_id]):
                if issue['member'].lower() == member_name.lower():
                    for book in books:
                        if book['id'] == book_id:
                            book['quantity'] += 1
                            issued_books[book_id].pop(i)
                            print(f"✓ Book '{issue['book_name']}' returned by {member_name}!")
                            break
                    break
            else:
                print(f"✗ No record found for this member!")
        else:
            print(f"✗ No issued books record for this ID!")
    
   
    elif choice == '6':
        print("\n--- Delete Book ---")
        book_id = input("Enter Book ID to delete: ")
        
        for i, book in enumerate(books):
            if book['id'] == book_id:
                removed_book = books.pop(i)
                print(f"✓ Book '{removed_book['name']}' deleted successfully!")
                break
        else:
            print(f"✗ Book ID '{book_id}' not found!")
    
  
    elif choice == '7':
        print("\n--- Issued Books ---")
        if len(issued_books) == 0:
            print("No books are currently issued!")
        else:
            print(f"\n{'Book ID':<10}{'Member':<20}{'Book Name':<25}")
            print("-" * 55)
            for book_id, issues in issued_books.items():
                for issue in issues:
                    print(f"{book_id:<10}{issue['member']:<20}{issue['book_name']:<25}")
    
  
    elif choice == '8':
        print("\n✓ Thank you for using Library Management System!")
        print("Exiting...")
        break