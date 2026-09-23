import os
Books={}
Books_out=[]
Available=''
def clear_screen() :
    os.system("cls" if os.name == "nt" else "clear")
def program() :
    book_number=input("Enter ISBN : ")
    book_title=input("Enter title : ")
    book_author=input("Enter author : ")
    return book_number, book_title, book_author
while True :
    print("Menu:\n1-Add Book\n2-Check Out Book\n3-Check In Book\n4-List Books\n5-Exit")
    user_choice=input("Enter your choice (1-5): ")
    if user_choice == '1' :
        while True :
            clear_screen()
            number,title,author=program()
            Books[number]={'Title' : title, 'Author' : author, 'Available' : Available}
            print(f"Book '{title}' by {author} added to the catalog with ISBN: {number}.")
            question=input("Do you want to add another book? (y/n): ").lower()
            if question == 'n' : clear_screen() ; break
            elif question == 'y' : clear_screen()
            else :clear_screen() ; print("Invalid input\n") ; break
    elif user_choice == '2' :
        while True :
          clear_screen()
          check_out=input("Enter ISBN to Check Out : ")
          if check_out in Books_out : print("Sorry,the book is currently checked out.\n") 
          elif check_out in Books :
           Books_out.append(check_out)
           print(f"Book '{Books[check_out]['Title']} checked out successfully.")
          else : print("Book not found in the catalog.\n") 
          question=input("Do you want to Check Out another book? (y/n): ").lower()
          if question == 'n' : clear_screen() ; break
          elif question == 'y' : clear_screen()
          else :clear_screen() ; print("Invalid input\n") ; break
    elif user_choice == '3' :
      while True :
        clear_screen()
        check_in=input("Enter ISBN to Check In : ")
        if check_in not in Books_out and check_in in Books:
           print("This book is available in the library and not checked out.\n")
        elif check_in in Books_out : print(f"Book '{Books[check_in]['Title']} Checked In successfully.'") ; Books_out.remove(check_in)
        else : print("Book not found in the catalog.\n")
        question=input("Do you want to Check In another book? (y/n): ").lower()
        if question == 'n' : clear_screen() ; break
        elif question == 'y' : clear_screen()
        else :clear_screen() ; print("Invalid input\n") ; break 
    elif user_choice == '4' :
        clear_screen()
        for isbn in Books :
          details=Books[isbn]
          if isbn in Books_out : Available = 'False'  
          else : Available = 'True'
          print(f"ISBN: {isbn}, Title: {details['Title']}, Author: {details['Author']}, Available: {Available}")
        question=input("Do you want to go back to the main menu? (y/n): ").lower()
        if question == 'y' : clear_screen() 
        elif question == 'n' : break
        else :clear_screen() ; print("Invalid input\n") 
    elif user_choice == '5' : print("Exiting the program ...") ; break
    else :clear_screen() ; print("Invalid input\n")