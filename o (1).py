
import os

FILE_NAME = "students.txt"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue...")



def load_students():
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 5:
                    students.append({
                        "id": data[0],
                        "name": data[1],
                        "class": data[2],
                        "attendance": data[3],
                        "marks": data[4]
                    })
    return students

def save_students(students):
    with open(FILE_NAME, "w") as file:
        for s in students:
            file.write(
                f"{s['id']},{s['name']},{s['class']},{s['attendance']},{s['marks']}\n"
            )

-

def add_student(students):
    clear_screen()
    print("=" * 50)
    print("            ADD STUDENT")
    print("=" * 50)

    sid = input("Student ID        : ").strip()

    # Duplicate check
    for s in students:
        if s["id"] == sid:
            print("\n Student ID already exists")
            pause()
            return

    name = input("Student Name      : ").strip()
    sclass = input("Class / Section   : ").strip()
    attendance = input("Attendance (%)    : ").strip()
    marks = input("Marks             : ").strip()

    if not all([sid, name, sclass, attendance, marks]):
        print("\n All fields are mandatory")
        pause()
        return

    students.append({
        "id": sid,
        "name": name,
        "class": sclass,
        "attendance": attendance,
        "marks": marks
    })

    save_students(students)
    print("\n Student added successfully")
    pause()

def view_students(students):
    clear_screen()
    print("=" * 70)
    print("                STUDENT RECORDS")
    print("=" * 70)

    if not students:
        print("No student records found.")
    else:
        print(f"{'ID':<10}{'Name':<20}{'Class':<15}{'Attendance':<12}{'Marks'}")
        print("-" * 70)
        for s in students:
            print(f"{s['id']:<10}{s['name']:<20}{s['class']:<15}{s['attendance']:<12}{s['marks']}")

    pause()

def update_student(students):
    clear_screen()
    print("=" * 50)
    print("          UPDATE STUDENT")
    print("=" * 50)

    sid = input("Enter Student ID: ").strip()

    for s in students:
        if s["id"] == sid:
            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Class")
            print("3. Attendance")
            print("4. Marks")
            print("5. Update All")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                s["name"] = input("New Name: ")
            elif choice == "2":
                s["class"] = input("New Class: ")
            elif choice == "3":
                s["attendance"] = input("New Attendance: ")
            elif choice == "4":
                s["marks"] = input("New Marks: ")
            elif choice == "5":
                s["name"] = input("New Name: ")
                s["class"] = input("New Class: ")
                s["attendance"] = input("New Attendance: ")
                s["marks"] = input("New Marks: ")
            else:
                print("\n Invalid option")
                pause()
                return

            save_students(students)
            print("\n Student record updated")
            pause()
            return

    print("\n Student not found")
    pause()

def delete_student(students):
    clear_screen()
    print("=" * 50)
    print("          DELETE STUDENT")
    print("=" * 50)

    sid = input("Enter Student ID: ").strip()

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_students(students)
            print("\n Student record deleted")
            pause()
            return

    print("\n Student not found")
    pause()

def clear_all_students(students):
    clear_screen()
    confirm = input("Are you sure you want to delete ALL records? (yes/no): ").lower()

    if confirm == "yes":
        students.clear()
        open(FILE_NAME, "w").close()
        print("\n All student records cleared")
    else:
        print("\n Operation cancelled")

    pause()

# ---------- Main Menu ----------

def main():
    students = load_students()

    while True:
        clear_screen()
        print("=" * 50)
        print("        STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        print("6. Clear All Student Records")
        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "6":
            clear_all_students(students)
        elif choice == "5":
            clear_screen()
            print("Thank you ")
            break
        else:
            print("\n Invalid choice")
            pause()

# ---------- Program Start ----------
main()


