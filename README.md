import os
from datetime import datetime

BOOK_FILE = "books.txt"
MEMBER_FILE = "members.txt"
ISSUE_FILE = "issued.txt"
FINE_PER_DAY = 5


def init_files():
    for file in [BOOK_FILE, MEMBER_FILE, ISSUE_FILE]:
        if not os.path.exists(file):
            open(file, "w").close()


def add_book():
    bid = input("Book ID: ")
    name = input("Book Name: ")
    author = input("Author: ")
    with open(BOOK_FILE, "a") as f:
        f.write(f"{bid},{name},{author},Available\n")
    print("Book added successfully")

def view_books():
    print("\nID  Name  Author  Status")
    print("------------------------")
    with open(BOOK_FILE, "r") as f:
        for line in f:
            print(line.strip().replace(",", "  "))

def update_book():
    bid = input("Enter Book ID to update: ")
    updated = False
    lines = open(BOOK_FILE).readlines()
    with open(BOOK_FILE, "w") as f:
        for line in lines:
            data = line.strip().split(",")
            if data[0] == bid:
                name = input("New Book Name: ")
                author = input("New Author: ")
                f.write(f"{bid},{name},{author},{data[3]}\n")
                updated = True
            else:
                f.write(line)
    print("Book updated" if updated else "Book not found")

def delete_book():
    bid = input("Enter Book ID to delete: ")
    lines = open(BOOK_FILE).readlines()
    with open(BOOK_FILE, "w") as f:
        for line in lines:
            if not line.startswith(bid + ","):
                f.write(line)
    print("Book deleted")


def add_member():
    mid = input("Member ID: ")
    name = input("Member Name: ")
    phone = input("Phone: ")
    with open(MEMBER_FILE, "a") as f:
        f.write(f"{mid},{name},{phone}\n")
    print("Member added")

def view_members():
    print("\nID  Name  Phone")
    print("----------------")
    with open(MEMBER_FILE, "r") as f:
        for line in f:
            print(line.strip().replace(",", "  "))


def issue_book():
    bid = input("Book ID: ")
    mid = input("Member ID: ")
    issue_date = datetime.now().strftime("%Y-%m-%d")

    lines = open(BOOK_FILE).readlines()
    with open(BOOK_FILE, "w") as f:
        issued = False
        for line in lines:
            data = line.strip().split(",")
            if data[0] == bid and data[3] == "Available":
                data[3] = "Issued"
                f.write(",".join(data) + "\n")
                issued = True
            else:
                f.write(line)

    if issued:
        with open(ISSUE_FILE, "a") as f:
            f.write(f"{bid},{mid},{issue_date}\n")
        print("Book issued successfully")
    else:
        print("Book not available")


def return_book():
    bid = input("Book ID: ")
    today = datetime.now()

    records = open(ISSUE_FILE).readlines()
    with open(ISSUE_FILE, "w") as f:
        for line in records:
            data = line.strip().split(",")
            if data[0] == bid:
                issue_date = datetime.strptime(data[2], "%Y-%m-%d")
                days = (today - issue_date).days
                fine = max(0, days - 7) * FINE_PER_DAY
                print("Book returned")
                print("Fine:", fine)
            else:
                f.write(line)

    
    lines = open(BOOK_FILE).readlines()
    with open(BOOK_FILE, "w") as f:
        for line in lines:
            data = line.strip().split(",")
            if data[0] == bid:
                data[3] = "Available"
                f.write(",".join(data) + "\n")
            else:
                f.write(line)

# ---------- MAIN MENU ----------
def main():
    init_files()
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Add Member")
        print("6. View Members")
        print("7. Issue Book")
        print("8. Return Book")
        print("9. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            add_book()
        elif ch == "2":
            view_books()
        elif ch == "3":
            update_book()
        elif ch == "4":
            delete_book()
        elif ch == "5":
            add_member()
        elif ch == "6":
            view_members()
        elif ch == "7":
            issue_book()
        elif ch == "8":
            return_book()
        elif ch == "9":
            print("Thank you!")
            break
        else:
            print("Invalid choice")

main()
