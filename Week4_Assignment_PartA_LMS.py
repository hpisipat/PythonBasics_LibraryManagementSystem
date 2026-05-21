from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

ZONE = ZoneInfo("Asia/Kolkata")

borrow_logs = []

books = [
    {"BookId": 101, "Title": "Let Us C", "Author": "Yeshwant Kanetkar", "Genre": "Computer Science",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None},
    {"BookId": 102, "Title": "Let Us C++", "Author": "Yeshwant Kanetkar", "Genre": "Computer Science",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None},
    {"BookId": 103, "Title": "Let Us C#", "Author": "Yeshwant Kanetkar", "Genre": "Computer Science",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None},
    {"BookId": 104, "Title": "Programming with Java", "Author": "E.Balaguruswamy", "Genre": "Computer Science",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None},
    {"BookId": 105, "Title": "Introduction to Algorithms", "Author": "Thomas H. Cormen", "Genre": "Computer Science",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None},
    {"BookId": 106, "Title": "The Art of Computer Programming", "Author": "Donald Ervin Knuth", "Genre": "Computer Science",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None},
    {"BookId": 107, "Title": "Introduction to the Theory of Computation", "Author": "Michael Sipser", "Genre": "Computer Science",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None},
    {"BookId": 108, "Title": "Structure and Interpretation of Computer Programs", "Author": "Harold Abelson", "Genre": "Fantasy",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None},
    {"BookId": 109, "Title": "Clean Code", "Author": "Robert C. Martin", "Genre": "Computer Science",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None},
    {"BookId": 110, "Title": "Designing Data-Intensive Applications", "Author": "Martin Kleppmann", "Genre": "Computer Science",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None},
    {"BookId": 111, "Title": "Harry Potter and the Deathly Hallows", "Author": "J.K. Rowling", "Genre": "Fantasy",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None},
    {"BookId": 112, "Title": "Harry Potter and the Philosopher's Stone", "Author": "J.K. Rowling", "Genre": "Fantasy",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None},
    {"BookId": 113, "Title": "Harry Potter and the Chamber of Secrets", "Author": "J.K. Rowling", "Genre": "Fantasy",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None},
    {"BookId": 114, "Title": "Harry Potter and the Prisoner of Azkaban", "Author": "J.K. Rowling", "Genre": "Fantasy",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None},
    {"BookId": 115, "Title": "Harry Potter and the Goblet of Fire", "Author": "J.K. Rowling", "Genre": "Fantasy",
     "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None}
]

members = [
    {"MemberId": "M1", "Name": "Haritha Pisipati", "Age": 39, "Contact": "8143696681", "BorrowedBooks": []},
    {"MemberId": "M2", "Name": "Raghuram Guda", "Age": 41, "Contact": "8123546682", "BorrowedBooks": []},
    {"MemberId": "M3", "Name": "Praveen Nayak", "Age": 45, "Contact": "8133668783", "BorrowedBooks": []},
    {"MemberId": "M4", "Name": "Anand Phatak", "Age": 54, "Contact": "8163696484", "BorrowedBooks": []},
    {"MemberId": "M5", "Name": "Agastya Guda", "Age": 11, "Contact": "8178696685", "BorrowedBooks": []},
    {"MemberId": "M6", "Name": "Vasishta Guda", "Age": 8, "Contact": "8183696686", "BorrowedBooks": []}
]


def get_next_member_id():
    if not members:
        return "M1"

    numbers = [
        int(member["MemberId"][1:])
        for member in members
        if member.get("MemberId", "").startswith("M")
    ]
    return f"M{max(numbers) + 1}"


def addMember():
    next_member_id = get_next_member_id()
    name = input("Name  : ").strip()
    age = input("Age : ").strip()
    contactnum = input("Contact : ").strip()
    members.append({"MemberId": next_member_id, "Name": name, "Age": age, "Contact": contactnum, "BorrowedBooks": []})
    print()
    print("Member added:")
    print("MemberId : ", next_member_id)
    print("Name : ", name)
    print("Age : ", age)
    print("Contact : ", contactnum)
    print()


def fetchMaxBookId():
    if not books:
        return 100
    return max(b["BookId"] for b in books)


def addBook():
    bname = input("Enter Book name : ").strip()
    author = input("Enter Author name : ").strip()
    genre = input("Enter genre : ").strip()
    BId = fetchMaxBookId()
    newBId = BId + 1
    books.append({"BookId": newBId, "Title": bname, "Author": author, "Genre": genre,
                  "Availability": "Available", "Issued_Date": None, "Issued_To": None, "DueDate": None})
    print()
    print("Book details added successfully")
    print("BookId : ", newBId)
    print("Title : ", bname)
    print("Author : ", author)
    print("Genre : ", genre)
    print()


def showAllBooks():
    for book in books:
        print()
        print("BookId :", book["BookId"])
        print("Title : ", book["Title"])
        print("Availability : ", book["Availability"])


def print_book_details(book):
    print("BookId : ", book["BookId"])
    print("Title : ", book["Title"])
    print("Author : ", book["Author"])
    print("Genre : ", book["Genre"])
    print("Availability : ", book["Availability"])
    print("Issued_Date : ", book["Issued_Date"])
    print("Issued_To : ", book["Issued_To"])
    print("Due_Date : ", book["DueDate"])
    print()


def searchByTitle(t, ch):
    for book in books:
        if (ch == "av" and t.lower() in book["Title"].lower() and book["Availability"] == "Available") or \
           (ch == "all" and t.lower() in book["Title"].lower()):
            print_book_details(book)


def searchByAuthor(t, ch):
    for book in books:
        if (ch == "av" and t.lower() in book["Author"].lower() and book["Availability"] == "Available") or \
           (ch == "all" and t.lower() in book["Author"].lower()):
            print_book_details(book)


def searchByGenre(t, ch):
    for book in books:
        if (ch == "av" and t.lower() in book["Genre"].lower() and book["Availability"] == "Available") or \
           (ch == "all" and t.lower() in book["Genre"].lower()):
            print_book_details(book)


def searchBook():
    mainchoice = input("Do you want to search all books ? or only available books ? Enter your choice ( av / all) : ").strip()
    print()
    print("Search Books by:")
    print("1. Title")
    print("2. Author")
    print("3. Genre")

    choice = input("Enter choice (1/2/3): ").strip()

    if mainchoice.lower() not in ("av", "all"):
        print("Invalid main choice. Use 'av' or 'all'.")
        return

    if choice == "1":
        t = input("Please enter keyword from Title : ").strip()
        searchByTitle(t, mainchoice.lower())
    elif choice == "2":
        t = input("Please enter Author name : ").strip()
        searchByAuthor(t, mainchoice.lower())
    elif choice == "3":
        t = input("Please enter keyword from Genre : ").strip()
        searchByGenre(t, mainchoice.lower())
    else:
        print("Invalid input. Please enter valid input from above options.")


def showBooks(bid):
    for book in books:
        if book["BookId"] == bid:
            print_book_details(book)
            return
    print("Book not found.")


def showIssuedBooks():
    mid = input("Enter member id : ").strip()
    found = False
    for book in books:
        if book["Availability"] == "Issued" and book["Issued_To"] == mid:
            found = True
            print_book_details(book)
    if not found:
        print("Invalid Member Id / No books have been issued to this member id")


def issueBook():
    bid_input = input("Enter Book Id : ").strip()
    mname = input("Enter Member Name : ").strip()
    mid = input("Enter Member Id: ").strip()

    try:
        bid = int(bid_input)
    except ValueError:
        print("BookId must be a number!")
        return

    # Find book
    book = next((b for b in books if b["BookId"] == bid), None)
    if not book:
        print("Invalid Book Id!")
        return

    if book["Availability"] == "Issued":
        print("Not Available. Book already issued to", book["Issued_To"])
        return

    # Find member
    member = next((m for m in members if m["MemberId"] == mid and mname.lower() in m["Name"].lower()), None)
    if not member:
        print("Member not found! Please enter a valid Member Id.")
        return

    now = datetime.now(ZONE)
    due_date = now + timedelta(days=14)

    # Update book record
    book["Availability"] = "Issued"
    book["Issued_Date"] = now.strftime("%Y-%m-%d %H:%M:%S %Z")
    book["Issued_To"] = mid
    book["DueDate"] = due_date.strftime("%Y-%m-%d %H:%M:%S %Z")

    # Update member record
    member["BorrowedBooks"].append(bid)

    # Create log (store both issued and due)
    borrow_logs.append({
        "BookId": bid,
        "MemberId": mid,
        "Action": "Issued",
        "Issued_Date": book["Issued_Date"],
        "Return_Date": None,
        "DueDate": book["DueDate"],
        "Timestamp": now.strftime("%Y-%m-%d %H:%M:%S %Z")
    })

    showBooks(bid)
    print(f"Book issued successfully to {member['Name']}!")
    print()


def getBookTitleById(bookId):
    for book in books:
        if book["BookId"] == bookId:
            return book["Title"]
    return "Unknown Book"


def showMembersWhoBorrowedBooks():
    for member in members:
        if member["BorrowedBooks"]:
            print("Name : ", member["Name"])
            for b in member["BorrowedBooks"]:
                print("BookId:", b, " Title:", getBookTitleById(b))
            print()


def showPopularGenre():
    genreCount = {}
    for book in books:
        if book["Availability"] == "Issued":
            genre = book["Genre"]
            genreCount[genre] = genreCount.get(genre, 0) + 1
    if not genreCount:
        print("No books have been issued yet!")
        return
    mostPopular = max(genreCount, key=genreCount.get)
    print()
    print("Most Popular Genre : ", mostPopular)
    print(genreCount)


def searchMember():
    memid = input("Enter Member Id : ").strip()
    for member in members:
        if member["MemberId"] == memid:
            print()
            print("MemberId : ", memid)
            print("Name : ", member["Name"])
            print("Age : ", member["Age"])
            print("Contact : ", member["Contact"])
            print("Borrowed Books : ", member["BorrowedBooks"])
            print()
            return
    print("Member not found.")


def returnBook():
    bid_input = input("Enter Book Id : ").strip()
    member_id = input("Enter Member Id : ").strip()

    try:
        bid = int(bid_input)
    except ValueError:
        print("BookId must be a number!")
        return

    # Find book
    book = next((b for b in books if b["BookId"] == bid), None)
    if not book:
        print("Book not found.")
        return

    if book["Issued_To"] != member_id or book["Availability"] != "Issued":
        print("Book is not issued to this member or book is not currently issued.")
        return

    # capture issued_date before clearing
    issued_date = book["Issued_Date"]

    return_time = datetime.now(ZONE)

    # Append return log (keeps a history)
    borrow_logs.append({
        "BookId": bid,
        "MemberId": member_id,
        "Issued_Date": issued_date,
        "Return_Date": return_time.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "Action": "Returned",
        "Timestamp": return_time.strftime("%Y-%m-%d %H:%M:%S %Z")
    })

    # Update book record
    book["Availability"] = "Available"
    book["Issued_To"] = None
    book["Issued_Date"] = None
    book["DueDate"] = None

    # Update member record: remove the book from BorrowedBooks (if present)
    member = next((m for m in members if m["MemberId"] == member_id), None)
    if member and bid in member["BorrowedBooks"]:
        member["BorrowedBooks"].remove(bid)

    print()
    print(f"Book {bid} returned by {member_id} successfully")
    print()

def showBorrowLogsByMember():
    m = input("Enter Member Id : ")
    #print(borrow_logs)
    found = False
    for log in borrow_logs:
        if log["MemberId"] == m:
            found = True
            print("----------- Log Entry -----------")
            for key,value in log.items():
                print(f"{key}  : {value}")
            print()
    if not found:
        print("No logs found for this member ")

def mainMenu():
    while True:
        print()
        print("Library Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. Show Issued Books")
        print("7. List of Members who borrowed books")
        print("8. Search Member by Id ")
        print("9. Display most popular genre (also displays count of books issued in each genre)")
        print("10. Show All Books")
        print("11. View Borrow Logs of a Member")
        print("12. Exit...")
        i = input("Enter your choice from above options (1..12) : ").strip()
        print()

        if i == "1":
            addBook()
        elif i == "2":
            addMember()
        elif i == "3":
            issueBook()
        elif i == "4":
            returnBook()
        elif i == "5":
            searchBook()
        elif i == "6":
            showIssuedBooks()
        elif i == "7":
            showMembersWhoBorrowedBooks()
        elif i == "8":
            searchMember()
        elif i == "9":
            showPopularGenre()
        elif i == "10":
            showAllBooks()
        elif i == "11":
            showBorrowLogsByMember()
        elif i == "12":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    mainMenu()
